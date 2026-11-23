#!/usr/bin/env python3
"""Validate LinkedIn Campaign Manager upload files before anyone uploads them.

    python3 linkedin_files.py companies <linkedin-company-list.csv>
    python3 linkedin_files.py template <filled.csv> <template.csv>

companies: a Matched Audiences company list. Every row needs at least one identifier
(companyname, companywebsite, companyemaildomain, linkedincompanypageurl, stocksymbol); columns
must come from LinkedIn's company template; no personal-data columns (email, first or last name,
phone) and no duplicate companies. Contact lists are never built by the plugin.

template: a bulk campaign or ad file filled from the account's own Campaign Manager template.
The header must equal the template's header exactly, and no cell may hold an em dash.

Exit 0: valid. Exit 1: problems. Exit 2: usage or unreadable file. Standard library only.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

COMPANY_COLUMNS = ["companyname", "companywebsite", "companyemaildomain", "linkedincompanypageurl",
                   "stocksymbol", "industry", "city", "state", "companycountry", "zipcode"]
IDENTIFIERS = {"companyname", "companywebsite", "companyemaildomain", "linkedincompanypageurl", "stocksymbol"}
PERSONAL = {"email", "emailaddress", "firstname", "lastname", "phone", "phonenumber", "jobtitle", "employeecompany"}
EM_DASH = "—"


def rows(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        data = [{(k or "").strip(): (v or "").strip() for k, v in r.items()} for r in reader]
        return [h.strip() for h in (reader.fieldnames or [])], data


def check_companies(path: Path) -> list[str]:
    header, data = rows(path)
    out = []
    norm = [h.lower().replace(" ", "") for h in header]
    for h in norm:
        if h in PERSONAL:
            out.append(f"personal-data column {h!r}: company lists hold companies only")
        elif h not in COMPANY_COLUMNS:
            out.append(f"column {h!r} is not in LinkedIn's company template")
    seen = set()
    for i, r in enumerate(data):
        r = {k.lower().replace(" ", ""): v for k, v in r.items()}
        if not any(r.get(k) for k in IDENTIFIERS):
            out.append(f"row {i + 2}: no identifier (companyname, companywebsite, companyemaildomain, linkedincompanypageurl or stocksymbol)")
        key = (r.get("companyname", "").lower(), r.get("companywebsite", "").lower().rstrip("/"))
        if key in seen and any(key):
            out.append(f"row {i + 2}: duplicate company {r.get('companyname') or r.get('companywebsite')!r}")
        seen.add(key)
        for k, v in r.items():
            if EM_DASH in v:
                out.append(f"row {i + 2}: em dash in {k}")
    return out


def check_template(filled: Path, template: Path) -> list[str]:
    head_f, data = rows(filled)
    head_t, _ = rows(template)
    out = []
    if head_f != head_t:
        missing = [h for h in head_t if h not in head_f]
        extra = [h for h in head_f if h not in head_t]
        out.append(f"header differs from the account's template (missing: {missing}, extra: {extra}, or a different order)")
    for i, r in enumerate(data):
        for k, v in r.items():
            if EM_DASH in v:
                out.append(f"row {i + 2}: em dash in {k}")
    return out


def main() -> int:
    try:
        if len(sys.argv) == 3 and sys.argv[1] == "companies":
            problems = check_companies(Path(sys.argv[2]))
        elif len(sys.argv) == 4 and sys.argv[1] == "template":
            problems = check_template(Path(sys.argv[2]), Path(sys.argv[3]))
        else:
            print(__doc__, file=sys.stderr)
            return 2
    except OSError as exc:
        print(f"cannot read file: {exc}", file=sys.stderr)
        return 2
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)" if problems else "valid")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
