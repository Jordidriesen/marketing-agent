# Discipline notes

What the specialist agents knew before 5.0.0, kept per discipline. Read the section for a step before running it in the main thread, and paste the section into the thread brief under `Discipline notes` when a thread runs it. The hard limits in each section also live in the skills themselves, so they hold when a skill runs on its own.

## Research: competitors, markets, PR

- Pick the reference that fits: `competitive-research` (competitor-analysis) for one named competitor's organic footprint, rankings, page content and positioning; (competitive-landscape) for several competitors at once; (competitor-teardown) for paid ad angles. `european-market-intelligence` for sizing, entry, pricing or public tenders in a named European market. `media-mapping` builds an outlet list and never drafts or sends pitches.
- Use OpenSEO for ranking, SERP and domain data where the method calls for it. If it is not reachable, say so and fall back to web research; never put an estimate in place of live data.
- When the findings feed a campaign plan, structure them so the plan can use them directly: what competitors already claim, where the gaps are, what that means for positioning and channel choice.
- Mark every finding as live tool data or web research. Never present an inferred competitor strategy as confirmed.

## Research: SEO and GEO

- `content-research-orchestrator` for a full pass (keywords through content gaps); the stage skills for narrower asks.
- First-party data: resolve once per task where it lives. The brand kit's `references/context.md` says whether the brand has an OpenSEO project; if it does, use OpenSEO's Search Console and GA4 tools with that project ID; if not, the standalone Search Console connector (see `CONNECTORS.md`). A brand without a project can still be researched through the scratch project. Say plainly when a connector is not reachable.
- Every content brief or page recommendation also covers GEO: a clean, quotable answer near the top, well-labelled sections, structured data where it fits, specific enough to be cited.
- To measure AI citations over time, use `ai-visibility-tracker`. It is a logged manual protocol, not an automated score.
- Output for writing is a brief (target keywords, clusters, page structure, GEO notes), not finished copy. Mark live data against estimates.

## Campaign plan

- Build on the research when it exists: positioning and messages account for what competitors claim, and the channel plan follows the real search and content-gap opportunity. If there is none and the request is broad, say so rather than planning blind.
- Name the channels and content types the calendar calls for, so each piece can go to the right skill. The plan does not draft the pieces.
- Missing or contradictory goal, audience or timeline: ask before planning around a guess.

## Web and long-form content

- `content-creation` routes when the format is open or several formats are asked; otherwise go straight to `web-content-pipeline` (any page a visitor reaches), `customer-story-writer` or `press-release-writer`.
- `cro-auditor` finds why a page does not convert, `ab-test-planner` turns the top finding into a test; `web-content-pipeline` does the rewrite.
- Built on an SEO brief, keep its GEO guidance alongside the SEO requirements.
- Every piece goes through `brand-review`, even when the voice seems fine. Translation waits until the source piece is signed off.
- An `OPEN ITEMS` comment in a page or story stays intact; it goes into the publish question.

## Social

- Organic posts: `social-content-writer`, which asks for the platform first; never assume one. Paid social and video sets: `ad-creative-matrix`.
- Platform norms differ. Reddit is community-first and averse to self-promotion; never reuse LinkedIn phrasing there.
- Working from a campaign plan or a finished piece, take the angle and key message from it rather than re-deriving them.
- `brand-review` before anything is handed back.

## Email

- One email: `newsletter-writer`. A flow with timing, branching and exits: `email-sequence-hubspot-brevo`, which asks HubSpot or Brevo first; never guess the platform.
- Use the platform's real menu and step names, so the build checklist can be followed as written.
- Brevo can read lists, segments, templates and stats and create draft campaigns. Never send or schedule without a yes (`security-policy`). If neither connector is reachable, say so and hand back copy and plan without live data.

## Paid media

- Google Ads: start with `list_accounts` (and `list_mcc_child_accounts` for a manager account) before any other call. Not reachable: say so; never use assumed figures.
- Routing: `google-ads-build` for structure, keywords, bidding and budget; `google-ads-ads` for RSAs and asset reading; `google-ads-analyse` for everything diagnostic; `measurement` (metric-detective) for "why did this change"; `meta-ads-manager` and `linkedin-ads-manager` for those platforms. The last two have no connector, so they return build plans; never present them as built campaigns. `paid-ads-report-writer` is for client-facing reports, not working analysis.
- Work from live account data, not benchmarks, unless a method calls for one. Rank findings by money impact (spend at risk). Name the ad group next to every keyword or search term.

## Reporting and analytics

- Build the structure yourself (metrics, trends, wins and misses, next-period priorities), only for the channels the campaign used.
- Paid slice: `paid-ads-report-writer` (live data where Google Ads or LinkedIn Ads are connected, exports for the rest, normalised). `measurement`: ga4-audit when the measurement itself is in doubt, attribution-readout when GA4 and platforms disagree, metric-detective for a single Google Ads metric that moved.
- Organic slice: first-party data as in the SEO section. With a brand OpenSEO project, add rank tracker data (`get_rank_tracker`, read only; never create or schedule a tracker without asking, it spends credits) and near-miss pages (`get_search_opportunities`). Save the SEO part with `save_report` only when asked (private by default).
- Email results from Brevo or HubSpot, whichever the brand uses. For sites in WP Umbrella, `get_uptime` and `get_performance` as context for a dip; `generate_report` emails recipients, so never run it without a yes.
- Every number traces to a tool call or a given source; an unverified metric is marked, never estimated.

## Localisation

- Source content is written, edited and signed off first. One pass per locale; never one blended "international" version.
- Load the brand kit's locked terms, market notes and per-locale glossary; locked terms are carried exactly.
- `content-translate` for the pass, keeping structure, headings, schema, extractable answers and internal links. `brand-review` in the target language.
- Hand back: one piece per locale; unresolved terms flagged; a layout-expansion flag when the target runs much longer (German and French often run about 30% longer) for whoever lays it out; a back-check that numbers, product names, URLs, CTAs and legal claims match the source.
- No claim, figure or product fact that is not in the source. Ambiguous source: ask.

## Outbound and sales enablement

- Hard limits in `references/outreach-rules.md` of `account-brief`, `abm-plan`, `cold-email-sequence` and `battlecard`.
- Target list, in this order: a list the user supplied (say where it came from); the scraper suite when installed (`scraper-orchestrator`, keeping its approval gates); otherwise ask, or source a segment with `european-market-intelligence` first. Never guess companies.
- `account-brief` on tier 1 accounts (tier 2 when asked); `abm-plan` for named accounts over time, with paid parts handed over as audience lists; `cold-email-sequence` only when asked, compliance gate first; `ai-content-cleaner` (CLEAN) on every email; `brand-review` on anything that makes a claim.
- `battlecard` compiles verified inputs. Thin competitive facts: run the competitor research first or ask for sources. Share the card with the cold email work so objections get the same answers. A card to be designed goes to the design step as approved copy.
- Hand back: the deliverables, **Needs decision** (what only the user decides, with a default), **Could not verify** (unsourced claims, legal points, unreachable data).
