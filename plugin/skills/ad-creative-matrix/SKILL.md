---
name: ad-creative-matrix
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Writes up the 50-5-3 ad method (50 hooks, 5 bodies, 3 CTAs), commonly attributed to Alex Hormozi, as an original workflow in this library's own terms: angle spread, a screening rubric, a compatibility check, tagged assembly and a staged test plan scaled to budget. The attribution has not been checked against a primary source.\n"
description: "Builds paid social and video ad sets with the 50-5-3 method (50 hooks, 5 bodies, 3 CTAs), screened, tagged and with a test plan, for LinkedIn, Meta, YouTube, TikTok. Use for \"ad hooks\", \"ad variations\", \"LinkedIn or Meta ads\"."
argument-hint: "<offer, audience, platform(s) and any budget or proof you can share>"
---

# Ad creative matrix (50-5-3)

You build ad creative like a modular kit, not like fifty separate ads. One offer, three kinds of
part: **50 hooks**, **5 bodies**, **3 CTAs**. Any hook can sit on any body and any CTA, which
gives 750 possible ads from 58 pieces of writing, and every result traces back to the one part that
caused it.

The method is commonly attributed to Alex Hormozi. This skill is an original write-up of the
workflow in this library's terms, not a copy of anyone's course material.

## The honest limit, stated up front

Fifty hooks is a generation target, not a test plan. Most accounts cannot put enough spend behind
fifty live ads to tell them apart, and B2B campaigns with small budgets and few conversions
certainly cannot. So you generate widely, **screen** hard, and test a shortlist in stages sized to
the real budget. The screening score is structured judgement, not a prediction of performance, and
you say so in the output.

## Inputs you need

- **The offer**, in one sentence. If this is unclear, ask one question before writing anything.
- **The audience**: role, situation, what they already believe. Take it from the brand kit's
  `references/context.md` when there is one.
- **Platform(s)** and **medium** (static, document, video).
- **Verifiable specifics** the user supplies: numbers, timeframes, named proof, guarantees.
  Only these may appear as claims.
- **Budget and expected volume**, if known. They set how many variants can run (Step 7).
- **Language and market.** Write in the brand's market language.

## Step 0: Load the brand

Determine which brand or client this is for and load its `[brand]-brand-kit` skill: voice
(`references/voice.md`) for tone and locked terms, context (`references/context.md`) for audience
and channels. Older kits keep this in a separate tone-of-voice skill. The kit's locked wording
and banned list outrank everything below. With no kit, say so and write in a plain, neutral
register.

For work that needs competitor angles first, run `competitor-teardown` and feed its open
positioning list in as inputs. For anything built on behavioural principles, pull
`content-references/references/behavioral-psychology.md`.

## Step 1: Fix the offer and the audience

State both in two lines and confirm anything you are assuming. Everything later depends on one
offer and one audience. A second offer is a second matrix.

## Step 2: Write 50 hooks

Use `references/angle-library.md`, section 1. Spread them across the angles (about five per
angle, ten angles), then vary the wording inside each angle.

- Tag every hook `H01` to `H50` with its angle.
- For video, each hook is three parts: the spoken line, the on-screen text, one shot description.
- For static and document ads, each hook is the first line of the primary text plus the headline.
- Check the visible character limit in `references/platform-limits.md` and count characters.
  Report the count next to each hook.
- Use only the specifics the user supplied. If a hook would need a number you do not have, write
  the version without the number, or mark the gap, but never invent one.

## Step 3: Screen to a shortlist

Score all 50 with the rubric in `references/angle-library.md`, section 4, and apply its selection
rules. Output the full scored table and the shortlist (8 to 10 by default, fewer if the budget
says so). Keep at least four angles in the shortlist.

State plainly that the scores are judgement, not forecasts.

## Step 4: Write 5 bodies

Use the structures in `references/angle-library.md`, section 2. Each body is a different
structure, written so it follows any hook without a seam. If the user lacks the input a structure
needs (verified proof, a real before and after), swap the structure and tell them why.

## Step 5: Write 3 CTAs

One per rung of the commitment ladder (`references/angle-library.md`, section 3). Respect locked
CTA wording from the brand kit. Match the CTA line to the platform's CTA button.

## Step 6: Assemble and check

1. Run the compatibility check (`references/angle-library.md`, section 5) across the shortlist,
   the bodies and the CTAs. Record incompatible pairings in the matrix.
2. Assemble 3 to 5 full example ads from the shortlist so the user sees real combinations, each
   tagged with the naming convention in `references/platform-limits.md`.
3. Run `ai-content-cleaner` in CLEAN mode on every hook, body and CTA. Then run `brand-review` on
   anything that makes a claim, particularly for regulated or security topics. Both come before
   delivery, not after.

## Step 7: Write the test plan

Size it to the budget, not to the ambition.

| Situation | Shape of the plan |
|---|---|
| Healthy volume and budget | Stage 1: shortlist hooks on one fixed body and one fixed CTA. Stage 2: best hooks across the bodies. Stage 3: best pairings across the CTAs. |
| Small budget or low conversion volume | Test 3 to 4 hooks at a time, rotate new hooks in as others are retired, and judge on the metric with enough events to read (often click-through or cost per click, not final conversions). |
| No budget figure given | Ask for it, or write the staged plan and mark the stage sizes as unknown. |

Rules for the plan:

- Change one part at a time, so a difference has one cause.
- Decide the stopping rule before launch, in the user's metric, and write it down.
- Do not state significance thresholds, sample sizes or expected lifts as facts. They depend on
  the account's real volumes. Offer to derive them from the user's figures when given.
- Name every live ad with the convention so `ad-copy-tester` and `paid-ads-report-writer` can read
  results back to hook, body and CTA.

## Output

Deliver, in this order:

1. The offer and audience lines, and any assumption made.
2. The 50 hooks as a table: ID, angle, text, character count (or the three video parts).
3. The scoring table and the shortlist.
4. The 5 bodies and 3 CTAs, with their IDs.
5. The compatibility notes.
6. 3 to 5 assembled example ads, tagged.
7. The staged test plan.
8. Open items: missing proof, claims that need a source, hooks near a policy line.

Deliver the full matrix as a sheet when a spreadsheet route exists (the `xlsx` skill or the Google
Drive connector, which the user must approve before anything is written). Otherwise deliver
markdown tables. Chat framing stays short; the deliverable keeps its full length.

## Rules

- **Never invent specifics.** No made-up figures, customers, results, testimonials or deadlines.
  Every claim traces to something the user gave you, or the gap is marked.
- **Every ad is a claim someone will read.** Anything touching security, compliance, finance or
  health goes through `brand-review`, and the open claims are listed for the user.
- **Never assert a personal attribute of the viewer** in a hook. Check the platform's current ad
  policy when a hook gets close.
- **No em dashes** in any ad copy. No exclamation marks unless the brand kit's voice allows them.
- Do not write fifty versions of one idea. If two hooks could be swapped without anyone noticing,
  cut one.
- Hooks and bodies for other languages are **re-written, not translated word for word**. Use
  `content-translate` for the locale pass and for locked terminology.

## Related Skills

- `competitor-teardown`: upstream. Its open-positioning list supplies angles worth writing hooks
  for.
- `creative-brief`: downstream. Turns the winning hooks and bodies into a visual direction and a
  deliverables table with real formats.
- `canva-workflow`, `figma-weavy-workflow`: produce the visual assets once the brief exists.
- `rsa-writer`: the Google search equivalent, with its own character limits and no hook, body and
  CTA structure.
- `social-content-writer`: organic posts. This skill is for paid ads.
- `ad-copy-tester`: reads asset performance once ads are live and calls keep, cut or replace.
- `content-translate`: locale versions after the source set is approved.
- `brand-review`, `ai-content-cleaner`: the gates before delivery.
- `campaign-plan`: the campaign context this creative serves.
- `content-references`: `behavioral-psychology.md` and `communication-frameworks.md` for the
  angle and structure work.
