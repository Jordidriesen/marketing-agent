# Job folder templates

## brief.md

```markdown
# <Job title>

- Brand: <brand> (brand kit: <[brand]-brand-kit>)
- What the brand sells: <copied word for word from the request or the brand kit; threads and the cold reviewer judge claims against this line>
- Date opened: <DD/MM/YYYY>
- Goal: <one sentence>
- Audience: <who, in which situation>
- Market and locales: <for example Belgium, nl-BE and fr-BE>
- Product facts that may be used: <list; mark unconfirmed facts "confirm">
- Constraints: <budget, dates, channels, legal, words to avoid>
- Proof available: <customers, figures, quotes; or "none">
- Storage: <linked folder path, or repository and branch; push agreed yes / no>
- Terms files: <brand/terms.txt, brand/terms-<product>.txt in the storage root; or "none yet">
- Voice examples: <brand/voice-examples.md, or "none yet">
- Connectors this job needs: <list; anything else is a reason to ask>

## What we already know

<rows from brand/learnings.md that touch this job, with dates and confidence; or "nothing logged yet">

## Deliverables

| # | Deliverable | Format and length | Done when |
|---|---|---|---|
| 1 | | | |

## Acceptance criteria (for every deliverable)

- In scope / out of scope:
- The non-negotiables apply.
- <criteria specific to this job>
```

## plan.md

The record of where the job stands. Only the director edits it; threads read it
and report back. A job reopened in a new session starts from this file.

```markdown
# Plan

| # | Step | Skill / reference | Depends on | Owner | Status | Output | Notes |
|---|---|---|---|---|---|---|---|
| 1 | <step> | <skill, reference> | none | director | To do | | |
| 2 | <step> | <skill> | 1 | <profile> (rule <n>) | To do | | |
```

Status is one of: To do, In progress, Waiting on user, Sent back, Done, Dropped.
On Sent back, Notes quotes the criterion that failed. Output is the path in
`research/` or `deliverables/` once the file exists.

## Terms files (per brand, outside the job folder)

`brand/terms.txt` in the storage root (`marketing-jobs/<brand>/` in a linked
folder, the repository root in a client repository), plus
`brand/terms-<product>.txt` for a product with its own names. Layout:
`references/storage.md`. Format and checks: `non-negotiables`, section Terms files.

```
Source: <brand>-brand-kit · Checked: DD/MM/YYYY
# correct form | wrong variants, comma-separated
<Correct Name> | <variant>, <variant>
```

## decisions.md

```markdown
# Decisions

- DD/MM/YYYY: <decision, and who made it>
- DD/MM/YYYY: Thread <profile> spawned for <task>. Rule: <1 parallel / 2 noise / 3 fresh eyes / 4 model or tools>. Model: <model>. Effort: <effort>. Tokens: <from the Agent result>. Time: <duration>.
- DD/MM/YYYY: Storage: <linked folder / repository and branch>. Checks passed: <list>. Push: <yes / no>, agreed by <who>.
- DD/MM/YYYY: Terms files checked against <brand>-brand-kit: <files>, <updated / no change>.
- DD/MM/YYYY: Threads: <n>, <total> tokens (main thread not counted).
- DD/MM/YYYY: Review tier <none / light / full-sonnet / full-opus> for <job>, because <reason>.
```
