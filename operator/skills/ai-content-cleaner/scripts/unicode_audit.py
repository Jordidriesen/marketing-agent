#!/usr/bin/env python3
"""Audit and clean invisible or deceptive Unicode in reader-facing text.

Two subcommands:

  inspect FILE   Report every suspicious character with its line, column,
                 code point and category. Exit code 1 if anything removable
                 was found, 0 if the text is clean.
  clean FILE     Write a cleaned copy (FILE.cleaned.ext by default, or -o).
                 Removes invisible and bidi-control characters, keeps the
                 ones that carry meaning (see below), and reports what it did.

Use "-" as FILE to read from stdin (clean then writes to stdout).

What is removed by default
  - zero-width space, word joiner, invisible math operators, BOM inside text
  - soft hyphens
  - bidirectional embedding, override and isolate controls
  - Unicode tag characters (U+E0000 to U+E007F), except inside a flag emoji
    tag sequence
  - Hangul filler and similar blank-looking letters

What is kept by default, because it carries meaning
  - zero-width joiner and non-joiner inside emoji or between letters of
    scripts that need them (Arabic, Indic); a ZWJ between two Latin letters
    is removed
  - left-to-right and right-to-left marks (reported only)
  - no-break spaces, narrow no-break spaces and other typographic spaces:
    French typography needs the narrow no-break space before ; : ! ?
    These are reported, and only normalised to ordinary spaces with
    --normalise-spaces.

Standard library only. Python 3.8+.
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

REMOVE = {
    0x200B: "zero-width space",
    0x2060: "word joiner",
    0x2061: "invisible function application",
    0x2062: "invisible times",
    0x2063: "invisible separator",
    0x2064: "invisible plus",
    0xFEFF: "zero-width no-break space (BOM)",
    0x00AD: "soft hyphen",
    0x180E: "Mongolian vowel separator",
    0x115F: "Hangul choseong filler",
    0x1160: "Hangul jungseong filler",
    0x3164: "Hangul filler",
    0xFFA0: "halfwidth Hangul filler",
    0x202A: "left-to-right embedding",
    0x202B: "right-to-left embedding",
    0x202C: "pop directional formatting",
    0x202D: "left-to-right override",
    0x202E: "right-to-left override",
    0x2066: "left-to-right isolate",
    0x2067: "right-to-left isolate",
    0x2068: "first strong isolate",
    0x2069: "pop directional isolate",
}
JOINERS = {0x200C: "zero-width non-joiner", 0x200D: "zero-width joiner"}
MARKS = {0x200E: "left-to-right mark", 0x200F: "right-to-left mark"}
SPACES = {
    0x00A0: "no-break space",
    0x202F: "narrow no-break space",
    0x2007: "figure space",
    0x2009: "thin space",
    0x200A: "hair space",
    0x2002: "en space",
    0x2003: "em space",
    0x2005: "four-per-em space",
    0x2006: "six-per-em space",
    0x2008: "punctuation space",
    0x205F: "medium mathematical space",
    0x3000: "ideographic space",
}
TAG_START, TAG_END = 0xE0000, 0xE007F
BLACK_FLAG = 0x1F3F4


def _is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return (
        0x1F000 <= cp <= 0x1FAFF
        or 0x2600 <= cp <= 0x27BF
        or cp in (0xFE0F, 0x20E3)
        or 0x1F3FB <= cp <= 0x1F3FF
    )


def _needs_joiner(ch: str) -> bool:
    """Letters from scripts where ZWJ/ZWNJ change shaping."""
    if not ch:
        return False
    name = unicodedata.name(ch, "")
    return any(
        s in name
        for s in ("ARABIC", "PERSIAN", "DEVANAGARI", "BENGALI", "GURMUKHI",
                  "GUJARATI", "ORIYA", "TAMIL", "TELUGU", "KANNADA",
                  "MALAYALAM", "SINHALA", "SYRIAC", "MONGOLIAN")
    )


def classify(text: str, i: int) -> tuple[str, str] | None:
    """Return (action, label) for the character at i, or None if ordinary."""
    cp = ord(text[i])
    prev = text[i - 1] if i > 0 else ""
    nxt = text[i + 1] if i + 1 < len(text) else ""

    if cp in REMOVE:
        if cp == 0xFEFF and i == 0:
            return ("remove", "byte order mark at start of text")
        return ("remove", REMOVE[cp])
    if cp in JOINERS:
        if _is_emoji(prev) or _is_emoji(nxt) or _needs_joiner(prev) or _needs_joiner(nxt):
            return ("keep", JOINERS[cp] + " (meaningful here)")
        return ("remove", JOINERS[cp])
    if cp in MARKS:
        return ("report", MARKS[cp])
    if cp in SPACES:
        return ("space", SPACES[cp])
    if TAG_START <= cp <= TAG_END:
        # Keep tag sequences that belong to a subdivision flag emoji.
        j = i
        while j > 0 and TAG_START <= ord(text[j - 1]) <= TAG_END:
            j -= 1
        if j > 0 and ord(text[j - 1]) == BLACK_FLAG:
            return ("keep", "tag character in flag emoji")
        return ("remove", "Unicode tag character (hidden text)")
    if unicodedata.category(text[i]) == "Cf":
        return ("report", "other invisible format character")
    return None


def scan(text: str) -> list[dict]:
    hits = []
    line, col = 1, 0
    for i, ch in enumerate(text):
        if ch == "\n":
            line, col = line + 1, 0
            continue
        col += 1
        result = classify(text, i)
        if result:
            action, label = result
            hits.append({
                "line": line,
                "column": col,
                "codepoint": f"U+{ord(ch):04X}",
                "label": label,
                "action": action,
            })
    return hits


def clean(text: str, normalise_spaces: bool) -> tuple[str, dict]:
    out, stats = [], {}
    for i, ch in enumerate(text):
        result = classify(text, i)
        if result:
            action, label = result
            if action == "remove" or (action == "space" and normalise_spaces):
                stats[label] = stats.get(label, 0) + 1
                if action == "space":
                    out.append(" ")
                continue
        out.append(ch)
    return "".join(out), stats


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_inspect = sub.add_parser("inspect", help="report suspicious characters")
    p_inspect.add_argument("file")
    p_inspect.add_argument("--json", action="store_true", help="print JSON instead of text")

    p_clean = sub.add_parser("clean", help="write a cleaned copy")
    p_clean.add_argument("file")
    p_clean.add_argument("-o", "--output", help="output path (default FILE.cleaned.ext)")
    p_clean.add_argument("--normalise-spaces", action="store_true",
                         help="also turn typographic spaces into ordinary spaces")

    args = parser.parse_args(argv)
    text = _read(args.file)

    if args.command == "inspect":
        hits = scan(text)
        removable = [h for h in hits if h["action"] == "remove"]
        if args.json:
            print(json.dumps({"removable": len(removable), "hits": hits}, indent=2))
        else:
            if not hits:
                print("No invisible or deceptive characters found.")
            for h in hits:
                print(f'{h["line"]}:{h["column"]}  {h["codepoint"]}  {h["action"]:<6}  {h["label"]}')
            print(f"\n{len(removable)} removable, {len(hits) - len(removable)} kept or reported.")
        return 1 if removable else 0

    cleaned, stats = clean(text, args.normalise_spaces)
    if args.file == "-" and not args.output:
        sys.stdout.write(cleaned)
    else:
        if args.output:
            out_path = Path(args.output)
        else:
            src = Path(args.file)
            out_path = src.with_name(f"{src.stem}.cleaned{src.suffix}")
        out_path.write_text(cleaned, encoding="utf-8")
        print(f"Wrote {out_path}")
    report = ", ".join(f"{n} x {label}" for label, n in sorted(stats.items())) or "nothing removed"
    print(f"Removed: {report}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
