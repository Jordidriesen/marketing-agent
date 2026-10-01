# Trend Analysis and Attribution

Supporting reference for `performance-report`'s Trend Analysis section.

## Trend identification

Look for: directional trends (consistently up/down/flat over 4+ periods), inflection points (where and why performance changed direction), seasonality (predictable day/month/quarter patterns), anomalies (one-time spikes — caused by what, and repeatable?), and leading indicators (which metrics move first and predict the rest).

**Process:** chart the metric over at least 8–12 data points, identify direction, calculate whether the rate of change is accelerating or decelerating, overlay key events (campaigns, product changes, market events), compare to benchmark/target, check correlations with other metrics, then form a causal hypothesis and plan a test to validate it — a trend without a hypothesis is just an observation.

**Simple forecasting:** linear projection (stable metrics), moving average (smooth 3–6 period noise), year-over-year baseline adjusted for growth rate, funnel math (forecast outputs from input×conversion-rate), or scenario modeling (best/expected/worst case). Short-term forecasts (1–3 months) are more reliable than long ones; flag anything built on fewer than 12 data points as low-confidence; always present forecasts as ranges, never single numbers.

## Attribution

Attribution determines which touchpoint gets credit for a conversion — this matters because buyers typically cross multiple channels before converting.

| Model | How it works | Best for | Limitation |
|---|---|---|---|
| Last touch | 100% to the final interaction | Understanding conversion triggers | Ignores awareness/nurture |
| First touch | 100% to the first interaction | Understanding top-of-funnel effectiveness | Ignores what actually converts |
| Linear | Equal credit to all touchpoints | Fair representation | Doesn't reflect relative impact |
| Time decay | More credit closer to conversion | Balanced, recency-weighted view | May undervalue awareness |
| Position-based (U-shaped) | 40% first, 40% last, 20% middle | Valuing discovery and conversion both | Somewhat arbitrary weighting |
| Data-driven | Algorithmic, based on conversion patterns | Most accurate | Needs high data volume |

**Guidance:** start with last-touch if nothing else is in place — simplest and most actionable. Compare first-touch vs. last-touch to separate awareness channels from conversion channels. Position-based is a reasonable default for most B2B accounts. Data-driven needs real conversion volume to be meaningful. No model is perfect — use attribution directionally.

**Pitfalls:** don't optimize a single channel off single-touch attribution alone — awareness channels (display, social, PR) always look weak in last-touch, and conversion channels (search, retargeting) always look weak in first-touch. Self-reported "how did you hear about us" is useful qualitative color, not quantitative data. Cross-device tracking gaps mean attribution data is always somewhat incomplete — report it as directional, not exact.
