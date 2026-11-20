#!/usr/bin/env python3
"""PostToolUse hook: run check_rules.py on a deliverable as soon as it is saved.

Fires after Write, Edit and MultiEdit, in the main thread and in threads. Acts only on
.md, .txt and .html files inside a folder named `deliverables`. Reports hard findings
only (em dash, RSA lengths and counts, totals and shares, locked terms, ad group column);
spelling and date candidates stay with the director's acceptance step.

Exit 0: nothing to report. Exit 2: hard findings, sent back to whoever wrote the file.
Standard library only.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

HARD = {"em-dash", "rsa-length", "rsa-count", "arith-total", "arith-share",
        "terms", "terms-conflict", "ad-group"}
TEXT = {".md", ".txt", ".html", ".htm"}
CHECKER = Path(__file__).resolve().parent.parent / "skills" / "non-negotiables" / "scripts" / "check_rules.py"


def terms_files(path: Path) -> list[Path]:
    """Terms files in the nearest storage root above the deliverable."""
    for parent in path.parents:
        brand = parent / "brand"
        if brand.is_dir():
            found = sorted(brand.glob("terms*.txt"))
            if found:
                return found
    return []


def flags_for(path: Path) -> list[str]:
    name = path.name.lower()
    flags = ["--arith"]
    if re.search(r"google-ads|rsa|paid|sea-|ppc", name):
        flags += ["--paid", "--rsa"]
    for t in terms_files(path):
        flags += ["--terms", str(t)]
    return flags


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    raw = (event.get("tool_input") or {}).get("file_path") or ""
    if not raw:
        return 0
    path = Path(raw)
    if "deliverables" not in path.parts or path.suffix.lower() not in TEXT or not path.is_file():
        return 0
    if not CHECKER.is_file():
        print(f"check_deliverable: checker not found at {CHECKER}", file=sys.stderr)
        return 1
    proc = subprocess.run([sys.executable, str(CHECKER), str(path), *flags_for(path)],
                          capture_output=True, text=True, encoding="utf-8")
    hard = []
    for line in proc.stdout.splitlines():
        m = re.search(r"\[([a-z-]+)\]", line)
        if m and m.group(1) in HARD:
            hard.append(line.strip())
    if not hard:
        return 0
    print(f"check_rules.py found {len(hard)} hard finding(s) in {path.name}. "
          "Fix the clear ones now; keep one only if it is verbatim client text, and say why.",
          file=sys.stderr)
    for line in hard[:40]:
        print("  " + line, file=sys.stderr)
    if len(hard) > 40:
        print(f"  ... and {len(hard) - 40} more", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
