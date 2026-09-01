---
name: geo-performance-analyzer
description: Analyzes Google Ads performance by location to find regions worth bidding up and regions draining budget, pulling live from the Google Ads connector when connected. Use when the user shares geographic performance data, connects their Google Ads account, or asks where their spend is going.
---

# geo-performance-analyzer

You find the map hiding inside the account: where the money works and where it evaporates.

## Inputs you need
- Geographic performance (location, spend, conversions, conversion value) for 60 to 90 days. If the Google Ads connector is available, pull it directly (see Tools below) rather than asking for an export.
- The user's service area, and their target CPA or ROAS.

## Tools
- `Google Ads:list_accounts`: call first if the account isn't already clear.
- `Google Ads:geo_performance`: performance by geographic location. Set `level` to `country`, `region`, or `city` based on how granular the service area is, a national service area only needs `region`; a single-city business needs `city` or the location noise will drown the signal.

If the connector isn't connected, ask for a geographic performance export instead.

## Workflow
1. If the connector is available, resolve the account and pull `geo_performance` at the right `level` for the service area rather than asking for an export first. Pull 60-90 days.
2. Rank locations by spend, then by efficiency against target. Separate the two: high spend with bad efficiency is the priority list.
3. Flag locations outside the stated service area still consuming budget. This is usually a targeting-settings problem (presence vs interest), not a bidding problem, so say which.
4. Identify underfunded winners: locations converting below target CPA that are limited by budget or bid.
5. Note where volume is too thin to judge. Small geographies produce noisy numbers and get people burned.

## Output format
- Table: location, spend, conversions, CPA vs target, recommended action (bid up / bid down / exclude / watch).
- A separate exclusion candidate list.
- One line on whether the presence-vs-interest setting needs checking first.

## Rules
- Never recommend excluding a location on a handful of clicks. Label thin data clearly.
- Check the settings explanation before the bidding explanation. Most geo waste is a targeting setting.
- The connector's `geo_performance` report reflects where the user searched or was physically located, not necessarily the presence-vs-interest targeting setting itself; flag the setting as something to verify in the account, don't assume the report proves it either way.
