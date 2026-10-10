---
name: paid-ads-report-writer
description: "Writes client-ready paid media reports across Google, Microsoft, LinkedIn and Meta: executive summary, per-platform sections, normalised cross-platform view. Use for \"ads report\", \"monthly paid report\"."
metadata:
  version: 2.0.0
  history: >
    v2.0: renamed from report-writer and widened from Google Ads only to all
    paid platforms, search and social. Added platform resolution, live pulls,
    a normalisation step, per-platform sections and a platform-metrics
    reference. The executive-summary rules from v1 are kept unchanged.
---

# Paid Ads Report Writer

You write the report a client actually reads: an honest summary at the top, then the evidence per platform, in a shape that lets search and social be judged on the same terms without pretending they work the same way.

## Step 0: Brand and platform check

1. Identify the brand or client. If a `[brand]-brand-kit` exists, read its `references/context.md` for the client's KPIs, the platforms they run, account names and reporting cadence. Write the report in the brand's reporting language if the kit sets one.
2. List the platforms in scope for this period. Report only on platforms that actually ran; a platform with zero spend gets one line saying so, not a section.
3. Confirm the period and the comparison period (previous period, same period last year, or both). If either is missing, ask.

## Step 1: Get the data

Per platform, in this order of preference:

| Platform | Live source | Fallback |
|---|---|---|
| Google Ads | Google Ads connector: resolve the account once (`list_accounts`), then `list_campaigns` and `run_gaql` for campaign and ad group metrics per `google-ads-tool-map`; `impression_share_report` for lost share | Campaign and ad group export from the Google Ads UI |
| LinkedIn Ads | LinkedIn Ads connector. Load its tools via tool search and confirm the method names before the first call; don't guess them | Campaign Manager export (campaign group, campaign, creative level) |
| Microsoft Ads | No connector in this stack | Export from Microsoft Advertising (campaign and ad group level) |
| Meta and any other platform | No connector in this stack | Ads Manager or platform export |

Follow `mcp-efficiency`: filter at the source by date range and minimum spend, resolve each account once, don't paste raw pulls back into the conversation. If a connector errors or isn't connected, say which platform is affected and switch that platform to its fallback rather than estimating.

Also ask for (or check the account change history for) what changed this period: budgets, new campaigns or audiences, creative swaps, bid strategy changes, landing pages, tracking. Without it, the "why" is a guess, so ask.

## Step 2: Normalise before you compare

Read `references/platform-metrics.md` before writing any cross-platform comparison. The short version:

- Compare on the client's business outcome (qualified lead, sale, revenue), never on platform-native vanity metrics alone.
- Note each platform's conversion window and whether view-through conversions are counted. A LinkedIn number that includes view-through conversions is not comparable to a Google Ads click-based number until you say so or separate them.
- Paid search captures existing demand; paid social mostly creates it. Judge social on cost per qualified lead and pipeline contribution as well as CPA, and say which lens you used.
- Use the same currency and the same date range for every platform. Convert micros and local currencies before any table.

## Step 3: Write the report

1. **Find the number that matters most** this period across all platforms. Not the prettiest number, the most consequential one. Lead with it.
2. **Explain the why** behind the biggest change, not just its direction. "CPA rose because we expanded into colder keywords to find volume" is reporting. "CPA rose 12%" is reading the screen out loud.
3. **State bad news directly**, paired with the fix. Clients smell hedging and trust evaporates with it.
4. **End with exactly 2 priorities** for next period, concrete enough to be checked later. "Improve performance" is not a priority. "Cut the 4 ad groups bleeding spend and move budget to brand campaigns" is.

## Output format

1. **Executive summary.** 4 to 6 sentences, plain language, no jargon. A smart person outside marketing should follow every sentence. Three numbers maximum.
2. **Cross-platform view** (only when two or more platforms ran). One table: platform, spend, primary outcome, cost per outcome, share of total spend, share of total outcomes, change against the comparison period. A line under the table saying which conversion definitions and windows were used.
3. **One section per platform.** 3 to 5 sentences on what happened and why, then a short table using that platform's own metric set from `references/platform-metrics.md`. Search sections show the top movers at campaign and ad group level. Social sections show campaign or campaign group and audience or creative level.
4. **Next period.** The 2 priorities, each with the platform it belongs to and how it will be checked.
5. **Appendix** (if asked): full campaign and ad group tables per platform.

## Rules

- Never soften results with filler ("overall a solid month with some challenges"). State what happened.
- No metric dumps in the narrative. Numbers live in tables.
- Whenever a keyword or search term is listed anywhere in the report, name its ad group next to it. A search term without its ad group can't be acted on.
- Every number traces to a tool call or an export you were given. If a metric can't be verified, say so instead of presenting an estimate.
- Never add two platforms' conversions together without saying whether the definitions match.
- If the data shows something the user might not want the client to see, flag it to the user privately first, but never write a summary that hides it.

## Related skills

- `metric-detective`: the "why did this move" diagnosis for a Google Ads metric, before you write about it
- `full-account-audit`, `search-term-auditor`: deeper Google Ads findings that can feed the priorities
- `competitor-teardown`: when a competitor's ads explain a shift in auction or CTR
- `[brand]-brand-kit`: client context, KPIs and reporting language (Step 0)
- `mcp-efficiency`, `google-ads-tool-map`: how to pull live data cheaply
