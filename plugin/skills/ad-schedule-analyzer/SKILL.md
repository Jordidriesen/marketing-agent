---
name: ad-schedule-analyzer
description: Builds a day and hour performance heatmap from Google Ads data and turns it into a dayparting plan. Use when the user asks when their ads perform best or wants to set an ad schedule.
---

# ad-schedule-analyzer

You find the hours that make money and the hours that just spend it.

## Inputs you need
- Performance segmented by day of week and hour, ideally 90 days for stable patterns.
- Target CPA or ROAS.

## Workflow
1. Build the grid: day by hour, with spend, conversions, and CPA in each cell.
2. Identify clear winners (consistently under target) and clear drains (consistent spend, no conversions).
3. Check for volume traps. A single converting hour on tiny data is noise. Require repetition across weeks before calling it a pattern.
4. Translate into a dayparting plan: which blocks to bid up, which to bid down, which to switch off.
5. Note whether the business can service the hours you recommend pushing. A lead at 3am is worth less if nobody calls back until 10.

## Output format
- The heatmap as a readable table, best and worst cells called out.
- A dayparting plan with specific bid adjustment recommendations per block.
- One caution line on any recommendation resting on thin data.

## Rules
- 90 days minimum for confident patterns. Say so if the user gives less.
- Never recommend switching off a block purely on low volume. Absence of conversions is not evidence of waste at small numbers.
