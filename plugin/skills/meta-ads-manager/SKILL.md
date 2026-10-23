---
name: meta-ads-manager
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Builds or restructures Meta (Facebook and Instagram) campaigns as a paste-ready build plan: objective and funnel stage, Advantage+ against manual structure, audiences and exclusions, placements, budget and pacing, creative specs, and the pixel, Conversions API and consent checklist. No Meta connector exists yet, so the plan is the deliverable.\n"
description: "Always use for any Meta, Facebook or Instagram ads campaign plan or restructure, however short: objective, Advantage+ vs manual, audiences and exclusions, placements, budget, creative specs, pixel and Conversions API checklist. Use for \"Meta ads\", \"Facebook campaign\", \"Advantage+\". Ad creative: ad-creative-matrix. Google Ads: campaign-architect."
argument-hint: "<the brand, the goal, the budget and period, the audience, and whether to plan only or also build via a connected tool>"
---

# Meta ads manager

You turn a goal and a budget into a Meta campaign that a person can build in Ads Manager in one sitting,
or that a connected tool can build once one exists. Meta changes its campaign flow often, so the plan is
written in stable concepts (objective, optimisation event, audience, placement, budget, tracking) and
every setting a person must confirm in the live interface is marked **confirm in Ads Manager**.

**Required skill calls.** When the plan needs ad creative or copy, call `ad-creative-matrix` through the Skill
tool; never write hooks or ad variants inline. Nothing in this plan is final until `brand-review` has seen the
copy. End the reply with one line: `Skills run: ...`.

## Connector status

No Meta connector is installed in this library yet. Say so in the first line of the output: "Meta is not
connected, so this is a build plan, not a built campaign." The plan stays complete and paste-ready, and
nothing is created, changed or paused in any account. Should a connector exist, build only after
explicit approval, per `security-policy`.

## Inputs you need

- **The brand and the offer**, from the `[brand]-brand-kit` and its product files.
- **The goal and the conversion that proves it**: leads, sales, traffic or reach, and the event that
  counts. If the goal is vague, ask one question before planning.
- **Budget and period**, and the **audience**: who, where (countries, regions), language.
- **Tracking state**: pixel and Conversions API installed or not, which events fire, consent banner in
  place. Unknown means it goes on the Could not verify list and the tracking checklist comes first.
- **History**: the account's own cost per result for this goal, if any. Without it, targets stay open.

## Step 0: Load the brand

Load the `[brand]-brand-kit`: `context.md` for markets and audience, the voice module and the product
files for what may be claimed. With no kit, say so and plan on the brief alone.

## Step 1: Objective and funnel stage

Choose the objective from the goal, not from habit: awareness, traffic, engagement, leads, app
promotion or sales. Then choose the **optimisation event** (the action Meta will hunt for), and be strict
about it: optimise for the highest-intent event the budget can feed with enough events for Meta's
learning phase (Ads Manager shows the current threshold: **confirm in Ads Manager**). A budget that
cannot produce those events for the chosen event means moving one step up the funnel and saying so.
For lead goals, state the route: instant (on-platform) form or website landing page, with the trade-off
(lower friction against lead quality and tracking depth).

## Step 2: Structure

Pick one structure and defend it:

- **Advantage+ campaign** (Meta's automated setup, which Meta increasingly makes the default for sales
  and lead goals): for accounts with proven creative and steady conversion volume. Few ad sets, broad
  audience signals, creative as the main lever.
- **Manual structure**: when the account is new or has little conversion data, when audience control
  matters (a small named audience, a restricted market), or when a test needs clean separation.

Name the campaign and ad set naming convention (goal, audience, geography, date) so reports stay
readable. Use campaign-level budget (Meta's automatic distribution) unless there is a stated reason to fix
budgets per ad set.

## Step 3: Audiences and exclusions

List each audience with its source and size where known: **broad** (location, age and language only, and
Meta's targeting suggestions as signals), **custom** (customer lists, website visitors, engagement),
**lookalike** (from a source list that is large and good enough to learn from; a poor source makes a
poor lookalike), **retargeting** (visitors, engagers, a short list of recency windows). Always list the
**exclusions**: existing customers, converters, employees and, to avoid overlap, the retargeting pools
from prospecting. Flag any overlap between ad sets that would make them compete in the same auction.
Audience lists come from the user or `abm-plan`; never invent them. Check Meta's current rules for
special ad categories and sensitive targeting before using any audience that touches them (**confirm in
Ads Manager**).

## Step 4: Placements, budget and pacing

Default to automatic placements unless a placement is excluded for a stated reason (a creative format
that cannot work there). **Budget**: show the arithmetic in one table: daily or lifetime budget, period,
target cost per result from the account's own history, and the resulting results per week. If there is
no history, leave the target open and plan a learning period with a stated stop-or-scale rule. No cost benchmarks from this skill or from memory, and no placeholder or scenario values for cost per result, CPM or CPC: show the arithmetic as a formula (results = budget / cost per result) or a table whose cost column is left blank for the user to fill in. Pacing: when to leave the campaign alone, when to review, and
the signals that justify a change (and the ones that do not, such as one bad day).

## Step 5: Creative requirements

State what the structure needs: how many distinct concepts, formats (static, video, carousel), aspect
ratios for feed, stories and reels (commonly 1:1, 4:5 and 9:16; **confirm current specs in Ads
Manager**), safe zones, text length, and the language. Hand the creative itself to `ad-creative-matrix`.
Check each ad's landing page for message match with `landing-page-matcher`.

## Step 6: Tracking and consent checklist

Pass or fail, each with the fix: Meta pixel installed and firing on the goal event; Conversions API
sending the same events from the server with deduplication against the pixel; event parameters
(value, currency) present where the goal needs them; domain verification and event prioritisation done
where Ads Manager asks for them; a consent banner in place for the markets served, with the pixel
respecting the choice (a legal question that stays on the Needs decision list); UTM parameters on every ad
URL, following the property's taxonomy (`ga4-audit`); the conversion also visible in GA4 so Meta's
numbers can be reconciled (`attribution-readout`).

## Step 7: Launch checklist

Policy and special-category check, creative and copy approved, tracking tested with a real conversion,
budget and schedule match the plan, naming applied, exclusions set, a review date in the calendar.

## Output

1. The connector line and a two-sentence summary: goal, structure, budget.
2. **Build plan table**: campaign, objective, optimisation event, structure, budget, schedule.
3. **Ad set table**: audience, source, size if known, exclusions, placements, budget.
4. **Budget arithmetic** and the stop-or-scale rule.
5. **Creative requirements** and the hand-off to `ad-creative-matrix`.
6. **Tracking and consent checklist** and the **launch checklist**.
7. **Needs decision** and **Could not verify** lists, with every **confirm in Ads Manager** item.

Deliver in the reply, or as a document in the run folder when one is in use.

## Rules

- Nothing goes live, is created or is changed without explicit approval, per `security-policy`.
- No invented CPMs, CPCs, cost per result or audience sizes, and no placeholder or scenario values for them; targets come from the account's own history or stay open.
- No invented audiences, customer lists or custom audience sizes.
- A budget too small for the chosen optimisation event is called out, never hidden.
- Microsoft Advertising is parked: no skill for it yet.
- No em dashes. Dutch output is Belgian Dutch.

## Related Skills

- `ad-creative-matrix`: the hooks, bodies and CTAs, and the test plan.
- `abm-plan`: named-account audiences and tiers.
- `landing-page-matcher`: message match from ad to page.
- `ga4-audit` and `attribution-readout`: the measurement behind the campaign.
- `campaign-architect`: Google Ads structure only.
- `paid-ads-report-writer`: reporting across platforms.
