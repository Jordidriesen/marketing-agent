#!/usr/bin/env python3
"""Tests for check_rules.py: every check on a sample with and without the problem.

Run: python3 -m unittest discover -s plugin/skills/non-negotiables/scripts/tests
Standard library only.
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "check_rules.py"
FIX = HERE / "fixtures"


def run(fixture: str, *flags: str) -> tuple[int, str]:
    args = [sys.executable, str(SCRIPT), str(FIX / fixture), *flags]
    for i, a in enumerate(args):
        if a.startswith("terms-") and a.endswith(".txt"):
            args[i] = str(FIX / a)
    p = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout + p.stderr


class LegacyChecks(unittest.TestCase):
    def test_en_clean(self):
        code, out = run("legacy_pass.md")
        self.assertEqual(code, 0, out)

    def test_en_findings(self):
        code, out = run("legacy_fail_en.md")
        self.assertEqual(code, 1, out)
        for rule in ("[em-dash]", "[us-spelling]", "[us-date]"):
            self.assertIn(rule, out)

    def test_nl_findings(self):
        code, out = run("legacy_fail_nl.md", "--lang", "nl")
        self.assertEqual(code, 1, out)
        self.assertIn("[nl-nl-word]", out)
        self.assertIn("gsm", out)

    def test_paid(self):
        self.assertEqual(run("paid_pass.md", "--paid")[0], 0)
        code, out = run("paid_fail.md", "--paid")
        self.assertEqual(code, 1, out)
        self.assertIn("[ad-group]", out)


class RsaChecks(unittest.TestCase):
    def test_clean(self):
        code, out = run("rsa_pass.md", "--rsa")
        self.assertEqual(code, 0, out)

    def test_findings(self):
        code, out = run("rsa_fail.md", "--rsa")
        self.assertEqual(code, 1, out)
        self.assertIn("headline has 39 characters, limit 30", out)
        self.assertIn("description has 93 characters, limit 90", out)
        self.assertIn("headline has 31 characters, limit 30", out)
        self.assertIn("stated count 20, actual 24", out)

    def test_off_by_default(self):
        self.assertNotIn("[rsa-", run("rsa_fail.md")[1])


class ArithChecks(unittest.TestCase):
    def test_clean(self):
        code, out = run("arith_pass.md", "--arith")
        self.assertEqual(code, 0, out)
        self.assertIn("2 table(s), 5 column(s) recomputed", out)

    def test_findings(self):
        code, out = run("arith_fail.md", "--arith")
        self.assertEqual(code, 1, out)
        self.assertIn("column 'Spend': total says 3,100.5, rows add up to 3,000.5", out)
        self.assertIn("column 'Share' adds up to 110, expected 100", out)
        self.assertNotIn("'CTR'", out)


class TermsChecks(unittest.TestCase):
    def test_clean(self):
        code, out = run("terms_pass.md", "--terms", "terms-brand.txt", "--terms", "terms-product.txt")
        self.assertEqual(code, 0, out)
        self.assertIn("terms-brand.txt checked 19/11/2026", out)

    def test_findings(self):
        code, out = run("terms_fail.md", "--terms", "terms-brand.txt", "--terms", "terms-product.txt")
        self.assertEqual(code, 1, out)
        self.assertEqual(out.count("[terms]"), 3, out)

    def test_conflict(self):
        code, out = run("terms_pass.md", "--terms", "terms-brand.txt", "--terms", "terms-conflict.txt")
        self.assertEqual(code, 1, out)
        self.assertIn("[terms-conflict]", out)

    def test_missing_file(self):
        code, out = run("terms_pass.md", "--terms", "terms-missing.txt")
        self.assertEqual(code, 2, out)


if __name__ == "__main__":
    unittest.main()
