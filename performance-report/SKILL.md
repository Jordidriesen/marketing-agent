---
name: performance-report
metadata:
  version: 1.0.0
  history: >
    Built for the marketing plugin. Moved the five metric-definition
    tables, attribution modeling basics, reporting templates, and
    optimization framework into references/, made the Google Ads-specific
    handoff to report-writer/metric-detective/quality-score-doctor
    explicit rather than duplicating PPC benchmarks inline, and tightened
    the executive summary rules to match report-writer's no-padding
    standard.
description: >
  Builds a marketing performance report — key metrics, trend analysis,
  wins and misses, and prioritized recommendations — from performance
  data for a period. Use when wrapping a campaign, preparing weekly,
  monthly, or quarterly channel summaries for stakeholders, or turning
  raw numbers into an executive summary with next-period priorities. For
  the Google Ads-specific pieces of a report — the executive-summary
  paragraph or diagnosing why a specific metric moved — prefer
  report-writer and metric-detective, which work from live account data
  instead of generic industry benchmarks.
argument-hint: "<time period or campaign>"
---

# Performance Report

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

You write the report a stakeholder actually reads, not the one that buries the one number that matters under a dashboard of metrics nobody asked for. Same discipline as `report-writer`: lead with what changed and why, state bad news plainly, end with priorities specific enough to check on next period.

## Step 0 — Identify the Brand and Load Its Kit

If the report is being written up as a client-facing deliverable, check for a `[brand]-brand-kit` skill and apply its tone to the executive summary — the metrics tables stay neutral either way, but the narrative around them shouldn't read generically if a specific voice exists.

## Trigger

User runs `/performance-report`, or asks for a marketing report, performance analysis, campaign results, or a metrics summary — weekly, monthly, quarterly, or ad hoc.

## Inputs

1. **Report type** — campaign, channel (email/social/paid/SEO/etc.), content performance, overall cross-channel, or custom scope.
2. **Time period** — the reporting window.
3. **Data source** — pull automatically if analytics/product tooling is connected; otherwise ask the user to paste spreadsheets, CSV data, described dashboard numbers, or just the key figures.
4. **Comparison period** — optional, prior period or YoY for trend context.
5. **Stakeholder audience** — optional, changes whether this reads as an executive summary or a detailed analyst view.

If this is a Google Ads-specific report, hand the raw-data-to-narrative step to `report-writer` and any "why did this change" question to `metric-detective` rather than building the executive summary from scratch here.

## Report Structure

### 1. Executive Summary
2–3 sentences. Headline metric with trend direction vs. prior period. One win, one concern. No filler ("overall a solid month with some challenges") — state what happened, same rule as `report-writer`.

### 2. Key Metrics Dashboard

| Metric | This Period | Prior Period | Change | Target | Status |
|---|---|---|---|---|---|

Status: on track / at risk / off track. Pick the relevant metric set from `references/metric-benchmarks.md` by report type — don't paste every table regardless of scope.

### 3. Trend Analysis
Direction over the period, notable inflection points and their cause, seasonality, comparison to benchmark/target. Methodology in `references/trend-analysis-and-attribution.md`.

### 4. What Worked
Top 3–5 wins with specific data, a hypothesis for why, and how to replicate or scale — not just "engagement was up."

### 5. What Needs Improvement
Bottom 3–5 performers with specific data, a hypothesis for the underperformance, and a recommended fix per item.

### 6. Insights and Observations
Patterns not obvious from the raw metrics — audience behavior, resonant creative themes, external factors (seasonality, news, competitive moves).

### 7. Recommendations
Per recommendation: what to do, why (tied to a specific insight from Sections 4–6, not generic advice), expected impact, effort, and priority. Prioritize in a 2x2:

| | Low Effort | High Effort |
|---|---|---|
| **High Impact** | Do first | Plan for next sprint |
| **Low Impact** | Do if time allows | Deprioritize |

### 8. Next Period Focus
Top 3 priorities, tests to run, targets for key metrics.

## Related Skills

For Google Ads-specific components: `report-writer` turns raw Ads data into the client-ready executive-summary paragraph, and `metric-detective` diagnoses why a specific Ads metric moved. `quality-score-doctor`, `device-performance-analyzer`, and `geo-performance-analyzer` cover their respective diagnostic areas in more depth than the generic Paid Advertising benchmark table here. If the report needs to reference competitor moves, pull from a recent `competitive-brief` rather than speculating.

## Output

Tables for data, bold for key numbers and trend direction. Executive summary short enough to forward to leadership as-is. A "detailed appendix" section only if the user supplied enough granular data to warrant one — don't manufacture appendix content to look thorough.

After the report, ask:

"Would you like me to:
- Create a slide-ready summary of these results?
- Draft a stakeholder email with the key takeaways?
- Dive deeper into any specific metric or channel?
- Set up a reporting template to reuse next period?"
