#!/usr/bin/env python3
"""Tests for the plugin hooks: each hook on inputs with and without the problem.

Run: python3 -m unittest discover -s plugin/hooks/tests
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOOKS = HERE.parent
FIX = HERE / "fixtures"


def run(script: str, event: dict) -> tuple[int, str, str]:
    p = subprocess.run([sys.executable, str(HOOKS / script)], input=json.dumps(event),
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout, p.stderr


def write_event(path: Path) -> dict:
    return {"hook_event_name": "PostToolUse", "tool_name": "Write", "tool_input": {"file_path": str(path)}}


def tool_event(name: str, tool_input: dict | None = None) -> dict:
    return {"hook_event_name": "PreToolUse", "tool_name": name, "tool_input": tool_input or {}}


class CheckDeliverable(unittest.TestCase):
    def test_hard_findings_block(self):
        code, _, err = run("check_deliverable.py", write_event(FIX / "job/deliverables/linkedin-posts_en.md"))
        self.assertEqual(code, 2, err)
        self.assertIn("[em-dash]", err)
        self.assertIn("[terms]", err)
        self.assertNotIn("us-spelling", err)

    def test_clean_file_passes(self):
        code, _, err = run("check_deliverable.py", write_event(FIX / "job/deliverables/clean_en.md"))
        self.assertEqual(code, 0, err)

    def test_rsa_flags_from_file_name(self):
        code, _, err = run("check_deliverable.py", write_event(FIX / "job/deliverables/google-ads-rsa_en.md"))
        self.assertEqual(code, 2, err)
        self.assertIn("[rsa-length]", err)

    def test_outside_deliverables_ignored(self):
        code, _, err = run("check_deliverable.py", write_event(FIX / "notes.md"))
        self.assertEqual(code, 0, err)

    def test_bad_input_ignored(self):
        p = subprocess.run([sys.executable, str(HOOKS / "check_deliverable.py")], input="not json",
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)


class ShellWrites(unittest.TestCase):
    def bash_event(self, command: str, cwd: Path) -> dict:
        return {"hook_event_name": "PostToolUse", "tool_name": "Bash",
                "tool_input": {"command": command}, "cwd": str(cwd)}

    def test_recent_shell_write_checked(self):
        import os
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp) / "job" / "deliverables"
            d.mkdir(parents=True)
            (d / "post_en.md").write_text("Hello \u2014 world\n", encoding="utf-8")
            code, _, err = run("check_deliverable.py", self.bash_event("echo x > job/deliverables/post_en.md", Path(tmp)))
            self.assertEqual(code, 2, err)
            self.assertIn("[em-dash]", err)
            old = d / "post_en.md"
            os.utime(old, (0, 0))
            code, _, err = run("check_deliverable.py", self.bash_event("cat job/deliverables/post_en.md", Path(tmp)))
            self.assertEqual(code, 0, err)

    def test_command_without_deliverables_ignored(self):
        code, _, err = run("check_deliverable.py", self.bash_event("ls -la", FIX))
        self.assertEqual(code, 0, err)


class MatcherInSync(unittest.TestCase):
    def test_hooks_json_matcher_matches_rules(self):
        p = subprocess.run([sys.executable, str(HOOKS / "build_matcher.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)

    def test_matcher_covers_only_listed_tools(self):
        import re
        data = json.loads((HOOKS / "hooks.json").read_text(encoding="utf-8"))
        rx = re.compile(data["hooks"]["PreToolUse"][0]["matcher"])
        self.assertTrue(rx.search("mcp__Brevo__send_campaign"))
        self.assertTrue(rx.search("mcp__OpenSEO__run_site_audit"))
        self.assertTrue(rx.search("mcp__novamira-site__mcp-adapter-execute-ability"))
        self.assertFalse(rx.search("mcp__OpenSEO__get_audit_pages"))
        self.assertFalse(rx.search("mcp__github__get_file_contents"))


class PublishGate(unittest.TestCase):
    def asks(self, name: str, tool_input: dict | None = None) -> bool:
        code, out, err = run("publish_gate.py", tool_event(name, tool_input))
        self.assertEqual(code, 0, err)
        if not out.strip():
            return False
        return json.loads(out)["hookSpecificOutput"]["permissionDecision"] == "ask"

    def test_send_and_publish_verbs(self):
        self.assertTrue(self.asks("mcp__Brevo__send_campaign"))
        self.assertTrue(self.asks("mcp__Typefully__schedule-draft"))
        self.assertTrue(self.asks("mcp__HubSpot__delete_contact"))

    def test_named_tools(self):
        self.assertTrue(self.asks("mcp__Zapier__execute_zapier_write_action"))
        self.assertTrue(self.asks("mcp__OpenSEO__run_site_audit"))
        self.assertFalse(self.asks("mcp__Zapier__execute_zapier_read_action"))
        self.assertFalse(self.asks("mcp__OpenSEO__get_audit_pages"))
        self.assertTrue(self.asks("mcp__SEOgets__create_topic_cluster"))
        self.assertFalse(self.asks("mcp__SEOgets__get_site_performance"))
        self.assertTrue(self.asks("mcp__Zapier__enable_zapier_action"))

    def test_wordpress_abilities(self):
        tool = "mcp__novamira-staging-site__mcp-adapter-execute-ability"
        self.assertTrue(self.asks(tool, {"ability_name": "elementor/publish-document"}))
        self.assertTrue(self.asks(tool, {"ability_name": "rank-math/set-homepage-seo"}))
        self.assertTrue(self.asks(tool, {"ability_name": "novamira/execute-php"}))
        self.assertFalse(self.asks(tool, {"ability_name": "elementor/create-page"}))
        self.assertFalse(self.asks(tool, {"ability_name": "rank-math/get-post-seo-meta"}))
        self.assertFalse(self.asks(tool, {"ability_name": "elementor/create-preview-link"}))

    def test_reads_pass(self):
        self.assertFalse(self.asks("mcp__github__get_file_contents"))
        self.assertFalse(self.asks("Write"))


if __name__ == "__main__":
    unittest.main()
