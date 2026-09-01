---
name: competitive-brief
metadata:
  version: 1.0.0
  history: >
    Built for the marketing plugin. Added the [brand]-brand-kit check for
    the "Our Differentiators" framing, moved research-source lists,
    positioning frameworks, and the battlecard template into references/,
    made the battlecard an explicit optional step rather than inline
    reference material, and sharpened the pointer to
    competitor-analysis/competitive-landscape for SEO-grounded data.
description: >
  Researches named competitors via web search and produces a positioning
  and messaging comparison — strengths, weaknesses, content gaps,
  opportunities, and threats. Use when building sales battlecards, finding
  positioning gaps and messaging angles competitors haven't claimed, or
  assessing the impact of a competitor's move. For organic-footprint and
  ranking-keyword research backed by live SEO tooling rather than web
  search, use competitor-analysis or competitive-landscape instead — this
  skill covers messaging and positioning, not SEO performance.
argument-hint: "<competitor or market segment>"
---

# Competitive Brief

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

You read a competitor's public-facing messaging the way their own prospects do, then find the gap between what they claim and what a battlecard actually needs to be true. A brief that just restates their homepage isn't competitive intelligence.

## Step 0 — Identify the Brand and Load Its Kit

If "Our Differentiators" (Section 7) or a battlecard is being produced, determine which brand/client this is for and check for a `[brand]-brand-kit` skill — its locked terminology and voice govern how differentiators are phrased, same pattern as `web-content-pipeline`.

## Trigger

User runs `/competitive-brief`, or asks for a competitive analysis, competitor research, market comparison, or a sales battlecard.

## Inputs

1. **Competitor name(s)** — required, one or more.
2. **Your company/product context** — optional but recommended: what you sell, to whom, your positioning, differentiators you want highlighted.
3. **Focus areas** — optional; default to covering all: messaging/positioning, product/feature comparison, content strategy, recent announcements, pricing (if public), market presence.

## Research Process

For each competitor, research via web search: company website (homepage, product pages, pricing, about), recent news (last 6 months — funding, launches, partnerships), content strategy (blog topics, resource types, social presence), review sites and third-party comparisons, and job postings as a strategic-direction signal. See `references/research-sources.md` for the full source list and recommended research cadence.

## Competitive Brief Structure

### 1. Executive Summary
2–3 sentences on the competitive landscape. Lead with the single biggest opportunity and the single biggest threat — not a balanced list of five of each.

### 2. Competitor Profiles
Per competitor: company overview (one-sentence positioning, audience, size/stage signals, recent developments), messaging analysis (tagline, value prop, 3–5 key themes, tone, how they frame the problem), product/solution positioning (category, emphasized features, claimed differentiators, pricing if public), content strategy (frequency, formats, SEO targets observed), strengths, and weaknesses. See `references/positioning-frameworks.md` for the Value Proposition and Narrative Analysis methodology behind the messaging analysis.

### 3. Messaging Comparison Matrix

| Dimension | Your Company | Competitor A | Competitor B |
|---|---|---|---|
| Primary tagline | | | |
| Target buyer | | | |
| Key differentiator | | | |
| Tone/voice | | | |
| Core value prop | | | |

Include the "Your Company" column only if positioning context was provided in Inputs.

### 4. Content Gap Analysis
Topics/formats/keywords competitors cover that you don't, and vice versa. Methodology and comparison tables in `references/positioning-frameworks.md`.

### 5. Opportunities
Positioning gaps to exploit, messaging angles nobody's claimed, underserved segments, content/channel openings — grounded in specific findings from Sections 2–4, not generic marketing advice.

### 6. Threats
Where competitors are strong and you're vulnerable, trends favoring their positioning, recent moves that could shift the market.

### 7. Recommended Actions
3–5 specific recommendations, split into quick wins (actionable this week) and strategic moves (longer-term positioning or content investment). Every recommendation should trace to a specific finding above — if it doesn't, it's generic advice, not competitive intelligence.

### 8. Battlecard (optional — only if requested)
See `references/battlecard-template.md`. Distinct artifact from the brief, built from its findings for sales use.

## Related Skills

For SEO-grounded competitor data — organic footprint, ranking keywords, content-gap analysis backed by live SERP tooling — use `competitor-analysis` (single competitor, deep dive) or `competitive-landscape` (multiple competitors, market-level view) and feed their findings into Section 4 rather than relying on web search alone. Once positioning gaps are identified, `campaign-plan` can build a campaign around them, and finished differentiator copy should pass `brand-review` before it ships.

## Output

Note the research date so the reader knows how fresh the findings are. Executive Summary stays to 2–3 sentences — the detail lives in the sections below it, not restated at the top.

After the brief, ask:

"Would you like me to:
- Build a battlecard from this analysis?
- Draft messaging that exploits the positioning gaps identified?
- Dive deeper into any specific competitor?
- Set up a competitive monitoring plan?"
