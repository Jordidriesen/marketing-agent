# SEO + AEO Core

Structural and technical rules for content meant to rank in search and be cited by AI answer engines (Gemini, Perplexity, SearchGPT). Apply the parts relevant to what you are producing: a landing page needs the keyword rules but not the hook and FAQ architecture, a blog post needs both. The optional formal scorecard lives in `seo-aeo-scorecard.md`.

---

## Why these rules exist

These rules follow from how LLMs actually parse web content, not from SEO
folklore. Understanding the mechanism matters for judgment calls when
rules conflict.

**The page is a raw data source, not a destination.** AI engines decompose
pages into "contextual fragments" for a RAG (Retrieval-Augmented
Generation) pipeline. The page is a source to be cited, not the final stop.

**Atomic content wins.** LLMs favor self-contained, factually dense
information units over narrative prose. Each chunk must be comprehensible
without surrounding context.

**The opening determines citation.** The first ~50 words are processed by
an extractive QA layer. Content that builds toward an answer gets skipped
in favor of content that opens with the answer: a direct answer in the
first 50 words meaningfully raises citation probability.

**Entity consistency enables attribution.** If a paragraph uses "the
company," "they," and "the vendor" to refer to the same entity, the model
can't confidently attribute the claim and moves on.

**DOM structure affects extraction.** Semantic HTML5 (`<article>`,
`<section>`, `<aside>`) signals extractable content boundaries. Clean
heading hierarchy (H1→H2→H3, no skipping) mirrors what the DOM should do:
a developer concern, but one content structure should support, not fight.

---

## AEO architecture (apply to any content meant to be cited)

**Content architecture:**
- Answer one clear primary question per piece
- Open with a direct, declarative answer in the first 50–100 words: no
  literary lead-in, no question, no statistic buildup first
- Structure every section as a standalone "atomic" chunk, answerable
  without the rest of the page for context

**Entity consistency:**
- Use canonical names throughout: always "OpenAI," never "the company"
  or "the startup," for the same entity in the same piece

**Chunk hygiene (the chunk rule, stated once):**
- 40–120 words per paragraph, one concept each. Over 120: split it.
  Under 40: merge or cut. Pages under about 500 words (landing pages) may
  run shorter, but never put two concepts in one paragraph.
- No pronoun without an explicit, unambiguous referent

**Factual density (the sourcing rule, stated once):** at least one
sourced statistic per 500 words, and at least four per piece, and every
material claim maps to a source ("per a 2025 Pew report," not "studies
show"). Vague claims are deprioritized by LLMs; precise, sourced statements
get cited. Never invent a number to meet the minimum: the canonical honesty
rule in `content-references/SKILL.md` wins, and a piece with fewer real
statistics says so in its hidden notes.

**Bolded certainty anchors:**
- Bold the single most citable sentence per section, ideally one
  containing a statistic or clear fact. Functions as an LLM "certainty
  anchor" for that chunk.

**Structured formats AI engines extract directly:**
- Numbered lists for any step-by-step process
- Markdown tables for any "X vs Y" or "which is better" comparison:
  built from structured tables, not prose comparisons
- FAQ answers: 40–60 words, one concept, standalone without page context

**Credibility chain:** each sourced statistic cites a high-authority
domain (.edu, .gov, tier-1 industry publications). This is what internal
trustworthiness classifiers weigh most.

---

## Traditional keyword integration

| Placement | Requirement |
|---|---|
| Title / H1 | Primary keyword, preferably at the start |
| First 100 words | Primary keyword |
| At least one H2 | Primary keyword or close variant |
| Body (H2/H3) | Secondary keywords and "people also ask" questions |
| Conclusion | Primary keyword |
| Meta description | Primary keyword, naturally integrated, 150–160 chars |

Secondary keywords and LSI/related terms: use naturally in H2s and body
paragraphs. Never force keyword density: semantic relevance and entity
clarity outrank density.

---

## Information gain audit

Before finalizing any piece meant to rank, verify it adds something beyond
a baseline LLM answer to the same question. At least one of:
- **Original data or research**: proprietary benchmarks, internal stats,
  first-party surveys
- **Expert or first-hand perspective**: practitioner verdicts, "I tried
  this" insight, named-source quotes
- **Numerical density**: precise, sourced figures vs. vague claims
- **An extra layer of analysis**: aligns with consensus but adds an angle
  competing pieces don't cover

No qualifying element present → flag it before shipping. AI engines
deprioritize consensus content with no differentiating layer.

---

## E-E-A-T quality gate

A compact pass for Experience/Expertise/Authoritativeness/Trustworthiness,
run once a draft is otherwise complete and before copy editing. Checks that
already live elsewhere in this file are not repeated here:

**Already covered; don't re-check here:** direct-answer opening (Content
architecture, above), heading hierarchy and TOC (the generation skill's
blog template), chunk size and section chunking (Chunk hygiene, above),
keyword placement (Traditional keyword integration, above), sourced
statistics (Factual density, above), entity
consistency at the canonical-name level (Entity consistency, above).

**Apply these:**

| Check | What it means | How to apply |
|---|---|---|
| Audience targeting | State plainly who the piece is for | One explicit sentence early on ("if you're evaluating X for Y, this covers..."): cheap, often skipped |
| Query coverage | Cover 3+ real query variants for the topic, synonyms, long-tail, question forms, not just the primary keyword | Pull variants from the keyword research stage rather than guessing at drafting time |
| Sourcing | The sourcing rule under Factual density: at least one sourced statistic per 500 words, minimum four, every material claim mapped to a source | Flag any claim in the draft with no evidence attached; sharpens `behavioral-psychology.md`'s precision-over-round-numbers principle |
| Entity precision | Full name for a person, org, or product on its first mention in the piece, even if later mentions use the canonical short form | Extends Entity consistency: use one name consistently, with the full name on first use |
| Multimedia structure | Every image or video has a caption and carries real information, never decorative filler | Cross-reference `behavioral-psychology.md`'s Picture superiority principle; decorative stock fails both checks at once |
| Practical tools | Offer a downloadable template, checklist, or calculator where the topic genuinely supports one | Don't build it inline: flag the opportunity and hand off to `free-tool-strategy` |

**Scoring:** give one overall read, how many of the six checks the piece clearly passes, and name the weak ones. They decide the fix. For a formal number see `seo-aeo-scorecard.md`.

---

## Schema recommendations (for implementation, not content itself)

**Baseline for every article or blog post:** `Article`/`BlogPosting` +
`Person` (author) + `Organization` (publisher) + `BreadcrumbList`. Include
`dateModified` on `Article` for freshness re-crawl signals.

- `FAQPage`: optional, only for pieces with visible FAQ content; an
  entity and AI-citation signal, not a Google rich-result target on its
  own
- `HowTo`: any step-by-step guide; include `step` and `instruction`
  properties

## Platform differences (brief)

- **Google Gemini:** favors first-party structured data and consistent
  site hierarchy
- **OpenAI SearchGPT:** favors third-party directory presence and
  consensus validation
- **Perplexity:** favors original research, academic citations, and high
  semantic concept density over backlinks

Write the core content for Perplexity-quality citability (precision,
originality, no fluff). Schema serves Gemini. Directory presence and
consensus serve SearchGPT.

---

## Visual assets for SEO/AEO content

From `behavioral-psychology.md`, the two principles that matter most here:
- **Picture superiority / dual coding:** pair any process, comparison, or
  structural explanation with a real diagram or screenshot, never
  decorative stock, paired image+text is remembered far better than
  prose alone, and gives AI engines an additional extraction target
- **Distinctive brand assets:** any chart, quote card, or pull-image
  should reuse the brand's established colour/shape/iconography system
  rather than a one-off style per piece, so recognition compounds
