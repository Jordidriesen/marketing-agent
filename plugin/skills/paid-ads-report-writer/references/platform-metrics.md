# Platform metrics and normalisation

Reference for `paid-ads-report-writer`. Read it before writing any table or cross-platform comparison.

## Metric set per platform

Use the platform's own metric set in its section, and the shared set in the cross-platform view.

| Platform type | Lead metrics | Supporting metrics | Diagnostic only (appendix) |
|---|---|---|---|
| Paid search (Google Ads, Microsoft Ads) | Spend, conversions, CPA or ROAS, conversion rate | Clicks, CTR, avg CPC, search impression share, impression share lost to budget and to rank | Quality Score, match type split, device and geo splits |
| Performance Max / shopping | Spend, conversions, conversion value, ROAS | Asset group performance, search categories, brand vs non-brand share | Listing group and product level |
| Paid social, B2B (LinkedIn Ads) | Spend, leads, cost per lead, cost per qualified lead where CRM data exists | Lead form open and completion rate, CTR, CPC, reach, frequency | Demographics by job function, seniority, company size, industry |
| Paid social, B2C (Meta and similar) | Spend, results against the campaign objective, cost per result | Reach, frequency, CTR (link), CPM, landing page views | Placement and creative breakdowns |

## Conversion windows and view-through

Conversion windows are configurable per account and per conversion action, so always read the actual setting from the account or ask. Typical defaults to check against, as at 2026:

| Platform | Click-through window (typical default) | View-through counted? |
|---|---|---|
| Google Ads | 30 days for most conversion actions | Only for engaged-view or view-through conversion columns, reported separately |
| Microsoft Ads | 30 days | Separate column when enabled |
| LinkedIn Ads | 30 days | Yes, included in conversions by default; the window is configurable |
| Meta | 7 days | Yes, 1-day view is included in the default attribution setting |

These defaults are a sanity check, not a source. If the report states a window, it must come from the account.

Rules that follow:

- When a social platform's conversions include view-through, show click-based and view-through separately in the platform section, and use click-based only when comparing against search.
- When the CRM or GA4 is the source of truth for leads, say so, and show the platform-reported number next to the CRM number rather than replacing one with the other.
- Never sum conversions across platforms into one total unless the definitions match. If they don't, show the per-platform numbers side by side and explain the gap in one line.

## Demand capture and demand creation

Paid search mostly captures demand that already exists; paid social mostly creates it. A report that ranks them on last-click CPA alone will always tell the client to cut social. To avoid that:

- Judge search on CPA or ROAS and on lost impression share (headroom).
- Judge social on cost per qualified lead, reach within the target audience, and, where the CRM allows it, pipeline or revenue influenced. Say which lens you used.
- If branded search volume or direct traffic moved during a social push, mention it as a possible assisted effect, clearly labelled as correlation.

## Cross-platform table, standard shape

| Platform | Spend | Primary outcome | Cost per outcome | Share of spend | Share of outcomes | Change vs comparison period |
|---|---|---|---|---|---|---|

Under the table, one line: the outcome definition per platform, the conversion windows used, and the currency.

## Housekeeping

- Convert Google Ads `cost_micros` by dividing by 1,000,000 before reporting.
- Use one currency across the report; state the conversion rate and date if any platform bills in another currency.
- Use the same date range on every platform, in the client's time zone where the platform allows it, and say if one platform reports in a different time zone.
- Search terms and keywords always carry their ad group name.
