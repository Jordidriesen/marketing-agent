# SEO + AEO Optimization Reference

Structural and technical rules for content meant to rank in traditional
search and be cited by AI answer engines (Gemini, Perplexity, SearchGPT).
Format-agnostic — a generation skill applies the parts relevant to what
it's producing rather than the whole reference every time. A landing page
needs the keyword-integration rules but not the FAQ/Hook architecture; a
blog post needs both.

Part of the `content-references` shared library.

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
in favor of content that opens with the answer — a direct answer in the
first 50 words meaningfully raises citation probability.

**Entity consistency enables attribution.** If a paragraph uses "the
company," "they," and "the vendor" to refer to the same entity, the model
can't confidently attribute the claim and moves on.

**DOM structure affects extraction.** Semantic HTML5 (`<article>`,
`<section>`, `<aside>`) signals extractable content boundaries. Clean
heading hierarchy (H1→H2→H3, no skipping) mirrors what the DOM should do —
a developer concern, but one content structure should support, not fight.

---

## AEO architecture (apply to any content meant to be cited)

**Content architecture:**
- Answer one clear primary question per piece
- Open with a direct, declarative answer in the first 50–100 words — no
  literary lead-in, no question, no statistic buildup first
- Structure every section as a standalone "atomic" chunk, answerable
  without the rest of the page for context

**Entity consistency:**
- Use canonical names throughout — always "OpenAI," never "the company"
  or "the startup," for the same entity in the same piece

**Chunk hygiene:**
- 40–120 words per paragraph, one concept each. Over 120: split it.
  Under 40: merge or cut.
- No pronoun without an explicit, unambiguous referent

**Factual density:**
- At least one verifiable, sourced statistic per major section ("per a
  2025 Pew report," not "studies show")
- Vague claims are deprioritized by LLMs; precise, sourced statements get
  cited

**Bolded certainty anchors:**
- Bold the single most citable sentence per section — ideally one
  containing a statistic or clear fact. Functions as an LLM "certainty
  anchor" for that chunk.

**Structured formats AI engines extract directly:**
- Numbered lists for any step-by-step process
- Markdown tables for any "X vs Y" or "which is better" comparison —
  built from structured tables, not prose comparisons
- FAQ answers: 40–60 words, one concept, standalone without page context

**Credibility chain:**
- 3–5 external citations to high-authority domains (.edu, .gov, tier-1
  industry publications) — this is what internal trustworthiness
  classifiers weigh most

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
paragraphs. Never force keyword density — semantic relevance and entity
clarity outrank density.

---

## Information gain audit

Before finalizing any piece meant to rank, verify it adds something beyond
a baseline LLM answer to the same question. At least one of:
- **Original data or research** — proprietary benchmarks, internal stats,
  first-party surveys
- **Expert or first-hand perspective** — practitioner verdicts, "I tried
  this" insight, named-source quotes
- **Numerical density** — precise, sourced figures vs. vague claims
- **An extra layer of analysis** — aligns with consensus but adds an angle
  competing pieces don't cover

No qualifying element present → flag it before shipping. AI engines
deprioritize consensus content with no differentiating layer.

---

## E-E-A-T quality gate

A compact, checkable pass for Experience/Expertise/Authoritativeness/
Trustworthiness — run once a draft is otherwise complete, as a gate before
copy editing rather than a drafting rule. Several E-E-A-T-adjacent checks
already live elsewhere in this file or in `web-content-pipeline` itself;
this section covers only what isn't already handled, so nothing gets
checked twice:

**Already covered — don't re-check here:** direct-answer opening (Content
architecture, above), heading hierarchy and TOC (`web-content-pipeline`'s
blog template), chunk size and section chunking (Chunk hygiene, above),
keyword placement (Traditional keyword integration, above), sourced
statistics (Factual density and Information gain audit, above), entity
consistency at the canonical-name level (Entity consistency, above).

**Genuinely additive — apply these:**

| Check | What it means | How to apply |
|---|---|---|
| Audience targeting | State plainly who the piece is for | One explicit sentence early on ("if you're evaluating X for Y, this covers...") — cheap, often skipped |
| Query coverage | Cover 3+ real query variants for the topic — synonyms, long-tail, question forms — not just the primary keyword | Pull variants from the keyword research stage rather than guessing at drafting time |
| Data precision floor | 5+ precise numbers with units per piece | Sharpens `behavioral-psychology.md`'s Precision-over-round-numbers principle with a concrete minimum |
| Citation density floor | 1+ external citation per 500 words | Tighter than this file's Credibility chain (3–5 per piece); apply whichever is stricter for the piece's length |
| Evidence-claim mapping | Every claim is backed by a cited or linked source, not just asserted | Flag any claim in the draft that has no evidence attached |
| Entity precision | Full name for a person, org, or product on its first mention in the piece, even if later mentions use the canonical short form | Extends Entity consistency (above) — that section says use one name consistently; this adds that the *first* use should be the full name |
| Multimedia structure | Every image or video has a caption and carries real information — never decorative filler | Cross-reference `behavioral-psychology.md`'s Picture superiority principle; decorative stock fails both checks at once |
| Practical tools | Offer a downloadable template, checklist, or calculator where the topic genuinely supports one | Don't build it inline — flag the opportunity and hand off to `free-tool-strategy` |

**Scoring:** after the checklist, give one overall read — how many of the
eight checks the piece clearly passes — rather than a formal 1–10 score.
The number matters less than which specific checks are weak, since those
are what determine the fix.

---

## Quality scorecard (optional 100-point pass)

A formal numeric score, for the moments that actually need one: client
reporting, a hard pre-publish gate, or benchmarking two drafts against each
other. Same underlying rules as everywhere else in this file; this just
weights and totals them. Skip it for routine drafting, the qualitative read
above is faster and usually enough.

Where a check is already fully defined elsewhere in this file, that
definition is the criterion, it isn't restated here. Where a check is
genuinely new, the criterion is inline.

**Content Quality, 30 points**

| Check | Points | Criterion |
|---|---|---|
| Coverage/comprehensiveness | 7 | Covers the reader task with useful subtopics, evidence, and examples; no raw word-count target |
| Readability | 7 | Flesch 60–70 default, 55–75 acceptable; denser prose can be justified for technical or YMYL topics |
| Originality/unique value | 5 | Passes the Information gain audit above, at least one qualifying element present |
| Sentence & paragraph structure | 4 | Follows Chunk hygiene above (40–120 words/paragraph, one concept each), plus varied sentence rhythm |
| Engagement elements | 4 | Summary box near the top, callouts, varied content blocks |
| Grammar/clarity | 3 | Handled by `copy-editing`'s Seven Sweeps; this line reflects whether that pass has run |

**SEO Optimization, 25 points**

| Check | Points | Criterion |
|---|---|---|
| Heading hierarchy | 5 | H1 to H2 to H3, no skipped levels; headings describe the reader task |
| Title clarity | 4 | Accurate, distinctive, consistent with visible content |
| Semantic topic consistency | 4 | Per Entity consistency above: one canonical name throughout, title/headings/body describing the same task |
| Internal linking | 4 | Per `internal-linking.md`: 3–10 contextual links scaled to length, descriptive anchors, bidirectional where relevant |
| URL structure | 3 | Stable, readable, consistently cased path |
| Meta description | 3 | Per the keyword integration table above, plus page-specific accuracy, 150–160 characters |
| External linking | 2 | Per Credibility chain above: 3–5 citations to tier 1–3 sources |

**E-E-A-T Signals, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Author attribution | 4 | Named author or editor with clear editorial ownership; never "Admin," "Staff," "Team," or no byline |
| Source fidelity | 4 | Per Evidence-claim mapping above: every material claim traces to a source that supports it |
| Trust indicators | 4 | Site has a contact page, an about page, and an editorial policy |
| Evidence basis | 3 | Verifiable sources or transparent original methodology; never first-person phrasing added just to perform experience |

**Technical Elements, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Schema markup baseline | 4 | Per Schema recommendations below: Article/BlogPosting + Person + Organization + BreadcrumbList; FAQPage optional |
| Image optimization | 3 | AVIF/WebP, descriptive alt text, lazy-loaded except the LCP image |
| Structured data elements | 2 | Per Structured formats above: tables, lists, comparison blocks present where the content calls for them |
| Page speed signals | 2 | LCP under 2.5s, no render-blocking JS, `fetchpriority` on the hero image |
| Mobile-friendliness | 2 | Responsive, accessible tap targets, no horizontal scroll |
| OG/social meta tags | 2 | `og:title`, `og:description`, `og:image` (1200x630), `twitter:card` |

**AI Citation Readiness, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Evidence-backed citability | 4 | Per Factual density above: important sections self-contained and sourced, no fixed word band |
| Purpose fit | 3 | Per AEO architecture above: clear page purpose, intent-matched headings |
| Entity clarity | 3 | Per Entity consistency above |
| Content structure for extraction | 3 | Per Structured formats above |
| AI crawler accessibility | 2 | Declared target crawlers can access or render the primary content; robots policy matches declared goals |

### Scoring bands

| Score | Rating | Action |
|-------|--------|--------|
| 90–100 | Exceptional | Publish as-is, flagship content |
| 80–89 | Strong | Minor polish, ready for publication |
| 70–79 | Acceptable | Targeted improvements needed before publish |
| 60–69 | Below standard | Significant rework required |
| < 60 | Rewrite | Fundamental issues, start from outline |

### Priority when reporting issues

Only issues not already triaged by the qualitative gate above need this
layer:

**Critical, must fix before publishing:** fabricated statistics (zero
tolerance), broken heading hierarchy (H1 to H3 skip), no source
attribution on claims, missing author attribution, verified
primary-content inaccessibility for a declared target crawler.

**High priority:** important sections that obscure their conclusion or
lack support, missing Article/Person/Organization/BreadcrumbList schema
baseline, fewer than 8 sourced statistics, missing meta description, title
tag outside 40–60 characters, no internal links, Flesch score outside
55–75, no OG/social meta tags, passive voice above 15%.

**Medium priority:** fewer than 2 charts, fewer than 3 images, tier 4–5
sources present, self-promotion beyond 1 mention, sections exceeding 300
words between headings, images not in AVIF/WebP format, average sentence
length above 22 words.

**Low priority:** missing chart-type diversity, images without alt text,
missing external links to tier 1–3 sources, entity terminology
inconsistency.

---

## Schema recommendations (for implementation, not content itself)

**Baseline for every article or blog post:** `Article`/`BlogPosting` +
`Person` (author) + `Organization` (publisher) + `BreadcrumbList`. Include
`dateModified` on `Article` for freshness re-crawl signals.

- `FAQPage` — optional, only for pieces with visible FAQ content; an
  entity and AI-citation signal, not a Google rich-result target on its
  own
- `HowTo` — any step-by-step guide; include `step` and `instruction`
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

Cross-reference `behavioral-psychology.md` for the full detail — the two
principles that matter most for this specific use case:
- **Picture superiority / dual coding:** pair any process, comparison, or
  structural explanation with a real diagram or screenshot, never
  decorative stock — paired image+text is remembered far better than
  prose alone, and gives AI engines an additional extraction target
- **Distinctive brand assets:** any chart, quote card, or pull-image
  should reuse the brand's established colour/shape/iconography system
  rather than a one-off style per piece, so recognition compounds
