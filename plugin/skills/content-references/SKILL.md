---
name: content-references
description: "Shared writing references (frameworks, SEO and AEO rules, psychology, schema) loaded by the content skills. Not for direct requests."
metadata:
  version: 1.0.1
  history: "v1.0.1: index describes each file truthfully and counts its modules correctly; canonical honesty rule added; the pointer-only humanising file removed."
---

# Content References: Shared Library

Five reference modules, each reusable across every content-creation skill
instead of duplicated inside each one. A generation skill pulls in only the
modules relevant to the piece it's producing, not all five, every time.

| Reference | What it covers | Pull it in when... |
|---|---|---|
| `references/content-intent-framework.md` | Informational / Navigational / Transactional classification | **Always**: the first step of any content-generation skill, not optional |
| `references/communication-frameworks.md` | Minto, Sparkline, StoryBrand, PAS, BLUF: structural framework selection | Any piece longer than a few sentences needs a deliberate structural choice, not just intent |
| `references/behavioral-psychology.md` | Shotton, Ehrenberg-Bass, Cialdini, fluency research: copy and visual persuasion principles | Copywriting and strategy work; lighter touch for pure reference/informational content |
| `references/seo-aeo-optimization.md` | Traditional SEO + AEO (AI citation) structural rules: AEO architecture, traditional keyword integration, an information gain audit, an E-E-A-T quality gate (eight additive checks), an optional 100-point quality scorecard for when a formal score is needed, schema recommendations, platform differences and visual asset rules | Any content meant to rank or be cited: blog posts, guides, product pages |
| `references/internal-linking.md` | Link density targets, anchor text distribution and anti-patterns, placement priority, bidirectional linking, hub-and-spoke architecture, orphan-page detection, an audit checklist, link velocity and tracking. Cannibalization detection lives in `keyword-clustering` and `seo-audit`, not here | Any piece over a couple hundred words: run during drafting, not as a post-publish afterthought |

## Canonical honesty rule

Every skill that loads this library follows this rule, stated once here. Never invent numbers, quotes, customers, logos, awards, certifications or prices. Missing proof becomes a visible placeholder (Lorem Ipsum in the form the proof will take on a web page, a bracketed placeholder in a story) with a hidden `PROOF NEEDED` note. A claim the sources (the brief, the brand kit, the product file) support at about 90% likelihood or better is written plainly. Anything weaker gets a hidden `confirm` note, or the general version the sources do support. Reference files in this library point here and never into a generation skill.

## How a generation skill should use this

1. **Classify intent first** (`content-intent-framework.md`); this determines
   everything downstream: CTA strength, proof type, which structural
   framework fits.
2. **Pick a structural framework** (`communication-frameworks.md`): informed
   by intent, but a separate decision. Intent says *what the reader wants*;
   the framework says *how the piece is built* to deliver it.
3. **Write the draft**, pulling behavioral-psychology, SEO/AEO, and
   internal-linking principles in only where they're relevant to the
   intent bucket and content type.
4. **Run the humanising pass** (the `ai-content-cleaner` skill) as the last
   step on every piece, regardless of type. It loads the brand voice and the
   right language file itself. It owns the humanising rules and the language pattern files.

## Why this exists

Previously, AEO rules, AI-pattern detection, and behavioral-science
principles were each fully re-implemented inside multiple skills
(`blog-content-pipeline`, `copywriting`, `copy-editing`, `seo-content-writer`
before it was retired). That meant editing a rule required finding and
updating every copy of it, and skills grew large with content that had
nothing to do with their actual differentiator. `blog-content-pipeline`
and `copywriting` were later merged into `web-content-pipeline` for the
same reason at a structural level: the split between "blog" and
"landing/product page" was artificial, both are web content, differing
only in page-type template, not in process. This hub holds the shared
knowledge once; skills hold only what's genuinely specific to the format
they produce.
