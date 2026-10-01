---
name: content-references
description: >
  Shared reference library for content-creation skills. Not triggered
  directly by user requests — loaded by other skills (web-content-pipeline,
  customer-story-writer, rsa-writer, social-content-writer, etc.)
  as needed. If you've landed here from a direct request, route to one of
  those skills instead; this is infrastructure, not a workflow.
---

# Content References — Shared Library

Five reference modules, each reusable across every content-creation skill
instead of duplicated inside each one. A generation skill pulls in only the
modules relevant to the piece it's producing — not all five, every time.

| Reference | What it covers | Pull it in when... |
|---|---|---|
| `references/content-intent-framework.md` | Informational / Navigational / Transactional classification | **Always** — the first step of any content-generation skill, not optional |
| `references/communication-frameworks.md` | Minto, Sparkline, StoryBrand, PAS, BLUF — structural framework selection | Any piece longer than a few sentences needs a deliberate structural choice, not just intent |
| `references/behavioral-psychology.md` | Shotton, Ehrenberg-Bass, Cialdini, fluency research — copy and visual persuasion principles | Copywriting and strategy work; lighter touch for pure reference/informational content |
| `references/seo-aeo-optimization.md` | Traditional SEO + AEO (AI citation) structural rules, off-page/freshness GEO signals, an E-E-A-T quality gate (with a Who/How/Why pre-gate), and an optional 100-point quality scorecard for when a formal score is actually needed | Any content meant to rank or be cited — blog posts, guides, product pages |
| `references/internal-linking.md` | Link density targets, anchor text distribution and anti-patterns, placement priority, hub-and-spoke architecture, orphan-page detection. Cannibalization detection lives in `keyword-clustering`/`seo-audit` instead, not duplicated here | Any piece over a couple hundred words — run during drafting, not as a post-publish afterthought |
| `references/ai-content-humanizing.md` | Pointer only: the humanising rules and language files moved to the `ai-content-cleaner` skill, which is now their single owner | Final pass on any drafted content: invoke `ai-content-cleaner` |

## How a generation skill should use this

1. **Classify intent first** (`content-intent-framework.md`) — this determines
   everything downstream: CTA strength, proof type, which structural
   framework fits.
2. **Pick a structural framework** (`communication-frameworks.md`) — informed
   by intent, but a separate decision. Intent says *what the reader wants*;
   the framework says *how the piece is built* to deliver it.
3. **Write the draft**, pulling behavioral-psychology, SEO/AEO, and
   internal-linking principles in only where they're relevant to the
   intent bucket and content type.
4. **Run the humanising pass** (the `ai-content-cleaner` skill) as the last
   step on every piece, regardless of type. It loads the brand voice and the
   right language file itself.

## Why this exists

Previously, AEO rules, AI-pattern detection, and behavioral-science
principles were each fully re-implemented inside multiple skills
(`blog-content-pipeline`, `copywriting`, `copy-editing`, `seo-content-writer`
before it was retired). That meant editing a rule required finding and
updating every copy of it, and skills grew large with content that had
nothing to do with their actual differentiator. `blog-content-pipeline`
and `copywriting` were later merged into `web-content-pipeline` for the
same reason at a structural level: the split between "blog" and
"landing/product page" was artificial — both are web content, differing
only in page-type template, not in process. This hub holds the shared
knowledge once; skills hold only what's genuinely specific to the format
they produce.
