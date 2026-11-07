#!/usr/bin/env python3
"""Keep shared reference files identical across the skills that use them.

Each shared file has one source of truth (its canonical skill). Skills that use it carry a copy in their
own references/ folder, so every path resolves from the skill root, as the Agent Skills specification
asks. Edit only the canonical file, then run this script.

    python scripts/sync_shared_refs.py           # copy canonical files into every target
    python scripts/sync_shared_refs.py --check   # exit 1 if any copy differs (used in CI)

The mapping lives in scripts/shared-refs.yaml.
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugin" / "skills"
MANIFEST = ROOT / "scripts" / "shared-refs.yaml"
HEADER = "<!-- Shared reference. Source of truth: {src}. Edit it there and run scripts/sync_shared_refs.py. -->\n"


def main(check: bool) -> int:
    manifest = yaml.safe_load(MANIFEST.read_text())
    problems = []
    for src, targets in manifest.items():
        src_path = SKILLS / src
        if not src_path.exists():
            problems.append(f"missing source: {src}")
            continue
        content = HEADER.format(src=f"plugin/skills/{src}") + src_path.read_text()
        name = src_path.name
        for skill in targets:
            dst = SKILLS / skill / "references" / name
            current = dst.read_text() if dst.exists() else None
            if current == content:
                continue
            if check:
                problems.append(f"out of date: {skill}/references/{name} (source {src})")
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(content)
                print(f"updated {skill}/references/{name}")
    for p in problems:
        print(p, file=sys.stderr)
    if problems:
        print("Run: python scripts/sync_shared_refs.py", file=sys.stderr)
        return 1
    if check:
        print("All shared references are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv[1:]))
