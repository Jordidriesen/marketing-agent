---
name: competitive-research
description: 'Competitor research: a deep dive on one competitor''s organic footprint, SEO market leaders across several competitors, content gaps by keyword cluster, and competitor ad teardowns. Use for "analyse this competitor", "competitor deep dive", "who is winning this market", "competitive landscape", "content gap analysis", "where are we behind", or shared competitor ads. Market sizing: european-market-intelligence.'
metadata:
  version: 1.0.0
  history: 'v1.0.0: new family skill in marketing-operator 0.2.0, generated once from marketing-agent 3.1.2. Absorbs competitor-analysis, competitive-landscape, content-gap-mapping, competitor-teardown as references, unchanged apart from names and paths.'
---

# Competitive Research

One skill for a family of related tasks that share the same inputs and connectors. Each task is a full reference file: pick the row that matches the request, read that file **in full**, and follow it as the skill. Where a request needs two tasks (an audit, then the search terms), run them one after the other, each from its own file.

| Task reference | Use it for |
|---|---|
| `references/competitor-analysis.md` | Deep dive on one named competitor's organic footprint, rankings and page content. Use for "analyse this competitor", "competitor deep dive". |
| `references/competitive-landscape.md` | Maps SEO market leaders across several competitors with OpenSEO and page crawls. Use for "who is winning this market", "competitive landscape". One competitor: competitor-analysis. |
| `references/content-gap-mapping.md` | Maps content gaps, parity and advantages between our site and competitors across keyword clusters. Use for "content gap analysis", "where are we behind". Does not write content. |
| `references/competitor-teardown.md` | Breaks down competitor ads: angles everyone claims, open angles, what to test first. Use when competitor ad copy or creative is shared. |

If no row fits, say so and name the skill that does fit rather than stretching a reference.

**Required skill calls.** The references name the skills they call (for example `brand-review` or `ai-content-cleaner`); call those through the Skill tool, never imitate them inline. End the reply with one line: `Skills run: ...`, naming this skill and the reference used, for example `Skills run: competitive-research (competitor-analysis)`.
