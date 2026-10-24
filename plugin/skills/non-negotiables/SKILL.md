---
name: non-negotiables
description: "Hard rules every deliverable must meet, each with how it is checked, loaded by the director and the specialists. Not for direct requests."
---

# Non-negotiables: Shared Reference

One module, reusable across every agent and skill that produces or accepts a
deliverable. It lists the rules that hold for all work in this plugin and says,
for each one, whether a script can check it or a person has to judge it. The
marketing-director writes these into every brief's acceptance criteria and
checks the returned work against them.

## How this layers with a brand kit

- **Brand kit first for style.** A loaded `[brand]-brand-kit` adds rules per
  brand. Where its voice module names a different language variety, punctuation
  rule or terminology, the kit wins over the language and punctuation rows below.
- **Never relaxed by any kit:** the honesty rows (no invented facts) and the
  gating row (no sending, publishing or live edits without a clear yes).
- Anything held back because a kit overrode a row here is named in the
  deliverable's notes, so Jordi can overrule it.

## The rules

| Rule | Check | How |
|---|---|---|
| No em dashes (U+2014) in any output | Mechanical | `check_rules.py` |
| English output in en_GB: British spelling, British date format (24 October 2026), no US vocabulary | Mechanical for common cases, judgement for the rest | `check_rules.py` lists candidates; a US spelling it does not know will slip through |
| Dutch output reads as written by a Fleming, not by someone from the Netherlands | Mechanical for the word list, judgement for phrasing | `check_rules.py --lang nl` uses the Netherlands-to-Flanders table in `ai-content-cleaner/references/patterns-nl.md`; phrasing and register stay with that skill |
| No invented facts, figures, names, file paths, account IDs or client details | Judgement | Every figure and claim is sourced, or marked `UNSURE` or `PROOF NEEDED`; the reviewer spot-checks the biggest claims against the source |
| Google Ads and paid media analysis names the ad group next to every keyword or search term | Mechanical for tables, judgement for lists | `check_rules.py --paid` flags tables that list keywords with no ad group column |
| Nothing is sent, published, scheduled or edited live without a clear yes from Jordi | Process | Enforced by the director's ask-before-proceed and ask-before-publish steps, and by `security-policy` for write-capable connectors |

## Running the mechanical checks

Resolve `SCRIPTS` to this skill's `scripts/` folder and use the available
Python 3 launcher:

```bash
python3 "$SCRIPTS/check_rules.py" INPUT                 # language detected
python3 "$SCRIPTS/check_rules.py" INPUT --lang nl       # force Dutch rules
python3 "$SCRIPTS/check_rules.py" INPUT --paid          # add the ad group table check
```

Use `-` for INPUT to read stdin. The script reads text, Markdown and HTML
source; never pass a PDF, DOCX, image or archive. It skips fenced code, inline
code, URLs, link targets and HTML tags. Exit code 1 means it found candidates,
0 means none.

**What a clean run means.** The language checks are a blocklist: they find
known US spellings, US date order and US words, so that they can be fixed. They
do not prove the text is en_GB or Belgian Dutch, because that would need a full
British dictionary and a reader. Report a clean run as "no known US patterns
found", never as "en_GB passed", and still read for British phrasing.

**Findings are candidates, not verdicts.** An em dash inside a verbatim client
quote, or "center" inside a product name, is a call for the reviewer. Judge each
finding, fix the clear ones, and list anything kept with the reason.

## Reporting

End the review with one line, in the same style as the `Skills run` line:

`Rules checked: <mechanical rules run>. Judged by reading: <rules>. Not checked: <rules and why>.`

A rule that could not be checked (no Bash, wrong file type) goes under Not
checked. Never write that a rule passed when it was not run.

## Adding a rule

Add a row only for a rule Jordi has stated. Say how it is checked. If it can be
checked by script, add the check to `scripts/check_rules.py` and test it on a
sample with and without the problem before relying on it.
