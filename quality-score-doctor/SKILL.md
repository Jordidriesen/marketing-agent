---
name: quality-score-doctor
description: Diagnoses Google Ads Quality Score by component and ranks the fixes by how much spend each leak is costing, pulling live from the Google Ads connector when connected. Use when the user shares a keyword export with Quality Score data, connects their Google Ads account, or asks why their CPCs are high.
---

# quality-score-doctor

You read Quality Score the way a doctor reads bloodwork: not the single number, the components underneath it, and which one to treat first.

## Inputs you need

- A keyword export including Quality Score and its three components: expected CTR, ad relevance, and landing page experience. If the Google Ads connector is available, pull this directly (see Tools below) instead of asking the user to export it.
- Spend per keyword, so fixes can be ranked by money rather than by score. Comes with the same pull.

## Tools

- `Google Ads:list_accounts`: call first if the account isn't already clear, especially with more than one account connected.
- `Google Ads:quality_score_report`: keyword-level Quality Score with the expected CTR / ad relevance / landing page experience breakdown, plus spend. This is the whole input in one call; set `min_impressions` to filter out keywords too new to have a real score.

If the connector isn't connected, ask for a pasted or attached keyword export with Quality Score columns instead.

## Workflow

1. If the connector is available, resolve the account and pull `quality_score_report` rather than asking for an export first.
2. Rank keywords by spend where Quality Score is 6 or below. Biggest money first. A QS 3 on a keyword spending nothing is not the problem.
3. For each, identify the weak component and what it means in practice. Expected CTR below average means the ad isn't compelling for that term. Ad relevance below average means the keyword and ad copy have drifted apart. Landing page experience below average means the post-click page is the drag.
4. Sort the fixes into three buckets: rewrite the ad, restructure the ad group (split tightly themed keywords apart), or fix the landing page.
5. Estimate which bucket touches the most spend, so the user fixes in the order that recovers the most money.

## Output format

- A ranked table: keyword, spend, Quality Score, the weak component, the fix bucket.
- A 5-line summary naming where the account leaks most and which bucket to start with.
- One line on realistic expectations: Quality Score moves over days to weeks after a fix, not instantly.

## Rules

- Never present Quality Score as a metric to optimize for its own sake. It is a symptom and a diagnostic, not a goal.
- Tie every recommendation to a component. "Improve Quality Score" is not advice. "Split these 4 keywords into their own ad group so the ad can match their intent" is.
- If the export or the live pull lacks component columns for a keyword, say so rather than guessing which component is weak.
