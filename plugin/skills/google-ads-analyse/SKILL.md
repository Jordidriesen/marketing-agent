---
name: google-ads-analyse
description: 'Google Ads diagnosis on live data: full account audit, search terms and negatives, Quality Score, Performance Max, geo, device and ad schedule, auction insights, conversion tracking, disapprovals, ad-to-page match. Use for "audit the account", "wasted spend", "negatives", "low Quality Score", "PMax", "where is my spend going", "mobile performance", "ad schedule", "auction insights", "disapproved ads", "conversions look wrong".'
metadata:
  version: 1.0.0
  history: 'v1.0.0: new family skill in marketing-agent 4.0.0 (built first in the marketing-operator trial). Absorbs full-account-audit, search-term-auditor, quality-score-doctor, pmax-decoder, geo-performance-analyzer, device-performance-analyzer, ad-schedule-analyzer, auction-insights-monitor, conversion-tracking-auditor, disapproval-diagnoser, landing-page-matcher as references, unchanged apart from names and paths.'
---

# Google Ads Analyse

One skill for a family of related tasks that share the same inputs and connectors. Each task is a full reference file: pick the row that matches the request, read that file **in full**, and follow it as the skill. Where a request needs two tasks (an audit, then the search terms), run them one after the other, each from its own file.

**Shared reference.** `references/google-ads-tool-map.md` lists the Google Ads connector tools and their parameters. Every task reference points to it; read it before the first live call, and load `mcp-efficiency` for how to call the connector cheaply.

| Task reference | Use it for |
|---|---|
| `references/full-account-audit.md` | Full Google Ads account audit (structure, budgets, bidding, keywords, tracking, creative) ranked by money impact. Use for account takeovers or periodic reviews. |
| `references/search-term-auditor.md` | Audits Google Ads search terms for wasted spend and builds paste-ready negative keyword lists with match types and placement. Use for "wasted spend", "negatives", "search term report". |
| `references/quality-score-doctor.md` | Diagnoses Google Ads Quality Score by component and ranks fixes by cost. Use for low Quality Score or high CPCs. |
| `references/pmax-decoder.md` | Shows what Performance Max hides: asset groups, search categories, brand cannibalisation. Use for PMax questions or exports. |
| `references/geo-performance-analyzer.md` | Analyses Google Ads performance by location: regions to bid up and regions draining budget. Use for "where is my spend going" by geography. |
| `references/device-performance-analyzer.md` | Breaks Google Ads performance down by device and recommends adjustments, separating device from landing page problems. Use for mobile performance questions. |
| `references/ad-schedule-analyzer.md` | Builds a day and hour heatmap from Google Ads data and a dayparting plan. Use for "when do my ads perform best", "ad schedule". |
| `references/auction-insights-monitor.md` | Tracks Google Ads auction insights week over week: new entrants, impression share shifts, lost position. Use for "auction insights", "who is moving against us". |
| `references/conversion-tracking-auditor.md` | Audits Google Ads conversion tracking for gaps, double counting and misconfigured actions. Use when numbers look wrong or before trusting smart bidding. |
| `references/disapproval-diagnoser.md` | Explains Google Ads disapprovals and limited-status assets and what to change. Use for disapproved ads, keywords or assets. |
| `references/landing-page-matcher.md` | Checks message match between search query, ad and landing page, and flags mismatches leaking conversions. Use when click-to-conversion is weak. |

If no row fits, say so and name the skill that does fit rather than stretching a reference.

**Required skill calls.** The references name the skills they call (for example `brand-review` or `ai-content-cleaner`); call those through the Skill tool, never imitate them inline. End the reply with one line: `Skills run: ...`, naming this skill and the reference used, for example `Skills run: google-ads-analyse (full-account-audit)`.
