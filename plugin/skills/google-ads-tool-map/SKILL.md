---
name: google-ads-tool-map
description: "Shared per-tool reference for the Google Ads MCP connector, tool names and key parameters already in live use across this account's Google Ads skills, plus the run_gaql fallback. Not triggered directly — loaded by whichever Google Ads skill is doing the work."
---

# Google Ads Tool Reference

Quick reference for every Google Ads MCP tool already in documented use
across this account's Google Ads skills. Compiled from what those skills
already call successfully, not independently re-verified against the live
connector schema from this file (the connector wasn't enabled in the chat
this file was compiled in), so treat an unfamiliar parameter name on an
actual error as more authoritative than this table, and update this file
if the two disagree.

**Known gap:** `device-performance-analyzer` and `ad-schedule-analyzer`
currently have no Tools section at all — both still ask for pasted data
only. Standard Google Ads reporting supports `segments.device` and
`segments.hour`/`segments.day_of_week`, so `run_gaql` (below) is the
likely path to make both live, but that's untested against this specific
connector, not confirmed. Worth a short trial before rewriting either
skill on the assumption it works.

---

## Resolving an account

Every tool below operates on one Google Ads account. Resolve it once per
task, the same discipline `openseo-tool-map.md` uses for `projectId`:

1. Call `Google Ads:list_accounts` when the account isn't already clear
   from context, especially with more than one account connected.
2. Carry the resolved `customer_id` through every subsequent call in the
   task. Don't re-call `list_accounts` per tool call.

---

## Account & campaign discovery

### list_accounts
**Purpose:** List connected Google Ads accounts. Call first whenever the
account isn't already unambiguous.

### list_campaigns
**Purpose:** List campaigns, with type and status. Used to find a subset
(e.g. PMax campaigns via `advertising_channel_type = PERFORMANCE_MAX`)
before pulling anything campaign-scoped.

---

## Search terms & wasted spend

### search_terms
**Purpose:** Account-wide search terms triggering ads, with cost,
impressions, conversions.

| Param | Notes |
|---|---|
| min_cost / min_impressions | Filter noise out before the call, not after |

**Known limit:** no campaign filter, caps at 500 rows account-wide — on
an active account this can silently drop most of a single campaign's
spend. Don't use for a single-campaign audit; use `run_gaql` against
`search_term_view` with an explicit `campaign.id` filter instead.

### wasted_spend_report
**Purpose:** Purpose-built for terms that spent money with zero
conversions. Sources from a different view than `search_terms` and the
two occasionally disagree at the edges — cross-check rather than relying
on either alone when the finding matters.

---

## Quality & auction signals

### quality_score_report
**Purpose:** Keyword-level Quality Score with the expected CTR / ad
relevance / landing page experience breakdown, plus spend, in one call.

| Param | Notes |
|---|---|
| min_impressions | Filters out keywords too new to have a real score |

### auction_insights
**Purpose:** Competitor impression share, overlap rate, position-above
rate, top-of-page rate, outranking share, per campaign.

| Param | Notes |
|---|---|
| date_range | One range per call — call twice for a two-period comparison and diff yourself, it doesn't do the comparison for you |

### impression_share_report
**Purpose:** Own impression share lost to budget vs lost to rank, per
campaign. The field that turns "losing impression share" into an actual
diagnosis instead of a guess.

---

## Asset & PMax performance

### asset_group_performance
**Purpose:** Per-asset-group spend, conversions, status.

| Param | Notes |
|---|---|
| campaign_id | Required — pass the PMax campaign's ID from `list_campaigns` |

### asset_performance
**Purpose:** Per-asset performance labels (LOW/GOOD/BEST/PENDING/
LEARNING) for headlines, descriptions, images.

| Param | Notes |
|---|---|
| field_type | Optional — isolate one asset type |

### shopping_products_report
**Purpose:** Product-level performance for Shopping-fed PMax or Shopping
campaigns — item-level winners and dead stock an asset-group view alone
won't show.

---

## Geography

### geo_performance
**Purpose:** Performance by geographic location.

| Param | Notes |
|---|---|
| level | `country` / `region` / `city` — match to how granular the service area actually is; too fine drowns signal in noise, too coarse hides it |

---

## Tracking & change history

### conversion_actions_breakdown
**Purpose:** Live conversion action list with settings — category, count
(every vs one), attribution, conversion window, primary flag.

### change_history
**Purpose:** Check whether tracking configuration changed recently.

| Param | Notes |
|---|---|
| (date range) | Hard cap at 14 days — `last_30_days` or an equivalent 30-day range errors. Default to 14 days; if a longer look-back matters for the diagnosis, say so rather than retrying a range already known to fail |

---

## General-purpose fallback

### run_gaql
**Purpose:** Direct Google Ads Query Language access for anything not
covered by a purpose-built tool above, or when a purpose-built tool's
scope doesn't match the task (e.g. `search_terms` has no campaign filter
and caps at 500 rows — `run_gaql` against `search_term_view` with an
explicit `campaign.id = X` filter covers a single-campaign audit that
`search_terms` can't). Standard GAQL syntax: segments (`segments.device`,
`segments.hour`, `segments.day_of_week`), resources (`campaign`,
`ad_group`, `search_term_view`, ...), and metrics (`metrics.cost_micros`,
`metrics.conversions`, ...) all apply the same way they do in the raw
Google Ads API.

Use this as the deliberate exception, not the default path — a
purpose-built tool above is usually cheaper and better-shaped for the
task than composing a raw GAQL query from scratch.

---

## Error handling

No specific rate-limit or credit costs are documented for this connector
in this account's existing skills (unlike OpenSEO's per-call credit
notes) — if a call returns a rate-limit error, back off per its own
error message rather than retrying immediately blind, per
`mcp-efficiency`.

| Error | Likely cause |
|---|---|
| Auth / account error | `customer_id` wasn't actually resolved via `list_accounts` first |
| Empty result | Wrong account, or a filter (min_cost/min_impressions/date range) too narrow for the account's actual volume |
| `change_history` errors on a 30-day range | Known hard cap at 14 days — see above, not a bug |
| `search_terms` missing spend for a known campaign | Its 500-row account-wide cap dropped it — use `run_gaql` scoped to that campaign instead |
