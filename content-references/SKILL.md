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
| `references/seo-aeo-optimization.md` | Traditional SEO + AEO (AI citation) structural and technical rules, an E-E-A-T quality gate, and an optional 100-point quality scorecard for when a formal score is actually needed | Any content meant to rank or be cited — blog posts, guides, product pages |
| `references/internal-linking.md` | Link density targets, anchor text distribution and anti-patterns, placement priority, hub-and-spoke architecture, orphan-page detection. Cannibalization detection lives in `keyword-clustering`/`seo-audit` instead, not duplicated here | Any piece over a couple hundred words — run during drafting, not as a post-publish afterthought |
| `references/ai-content-humanizing.md` | AI-writing-pattern detection and removal, DETECT/CLEAN/BALANCED modes. Its own Step 0 routes to the matching language-specific pattern file (`ai-humanizing-patterns-nl.md`, `-fr.md`, `-de.md`, `-es.md`) when the draft isn't in English | Final pass on any drafted content, before delivery |

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
4. **Run the humanizing pass** (`ai-content-humanizing.md`) as the last step
   on every piece, regardless of type — it loads the right language file
   itself.

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
