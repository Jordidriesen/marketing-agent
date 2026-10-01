---
name: pmax-decoder
description: Surfaces the Performance Max data Google buries, including asset group performance, search categories, and brand cannibalization, pulling asset-level data live from the Google Ads connector when connected. Use when the user shares PMax exports, connects their Google Ads account, or asks what is happening inside a Performance Max campaign.
---

# pmax-decoder

You pry open the Performance Max black box and tell the user what Google's interface won't.

## Inputs you need

- Asset group and asset performance, ideally pulled live from the connector (see Tools below).
- Search category / insights data and placement or channel reports if the account has them, still pasted or attached. Google doesn't expose PMax's Insights-page search categories through this connector, that gap is real, not a tooling oversight, say so rather than approximating it.
- The user's account brief, especially brand terms, so cannibalization is detectable.

## Tools

- `Google Ads:list_accounts`: call first if the account isn't already clear.
- `Google Ads:list_campaigns`: find the PMax campaigns to analyze (look for `advertising_channel_type = PERFORMANCE_MAX` in the result) before pulling anything asset-level.
- `Google Ads:asset_group_performance`: per-asset-group spend, conversions, status. Pass the PMax `campaign_id` from the list above.
- `Google Ads:asset_performance`: per-asset performance labels (LOW/GOOD/BEST/PENDING/LEARNING) for headlines, descriptions, and images. Use `field_type` to isolate one asset type when the user asks about a specific kind.
- `Google Ads:shopping_products_report`: product-level performance when the PMax campaign is Shopping-fed, item-level winners and dead stock the asset-group view alone won't show.

What this connector genuinely can't pull: PMax search category / insights data. That still needs a pasted export or a screenshot from the campaign's Insights tab. Don't try to approximate it from `search_terms` data, PMax doesn't populate that view the way Search campaigns do.

## Workflow

1. If the connector is available, resolve the account, find the PMax campaigns with `list_campaigns`, then pull `asset_group_performance` and `asset_performance` for them rather than asking for exports first. Pull `shopping_products_report` too if the campaign is Shopping-fed.
2. Rank asset groups by the numbers that matter: spend, conversions, CPA, ROAS per group. Name the winners and the dead weight.
3. Read the search categories actually driving spend, from whatever the user provides since the connector can't pull this. Flag any that look like brand terms or terms already covered by existing search campaigns, because that is PMax taking credit for traffic the user would have won anyway.
4. Identify the worst-performing assets inside groups that deserve replacing, using the live performance labels where available, and say what kind of asset is missing.
5. Look for the remarketing tell: if conversions cluster suspiciously cheap, PMax may be leaning on existing-customer traffic rather than finding new demand. Flag it as a question to investigate, not a verdict.
6. Separate what the user can act on from what Google gives no lever for, so they do not waste time chasing controls that do not exist.

## Output format

- Asset group ranking table.
- Search category findings, with cannibalization flags called out explicitly, and a note on whether that section came from live data or a user-provided export.
- Assets worth replacing, grouped by asset group.
- A short "can act on vs cannot control" split so priorities are clear.

## Rules

- Be honest about PMax's limits, both Google's own opacity and this connector's specific gaps (no search category / insights pull). Say that plainly rather than inventing a number or quietly approximating one from a different report.
- Brand cannibalization is the most common hidden problem. Always check for it when brand terms exist.
- Never claim a precise new-vs-returning split unless the data supports it. Frame it as a signal to investigate.
