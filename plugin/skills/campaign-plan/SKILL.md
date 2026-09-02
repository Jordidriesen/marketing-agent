---
name: campaign-plan
metadata:
  version: 1.0.0
  history: >
    Built for the marketing plugin. Added the [brand]-brand-kit check,
    linked Key Messages to content-references' framework-selection
    guidance instead of freestyling tone, moved the channel/budget/metrics
    reference tables out of the main flow into references/, and tightened
    Output to this library's no-padding standard.
description: >
  Generates a full campaign brief — objectives, audience, key messages,
  channel strategy, content calendar, success metrics, budget, and risks —
  from a goal and a timeline. Use when planning a product launch, lead-gen
  push, or awareness campaign, when a marketing goal needs to become a
  structured executable plan, or when a week-by-week content calendar with
  channel dependencies is needed. Not for producing the individual pieces
  the plan calls for — hand those to the relevant content skill once the
  calendar is set.
argument-hint: "<campaign objective or product>"
---

# Campaign Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

You turn a goal and a deadline into a plan someone could greenlight as written — not a menu of marketing options. Every section below should be specific enough to act on immediately, not a framework the reader still has to fill in themselves.

## Step 0 — Identify the Brand and Load Its Kit

Same pattern as `web-content-pipeline`: determine which brand/client this campaign is for — from the brief, conversation context, or by asking if unclear — and check for a matching `[brand]-brand-kit` skill.

- **If found:** load it. Its voice and locked terminology govern the Key Messages section below and every piece of copy the campaign calendar hands off to other skills.
- **If not found:** proceed without one, and note that documenting this brand's voice is worth doing once campaign work for it recurs.

## Trigger

User runs `/campaign-plan`, or asks to plan, design, or build a marketing campaign — a launch, a lead-gen push, an awareness push, or a goal that needs turning into a structured, dated plan.

## Inputs

Gather before proceeding; ask for anything missing rather than guessing:

1. **Campaign goal** — the primary objective (signups, awareness, product launch, leads, re-engagement).
2. **Target audience** — roles, industries, pain points, buying stage.
3. **Timeline** — duration and any fixed dates (launch, event, seasonal deadline).
4. **Budget range** — optional; without it, produce a channel-agnostic plan and flag where budget would change the recommendation.
5. **Brand/client** (Step 0) — determines which brand kit governs the messaging.
6. **Optional context** — product/service, differentiators, prior campaign learnings, geographic focus.

## Campaign Brief Structure

### 1. Campaign Overview
Campaign name, one-sentence summary, primary objective with a specific measurable goal, secondary objectives if any.

### 2. Target Audience
Primary (and secondary, if applicable) segment, pain points and motivations, where they spend time, buying-stage alignment.

### 3. Key Messages
Core message (one sentence) plus 3–4 supporting messages with proof points. Pick the structural framework from `content-references/references/communication-frameworks.md` based on the objective and the channels chosen in Section 4 — a lead-gen push over paid channels wants PAS, an awareness campaign wants Sparkline, don't default to whichever framework was used last time. If a brand kit is loaded, its voice and locked terminology apply here directly.

### 4. Channel Strategy
Recommend channels from owned/earned/paid — see `references/planning-playbook.md`'s Channel Selection Guide for the full option set and typical metrics per channel. For each recommended channel: why it fits the audience and objective, content format, effort level, and budget allocation if budget was provided.

### 5. Content Calendar
Week-by-week (day-by-day for short campaigns), built backward from fixed milestones per `references/planning-playbook.md`'s Content Calendar Creation process. Format as a table:

| Week | Content Piece | Channel | Owner/Notes | Status |
|---|---|---|---|---|

### 6. Content Pieces Needed
Every asset required: name, type, one-line brief, must-have vs. nice-to-have, suggested creation timeline.

### 7. Success Metrics
Primary KPI with a target number, 3–5 secondary KPIs, how each is tracked, reporting cadence. See `references/success-metrics-by-type.md` for the metric set matching this campaign's type. If historical performance data is available, reference it to ground the targets rather than picking round numbers.

### 8. Budget Allocation (if budget provided)
Breakdown by channel/activity, production vs. distribution cost split, 10–15% contingency. See `references/planning-playbook.md`'s Budget Allocation Approaches for starting-point ratios.

### 9. Risks and Mitigations
2–3 real risks (timeline, audience mismatch, channel underperformance) each with a specific mitigation — not a generic "monitor closely."

### 10. Next Steps
Immediate action items, stakeholder approvals needed, key decision points.

## Related Skills

Once the calendar is set, hand individual pieces to the specialist skill for that format: `web-content-pipeline` for a landing or blog page, `email-sequence-hubspot-brevo` for a lifecycle flow, `social-content-writer` for a social post, `newsletter-writer` for a one-off email, `press-release-writer` for a launch announcement, `rsa-writer` for paid search ad copy. Before finalizing messaging, `competitive-brief` can surface positioning gaps worth building the campaign's Key Messages around. `brand-review` is the gate to run finished pieces through before they ship.

## Output

Present the full brief with clear headings. Three numbers maximum in the Campaign Overview — the rest belongs in the relevant section's table, not the summary. No hedged objectives ("aim to potentially increase") — state the target number or state that none was provided.

After the brief, ask:

"Would you like me to:
- Dive deeper into any section?
- Draft specific content pieces from the calendar?
- Run a `competitive-brief` to sharpen the messaging?
- Adjust the plan for a different budget or timeline?"
