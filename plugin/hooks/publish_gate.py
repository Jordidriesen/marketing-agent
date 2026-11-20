#!/usr/bin/env python3
"""PreToolUse hook: ask before any tool that publishes, sends, spends or changes an account.

Rules live in publish-tools.txt next to this script. On a match the hook returns
permissionDecision "ask", so Claude Code shows a confirmation prompt for that call.
No match: exit 0 and the call follows the normal permission settings.
Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RULES = Path(__file__).resolve().parent / "publish-tools.txt"


def load_rules() -> list[tuple]:
    rules = []
    for line in RULES.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 3)
        if parts[0] == "tool" and len(parts) >= 2:
            rules.append(("tool", re.compile(" ".join(parts[1:]), re.I)))
        elif parts[0] == "input" and len(parts) == 4:
            rules.append(("input", re.compile(parts[1], re.I), parts[2], re.compile(parts[3], re.I)))
    return rules


def match(tool: str, tool_input: dict, rules: list[tuple]) -> str | None:
    for rule in rules:
        if rule[0] == "tool" and rule[1].search(tool):
            return tool
        if rule[0] == "input" and rule[1].search(tool):
            value = str(tool_input.get(rule[2], ""))
            if rule[3].search(value):
                return f"{tool} ({rule[2]}: {value})"
    return None


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    tool = event.get("tool_name") or ""
    hit = match(tool, event.get("tool_input") or {}, load_rules())
    if not hit:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": f"Publish gate: {hit} can publish, send, spend or change an account. "
                                    "Confirm only if you said yes to this exact action.",
    }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
