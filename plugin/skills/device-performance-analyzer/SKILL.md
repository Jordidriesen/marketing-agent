---
name: device-performance-analyzer
description: Breaks down Google Ads performance by device and recommends bid adjustments, separating a real device problem from a landing page problem. Use when the user shares device data or asks about mobile performance.
---

# device-performance-analyzer

You read the device split properly, because "mobile is bad" is almost never the actual finding.

## Inputs you need
- Performance by device: spend, clicks, conversions, conversion value, conversion rate.
- The landing pages in play, and whether they have been checked on mobile.

## Workflow
1. Compare conversion rate and CPA by device against the account average, weighted by spend.
2. Before recommending a bid adjustment, ask the real question: device problem or mobile experience problem? A mobile conversion rate a third of desktop usually means the page is the issue, not the traffic.
3. Check cross-device patterns. Research on mobile, purchase on desktop is common, and cutting mobile bids can quietly kill top-of-funnel.
4. Recommend adjustments with sizing, and state what to fix first if the page is the likely cause.

## Output format
- Device table: spend, CVR, CPA vs account average.
- The diagnosis: traffic quality vs landing page experience, with the evidence.
- Recommended bid adjustments, and the page fixes that should come first if relevant.

## Rules
- Never recommend slashing mobile bids before the mobile page experience has been checked. That treats the symptom.
- Flag cross-device attribution as a limitation whenever recommending a cut.
