#!/usr/bin/env python3
"""Mechanical checks for the non-negotiables skill.

Usage:
  check_rules.py FILE [--lang auto|en|nl|none] [--paid] [--rsa] [--arith]
                      [--terms TERMS_FILE ...]

FILE is a text, Markdown or HTML source file, or "-" for stdin.

What it checks
  - em dashes (U+2014), always
  - English (en_GB): common US spellings, US date order ("October 24, 2026"),
    a short list of US vocabulary
  - Dutch (Belgian): Netherlands-only words and phrases, taken from the
    Belgisch Nederlands section of ai-content-cleaner/references/patterns-nl.md
  - --paid: markdown tables that list keywords or search terms without an
    ad group column
  - --rsa: responsive search ad assets over the limit (headlines 30,
    descriptions 90) and stated character counts that do not match the text
  - --arith: markdown tables whose Total row does not match the sum of the
    rows above it, and share columns that do not add up to 100
  - --terms FILE: wrong variants of locked brand or product terms, from one or
    more terms files (repeat the flag per file); conflicts between files are
    reported too

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


# ---------------------------------------------------------------- --rsa
RSA_LIMITS = {"headline": 30, "description": 90}
HEADING_RE = re.compile(r"^\s*(?:#{1,6}\s+(.*?)\s*#*\s*$|\*\*([^*]+)\*\*:?\s*$|([A-Za-z][^|]{0,60}):\s*$)")
HEADLINE_WORD = re.compile(r"headline|kop", re.I)
DESCRIPTION_WORD = re.compile(r"description|beschrijving|omschrijving", re.I)
NUMBERED_RE = re.compile(r"^\s*(\d{1,2})[.)]\s+(.*\S)\s*$")
COUNT_RE = re.compile(r"\((\d{1,3})(?:\s*(?:chars?|characters|tekens|karakters))?\)")
COUNT_HDR = re.compile(r"char|teken|karakter|length|lengte|count|^#$", re.I)


def asset_kind(text: str):
    h, d = bool(HEADLINE_WORD.search(text)), bool(DESCRIPTION_WORD.search(text))
    if h and not d:
        return "headline"
    if d and not h:
        return "description"
    return None


def clean_asset(text: str) -> str:
    text = text.strip()
    for a, b in (("**", "**"), ("__", "__"), ("*", "*"), ("_", "_"),
                 ('"', '"'), ("“", "”"), ("'", "'"), ("`", "`")):
        if len(text) > len(a) + len(b) and text.startswith(a) and text.endswith(b):
            text = text[len(a):-len(b)].strip()
    return text


def table_rows(lines: list[str], start: int):
    """Yield (line_no, cells) for a markdown table whose header is at start."""
    i = start + 2
    while i < len(lines) and lines[i].lstrip().startswith("|"):
        yield i, [c.strip() for c in lines[i].strip().strip("|").split("|")]
        i += 1


def is_table_head(lines: list[str], i: int) -> bool:
    return (i + 1 < len(lines) and lines[i].lstrip().startswith("|")
            and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]) is not None)


def rsa_finding(findings, line_no, kind, text, stated, ctx):
    limit = RSA_LIMITS[kind]
    n = len(text)
    if n > limit:
        findings.append((line_no, 1, "rsa-length",
                         f"{kind} has {n} characters, limit {limit}", ctx[:80]))
    if stated is not None and stated != n:
        findings.append((line_no, 1, "rsa-count",
                         f"stated count {stated}, actual {n}", ctx[:80]))


def check_rsa(original: list[str], fenced: list[bool]) -> list[tuple]:
    findings: list[tuple] = []
    section = None
    in_table_until = -1
    for i, line in enumerate(original):
        if fenced[i] or i <= in_table_until:
            continue
        if is_table_head(original, i):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            text_cols = [(j, asset_kind(c)) for j, c in enumerate(cells)
                         if asset_kind(c) and not COUNT_HDR.search(c)]
            count_cols = [j for j, c in enumerate(cells) if COUNT_HDR.search(c)]
            last = i + 1
            for row_no, row in table_rows(original, i):
                last = row_no
                for j, kind in text_cols:
                    if j >= len(row) or not row[j]:
                        continue
                    raw = row[j]
                    m = COUNT_RE.search(raw)
                    stated = int(m.group(1)) if m else None
                    text = clean_asset(raw[:m.start()] if m else raw)
                    if stated is None and len(count_cols) == 1 and count_cols[0] < len(row):
                        digits = re.sub(r"\D", "", row[count_cols[0]])
                        stated = int(digits) if digits else None
                    rsa_finding(findings, row_no + 1, kind, text, stated, original[row_no].strip())
            in_table_until = last
            continue
        h = HEADING_RE.match(line)
        if h:
            section = asset_kind(next(g for g in h.groups() if g is not None))
            continue
        if section is None:
            continue
        m = NUMBERED_RE.match(line)
        if not m:
            continue
        body = m.group(2)
        c = COUNT_RE.search(body)
        stated = int(c.group(1)) if c else None
        text = clean_asset(body[:c.start()] if c else body)
        rsa_finding(findings, i + 1, section, text, stated, line.strip())
    return findings


# ---------------------------------------------------------------- --arith
TOTAL_LABEL = re.compile(r"^\W*(?:grand\s+)?(?:total|totaal|totale|sum|som|totaux|gesamt)\b", re.I)
SUBTOTAL_LABEL = re.compile(r"sub\s*-?\s*tota", re.I)
DERIVED_HDR = re.compile(
    r"rate|ratio|ctr|cpc|cpm|cpa|cpl|cpv|roas|roi|avg|average|gem\.|gemiddel|mean|"
    r"median|\bper\b|position|positie|quality|score|\bqs\b|index|date|datum|year|jaar|"
    r"week|month|maand|rank|\bid\b|^#$|growth|groei|change|verschil|delta|share of voice",
    re.I)
SHARE_HDR = re.compile(r"share|aandeel|\bpart\b|% of|% van|% du|% de|\bmix\b|split|verdeling|^%$", re.I)
NULL_CELL = {"", "-", "\u2013"}


def parse_num(cell: str, decimal: str):
    s = re.sub(r"[*_`    ]", "", cell)
    s = re.sub(r"^(?:EUR|USD|GBP|[€$£])|(?:EUR|USD|GBP|[€$£%])$", "", s)
    s = re.sub(r"^(?:EUR|USD|GBP|[€$£])", "", s)
    if s in ("", "-", "–"):
        return 0.0
    if not re.fullmatch(r"[+-]?\d[\d.,]*", s):
        return None
    thousands = "." if decimal == "," else ","
    if s.count(decimal) > 1:
        return None
    s = s.replace(thousands, "").replace(decimal, ".")
    try:
        return float(s)
    except ValueError:
        return None


def decimals(cell: str, decimal: str) -> int:
    s = re.sub(r"[^\d.,]", "", cell)
    if decimal in s:
        return len(s.rsplit(decimal, 1)[1])
    return 0


def decimal_marks(cells: list[str]) -> tuple:
    """Decimal mark(s) to try: fixed when a cell shows both separators."""
    for c in cells:
        digits = re.sub(r"[^\d.,]", "", c)
        if "." in digits and "," in digits:
            return ("," if digits.rfind(",") > digits.rfind(".") else ".",)
    return (",", ".")


def column_values(cells: list[str], decimal: str):
    vals = [parse_num(c, decimal) for c in cells]
    return None if any(v is None for v in vals) else vals


def fmt(x: float) -> str:
    return f"{x:,.2f}".rstrip("0").rstrip(".")


def check_arith(original: list[str], fenced: list[bool]):
    findings: list[tuple] = []
    stats = {"tables": 0, "columns": 0}
    i = 0
    while i < len(original):
        if fenced[i] or not is_table_head(original, i):
            i += 1
            continue
        head = [c.strip() for c in original[i].strip().strip("|").split("|")]
        rows = list(table_rows(original, i))
        end = rows[-1][0] if rows else i + 1
        totals = [k for k, (_, r) in enumerate(rows) if r and TOTAL_LABEL.match(r[0])
                  and not SUBTOTAL_LABEL.search(r[0])]
        has_subtotals = any(r and SUBTOTAL_LABEL.search(r[0]) for _, r in rows)
        checked_here = False
        for j, name in enumerate(head):
            if j == 0:
                continue
            share = bool(SHARE_HDR.search(name)) and not re.search(r"ctr|rate|share of voice|impression share", name, re.I)
            derived = bool(DERIVED_HDR.search(name)) or (("%" in name) and not share)
            if derived and not share:
                continue
            if share:
                body = [r for k, (_, r) in enumerate(rows) if k not in totals and not (r and SUBTOTAL_LABEL.search(r[0]))]
                cells = [r[j] if j < len(r) else "" for r in body]
                if not cells or not all(re.search(r"\d", c) or c.strip() in NULL_CELL for c in cells):
                    continue
                ok, best = False, None
                for dec in decimal_marks(cells):
                    vals = column_values(cells, dec)
                    if vals is None:
                        continue
                    s = sum(vals)
                    scale = 100.0 if s > 2 else 1.0
                    tol = max(1.0 * scale / 100, len(vals) * 0.5 * 10 ** -max(decimals(c, dec) for c in cells))
                    best = (s, scale)
                    if abs(s - scale) <= tol:
                        ok = True
                if best is None:
                    continue
                stats["columns"] += 1
                checked_here = True
                if not ok:
                    findings.append((i + 1, 1, "arith-share",
                                     f"column '{name}' adds up to {fmt(best[0])}, expected {fmt(best[1])}",
                                     original[i].strip()[:80]))
                continue
            if len(totals) != 1 or totals[0] != len(rows) - 1 or has_subtotals:
                continue
            body = [r for _, r in rows[:-1]]
            total_row_no, total_row = rows[-1]
            if j >= len(total_row) or not re.search(r"\d", total_row[j]):
                continue
            cells = [r[j] if j < len(r) else "" for r in body]
            ok, seen = False, None
            for dec in decimal_marks(cells + [total_row[j]]):
                vals = column_values(cells, dec)
                tot = parse_num(total_row[j], dec)
                if vals is None or tot is None:
                    continue
                d = max([decimals(c, dec) for c in cells + [total_row[j]]] or [0])
                tol = (len(vals) + 1) * 0.5 * 10 ** -d + 1e-9
                seen = (sum(vals), tot)
                if abs(sum(vals) - tot) <= tol:
                    ok = True
            if seen is None:
                continue
            stats["columns"] += 1
            checked_here = True
            if not ok:
                findings.append((total_row_no + 1, 1, "arith-total",
                                 f"column '{name}': total says {fmt(seen[1])}, rows add up to {fmt(seen[0])}",
                                 original[total_row_no].strip()[:80]))
        if checked_here:
            stats["tables"] += 1
        i = end + 1
    return findings, stats


# ---------------------------------------------------------------- --terms
def load_terms(paths: list[str]):
    """Return (variant -> (correct, file)), notes, conflict findings."""
    variants: dict[str, tuple[str, str]] = {}
    corrects: dict[str, str] = {}
    notes: list[str] = []
    conflicts: list[tuple] = []
    for p in paths:
        path = Path(p)
        checked = None
        for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith("source:"):
                m = re.search(r"checked:\s*(\S+)", line, re.I)
                checked = m.group(1) if m else None
                continue
            if "|" not in line:
                continue
            correct, rest = (x.strip() for x in line.split("|", 1))
            if not correct:
                continue
            corrects.setdefault(correct, path.name)
            for v in (x.strip() for x in rest.split(",")):
                if not v or v == correct:
                    continue
                prev = variants.get(v)
                if prev and prev[0] != correct:
                    conflicts.append((0, 0, "terms-conflict",
                                      f"'{v}' -> '{prev[0]}' in {prev[1]} but -> '{correct}' in {path.name}",
                                      raw.strip()[:80]))
                variants[v] = (correct, path.name)
        notes.append(f"{path.name} checked {checked}" if checked
                     else f"{path.name} has no Checked date")
    for v, (correct, f) in variants.items():
        if v in corrects and corrects[v] != f:
            conflicts.append((0, 0, "terms-conflict",
                              f"'{v}' is a correct term in {corrects[v]} but a wrong variant of '{correct}' in {f}",
                              v))
    return variants, notes, conflicts


def check_terms(masked: list[str], original: list[str], variants) -> list[tuple]:
    findings: list[tuple] = []
    compiled = [(re.compile(r"(?<!\w)" + re.escape(v) + r"(?!\w)"), v, c)
                for v, (c, _) in variants.items()]
    for i, line in enumerate(masked):
        for rx, v, correct in compiled:
            for m in rx.finditer(line):
                findings.append((i + 1, m.start() + 1, "terms",
                                 f"'{v}' -> {correct}",
                                 snippet(original[i], m.start(), m.end())))
    return findings


def fence_map(text: str) -> list[bool]:
    out, fenced = [], False
    for raw in text.splitlines():
        if raw.lstrip().startswith("```") or raw.lstrip().startswith("~~~"):
            fenced = not fenced
            out.append(True)
            continue
        out.append(fenced)
    return out


def run_checks(text: str, lang: str, paid: bool, rsa: bool = False,
               arith: bool = False, variants=None, stats=None) -> list[tuple]:
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

    fenced = fence_map(text)
    if rsa:
        findings += check_rsa(original, fenced)
    if arith:
        arith_findings, arith_stats = check_arith(original, fenced)
        findings += arith_findings
        if stats is not None:
            stats.update(arith_stats)
    if variants:
        findings += check_terms(masked, original, variants)

    findings.sort(key=lambda f: (f[0], f[1]))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("file", help="text, Markdown or HTML file, or - for stdin")
    ap.add_argument("--lang", choices=["auto", "en", "nl", "none"], default="auto")
    ap.add_argument("--paid", action="store_true",
                    help="also check keyword tables for an ad group column")
    ap.add_argument("--rsa", action="store_true",
                    help="check RSA headline (30) and description (90) lengths and stated counts")
    ap.add_argument("--arith", action="store_true",
                    help="check table Total rows and share columns")
    ap.add_argument("--terms", action="append", default=[], metavar="TERMS_FILE",
                    help="locked terms file; repeat for brand and product files")
    args = ap.parse_args()

    variants, term_notes, conflicts = ({}, [], [])
    if args.terms:
        missing = [t for t in args.terms if not Path(t).is_file()]
        if missing:
            print(f"Terms file not found: {', '.join(missing)}", file=sys.stderr)
            return 2
        variants, term_notes, conflicts = load_terms(args.terms)

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
    stats: dict = {}
    findings = run_checks(text, lang, args.paid, args.rsa, args.arith, variants, stats)

    for _, _, rule, msg, ctx in conflicts:
        print(f"terms:0:0 [{rule}] {msg}")
    for line, col, rule, msg, ctx in findings:
        print(f"{name}:{line}:{col} [{rule}] {msg}   ...{ctx}...")
    findings += conflicts

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
    if args.rsa:
        ran += ["rsa-length", "rsa-count"]
    if args.arith:
        ran += ["arith-total", "arith-share"]
    if args.terms:
        ran += ["terms"]
    print(f"\nLanguage: {lang}. Checks run: {', '.join(ran)}. Findings: {summary}.")
    if args.arith:
        print(f"Arithmetic: {stats.get('tables', 0)} table(s), {stats.get('columns', 0)} column(s) "
              "recomputed. Figures in running text and derived metrics (rates, averages, "
              "ratios) are not checked.")
    if args.terms:
        print(f"Terms: {len(variants)} variant(s) from {'; '.join(term_notes)}.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
