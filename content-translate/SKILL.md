---
name: content-translate
description: >
  Translate existing web content (blog posts, landing pages, product pages,
  customer stories) into one or more target languages with locale-correct
  formatting, native-sounding tone, and brand-locked terminology carried
  over. Combines language translation and cultural adaptation into one
  pass — formality, brand examples, legal references, and CTA tone are
  applied during translation itself, not as a separate step. Use when the
  user says "translate this," "translate to German/French/Dutch/Spanish,"
  "vertalen naar het Nederlands," "traduire en français," "übersetzen ins
  Deutsche," "traducir al español," or wants a page localized for a
  specific European market. Composes with the relevant `[brand]-brand-kit`
  skill for voice and locked terminology, and with `content-references`
  for schema rules and the target-language humanizing pass.
metadata:
  version: 1.0.0
  history: >
    Adapted from a third-party blog-translate/blog-localize/blog-multilingual
    module. Two changes from the original: the sub-agent ("Task") spawning
    architecture is replaced with a single direct pass, matching how the
    rest of this library works, and cultural adaptation is folded into the
    same pass rather than deferred to a separate localize skill, since the
    real workflow here is translating already-written English content, not
    writing five market versions from scratch. The original's hreflang/
    sitemap generation (blog-multilingual Phase 5) isn't included yet —
    every market is already live with its own URL structure; build that
    piece later if a from-scratch multi-market launch actually needs it.
---

# Content Translate

Takes an existing piece of web content, a blog post, landing page, product
page, or customer story, and produces a native-quality, publish-ready
version in one or more target languages: correct formality register,
locale number/date/currency/quote formats, market-appropriate brand
examples and legal references, and any brand-locked terminology already
confirmed for that client.

**Scope:** translating and culturally adapting existing content. Not for
writing original content in multiple languages from scratch
(`web-content-pipeline` handles the source-language draft first). Not for
generating hreflang tags or sitemaps.

---

## The Sequence

```
0. Parse source + targets       Resolve locale codes, detect source language
1. Extract translatable surface Frontmatter, headings, body, alt text, schema
2. Identify brand               Load [brand]-brand-kit if the content is branded
3. Localize keywords            Keep vs. swap, checked via seo-keyword-research when unclear
4. Select cultural profile      references/cultural-adaptation.md, per target locale
5. Translate                    references/translation-rules.md + cultural profile + brand terms, one pass
6. Humanize in target language  content-references/references/ai-content-humanizing.md
7. QA sweep                     translation-rules.md's Quality Criteria Checklist
        ↓
     Delivered translation(s)
```

Run Steps 2-7 once per target language. Parallelize across languages when
translating into more than one at a time — there's no dependency between
target languages, only between steps within a single language.

---

## Step 0 — Parse Source and Targets

1. Resolve the source: an uploaded file, pasted content, or an existing
   published page. If it's a file path, resolve it against the project
   root, reject symlinked paths, traversal outside the root, files over
   10 MB, and binary files.
2. Detect source language, in order of preference: frontmatter `lang`
   field, HTML `lang` attribute, then content analysis.
3. Parse target languages as Google-compatible hreflang tags (`de`, `fr`,
   `nl-BE`, `es`, `ja`, `pt-BR`). If the target list is missing or
   unclear, ask once: "Which languages? Give hreflang tags such as de,
   fr, nl, es."
4. Normalize each code: ISO 639-1 language in lowercase, optional ISO
   15924 script in title case, optional ISO 3166-1 Alpha-2 region in
   uppercase. Reject invalid codes with a suggestion (`jp` becomes "Did
   you mean `ja`?"). Require a region, or an explicit neutral mode, for
   ambiguous language-only targets: `es`, `pt`, `zh`. `de`, `fr`, `nl`,
   and `ja` can resolve without a region per
   `cultural-adaptation.md`'s Profile Selection Logic.
5. If a target equals the normalized source language, skip it with a
   notice.

---

## Step 1 — Extract the Translatable Surface

Extract:

- Frontmatter: `title`, `description`, `tags`, `author` role labels (not
  personal names).
- All headings (H1, H2, H3).
- Body paragraphs.
- Image `alt` text and `<figcaption>` content.
- Chart `<text>` and `<tspan>` content; preserve every other SVG
  attribute.
- FAQ questions and answers.
- Evidence-backed explanation text and sourced statistics.
- Key Takeaways or summary box.
- CTA text.
- Internal-link zone anchor text.

Preserve unchanged: markdown/HTML structure and attributes, image and link
URLs, frontmatter keys, executable code fences and inline code (translate
comments only if explicitly asked), internal-link zone markers, source
organization names in citations, person names, and Schema JSON-LD
identifiers/URLs/`@id`/`sameAs` (translate only the user-facing content
strings).

Identify the primary and secondary keywords for Step 3.

---

## Step 2 — Identify the Brand

Check whether the content belongs to a brand with its own
`[brand]-brand-kit` skill (`acme-brand-kit` today; more to follow the
same pattern per that skill's "Brand Kit Pattern" section). If found, load
it now:

- Apply its voice pillars in the target language, not just the source.
- Treat any **Locked Terminology** section in the brand kit as
  authoritative. It overrides Step 3's keyword-localization judgment call
  and this skill's own defaults — don't re-derive a term the brand has
  already confirmed.
- If no brand kit exists yet, translate against the source content's
  existing voice and flag that a brand kit doesn't exist for this client,
  the same gap `web-content-pipeline` flags in its own requirements step.

---

## Step 3 — Localize Keywords

Per `references/translation-rules.md`'s SEO Translation Principles:

1. Decide whether the source keyword is the established term in the
   target market (e.g., "Content Marketing" stays in German). If yes,
   keep it.
2. If a local equivalent has real search behavior, swap to it.
3. Where it's genuinely unclear, run both variants through
   `seo-keyword-research` for the target market and keep whichever has
   real search volume, rather than guessing.
4. Apply the same logic to secondary keywords.
5. Record the mapping so the title, meta description, and H2 headings
   update consistently with it in Step 5.

---

## Step 4 — Select the Cultural Profile

Per `references/cultural-adaptation.md`'s Profile Selection Logic: exact
locale match, then unambiguous language-only fallback, then regional
grouping (DACH, LATAM, Benelux), then the custom-locale template for
anything not covered.

Pick one formality register for the whole piece per the profile (e.g.
DACH `Sie` vs `du`) and hold it — don't drift mid-document. Note which
brand examples, statistics sources, legal references, and CTA tone apply;
these get applied during translation in Step 5, not as a follow-up pass.

If a brand kit was loaded in Step 2 and it specifies its own formality
convention for that market, the brand kit wins over the general profile
default.

---

## Step 5 — Translate

One integrated pass per target language, applying all three inputs
together rather than translating first and adapting later:

- **Mechanics** from `references/translation-rules.md`: format
  preservation, number/date/currency/quote conversion, SVG text length
  adjustment, banned patterns.
- **Cultural fit** from the Step 4 profile: formality register, brand
  examples, legal references, CTA tone, idiom adaptation.
- **Brand voice and locked terminology** from the Step 2 brand kit, when
  one applies.

Reserve judgment calls for what the references don't already answer. If a
rule and the brand kit conflict, the brand kit wins. If the cultural
profile and a literal translation conflict, the cultural profile wins.

---

## Step 6 — Humanize in the Target Language

Run `content-references/references/ai-content-humanizing.md`. Its own
Step 0 routes to the matching language-specific pattern file
(`ai-humanizing-patterns-de.md`, `-fr.md`, `-nl.md`, `-es.md`)
automatically — translated copy carries its own AI tells, distinct from
the English source's, and this catches them in the target language rather
than assuming a clean English draft stays clean after translation.

Use **BALANCED mode** for anything with FAQ or comparison-table structure
worth protecting (matches `web-content-pipeline`'s Step 6 default for the
same content types); **CLEAN mode** otherwise.

---

## Step 7 — QA Sweep

Run `references/translation-rules.md`'s Quality Criteria Checklist
directly — it already covers structural integrity, format correctness,
machine-translation artifacts, and mixed-language sentences. Nothing new
to check here; this step is "run that checklist," not a second list.

Flag every failure inline: file or section, what's wrong, the fix. Re-pass
any flagged section before delivery rather than shipping with known
issues.

---

## Step 8 — Delivery

```
## Translation complete: [Original title]

### Source
- Language: [source]
- Brand: [brand, or "none identified"]

### Translations
| Language | Keywords adapted | Brand terms applied | Status |
|----------|------------------|----------------------|--------|
| de-DE | [N] | [N] | ok |
| fr-BE | [N] | [N] | ok |

### Quality checklist
- Structural integrity: pass/fail per language
- Format correctness (numbers, dates, currency, quotes): pass/fail
- Machine-translation artifacts flagged: [N] (see notes above)
- Humanizing pass: BALANCED/CLEAN per language

### Next steps
- [Any flagged sections needing a second look]
- Resolve `[INTERNAL-LINK]` placeholders with locale-specific URLs
- If this becomes a from-scratch multi-market launch rather than a
  translation of existing content, hreflang/sitemap generation would be
  the next thing to build, not part of this skill today
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Unsupported or ambiguous language code | Suggest the correct hreflang code, or ask for the region on `es`/`pt`/`zh` |
| Source equals a target | Skip with "Source is already in [lang]" |
| File not found | Report the error with a suggested path |
| No brand kit exists for this client | Translate against the source voice, flag the gap, suggest building one on the `acme-brand-kit` pattern |
| Binary or non-text file | Report the error, suggest the correct file |
| Cultural profile not covered | Build one inline from the Custom-Locale Template in `cultural-adaptation.md`, and suggest adding it permanently if the market is likely to recur |

---

## Full Checklist (One-Page Summary)

- [ ] Source language detected, target codes normalized and validated
- [ ] Brand identified, `[brand]-brand-kit` loaded if one exists, Locked
      Terminology noted
- [ ] Keywords localized (kept or swapped); unclear cases checked via
      `seo-keyword-research`
- [ ] Cultural profile selected, one formality register held throughout
- [ ] Translation complete: mechanics + cultural fit + brand voice applied
      together
- [ ] Humanizing pass run in the target language (BALANCED or CLEAN)
- [ ] Quality Criteria Checklist (`translation-rules.md`) run, failures
      flagged and re-passed
- [ ] Schema `inLanguage` updated, `translationOfWork` added

---

## Related Skills

- **`acme-brand-kit`** (and future `[brand]-brand-kit` skills) — Step 2
  loads these for voice and locked terminology
- **`web-content-pipeline`** — usually where the source-language content
  came from; this skill picks up after that one delivers
- **`seo-keyword-research`** — Step 3 checks real search volume for
  ambiguous keyword-localization calls
- **`content-references`** (`ai-content-humanizing.md`) — Step 6's
  target-language polish pass
- **`content-references`** (`seo-aeo-optimization.md`) — the schema
  baseline (Article/Person/Organization/BreadcrumbList) translated schema
  JSON-LD should match

## Reference Docs

- `references/translation-rules.md`
- `references/cultural-adaptation.md`
