---
name: content-references
description: "Shared writing references (frameworks, SEO and AEO rules, psychology, schema) loaded by the content skills. Not for direct requests."
metadata:
  version: 1.1.0
  history: "v1.1.0: restructured for load efficiency. Intent and frameworks merged into content-briefing; page templates moved out of the pipeline; SEO/AEO and internal linking split into always-load and on-demand files; dependency map added; one rule each for sourcing, chunk size and CTA strength. v1.0.1: truthful index, canonical honesty rule, pointer file removed. Provenance: the shared library replaced rules once duplicated inside several skills."
---

# Content References: Shared Library

Eight reference files, each reusable across the content skills instead of duplicated inside each one. Reference files are not loaded for you: a skill that needs one reads it, and loads only what the piece in hand needs. The first column says when.

| File | What it covers | Load when |
|---|---|---|
| `references/content-briefing.md` | Intent (Informational, Navigational, Transactional), page type, structural framework (Minto, Sparkline, StoryBrand, PAS, BLUF), one decision path, the CTA-strength rule | A brief needs intent or framework reasoning the skill's own table does not settle, and for any piece longer than a few sentences with no table to follow |
| `references/page-templates-article.md` | Blog, pillar or hub, comparison and glossary templates, full-weight keyword and linking rules, the E-E-A-T gate | Step 4 for article types (required) |
| `references/page-templates-conversion.md` | Landing, product, solution, feature, homepage, pricing and about templates, CTA formulas, implementation brief, behavioural layer, visual cues | Step 4 for conversion and site pages (required) |
| `references/behavioral-psychology.md` | Shotton, Ehrenberg-Bass, Cialdini and fluency research: copy and visual persuasion principles, with caveats | Persuasion detail for conversion pages, ads and emails; light touch for informational content |
| `references/seo-aeo-core.md` | AEO architecture, the sourcing rule and chunk rule, keyword integration, information gain audit, E-E-A-T gate (six additive checks), schema, platform differences, visual asset rules | Articles meant to rank or be cited; schema and AEO questions |
| `references/seo-aeo-scorecard.md` | Optional 100-point scorecard, scoring bands, triage priorities | Only when a formal quality score is requested |
| `references/internal-linking-drafting.md` | Link density, anchor text distribution, placement, bidirectional linking, hub-and-spoke | While drafting any piece over a couple of hundred words |
| `references/internal-linking-audit.md` | Orphan-page detection, audit checklist, link velocity, tracking | Only when auditing an existing site section |

Cannibalization detection lives in `keyword-clustering` and `seo-audit`, not here.

## Dependency map

Who loads what. "Required" means the skill reads it every run; the rest are on demand.

| Skill | Loads |
|---|---|
| `web-content-pipeline` | page-templates-article or page-templates-conversion (required, one of them); content-briefing, seo-aeo-core, behavioral-psychology (on demand); the template files point to seo-aeo-core and internal-linking-drafting for articles |
| `customer-story-writer` | content-briefing (framework definitions) |
| `social-content-writer`, `press-release-writer`, `newsletter-writer`, `email-sequence-hubspot-brevo`, `campaign-plan`, `landing-page-matcher`, `ad-creative-matrix` | content-briefing; behavioral-psychology where the skill cites it |
| `copy-editing`, `ad-copy-tester`, `rsa-writer`, `competitor-teardown`, `disapproval-diagnoser`, `lead-magnets` | behavioral-psychology |
| `seo-audit`, `content-translate` | seo-aeo-core (AEO rules, schema) |
| nobody by default | seo-aeo-scorecard (a formal score), internal-linking-audit (a site audit) |

## Canonical honesty rule

Every skill that loads this library follows this rule, stated once here. Never invent numbers, quotes, customers, logos, awards, certifications or prices. Missing proof becomes a visible placeholder (Lorem Ipsum in the form the proof will take on a web page, a bracketed placeholder in a story) with a hidden `PROOF NEEDED` note. A claim the sources (the brief, the brand kit, the product file) support at about 90% likelihood or better is written plainly. Anything weaker gets a hidden `confirm` note, or the general version the sources do support. Reference files in this library point here and never into a generation skill.

## How a generation skill should use this

1. **Classify intent and page type first**, then choose a structural framework (`content-briefing.md`). Intent says what the reader wants; the framework says how the piece is built to deliver it.
2. **Read the page template** for the page type, then pull in persuasion, SEO/AEO and linking detail only where the piece needs it.
3. **Run the humanising pass** (`ai-content-cleaner`) as the last step on every piece. It owns the humanising rules and the language pattern files, and loads the brand voice itself.
