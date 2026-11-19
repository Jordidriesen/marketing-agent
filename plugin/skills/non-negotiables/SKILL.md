---
name: non-negotiables
description: Hard rules every deliverable must meet, each with how it is checked, loaded by the director, its thread profiles and the skills. Not for direct requests.
user-invocable: false
---

# Non-negotiables: Shared Reference

One module, reusable across every thread profile and skill that produces or accepts a
deliverable. It lists the rules that hold for all work in this plugin and says,
for each one, whether a script can check it or a person has to judge it. The
director writes these into every brief's acceptance criteria and
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
| Dutch output reads as written by a Fleming, not by someone from the Netherlands | Mechanical for the word list, judgement for phrasing | `check_rules.py --lang nl` uses the Netherlands-to-Flanders table in `references/patterns-nl.md`; phrasing and register stay with that skill |
| No invented facts, figures, names, file paths, account IDs or client details | Judgement | Every figure and claim is sourced, or marked `UNSURE` or `PROOF NEEDED`; the reviewer spot-checks the biggest claims against the source |
| Google Ads and paid media analysis names the ad group next to every keyword or search term | Mechanical for tables, judgement for lists | `check_rules.py --paid` flags tables that list keywords with no ad group column |
| Missing goal, audience, facts, brand or source material is asked for before drafting, in a **Needs input** block of 2 to 5 specific questions (why each matters, what happens once answered); a skill's "draft with placeholders" does not override this, and format choices may default if stated | Process | The thread or skill stops before drafting; the director merges the questions and asks once |
| Nothing is sent, published, scheduled or edited live without a clear yes from Jordi | Process | Enforced by the director's ask-before-proceed and ask-before-publish steps, and by `security-policy` for write-capable connectors |

## Running the mechanical checks

Resolve `SCRIPTS` to this skill's `scripts/` folder and use the available
Python 3 launcher:

```bash
python3 "$SCRIPTS/check_rules.py" INPUT                 # language detected
python3 "$SCRIPTS/check_rules.py" INPUT --lang nl       # force Dutch rules
python3 "$SCRIPTS/check_rules.py" INPUT --paid          # add the ad group table check
python3 "$SCRIPTS/check_rules.py" INPUT --rsa           # RSA headline and description lengths
python3 "$SCRIPTS/check_rules.py" INPUT --arith         # table totals and share columns
python3 "$SCRIPTS/check_rules.py" INPUT --terms BRAND.txt --terms PRODUCT.txt   # locked terms
```

The flags combine. Three of them check accuracy rather than a rule from the
table above:

- `--rsa` measures every numbered item under a heading that says Headlines or
  Descriptions, and every cell in a table column with that header, against
  Google's limits (30 and 90 characters). It also flags a stated count, such as
  `(24)`, that does not match the text. It counts plain characters.
- `--arith` recomputes markdown tables whose last row is labelled Total (or
  Totaal, Sum) and checks that share columns (Share, Aandeel, Split, `% of`) add
  up to 100, within rounding. It reads 1.234,5 and 1,234.5. It skips rates,
  averages and ratios (CTR, CPC, ROAS, conversion rate), tables with subtotals,
  and every figure in running text: those stay with the reader. The summary line
  says how many tables and columns it recomputed; zero means nothing was checked.
- `--terms` reads one or more terms files and flags wrong variants of locked
  brand and product names, case-sensitively, outside code, URLs and link
  targets. It reports a conflict when two files disagree on a term. The format
  is below.

### Terms files

One file per brand and one per product where a product has its own names, kept
with the client's jobs: `marketing-jobs/<brand>/terms.txt` and
`marketing-jobs/<brand>/terms-<product>.txt`. Never in this repository.

```
Source: <brand>-brand-kit · Checked: DD/MM/YYYY
# correct form | wrong variants, comma-separated
Acme Access | acme access, ACME Access, AcmeAccess
```

The director compares the file with the brand kit when it writes a brief,
updates it where they differ, sets the Checked date and logs that in
`decisions.md`. The script prints each file's Checked date, so an old file shows.

### Tests

`scripts/tests/` holds a sample with and without the problem for every check.
Run them after any change to the script, from the repository root:

```bash
python3 -m unittest discover -s plugin/skills/non-negotiables/scripts/tests
```

CI runs the same tests on every push and pull request to main.

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
checked by script, add the check to `scripts/check_rules.py`, add a sample with
and without the problem to `scripts/tests/fixtures/` and a test to
`scripts/tests/test_check_rules.py`, and run the tests before relying on it.
