#!/usr/bin/env python3
"""Keep the publish gate's hook matcher in hooks.json identical to publish-tools.txt.

The gate hook runs with onFailure "block", so it must trigger only on the tools in
publish-tools.txt: on a machine without Python, those tools are blocked and every other
tool keeps working. This script builds the PreToolUse matcher from the rules file.

    python3 plugin/hooks/build_matcher.py           # rewrite the matcher in hooks.json
    python3 plugin/hooks/build_matcher.py --check   # exit 1 if hooks.json is out of date (tests)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES = HERE / "publish-tools.txt"
HOOKS = HERE / "hooks.json"
GATE = "publish_gate.py"


def tool_patterns() -> list[str]:
    out = []
    for line in RULES.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 3)
        if parts[0] == "tool" and len(parts) >= 2:
            out.append(" ".join(parts[1:]))
        elif parts[0] == "input" and len(parts) == 4:
            out.append(parts[1])
    return out


def matcher() -> str:
    return "|".join(f"(?:{p})" for p in tool_patterns())


def gate_entry(data: dict) -> dict:
    for entry in data["hooks"]["PreToolUse"]:
        if any(GATE in " ".join(h.get("args", [])) for h in entry["hooks"]):
            return entry
    raise SystemExit("publish gate entry not found in hooks.json")


def main() -> int:
    data = json.loads(HOOKS.read_text(encoding="utf-8"))
    entry = gate_entry(data)
    want = matcher()
    if "--check" in sys.argv:
        if entry["matcher"] != want:
            print("hooks.json matcher is out of date: run python3 plugin/hooks/build_matcher.py", file=sys.stderr)
            return 1
        return 0
    entry["matcher"] = want
    HOOKS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(want)
    return 0


if __name__ == "__main__":
    sys.exit(main())
