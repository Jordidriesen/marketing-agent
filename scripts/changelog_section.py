#!/usr/bin/env python3
"""Print one version's section of CHANGELOG.md, for the release notes.

    python scripts/changelog_section.py 5.3.0

Prints everything under the heading "## [5.3.0]" up to the next "## [" heading.
Exits 1 when the version has no section, so a release never goes out without notes.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def section(text: str, version: str) -> str:
    lines, out, inside = text.splitlines(), [], False
    head = re.compile(r"^## \[" + re.escape(version) + r"\]")
    for line in lines:
        if line.startswith("## ["):
            if inside:
                break
            inside = bool(head.match(line))
            continue
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    notes = section((ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), sys.argv[1])
    if not notes:
        print(f"No section for {sys.argv[1]} in CHANGELOG.md", file=sys.stderr)
        return 1
    print(notes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
