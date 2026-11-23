#!/usr/bin/env python3
"""PostToolUse hook: run check_rules.py on a deliverable as soon as it is saved.

Fires after Write, Edit and MultiEdit, in the main thread and in threads. Acts only on
.md, .txt, .html and .csv files inside a folder named `deliverables`. A Google Ads Editor bundle
file (google-ads-*.csv) also runs google_ads_bundle.py on its folder, and a LinkedIn company list
(linkedin-company-list*.csv) runs linkedin_files.py. Also fires after a shell
command (Bash or PowerShell) that mentions `deliverables`: it then checks the deliverable files under the
working directory that changed in the last two minutes, so a file written with a shell
command is checked too. Reports hard findings
only (em dash, RSA lengths and counts, totals and shares, locked terms, ad group column);
spelling and date candidates stay with the director's acceptance step.

Exit 0: nothing to report. Exit 2: hard findings, sent back to whoever wrote the file.
Standard library only.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HARD = {"em-dash", "rsa-length", "rsa-count", "arith-total", "arith-share",
        "terms", "terms-conflict", "ad-group"}
TEXT = {".md", ".txt", ".html", ".htm", ".csv"}
PLUGIN = Path(__file__).resolve().parent.parent
GADS = PLUGIN / "skills" / "google-ads-build" / "scripts" / "google_ads_bundle.py"
LINKEDIN = PLUGIN / "skills" / "linkedin-ads-manager" / "scripts" / "linkedin_files.py"
CHECKER = Path(__file__).resolve().parent.parent / "skills" / "non-negotiables" / "scripts" / "check_rules.py"
RECENT_SECONDS = 120
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build"}
MAX_DIRS = 5000


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


def is_deliverable(path: Path) -> bool:
    return "deliverables" in path.parts and path.suffix.lower() in TEXT and path.is_file()


def recent_deliverables(root: Path) -> list[Path]:
    """Deliverable files under root changed in the last RECENT_SECONDS."""
    cutoff, found, seen = time.time() - RECENT_SECONDS, [], 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        seen += 1
        if seen > MAX_DIRS:
            break
        if "deliverables" not in Path(dirpath).parts:
            continue
        for name in filenames:
            p = Path(dirpath) / name
            try:
                if p.suffix.lower() in TEXT and p.stat().st_mtime >= cutoff:
                    found.append(p)
            except OSError:
                pass
    return sorted(found)


def targets(event: dict) -> list[Path]:
    tool_input = event.get("tool_input") or {}
    if event.get("tool_name") in ("Bash", "PowerShell"):
        command = str(tool_input.get("command") or "")
        if "deliverables" not in command:
            return []
        return recent_deliverables(Path(event.get("cwd") or os.getcwd()))
    raw = tool_input.get("file_path") or ""
    path = Path(raw) if raw else None
    return [path] if path and is_deliverable(path) else []


def upload_file_findings(path: Path) -> list[str]:
    """Validator problems for Google Ads Editor bundles and LinkedIn company lists."""
    name = path.name.lower()
    if name.startswith("google-ads-") and GADS.is_file():
        cmd = [sys.executable, str(GADS), str(path.parent)]
        label = "google-ads bundle"
    elif name.startswith("linkedin-company-list") and LINKEDIN.is_file():
        cmd = [sys.executable, str(LINKEDIN), "companies", str(path)]
        label = path.name
    else:
        return []
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 1:
        return []
    return [f"{label}: {line}" for line in proc.stdout.splitlines()
            if line.strip() and not line.endswith("problem(s)")]


def hard_findings(path: Path) -> list[str]:
    if path.suffix.lower() == ".csv":
        found = upload_file_findings(path)
    else:
        found = []
    proc = subprocess.run([sys.executable, str(CHECKER), str(path), *flags_for(path)],
                          capture_output=True, text=True, encoding="utf-8")
    hard = found
    for line in proc.stdout.splitlines():
        m = re.search(r"\[([a-z-]+)\]", line)
        if m and m.group(1) in HARD:
            hard.append(line.strip())
    return hard


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    files = targets(event)
    if not files:
        return 0
    if not CHECKER.is_file():
        print(f"check_deliverable: checker not found at {CHECKER}", file=sys.stderr)
        return 1
    report = []
    for path in files:
        hard = hard_findings(path)
        if hard:
            report.append((path, hard))
    if not report:
        return 0
    total = sum(len(h) for _, h in report)
    print(f"check_rules.py found {total} hard finding(s) in {', '.join(p.name for p, _ in report)}. "
          "Fix the clear ones now; keep one only if it is verbatim client text, and say why.",
          file=sys.stderr)
    shown = 0
    for _, hard in report:
        for line in hard:
            if shown == 40:
                break
            print("  " + line, file=sys.stderr)
            shown += 1
    if total > shown:
        print(f"  ... and {total - shown} more", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
