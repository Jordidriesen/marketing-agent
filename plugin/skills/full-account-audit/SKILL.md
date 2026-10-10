---
name: full-account-audit
description: "Runs a complete structured audit of a Google Ads account covering structure, budgets, bidding, keywords, tracking, and creative, ranked by money impact, pulling live from the Google Ads connector when connected. Use for new account takeovers or a periodic full review."
---

# full-account-audit

You run the audit a senior PPC would charge four figures for, and you rank it by money instead of by tidiness.

**Efficiency:** this skill can plausibly fire dozens of connector calls
across six layers. Follow `mcp-efficiency` throughout, resolve the
account once, filter and batch every call, don't restate raw pulls in
the reply, and use `google-ads-tool-map` for the actual tool names and
parameters referenced below.

## Inputs you need
- If the Google Ads connector is available, pull live per layer (see
  Tools below) rather than asking for exports first. Otherwise:
  account-level exports, campaigns, ad groups, keywords, search terms,
  ads, conversion actions.
- Target CPA or ROAS, monthly budget, and what the business sells.

## Tools

Full parameter reference: `google-ads-tool-map`. Per layer:

| Layer | Tool(s) |
|---|---|
| Tracking | `conversion_actions_breakdown`, `change_history` |
| Structure | `list_accounts`, `list_campaigns` |
| Budget & bidding | `list_campaigns` (budgets/status), `run_gaql` for anything campaign-performance-shaped not covered by a named tool |
| Keywords & queries | `search_terms`, `wasted_spend_report`, `quality_score_report` |
| Creative | `asset_performance`, `asset_group_performance` (PMax) |
| Post-click | No connector data: needs the actual landing pages, checked directly |

If the connector isn't connected, ask for the account-level exports
listed in Inputs instead and proceed the same way, layer by layer.

## Workflow

Work through six layers in order, because each depends on the one before
it. Resolve the account once via `list_accounts` (if ambiguous) before
the first call, then carry the resolved `customer_id` through every
layer: don't re-resolve per layer.

1. **Tracking.** Is measurement trustworthy? Pull
   `conversion_actions_breakdown` and `change_history` (14-day cap). If
   not, stop: nothing below is reliable. Flag it as finding number one.

   > **GATE:** present the Tracking finding and stop before pulling
   > anything for Structure. If tracking is broken enough that
   > downstream numbers can't be trusted, say so explicitly and ask
   > whether to continue the remaining layers anyway (useful for
   > cataloguing structural issues even under bad measurement) or fix
   > tracking first. If tracking is sound, this gate is a one-line
   > confirmation, not a hard stop: continue automatically and note
   > that tracking passed.

2. **Structure.** Campaign and ad group organization, intent separation,
   brand isolated from non-brand, enough conversion volume per campaign
   to learn. Pull `list_campaigns`.
3. **Budget and bidding.** Where the money goes vs where conversions
   come from. Budget-limited winners, saturated losers, bid strategies
   lacking the data to work.
4. **Keywords and queries.** Coverage gaps, wasted spend, match type
   discipline, negative list health. Pull `search_terms` and
   `wasted_spend_report` together (they source from different views and
   occasionally disagree at the edges, per `google-ads-tool-map`); pull
   `quality_score_report` if CPC or Quality Score looks like part of the
   story.
5. **Creative.** Asset coverage, angle variety, relevance to the ad
   group theme. Pull `asset_performance`, and `asset_group_performance`
   for any PMax campaigns found in Structure.
6. **Post-click.** Message match and mobile experience on the
   highest-spend pages, identified from the Budget/bidding layer's spend
   ranking.

Then rank every finding by estimated money impact, not by severity of
the rule broken.

**Call volume:** this is a genuinely large pull across six layers. If
the account has more than roughly 20 campaigns, treat the layer-by-layer
pulls above as the batch: don't fan out to a separate call per campaign
within a layer where a tool accepts an account-wide or multi-campaign
pull instead. For an account large enough that the full six-layer pull
would be dozens of individual calls, consider delegating the raw
data-gathering for layers 2-6 to a subagent that returns only the
per-layer findings tables, per `mcp-efficiency`'s subagent-delegation
rule, so the raw pulls don't sit in the main conversation.

## Output format
- Executive summary: the three findings that matter most, in plain
  English.
- Full findings table: layer, finding, evidence, estimated impact,
  recommended fix.
- A prioritized action list: this week, this month, this quarter.

## Rules
- Tracking findings always come first. An audit built on broken
  measurement is fiction.
- Every finding needs evidence from the data, never a generic
  best-practice complaint.
- Estimate impact in money or spend affected wherever possible.
- Say plainly when the data provided is not enough to judge a layer.
- Live-pulled data is only as fresh as the connector's last sync; if a
  number looks stale or inconsistent with what the user expects, say so
  rather than presenting it as certain (same caution `search-term-
  auditor` already applies).
