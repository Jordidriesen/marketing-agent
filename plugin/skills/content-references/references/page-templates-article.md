# Page Templates: Articles and Reference Pages

Load this at Step 4 of `web-content-pipeline` for blog posts, pillar pages and content hubs, comparison pages, and glossary or reference pages. Landing, product, solution, feature, homepage, pricing and about pages use `page-templates-conversion.md` instead.

## Blog post template (Informational)

Apply the AEO architecture from
`content-references/references/seo-aeo-core.md` (atomic chunking,
entity consistency, factual density, bolded certainty anchors, credibility
chain) to this shape:

```
[Title]               H1: primary keyword near the front, ≤60 chars.
                      Precise numbers beat vague superlatives.
[Hook]                First 50–100 words: direct declarative answer
                      (Minto-style) or a brief status-quo pain point
                      before the answer (Sparkline-style, per Step 2).
                      Bold the answer paragraph.
[Audience line]       One sentence after the hook: who the page is for
                      and what it covers, with a link to the pillar page.
[Table of Contents]   Anchor-linked H2 list
[H2 sections]         Each = one atomic topic, paragraphs per the chunk rule in seo-aeo-core.md
[Key Takeaways box]   Bulleted; bold the most citable sentence per section
[Comparison table]    For any "A vs B" angle
[FAQ section]         Min. 3 questions, standalone answers (length per seo-aeo-core.md)
[Conclusion]          Re-answers the opening question, then one short
                      product paragraph and ONE bold CTA line with a link
[Production notes]    Hidden HTML comment at the end: meta description
                      (150–160 chars, primary keyword, CTA hook), schema
                      suggestion (Article or TechArticle; FAQPage for the
                      FAQ), word-count target, byline placeholder, and
                      `verify` flags on unconfirmed claims
```

**Comparison pages ("A vs B")** are written fair to the incumbent: say what it
does well, keep "when to choose" lists that a reader can honestly answer no to,
and say when the current setup is the right answer. **Regulatory or legal topics**
cite the instrument and article, add a Sources section, and flag a legal review gate
in the production notes. Never present a draft as legal advice.

Run the information-gain audit from `seo-aeo-core.md` before
finalizing.


## Pillar page or content hub

Use the blog template. The hook answers the broad question, then a map of the subtopics links out to every spoke, and each spoke links back to the pillar. Update the pillar as the cluster grows. Keep spokes distinct in search intent and do not publish thin spokes to add volume.

## Comparison page ("A vs B")

Decision rule first, then a side-by-side table, then when to choose each option and what can stay as it is. Fair to the option the reader runs today, with no vendor attacks.

## Glossary or reference page

Definitions that stand alone, grouped by theme, with stable anchors that other pages link to on first mention of a term. Never rename or delete an anchor once published. No sales arc.

## Keyword integration (full weight on articles)

Per the placement table in `seo-aeo-core.md`: primary keyword in the title or H1, the first 100 words, at least one H2, the conclusion and the meta description.

## Internal linking (full weight on articles)

Per `internal-linking-drafting.md`: 3 to 10 contextual links scaled to length, descriptive anchors, at least one link in the first two or three paragraphs, and a link to the pillar early in any supporting article.

## E-E-A-T quality gate

Run `content-references/references/seo-aeo-core.md`'s E-E-A-T
quality gate against the draft before moving to Step 5. Full weight for
blog posts and other Informational-bucket pages, where ranking and AI
citation trust matter most; lighter touch for Transactional pages: check
audience targeting and entity precision, skip query coverage and citation
density if the page isn't trying to rank on breadth. Note which of the
eight checks are weak; that's more useful than a formal score.

For client reporting or a hard pre-publish gate where a formal number is
actually needed, run the same reference file's Quality Scorecard instead
of, not in addition to, the checklist above.

---

