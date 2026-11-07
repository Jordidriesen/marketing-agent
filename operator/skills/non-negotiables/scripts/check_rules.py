#!/usr/bin/env python3
"""Mechanical checks for the non-negotiables skill.

Usage:
  check_rules.py FILE [--lang auto|en|nl|none] [--paid]

FILE is a text, Markdown or HTML source file, or "-" for stdin.

What it checks
  - em dashes (U+2014), always
  - English (en_GB): common US spellings, US date order ("October 24, 2026"),
    a short list of US vocabulary
  - Dutch (Belgian): Netherlands-only words and phrases, taken from the
    Belgisch Nederlands section of ai-content-cleaner/references/patterns-nl.md
  - --paid: markdown tables that list keywords or search terms without an
    ad group column

What it skips: fenced code, inline code, URLs, markdown link targets, HTML tags.

Findings are candidates, not verdicts: a reviewer judges each one.
Exit code 1 if anything was found, 0 if clean.

Standard library only. Python 3.8+.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EM_DASH = "—"

MONTHS = (
    "January|February|March|April|May|June|July|August|September|October|"
    "November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
)

# Words that match the -ize pattern but are spelt the same in en_GB.
IZE_OK = {
    "size", "sizes", "sized", "sizing", "resize", "resized", "resizes",
    "resizing", "downsize", "downsized", "downsizing", "upsize", "upsized",
    "oversize", "oversized", "undersize", "undersized", "prize", "prizes",
    "prized", "seize", "seized", "seizes", "seizing", "capsize", "capsized",
    "capsizing", "baptize", "baptized",
}
IZE_RE = re.compile(r"\b[A-Za-z]+iz(?:e|es|ed|ing|ation|ations|er|ers)\b", re.I)

US_PATTERNS = [
    (r"\bcolor(?:s|ed|ing|ful)?\b", "colour"),
    (r"\bfavorite(?:s)?\b", "favourite"),
    (r"\bbehavior(?:s|al)?\b", "behaviour"),
    (r"\b(?:neighbor|honor|labor|humor|flavor|harbor|rumor|savor|odor)"
     r"(?:s|ed|ing|able)?\b", "-our spelling"),
    (r"\bcenter(?:s|ed|ing)?\b", "centre"),
    (r"\b(?:liter|theater|fiber)(?:s)?\b", "-re spelling"),
    (r"\b(?:defense|offense)\b", "defence / offence"),
    (r"\bcatalog(?:s|ed|ing)?\b", "catalogue"),
    (r"\bgray\b", "grey"),
    (r"\b[A-Za-z]*lyz(?:e|es|ed|ing|er|ers)\b", "-yse spelling"),
    (r"\b(?:traveled|traveling|traveler|travelers|canceled|canceling|"
     r"labeled|labeling|modeled|modeling|signaled|signaling|leveled|"
     r"leveling|fueled|fueling|channeled|channeling|counseled|counseling|"
     r"totaled|totaling)\b", "double l"),
    (r"\bfulfill(?:s|ment)?\b", "fulfil / fulfils / fulfilment"),
    (r"\benroll(?:s|ment)?\b", "enrol / enrols / enrolment"),
    (r"\binstallment(?:s)?\b", "instalment"),
    (r"\bskillful\b", "skilful"),
    (r"\baluminum\b", "aluminium"),
    (r"\bskeptic(?:s|al|ism)?\b", "sceptic"),
    (r"\bpajamas\b", "pyjamas"),
    (r"\bplow(?:s|ed|ing)?\b", "plough"),
    (r"\bmold(?:s|ed|ing|y)?\b", "mould"),
    (r"\baging\b", "ageing"),
]
US_COMPILED = [(re.compile(p, re.I), s) for p, s in US_PATTERNS]

US_VOCAB = [
    (r"\bgotten\b", "got"),
    (r"\bsidewalks?\b", "pavement"),
    (r"\bcell phones?\b", "mobile phone"),
    (r"\bzip codes?\b", "postcode"),
    (r"\bparking lots?\b", "car park"),
    (r"\bvacations?\b", "holiday"),
    (r"\bmath\b", "maths"),
    (r"\bmoms?\b", "mum"),
    (r"\bgas stations?\b", "petrol station"),
    (r"\bdiapers?\b", "nappy"),
    (r"\bfaucets?\b", "tap"),
]
US_VOCAB_COMPILED = [(re.compile(p, re.I), s) for p, s in US_VOCAB]

US_DATE = re.compile(
    r"\b(?:%s)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,\s*\d{4})?\b(?!\d)" % MONTHS
)

# Netherlands-only words and phrases. Source: the table and the list of
# Hollandse wendingen in ai-content-cleaner/references/patterns-nl.md.
NL_PATTERNS = [
    (r"\bmobieltjes?\b", "gsm"),
    (r"\b(?:pinnen|gepind|pinpassen|pinpas)\b", "betalen met de kaart / bankkaart"),
    (r"\bkassabon(?:nen|netje|netjes)?\b", "kasticket"),
    (r"\bpatat\b", "frieten"),
    (r"\btosti(?:'s)?\b", "croque-monsieur"),
    (r"\bsalarissen\b|\bsalaris\b", "loon / wedde"),
    (r"\bzzp'?ers?\b", "zelfstandige"),
    (r"\bKvK(?:-nummer)?\b", "ondernemingsnummer (KBO)"),
    (r"\bBSN\b", "rijksregisternummer"),
    (r"\bbasisscholen?\b|\bmiddelbare scholen?\b", "lagere school / secundair onderwijs"),
    (r"\brijtjeshuis\b|\brijtjeshuizen\b", "rijwoning"),
    (r"\bdekvloer(?:en)?\b", "chape"),
    (r"\bstucwerk\b|\bstukadoors?\b", "pleisterwerk / plafonneerder"),
    (r"\bbouwplaats(?:en)?\b", "werf"),
    (r"\bhartstikke\b", "tone: use tof / fijn or nothing"),
    (r"\bgaaf\b", "tone: use tof / fijn"),
    (r"\bdoei\b", "tone: use dag"),
    (r"\bhoi\b", "tone: use dag / hallo"),
    (r"\b(?:mailtjes?|belletjes?|momentjes?)\b", "diminutive as politeness"),
    (r"\beven (?:checken|laten weten)\b", "'even' as softener (a tic if repeated)"),
]
NL_COMPILED = [(re.compile(p, re.I), s) for p, s in NL_PATTERNS]

EN_STOP = set("the and of to is for with that this are you your we our in on it".split())
NL_STOP = set("de het een van en is voor niet met dat die zijn wij uw ons op te".split())

KEYWORD_HDR = re.compile(r"keyword|search term|zoekterm|zoekwoord|trefwoord", re.I)
ADGROUP_HDR = re.compile(r"ad[\s-]?group|advertentiegroep", re.I)


def mask_line(line: str, in_fence: bool) -> str:
    """Blank out protected spans, keeping columns stable."""
    if in_fence:
        return " " * len(line)

    def blank(m: re.Match) -> str:
        return " " * (m.end() - m.start())

    line = re.sub(r"`[^`]*`", blank, line)
    line = re.sub(r"https?://\S+", blank, line)
    line = re.sub(r"\]\([^)]*\)", blank, line)
    line = re.sub(r"<[^>\n]+>", blank, line)
    return line


def masked_lines(text: str) -> list[str]:
    out, fenced = [], False
    for raw in text.splitlines():
        if raw.lstrip().startswith("```") or raw.lstrip().startswith("~~~"):
            fenced = not fenced
            out.append(" " * len(raw))
            continue
        out.append(mask_line(raw, fenced))
    return out


def detect_lang(text: str) -> str:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    en = sum(1 for w in words if w in EN_STOP)
    nl = sum(1 for w in words if w in NL_STOP)
    if en == 0 and nl == 0:
        return "none"
    return "nl" if nl > en else "en"


def snippet(line: str, start: int, end: int) -> str:
    a, b = max(0, start - 25), min(len(line), end + 25)
    return line[a:b].strip()


def run_checks(text: str, lang: str, paid: bool) -> list[tuple]:
    findings: list[tuple] = []
    original = text.splitlines()
    masked = masked_lines(text)

    for i, line in enumerate(masked):
        orig = original[i]
        for m in re.finditer(EM_DASH, line):
            findings.append((i + 1, m.start() + 1, "em-dash",
                             "em dash: use a comma, colon, semicolon or a new sentence",
                             snippet(orig, m.start(), m.end())))
        if lang == "en":
            for rx, suggestion in US_COMPILED:
                for m in rx.finditer(line):
                    findings.append((i + 1, m.start() + 1, "us-spelling",
                                     f"'{m.group(0)}' -> {suggestion}",
                                     snippet(orig, m.start(), m.end())))
            for m in IZE_RE.finditer(line):
                if m.group(0).lower() in IZE_OK:
                    continue
                findings.append((i + 1, m.start() + 1, "us-spelling",
                                 f"'{m.group(0)}' -> -ise spelling",
                                 snippet(orig, m.start(), m.end())))
            for rx, suggestion in US_VOCAB_COMPILED:
                for m in rx.finditer(line):
                    findings.append((i + 1, m.start() + 1, "us-vocabulary",
                                     f"'{m.group(0)}' -> {suggestion}",
                                     snippet(orig, m.start(), m.end())))
            for m in US_DATE.finditer(line):
                findings.append((i + 1, m.start() + 1, "us-date",
                                 f"'{m.group(0)}' -> day first, e.g. 24 October 2026",
                                 snippet(orig, m.start(), m.end())))
        elif lang == "nl":
            for rx, suggestion in NL_COMPILED:
                for m in rx.finditer(line):
                    findings.append((i + 1, m.start() + 1, "nl-nl-word",
                                     f"'{m.group(0)}' -> {suggestion}",
                                     snippet(orig, m.start(), m.end())))

    if paid:
        for i in range(len(masked) - 1):
            head, sep = original[i], original[i + 1]
            if not head.lstrip().startswith("|"):
                continue
            if not re.match(r"^\s*\|?\s*:?-{2,}", sep):
                continue
            cells = [c.strip() for c in head.strip().strip("|").split("|")]
            if any(KEYWORD_HDR.search(c) for c in cells) and not any(
                ADGROUP_HDR.search(c) for c in cells
            ):
                findings.append((i + 1, 1, "ad-group",
                                 "table lists keywords or search terms without an ad group column",
                                 head.strip()[:80]))

    findings.sort(key=lambda f: (f[0], f[1]))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file", help="text, Markdown or HTML file, or - for stdin")
    ap.add_argument("--lang", choices=["auto", "en", "nl", "none"], default="auto")
    ap.add_argument("--paid", action="store_true",
                    help="also check keyword tables for an ad group column")
    args = ap.parse_args()

    if args.file == "-":
        text = sys.stdin.read()
        name = "stdin"
    else:
        path = Path(args.file)
        if path.suffix.lower() in {".pdf", ".docx", ".xlsx", ".pptx", ".png",
                                   ".jpg", ".jpeg", ".zip"}:
            print(f"Not a text file: {path.name}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8", errors="replace")
        name = path.name

    lang = detect_lang(text) if args.lang == "auto" else args.lang
    findings = run_checks(text, lang, args.paid)

    for line, col, rule, msg, ctx in findings:
        print(f"{name}:{line}:{col} [{rule}] {msg}   ...{ctx}...")

    counts: dict[str, int] = {}
    for f in findings:
        counts[f[2]] = counts.get(f[2], 0) + 1
    summary = ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "none"
    ran = ["em-dash"]
    if lang == "en":
        ran += ["us-spelling", "us-vocabulary", "us-date"]
    elif lang == "nl":
        ran += ["nl-nl-word"]
    if args.paid:
        ran += ["ad-group"]
    print(f"\nLanguage: {lang}. Checks run: {', '.join(ran)}. Findings: {summary}.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
