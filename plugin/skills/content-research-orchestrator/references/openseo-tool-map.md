# OpenSEO Tool Reference

Quick reference for every tool used across the content research skills —
`content-research-orchestrator` and its component stages
(`seo-keyword-research`, `keyword-clustering`, `competitive-landscape`,
`competitor-analysis`, `content-gap-mapping`), plus `media-mapping` and
`sea-keyword-research`. Required params marked with *.

**Replaces `dfs-tool-map.md`.** OpenSEO wraps DataForSEO with a
project-scoped, credit-tracked interface. Every OpenSEO tool call needs a
`projectId` — resolve one first (below) before anything else in this file.
Three DataForSEO Labs tools that had no OpenSEO wrapper (domain
intersection, page intersection, domain-based competitor discovery) are
handled with a workaround pattern instead of a direct call (also below).
Four other DataForSEO tools that appeared in the old reference (bulk
traffic estimation, both historical-data endpoints, all Trends endpoints)
are dropped entirely — a check of every skill's actual workflow steps, not
just its Tools list, found none of them are called by anything live, so
nothing is lost by removing them.

---

## Resolving a project

Every call below needs a `projectId`. Resolve one before the first call of
any session:

0. If the work is for a brand with a `[brand]-brand-kit`, read the
   "Data sources" section of its `references/context.md` first. It says
   whether the brand has an OpenSEO project (and its ID) and where its
   first-party search data lives. Follow it over the steps below.
1. Call `list_projects`. It's free and returns `{id, name, domain,
   locationCode, languageCode}` per project.
2. Match by domain: if the target domain (client site, or the primary
   domain the work is about) already has a project, use its `id`.
3. **Ongoing client work** (a named client or brand, any recurring
   engagement): if no project exists yet, ask before creating one. Not
   every brand gets an OpenSEO project on purpose; when the answer is no,
   use the scratch project (step 4) for keyword, SERP, ranking and backlink
   research, and the standalone Search Console connector for the brand's
   own first-party data (see the plugin's `CONNECTORS.md` data-source
   rule). When the answer is yes, `create_project` with the
   client's name, root domain, and default market. One project per
   client, not per market — override `locationCode`/`languageCode` on
   individual calls for each of a client's markets rather than creating a
   project per market.
4. **One-off or prospective research** (a cold competitor lookup, a
   speculative keyword check with no client attached): reuse a single
   generic "scratch" project rather than creating a new named project per
   task. Create it once if it doesn't exist yet; after that, just reuse
   its `id`.
5. Pass the resolved `projectId` to every OpenSEO call for the rest of the
   task. Don't re-resolve per tool call.

`create_project` uses no credits and doesn't call DataForSEO, so getting
this step wrong costs nothing to fix, just don't skip straight to a
keyword or SERP call without a `projectId` in hand.

---

## Keyword tools

### research_keywords

**Purpose:** Expand from 1-5 seed keywords into related keywords with
volume/difficulty/CPC. Replaces `dataforseo_labs_google_keyword_ideas`,
`_keyword_suggestions`, and `_related_keywords` — OpenSEO merges what used
to be three separate calls into one.

| Param | Required | Notes |
|---|---|---|
| projectId | * | From project resolution above |
| seeds | * | Array of 1-5 `{seed, locationCode?, languageCode?}` objects |
| includeClickstreamData | optional | Refines volume, doubles credit cost per seed |
| resultLimit | optional | 150 / 300 / 500 per seed, defaults to 150 |

**Key output fields per seed:** related keywords with `searchVolume`,
`keywordDifficulty`, `cpc`, `intent`.

### get_keyword_metrics

**Purpose:** Hydrate up to 700 known keywords with volume, KD, CPC,
intent, and monthly trends in one call. Replaces
`dataforseo_labs_google_keyword_overview`, `_bulk_keyword_difficulty`, and
`_search_intent` — intent classification is now a field on this response,
not a separate call.

| Param | Required | Notes |
|---|---|---|
| projectId | * | |
| keywords | * | 1-700 keywords |
| includeClickstreamData | optional | Doubles credit cost |
| includeMonthlyTrends | optional | Defaults to true |
| sortBy | optional | `search_volume` (default), `keyword_difficulty`, `cpc`, `competition` |

**Key output fields:** `keyword`, `searchVolume`, `keywordDifficulty`,
`cpc`, `competition`, `intent` (`informational`/`navigational`/
`transactional`/`commercial`/`unknown` — same four labels DataForSEO used).

---

## Ranking and SERP tools

### get_ranked_keywords

**Purpose:** Every keyword a domain or page ranks for. Direct replacement
for `dataforseo_labs_google_ranked_keywords`, plus a `scope` parameter
DataForSEO didn't expose as cleanly.

| Param | Required | Notes |
|---|---|---|
| projectId | * | |
| target | * | Domain (no protocol) or a full page URL |
| scope | optional | `domain`, `subdomains`, `subfolder`, or `exact_url` — use `exact_url` when comparing one specific page |
| minSearchVolume / maxRank | optional | Filter noise out before it hits the table |
| excludeBrandTerms | optional | Up to 10 terms |
| limit | optional | 1-100, defaults to 50 |
| sortBy | optional | `rank` / `search_volume` (default) / `traffic_estimate` / `cpc` |

**Key output fields:** `keyword`, `rank`, `url`, `searchVolume`, `intent`,
`trafficEstimate`.

### get_serp_results

**Purpose:** Live Google organic SERPs for 1-10 keywords in one call.
Direct replacement for `serp_organic_live_advanced` — bulk by default
instead of one keyword per call.

| Param | Required | Notes |
|---|---|---|
| projectId | * | |
| queries | * | 1-10 `{keyword, locationCode?, languageCode?}` objects |
| depth | optional | Multiple of 10, 10-100, defaults to 20 |

**Key output fields per result row:** `rank`, `url`, `title`, `domain`,
result type (organic/paid/featured snippet/local pack).

### find_serp_competitors

**Purpose:** Which domains dominate the SERP for a keyword set. Direct
replacement for `dataforseo_labs_google_serp_competitors`.

| Param | Required | Notes |
|---|---|---|
| projectId | * | |
| keywords | * | 1-100 |
| excludeDomains | optional | e.g. the user's own site |
| resultTypes | optional | Defaults to organic + local_pack |
| limit | optional | 1-100, defaults to 50 |

---

## Domain tools

### get_domain_overview

**Purpose:** High-level organic footprint — traffic, keyword count,
backlinks, referring domains. Direct replacement for
`dataforseo_labs_google_domain_rank_overview`.

| Param | Required | Notes |
|---|---|---|
| projectId | * | |
| domain | * | |
| scope | optional | `domain` / `subdomains` (default for root input) / `subfolder` / `exact_url` |

### get_domain_keyword_suggestions

**Purpose:** The detailed ranked-keyword list for a competitor or
reference domain. Call after `get_domain_overview` when the aggregate
number isn't enough. New capability, no direct DataForSEO Labs equivalent
was in active use, but it's a natural companion to `get_ranked_keywords`.

---

## Workaround patterns: three DataForSEO Labs tools with no OpenSEO wrapper

`dataforseo_labs_google_domain_intersection`, `_page_intersection`, and
`_competitors_domain` have no OpenSEO wrapper. Checked every skill that
used them (`competitor-analysis`, `content-gap-mapping`,
`keyword-clustering`, `competitive-landscape`): all three were already
documented in those skills' own text as either a shortcut over a fallback
the skill already knew how to do, or an explicitly secondary/complementary
check, not the primary mechanism. Nothing is actually blocked, it's a few
extra calls instead of one.

**Domain overlap** (which keywords do domain A and domain B both rank
for): call `get_ranked_keywords` for each domain separately, then
intersect the two `keyword` sets directly. Two calls and a set
intersection instead of one `domain_intersection` call.

**Page overlap** (which keywords do specific URLs both cover): call
`get_ranked_keywords` with `scope: exact_url` once per URL, then compare
which keywords appear across which URLs. Alternatively, for a handful of
already-known candidate keywords, `get_serp_results` on those keywords and
check which URLs from the tracked set show up in each SERP is often
faster than intersecting full ranked-keyword pulls.

**Domain-based competitor discovery** (given one domain, who are its real
organic competitors): chain two calls instead of one — pull that domain's
top keywords with `get_domain_keyword_suggestions`, then run
`find_serp_competitors` on that keyword set. Slightly more roundabout than
a single `competitors_domain` call, but both steps already exist in this
file for other reasons, so it isn't new surface area.

If a future use case needs any of the three at real bulk scale (dozens of
domain or URL pairs in one sweep, where the extra-calls overhead actually
compounds), that's worth revisiting as a narrow, named exception. The raw
DataForSEO connector is no longer connected, so there is no fallback
outside OpenSEO; batch the extra calls instead.

---

## Firecrawl Scrape (via MCP)

**Purpose:** Extract cleaned markdown content from a competitor URL.
Unchanged, not part of this migration.

```
Tool: firecrawl scrape
Required params:
  url: full URL string (e.g. "https://competitor.com/their-page")
  formats: ["markdown"]          — returns cleaned body text in markdown
  onlyMainContent: true          — strips nav, footer, sidebar
Optional params:
  includeTags: ["h1","h2","h3"]  — limit to specific HTML tags
  excludeTags: ["footer","nav"]  — exclude unwanted elements
  waitFor: 2000                  — ms to wait before scraping (for JS-heavy pages)
  timeout: 15000                 — max wait in ms
```

**Output fields:** `markdown` (full page text), `metadata.title`,
`metadata.description`, `metadata.language`

**Error cases:**
- 403 / bot detection → skip URL, note in output
- Timeout → increase waitFor, retry once
- Paywall → skip, note as "manual review needed"

---

## Other OpenSEO tools used elsewhere in the plugin

Checked against the live connector on 1 Oct 2026. Full parameters come from the tool schema; load it before the first call.

| Tool | What it does | Credits | Used by |
|---|---|---|---|
| `get_search_opportunities` | Search Console pages in positions 4 to 20 joined with GA4 outcomes, scored | None; needs SC and GA4 linked in the project | `seo-keyword-research`, `content-gap-mapping`, `performance-reporter` |
| `inspect_urls` | Google's stored index status, canonical and crawl date for up to 10 URLs | None; needs SC linked | `seo-audit`, `content-gap-mapping`, `frontend-design` redesigns |
| `get_search_console_performance`, `get_google_analytics_*` | First-party search and analytics data | None; needs the links | Data-source rule in `CONNECTORS.md` |
| `save_keywords`, `list_saved_keywords`, `remove_saved_keywords` | Persist a keyword set to the project, optionally tagged | None; ask before tagging | `seo-keyword-research`, `content-gap-mapping` |
| `get_rank_tracker`, `create_rank_tracker`, `add_rank_tracking_keywords`, `estimate_rank_tracker_cost`, `run_rank_tracker` | Rank tracking | Creating an empty manual tracker is free; scheduled trackers and runs spend credits. Estimate first and ask | `seo-audit`, `performance-reporter` |
| `get_local_serp_results` | Local pack for a query and location | Yes | `competitor-analysis`, `competitive-landscape` |
| `get_local_rank_grid` | Maps rank for one business across a 3x3 or 5x5 grid | One search per grid point (9 or 25) | Local competitor work, `seo-audit` |
| `get_business_profile`, `get_business_reviews`, `get_google_business_questions`, `search_local_businesses` | Google Business Profile data, reviews (billed per 10), Q&A | Yes | Local competitor work |
| `get_backlinks_overview`, `get_backlinks_profile` | Backlink data | Yes, roughly 50 per domain | Competitor skills |
| `run_site_audit`, `get_audit_status`, `get_audit_issues`, `get_audit_pages` | Site crawl | Yes | `seo-audit` |
| `list_reports`, `save_report`, `list_report_templates` | Store a finished HTML report in the project, private by default | None; making it public needs the user's request | `performance-reporter`, `seo-audit` |

## Location & Language Codes (Common)

Unaffected by this migration: `locationCode` is the same DataForSEO
numeric code either way. The common markets are covered here; for
anything else use `OpenSEO:search_serp_locations`:

| Country | locationCode | languageCode |
|---|---|---|
| Belgium (NL) | 2056 | nl |
| Belgium (FR) | 2056 | fr |
| Netherlands | 2528 | nl |
| Germany | 2276 | de |
| United Kingdom | 2826 | en |
| United States | 2840 | en |
| France | 2250 | fr |

For a market outside this table, or a city or region for local volume:
call `OpenSEO:search_serp_locations` and pass its result verbatim. Note the
code here once a market recurs.

---

## Dropped from the old reference

`dataforseo_labs_bulk_traffic_estimation`, `dataforseo_labs_google_
historical_serp`, `dataforseo_labs_google_historical_keyword_data`, and
every `kw_data_dfs_trends_*` / `kw_data_google_trends_*` tool were
documented in the old `dfs-tool-map.md` but never actually called by any
skill's workflow steps, confirmed by checking each skill's numbered
Workflow section, not just its Tools list. Removed here rather than
carried forward as unused weight. If a future task genuinely needs
historical trend or traffic-estimate data, say it isn't available in this
toolset: the raw DataForSEO connector is no longer connected and OpenSEO
has no wrapper for these.
