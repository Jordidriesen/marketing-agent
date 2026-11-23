#!/usr/bin/env python3
"""Validate a Google Ads Editor import bundle before anyone imports it.

    python3 google_ads_bundle.py <folder>

Reads the bundle files in <folder> (any that exist), all CSV with Google Ads Editor column names:

  google-ads-campaigns.csv   Campaign, Campaign type, Campaign daily budget, Bid strategy type, Campaign status
  google-ads-ad-groups.csv   Campaign, Ad group, Max CPC
  google-ads-keywords.csv    Campaign, Ad group, Keyword, Criterion Type (Broad | Phrase | Exact)
  google-ads-negatives.csv   Campaign, Ad group (empty for campaign level), Keyword,
                             Criterion Type (Negative Broad | Negative Phrase | Negative Exact |
                             Campaign Negative Broad | Campaign Negative Phrase | Campaign Negative Exact)
  google-ads-rsas.csv        Campaign, Ad group, Headline 1..15, Description 1..4, Path 1, Path 2, Final URL
  google-ads-sitelinks.csv   Campaign, Sitelink text, Description line 1, Description line 2, Final URL
  google-ads-callouts.csv    Campaign, Callout text

Problems reported (one line each): character limits (headline 30, description 90, path 15,
sitelink text 25, sitelink description line 35, callout 25, keyword 80 characters and 10 words),
exclamation marks in headlines, em dashes, missing or unknown match types, match-type symbols in
keyword text, duplicate rows, keywords or ads in ad groups that the bundle does not define,
campaigns not imported as Paused or Scratchpad, RSAs with fewer than 3 headlines or 2 descriptions
or with repeated headlines, and negatives that would block one of the bundle's own keywords.

Exit 0: no problems. Exit 1: problems. Exit 2: no bundle files found. Standard library only.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

FILES = {
    "campaigns": "google-ads-campaigns.csv",
    "ad_groups": "google-ads-ad-groups.csv",
    "keywords": "google-ads-keywords.csv",
    "negatives": "google-ads-negatives.csv",
    "rsas": "google-ads-rsas.csv",
    "sitelinks": "google-ads-sitelinks.csv",
    "callouts": "google-ads-callouts.csv",
}
POSITIVE = {"broad", "phrase", "exact"}
NEGATIVE = {"negative broad", "negative phrase", "negative exact",
            "campaign negative broad", "campaign negative phrase", "campaign negative exact"}
LIMITS = {"Headline": 30, "Description": 90, "Path 1": 15, "Path 2": 15,
          "Sitelink text": 25, "Description line 1": 35, "Description line 2": 35, "Callout text": 25}
EM_DASH = "—"


def read(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return [{(k or "").strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def words(text: str) -> list[str]:
    return re.findall(r"[\w'&+.-]+", text.lower())


def blocks(neg: str, neg_type: str, kw: str) -> bool:
    """Would this negative stop the keyword's own text from matching?"""
    n, k = words(neg), words(kw)
    if neg_type.endswith("exact"):
        return n == k
    if neg_type.endswith("phrase"):
        return any(k[i:i + len(n)] == n for i in range(len(k) - len(n) + 1)) if n else False
    return bool(n) and set(n) <= set(k)


def check(folder: Path) -> list[str]:
    data = {key: read(folder / name) for key, name in FILES.items() if (folder / name).is_file()}
    if not data:
        return ["no bundle files found"]
    out: list[str] = []

    def where(key, i):
        return f"{FILES[key]} row {i + 2}"

    for key, rows in data.items():
        seen = set()
        for i, row in enumerate(rows):
            sig = tuple(sorted(row.items()))
            if sig in seen:
                out.append(f"{where(key, i)}: duplicate row")
            seen.add(sig)
            for col, val in row.items():
                if EM_DASH in val:
                    out.append(f"{where(key, i)}: em dash in {col}")
                base = re.sub(r"\s+\d+$", "", col) if col.startswith(("Headline", "Description ")) else col
                limit = LIMITS.get(col) or LIMITS.get(base)
                if limit and val and len(val) > limit:
                    out.append(f"{where(key, i)}: {col} has {len(val)} characters, limit {limit}: {val!r}")
                if col.startswith("Headline") and "!" in val:
                    out.append(f"{where(key, i)}: exclamation mark in {col} (not allowed in headlines)")

    groups = {(r.get("Campaign", ""), r.get("Ad group", "")) for r in data.get("ad_groups", [])}
    campaigns = {r.get("Campaign", "") for r in data.get("campaigns", [])} | {c for c, _ in groups}

    for i, r in enumerate(data.get("campaigns", [])):
        status = r.get("Campaign status", "").lower()
        if status not in ("paused", "scratchpad"):
            out.append(f"{where('campaigns', i)}: Campaign status must be Paused or Scratchpad, found {r.get('Campaign status')!r}")

    for i, r in enumerate(data.get("keywords", [])):
        kw, mt = r.get("Keyword", ""), r.get("Criterion Type", "").lower()
        if mt not in POSITIVE:
            out.append(f"{where('keywords', i)}: match type must be Broad, Phrase or Exact, found {r.get('Criterion Type')!r}")
        if re.search(r'[\[\]"+]', kw):
            out.append(f"{where('keywords', i)}: match-type symbols in keyword text {kw!r}; put the match type in Criterion Type")
        if len(kw) > 80 or len(kw.split()) > 10:
            out.append(f"{where('keywords', i)}: keyword over 80 characters or 10 words: {kw!r}")
        if groups and (r.get("Campaign", ""), r.get("Ad group", "")) not in groups:
            out.append(f"{where('keywords', i)}: ad group {r.get('Ad group')!r} in {r.get('Campaign')!r} is not in google-ads-ad-groups.csv")

    for i, r in enumerate(data.get("negatives", [])):
        mt = r.get("Criterion Type", "").lower()
        if mt not in NEGATIVE:
            out.append(f"{where('negatives', i)}: negative match type not recognised: {r.get('Criterion Type')!r}")
            continue
        if mt.startswith("campaign") and r.get("Ad group"):
            out.append(f"{where('negatives', i)}: campaign negative with an ad group filled in; leave Ad group empty")
        for kw in data.get("keywords", []):
            same_scope = kw.get("Campaign") == r.get("Campaign") and (
                mt.startswith("campaign") or not r.get("Ad group") or kw.get("Ad group") == r.get("Ad group"))
            if same_scope and blocks(r.get("Keyword", ""), mt, kw.get("Keyword", "")):
                out.append(f"{where('negatives', i)}: {r.get('Criterion Type')} {r.get('Keyword')!r} blocks the keyword "
                           f"{kw.get('Keyword')!r} in {kw.get('Campaign')!r} / {kw.get('Ad group')!r}")

    for i, r in enumerate(data.get("rsas", [])):
        heads = [v for k, v in r.items() if re.fullmatch(r"Headline \d+", k) and v]
        descs = [v for k, v in r.items() if re.fullmatch(r"Description \d+", k) and v]
        if len(heads) < 3 or len(descs) < 2:
            out.append(f"{where('rsas', i)}: needs at least 3 headlines and 2 descriptions, found {len(heads)} and {len(descs)}")
        dup = {h for h in heads if heads.count(h) > 1}
        if dup:
            out.append(f"{where('rsas', i)}: repeated headline(s): {sorted(dup)}")
        if not r.get("Final URL"):
            out.append(f"{where('rsas', i)}: Final URL is empty")
        if groups and (r.get("Campaign", ""), r.get("Ad group", "")) not in groups:
            out.append(f"{where('rsas', i)}: ad group {r.get('Ad group')!r} is not in google-ads-ad-groups.csv")

    for key in ("sitelinks", "callouts"):
        for i, r in enumerate(data.get(key, [])):
            if campaigns and r.get("Campaign") not in campaigns:
                out.append(f"{where(key, i)}: campaign {r.get('Campaign')!r} is not in the bundle")
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    problems = check(Path(sys.argv[1]))
    if problems == ["no bundle files found"]:
        print("no Google Ads bundle files found in", sys.argv[1])
        return 2
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)" if problems else "bundle valid")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
