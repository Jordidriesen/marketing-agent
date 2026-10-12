# SEO + AEO Scorecard (on demand)

Load this only when a formal numeric score is needed: client reporting, a hard pre-publish gate, or benchmarking two drafts. For routine drafting the qualitative E-E-A-T read in `seo-aeo-core.md` is faster and usually enough.

Where a check is defined in `seo-aeo-core.md`, that definition is the criterion and is not restated here. Where a check is
genuinely new, the criterion is inline.

**Content Quality, 30 points**

| Check | Points | Criterion |
|---|---|---|
| Coverage/comprehensiveness | 7 | Covers the reader task with useful subtopics, evidence, and examples; no raw word-count target |
| Readability | 7 | Flesch 60–70 default, 55–75 acceptable; denser prose can be justified for technical or YMYL topics |
| Originality/unique value | 5 | Passes the Information gain audit in `seo-aeo-core.md` |
| Sentence & paragraph structure | 4 | Follows the chunk rule in `seo-aeo-core.md`, plus varied sentence rhythm |
| Engagement elements | 4 | Summary box near the top, callouts, varied content blocks |
| Grammar/clarity | 3 | Handled by `copy-editing`'s Seven Sweeps; this line reflects whether that pass has run |

**SEO Optimization, 25 points**

| Check | Points | Criterion |
|---|---|---|
| Heading hierarchy | 5 | H1 to H2 to H3, no skipped levels; headings describe the reader task |
| Title clarity | 4 | Accurate, distinctive, consistent with visible content |
| Semantic topic consistency | 4 | Per Entity consistency in `seo-aeo-core.md`: one canonical name throughout, title/headings/body describing the same task |
| Internal linking | 4 | Per `internal-linking-drafting.md`: 3–10 contextual links scaled to length, descriptive anchors, bidirectional where relevant |
| URL structure | 3 | Stable, readable, consistently cased path |
| Meta description | 3 | Per the keyword integration table in `seo-aeo-core.md`, plus page-specific accuracy, 150–160 characters |
| External linking | 2 | Each sourced statistic cites a tier 1–3 source (credibility chain in `seo-aeo-core.md`) |

**E-E-A-T Signals, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Author attribution | 4 | Named author or editor with clear editorial ownership; never "Admin," "Staff," "Team," or no byline |
| Source fidelity | 4 | Per Sourcing in `seo-aeo-core.md`: every material claim traces to a source that supports it |
| Trust indicators | 4 | Site has a contact page, an about page, and an editorial policy |
| Evidence basis | 3 | Verifiable sources or transparent original methodology; never first-person phrasing added just to perform experience |

**Technical Elements, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Schema markup baseline | 4 | Per Schema recommendations in `seo-aeo-core.md`: Article/BlogPosting + Person + Organization + BreadcrumbList; FAQPage optional |
| Image optimization | 3 | AVIF/WebP, descriptive alt text, lazy-loaded except the LCP image |
| Structured data elements | 2 | Per Structured formats in `seo-aeo-core.md`: tables, lists, comparison blocks present where the content calls for them |
| Page speed signals | 2 | LCP under 2.5s, no render-blocking JS, `fetchpriority` on the hero image |
| Mobile-friendliness | 2 | Responsive, accessible tap targets, no horizontal scroll |
| OG/social meta tags | 2 | `og:title`, `og:description`, `og:image` (1200x630), `twitter:card` |

**AI Citation Readiness, 15 points**

| Check | Points | Criterion |
|---|---|---|
| Evidence-backed citability | 4 | Per Factual density in `seo-aeo-core.md`: important sections self-contained and sourced, no fixed word band |
| Purpose fit | 3 | Per AEO architecture in `seo-aeo-core.md`: clear page purpose, intent-matched headings |
| Entity clarity | 3 | Per Entity consistency in `seo-aeo-core.md` |
| Content structure for extraction | 3 | Per Structured formats in `seo-aeo-core.md` |
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

Only issues not already triaged by the qualitative gate in `seo-aeo-core.md` need this
layer:

**Critical, must fix before publishing:** fabricated statistics (zero
tolerance), broken heading hierarchy (H1 to H3 skip), no source
attribution on claims, missing author attribution, verified
primary-content inaccessibility for a declared target crawler.

**High priority:** important sections that obscure their conclusion or
lack support, missing Article/Person/Organization/BreadcrumbList schema
baseline, fewer sourced statistics than the sourcing rule requires, missing meta description, title
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
