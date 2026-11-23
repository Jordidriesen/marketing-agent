#!/usr/bin/env python3
"""Tests for the upload-file validators: google_ads_bundle.py and linkedin_files.py.

Run: python3 -m unittest discover -s scripts/tests
"""
from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GADS = ROOT / "plugin/skills/google-ads-build/scripts/google_ads_bundle.py"
LI = ROOT / "plugin/skills/linkedin-ads-manager/scripts/linkedin_files.py"


def write(folder: Path, name: str, header: list[str], rows: list[list[str]]) -> Path:
    path = folder / name
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return path


def run(*args) -> tuple[int, str]:
    p = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def good_bundle(d: Path) -> None:
    write(d, "google-ads-campaigns.csv", ["Campaign", "Campaign type", "Campaign daily budget", "Bid strategy type", "Campaign status"],
          [["Search - Visitor management", "Search", "40", "Maximize clicks", "Scratchpad"]])
    write(d, "google-ads-ad-groups.csv", ["Campaign", "Ad group", "Max CPC"],
          [["Search - Visitor management", "Visitor management software", "2.50"]])
    write(d, "google-ads-keywords.csv", ["Campaign", "Ad group", "Keyword", "Criterion Type"],
          [["Search - Visitor management", "Visitor management software", "visitor management software", "Exact"],
           ["Search - Visitor management", "Visitor management software", "visitor management system", "Phrase"]])
    write(d, "google-ads-negatives.csv", ["Campaign", "Ad group", "Keyword", "Criterion Type"],
          [["Search - Visitor management", "", "free", "Campaign Negative Broad"],
           ["Search - Visitor management", "", "jobs", "Campaign Negative Phrase"]])
    heads = ["QR Check-In for Visitors", "Visitor Management Software", "Know Who Is On Site"]
    write(d, "google-ads-rsas.csv", ["Campaign", "Ad group", "Headline 1", "Headline 2", "Headline 3", "Description 1", "Description 2", "Path 1", "Path 2", "Final URL"],
          [["Search - Visitor management", "Visitor management software", *heads,
            "Visitors pre-register by link and show a QR code at the gate.", "Hosts get a notification when their visitor arrives.",
            "visitors", "qr-check-in", "https://example.com/visitor-management-software/"]])
    write(d, "google-ads-sitelinks.csv", ["Campaign", "Sitelink text", "Description line 1", "Description line 2", "Final URL"],
          [["Search - Visitor management", "Book a demo", "See QR check-in live", "Thirty minutes, no slides", "https://example.com/demo/"]])


class GoogleAdsBundle(unittest.TestCase):
    def test_valid_bundle(self):
        with tempfile.TemporaryDirectory() as t:
            good_bundle(Path(t))
            code, out = run(GADS, t)
            self.assertEqual(code, 0, out)

    def test_problems(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t)
            good_bundle(d)
            write(d, "google-ads-campaigns.csv", ["Campaign", "Campaign type", "Campaign daily budget", "Bid strategy type", "Campaign status"],
                  [["Search - Visitor management", "Search", "40", "Maximize clicks", "Enabled"]])
            write(d, "google-ads-keywords.csv", ["Campaign", "Ad group", "Keyword", "Criterion Type"],
                  [["Search - Visitor management", "Visitor management software", "[visitor management software]", "Exact"],
                   ["Search - Visitor management", "Visitor management software", "free visitor sign in app", "Broad"],
                   ["Search - Visitor management", "Wrong group", "visitor app", ""]])
            write(d, "google-ads-rsas.csv", ["Campaign", "Ad group", "Headline 1", "Headline 2", "Description 1", "Final URL"],
                  [["Search - Visitor management", "Visitor management software", "Visitor Management Software for Offices", "Try it now!", "One — two", ""]])
            code, out = run(GADS, t)
            self.assertEqual(code, 1, out)
            for needle in ("must be Paused or Scratchpad", "match-type symbols", "match type must be Broad",
                           "is not in google-ads-ad-groups.csv", "blocks the keyword 'free visitor sign in app'",
                           "has 39 characters, limit 30", "exclamation mark", "em dash", "at least 3 headlines",
                           "Final URL is empty"):
                self.assertIn(needle, out)

    def test_no_files(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(run(GADS, t)[0], 2)


class LinkedInFiles(unittest.TestCase):
    def test_company_list(self):
        with tempfile.TemporaryDirectory() as t:
            ok = write(Path(t), "ok.csv", ["companyname", "companywebsite", "companycountry"],
                       [["Acme Logistics", "https://acme-logistics.example", "Belgium"]])
            self.assertEqual(run(LI, "companies", ok)[0], 0)
            bad = write(Path(t), "bad.csv", ["companyname", "companywebsite", "email"],
                        [["", "", "a@b.example"], ["Acme", "", ""], ["Acme", "", ""]])
            code, out = run(LI, "companies", bad)
            self.assertEqual(code, 1, out)
            for needle in ("personal-data column", "no identifier", "duplicate company"):
                self.assertIn(needle, out)

    def test_template(self):
        with tempfile.TemporaryDirectory() as t:
            tpl = write(Path(t), "tpl.csv", ["Campaign Name", "Ad Name", "Introductory Text"], [])
            ok = write(Path(t), "ok.csv", ["Campaign Name", "Ad Name", "Introductory Text"], [["C1", "A1", "Plain text"]])
            self.assertEqual(run(LI, "template", ok, tpl)[0], 0)
            bad = write(Path(t), "bad.csv", ["Campaign Name", "Intro"], [["C1", "One — two"]])
            code, out = run(LI, "template", bad, tpl)
            self.assertEqual(code, 1, out)
            self.assertIn("header differs", out)
            self.assertIn("em dash", out)


if __name__ == "__main__":
    unittest.main()
