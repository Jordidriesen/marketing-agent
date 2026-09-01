---
name: sea-keyword-research
description: Runs first-pass Google Ads (SEA) keyword research grouped by intent, with trap keywords flagged and a launch list sized to a stated budget, using OpenSEO's Google-Ads-derived data for real search volume, competition, and CPC. Use when the user asks for PPC keywords, search terms to target with paid budget, or is planning a new Google Ads campaign. For organic/content keyword research (keyword difficulty, clustering into pages), see seo-keyword-research instead.
---

# sea-keyword-research

You do the first pass a good freelancer charges a day for, and you do it without padding the list to look thorough.

This is the PPC launch-list version of keyword research: sized to a stated ad budget, weighted toward buy-now intent, with real Google-Ads-derived search volume and CPC data instead of relative guesses. For organic content keyword research with page-level clustering, use `seo-keyword-research` instead. The two answer different questions and shouldn't be merged: this one picks what to bid on, that one picks what to write about.

## Inputs you need

- Product or service, and the location it serves.
- Target country and language, for the volume/bid lookup. If unclear and it would materially change the numbers, ask; otherwise default to the user's own locale.
- Monthly budget.
- What a customer is worth, roughly. This decides how aggressive the launch list can be.

## Tools

- **Resolve a `projectId` first** per `content-research-orchestrator/references/openseo-tool-map.md`'s "Resolving a project" section.
- `OpenSEO:get_keyword_metrics`: primary data pull. Google-Ads-derived search volume, `competition` (a 0-1 float, convert to LOW/MEDIUM/HIGH bands for the output: roughly <0.33 / 0.33-0.66 / >0.66), and `cpc` per keyword. Same underlying data source Keyword Planner reads from. One difference from the old source worth flagging in the output: this returns a single `cpc` estimate, not a separate low/high top-of-page bid range, if the budget sanity check needs a range rather than a point estimate, say so and treat `cpc` as the midpoint rather than presenting false precision.
- `dataforseo:kw_data_google_ads_locations`: raw fallback to look up the right location code when the user names a city or region outside `content-research-orchestrator/SKILL.md`'s common-codes table. No OpenSEO wrapper for this lookup.

Call `get_keyword_metrics` with the full candidate list batched into as few calls as possible rather than one call per keyword (up to 700 keywords per call).

## Workflow

1. Resolve a `projectId` per `openseo-tool-map.md` before any other call.
2. Build 30-50 candidate keywords grouped by intent: buy-now (transactional), comparing (commercial investigation), researching (informational). Label each group with what to expect: buy-now converts but costs more, research traffic is cheap and mostly doesn't buy.
3. Call `get_keyword_metrics` on the full candidate list (batched) to pull real search volume, competition, and CPC for each. This replaces relative high/medium/low guesswork with the actual auction signal.
4. Flag the trap keywords: 8-10 terms that look attractive but typically waste money, each with the reason. Use the real data here too: a term with high volume and a high CPC but generic or ambiguous intent is a stronger trap flag than a guess ever was. Still name the qualitative traps data alone won't catch: freebie-seekers, wrong-audience overlap, ambiguous phrasing.
5. Pick the launch list: the 10 keywords you'd actually start with on this budget, weighted toward buy-now intent. Sanity-check the pick against the budget: if the CPC estimate would burn the monthly budget on a handful of clicks, say so and adjust the list toward lower-competition terms in the same intent group rather than silently proposing a list the budget can't sustain.
6. List every assumption you made about the business so the user can correct them. Wrong assumptions are the main way keyword research fails.

## Output format

- Intent-grouped keyword table: keyword, intent, search volume, competition, CPC.
- Trap keywords with one-line reasons.
- The 10 launch picks with match types, and a one-line budget sanity check (how many clicks the budget realistically buys at this CPC).
- Assumptions list, explicitly labeled.

## Rules

- Do not invent metrics. If OpenSEO returns no data for a term (common for very long-tail or brand-new terms), write "unknown," don't estimate one.
- 50 mediocre keywords help nobody. If the niche is narrow, deliver 25 good ones and say why.
- Competition and CPC come from Google Ads' own underlying data source, so don't hedge them as relative estimates the way an older guesswork-based version might. Do still flag that actual auction CPC will move with Quality Score and ad relevance once the campaign is live, and that this is a single CPC estimate rather than a bid range, both are planning inputs, not a guarantee.
