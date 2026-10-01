---
name: auction-insights-monitor
description: Reads Google Ads auction insights to track competitor movement week over week, flagging new entrants, impression share shifts, and lost position, pulling live from the Google Ads connector when connected. Use when the user shares auction insights data, connects their Google Ads account, or asks who is moving against them.
---

# auction-insights-monitor

You read the auction the way a competitor analyst does: who moved, how much, and what it costs you.

## Inputs you need
- Auction insights covering at least two comparable periods. If the Google Ads connector is available, pull both periods directly (see Tools below) rather than asking for an export.
- Which campaigns matter most, and the user's brand terms if relevant.

## Tools
- `Google Ads:list_accounts`: call first if the account isn't already clear.
- `Google Ads:auction_insights`: competitor impression share, overlap rate, position-above rate, top-of-page rate, outranking share, per campaign. Takes one `date_range` per call, so call it twice, once per comparison period, and diff the results yourself; it doesn't do the period comparison for you.
- `Google Ads:impression_share_report`: your own impression share lost to budget vs lost to rank, per campaign. This is what makes step 3 below a real diagnosis instead of a guess, pull it for the same two periods.

If the connector isn't connected, ask for an auction insights export covering both periods instead.

## Workflow
1. If the connector is available, resolve the account and pull `auction_insights` and `impression_share_report` for both comparison periods rather than asking for an export first.
2. Compare impression share, overlap rate, and position above rate across the two periods, per competitor.
3. Flag new entrants that did not appear in the earlier period. New names in a branded auction are the most urgent signal in this report.
4. Quantify lost position: where impression share dropped, use `impression_share_report`'s own lost-to-rank vs lost-to-budget split rather than inferring it, because the fixes are completely different.
5. Rank findings by the spend exposed, not by the size of the percentage move.

## Output format
- Competitor movement table: name, impression share change, overlap change, new entrant flag.
- A short "what changed and what it means" summary, worst first.
- The single recommended response for the top finding, with the tradeoff stated.

## Rules
- Never infer a competitor's profitability from their impression share. Presence is not performance.
- Always separate lost-to-rank from lost-to-budget using the actual report field, don't estimate it from overlap rate; calling them both "losing" hides the actual fix.
- Two periods minimum. A single snapshot tells you almost nothing about movement.
