#!/usr/bin/env python3
"""Validate that every skill folder has a well-formed SKILL.md.

Checks:
- SKILL.md exists in every top-level folder (excluding dotfiles/scripts)
- Frontmatter is valid YAML, delimited by --- ... ---
- 'name' field is present and matches the folder name
- 'description' field is present and non-trivial (catches empty/placeholder text)

Exits non-zero on any failure so it can gate CI.
"""
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".github", ".git", "scripts"}
MIN_DESCRIPTION_LEN = 20

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def check_skill(folder: Path) -> list[str]:
    errors = []
    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        return [f"{folder.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return [f"{folder.name}: SKILL.md has no valid --- frontmatter block"]

    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return [f"{folder.name}: frontmatter is not valid YAML ({e})"]

    name = fm.get("name")
    if not name:
        errors.append(f"{folder.name}: frontmatter missing 'name'")
    elif name != folder.name:
        errors.append(
            f"{folder.name}: frontmatter name '{name}' does not match folder name"
        )

    description = fm.get("description")
    if not description or len(str(description).strip()) < MIN_DESCRIPTION_LEN:
        errors.append(f"{folder.name}: frontmatter 'description' missing or too short")

    return errors


def main() -> int:
    all_errors = []
    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir() or folder.name in SKIP_DIRS or folder.name.startswith("."):
            continue
        all_errors.extend(check_skill(folder))

    if all_errors:
        print(f"Found {len(all_errors)} issue(s):\n")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("All skills passed frontmatter validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
