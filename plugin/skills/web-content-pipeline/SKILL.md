---
name: web-content-pipeline
metadata:
  version: 1.5.1
  history: "v1.5.1: chat reply is the file plus two sentences; no visible instructions in navigation rows. v1.5.0: questions and doubts become QUESTION and UNSURE comments collected in an OPEN ITEMS block for the person operating the chat. v1.4.1: required skill calls stated at the top, no inline substitute for copy-editing and ai-content-cleaner. v1.4.0: framework is the skill's choice, not forced; editor notes are hidden comments; component tags above each section; Lorem Ipsum proof placeholders; neutral headings; page-type guide with FAQ counts; pillar, comparison and glossary page types. v1.3.0: hidden confirm comments and visible proof placeholders replace the claim placeholders; ask-first gate; audience line, closing CTA block and hidden production notes for articles; implementation brief, single goal and objection FAQ for landing pages; Steps 5 and 6 are mandatory and reported. v1.2.0: description rewritten for the skill listing budget and widened to copywriting and page design; Steps 5 and 6 invoked through the Skill tool; claim test added. Body otherwise unchanged from 1.1.0."
description: "Always use for any website copy or copywriting, however short or fully specified: landing pages, homepages, product, solution, feature, pricing and about pages, page design and page copy work, a hero section, benefit blocks, CTAs, SEO or AEO blog posts. Not social posts or ebooks."
---

# Web Content Pipeline

Takes any web page, blog post, landing page, product page, solution page,
homepage, pricing page, feature page, or about page, from brief to
publish-ready. One pipeline instead of two, because the underlying
process is identical: classify intent, classify page type, pick a
structural framework, write to the right template, edit, humanize. What
differs by page type is the template in Step 4, not the process around it.

**Required skill calls.** Two other skills are part of this pipeline and must be called through the
Skill tool, never imitated with an inline edit: `copy-editing` after the Step 4 draft, and
`ai-content-cleaner` after that. If you have a draft and have not called both, call them now, before you
reply. A reply that says the edit pass was done inline, or that skips either skill, is not finished.

**Scope:** Web content only. Not social media (separate skill). Not
print/downloadable content like ebooks or whitepapers.

**Formerly two skills** (`web-content-pipeline` for blog posts,
`copywriting` for landing/product/solution pages): merged because the
split was artificial. A comparison-intent article and a landing page
making the same argument differ in structural framework and template, not
in process.

---

## Claim test: write what is plausible, never what is invented

Facts about the product, the offer or the company come from the brief, then the brand kit or the product
file (`products/<slug>.md`). Before you write a statement about what the product does or what a visitor
gets, ask: given those sources, is this at least about 90% likely to be true? If yes, write it plainly,
with no hedge, and let the framework do its work (the problem and agitation steps describe the audience's
situation, and outcomes that follow from a stated feature are fine). A plausible claim the sources do not
confirm (EU hosting, a walkthrough length, a deployment option) is still written, with a hidden note next to
it: `<!-- confirm: EU hosting, check region before publish -->`. The reader sees clean copy and the
editor sees what to check. If you would be guessing below that level (a specific mechanism, integration,
setting or step), use the general version the sources support.

These always need a source, however plausible they sound: numbers and percentages, customer names and
logos, quotes, awards and ratings, certifications and compliance claims, and prices. Missing proof is a
Lorem Ipsum placeholder in the form the proof will take, with a hidden `PROOF NEEDED` comment (see Step 4).
Never invent a customer or a figure to fill it. Leave a fact out, with a hidden
note, rather than approximate it.

A call to action may promise what the offering is meant to fix, as the brief states it.

Do not build selling points on a single fact. "A Belgian company" does not mean "a team in your time
zone and language", and "cloud" does not mean a named hosting region. If a benefit rests on something
the sources only hint at, leave it out or flag it with a hidden `confirm` note.

---

## The Sequence

```
0. Classify content intent    (content-references/references/content-intent-framework.md)
1. Classify page type         (blog post / landing / product / solution / homepage / pricing / feature / about)
2. Choose structural framework (content-references/references/communication-frameworks.md)
3. Gather requirements (incl. identify brand + load its brand kit)
4. Write to page-type template, applying:
     - content-references/references/seo-aeo-optimization.md
     - content-references/references/behavioral-psychology.md
     - content-references/references/internal-linking.md
5. Copy-edit                  (copy-editing skill, Seven Sweeps)
6. Humanize                   (ai-content-cleaner skill)
        ↓
     Final Page
```

---

## Step 0: Classify Content Intent

Per `content-references/references/content-intent-framework.md`:

| Bucket | Typical signal | What it usually means for page type |
|---|---|---|
| **Informational** | how/what/why/guide/tips, question-form | Usually a blog post. Soft CTA, authority-based proof. |
| **Transactional / Commercial Investigation** | buy/price/quote/best/vs, near-decision comparison | Usually landing, product, solution, or pricing page. Firm CTA, heavy proof. |
| **Navigational** | brand + specific page name | Homepage or a specific already-decided destination. Persuasion is the wrong tool; clarity and speed are. |

This is a starting signal, not a rule: a Transactional query can still be
best served by a comparison-style blog post if the business goal is
topical authority rather than immediate conversion. State the reasoning
if Step 1's page type doesn't match this table's default.

## Step 1: Classify Page Type

| Page type | Typical Content Bucket | Notes |
|---|---|---|
| Blog post | Informational (usually) | AEO structure matters most here |
| Landing page | Transactional | Single message, single CTA, matches traffic source |
| Product page | Transactional | Feature → benefit → outcome, clear path to buy |
| Solution page | Transactional | Same as product page, usually broader/more strategic framing |
| Homepage | Navigational-leaning, serves all buckets at once | Must route multiple audiences without being generic |
| Pricing page | Transactional | Decision-support as much as persuasion |
| Feature page | Transactional | Narrower than a product page: one feature, one use case |
| About page | Informational/brand | Origin story, still needs a CTA |
| Pillar page / content hub | Informational | Broad topic, links out to every spoke, each spoke links back |
| Comparison page (A vs B) | Informational leaning Transactional | Fair to the option the reader runs today; helps them decide |
| Glossary / reference page | Informational | Stand-alone definitions with stable anchors; no sales arc |

If unclear from the brief, ask. Getting this wrong wastes the rest of the
pipeline: the template in Step 4 depends entirely on it.

## Step 2: Choose Structural Framework

Consult `content-references/references/communication-frameworks.md` for
full detail. Page type drives the default; override with reasoning if the
piece has an unusual goal.

| Page type | Default framework | Why |
|---|---|---|
| Blog post | **Minto-style** (answer-first, for AEO) or **Sparkline-style** (status-quo pain before the answer, for thought-leadership posts) | Matches the Hook requirement either way: see Step 4 |
| Landing page | **StoryBrand** (longer narrative page) or **PAS** (short, punchy, ad-driven page) | Customer-as-hero beats company-as-hero when the visitor hasn't yet decided to trust you |
| Product page | **StoryBrand** | Character/problem/guide/plan maps directly onto persona/pain/product/how-it-works |
| Solution page | **StoryBrand** | Same logic, usually longer and more strategic in framing |
| Homepage | **StoryBrand-lite** | Position the brand as guide without forcing a single character arc: homepage serves multiple personas at once |
| Pricing page | **Minto-flavored comparison** (MECE-grouped plan differences) layered with **PAS-style** anchoring in the surrounding copy | Plan comparison is a logical-grouping problem; the sales copy around it is still an urgency/persuasion problem |
| Feature page | **PAS** (narrow, ad-driven) or **StoryBrand** (broader in-app explainer) | Depends on traffic source: ad-driven feature pages behave like landing pages |
| About page | **Sparkline-style** (origin story: what was → what is now) | Natural fit for a "what is / what could be" arc |
| Pillar page / content hub | **Minto-style** (answer first, then the map of subtopics) | The hub states the answer to the broad question, then routes the reader to the spokes |
| Comparison page (A vs B) | **Minto-style** with a side-by-side table | The reader wants the decision rule first, then the evidence |
| Glossary / reference page | None (definition format) | Each entry stands alone; no persuasion arc |

The skill chooses the framework that fits the page type, the traffic source and the goal. StoryBrand is the
common default for conversion pages, not a requirement: use PAS, Minto, Sparkline or another when it
fits better, and say which in one line with the reason. Note the chosen framework explicitly: it shapes
Step 4's template. If the brief names a framework, use it unless it clearly does not fit, and say so.

## Step 3: Gather Requirements

**Check for product marketing context first:** if `.agents/product-marketing-context.md`
exists (or `.claude/product-marketing-context.md` in older setups), read
it before asking questions. Use that context and only ask for what isn't
already covered.

**Identify the brand and load its brand kit.** Most people writing across
multiple brands or clients need this, each with its own voice: there's no
single default tone this skill can assume. Before drafting anything:

1. Determine which brand/client this piece is for, from the brief, from
   context already in the conversation, or by asking if genuinely unclear.
2. Check for a matching `[brand]-brand-kit` skill for that brand. Skills
   follow that naming convention specifically so this lookup can be done
   by pattern, not a hardcoded list.
3. **If found:** load it and apply its voice (and, once documented, visual
   identity) throughout Steps 4–6. Its rules override this skill's generic
   "Voice and Tone" section below, that section is a fallback, not a
   default to layer on top of a brand kit.
4. **If not found:** flag that no brand kit exists for this brand yet, fall
   back to the generic Voice and Tone section, and note that a
   `[brand]-brand-kit` skill is worth building if this becomes recurring
   work, see the "Brand Kit Pattern" section of an existing `[brand]-brand-kit`
   skill for the shape to follow, if you have one.

| Field | Input |
|---|---|
| Brand/client | Which brand: determines which brand kit applies |
| Page type (Step 1) | |
| Content Bucket (Step 0) | |
| Structural framework (Step 2) | |
| Primary keyword + secondary keywords | (still relevant for landing/product/solution pages, not just blog) |
| Target audience | Who is the ideal visitor/reader? |
| Primary action | The ONE thing you want them to do |
| Product/offer | What's being sold or explained; what makes it different; proof points |
| Traffic source | Ads, organic, email: shapes how much context the visitor already has |
| Tone (only if no brand kit exists) | professional / casual / technical |
| Competitor URLs or top-ranking posts | if known |

If any field is missing, ask before writing. When the brand, the primary action, the audience or the
product facts the page needs are missing from the brief, the brand kit and the product files, stop and
reply with 2 to 5 specific questions and nothing else: no draft, no copy with placeholders. Tone, length and
language may default; say which default you used.

---

## Step 4: Write to Page-Type Template

### Writing style rules (apply to every page type)

1. **Simple over complex**: "use" not "utilize," "help" not "facilitate"
2. **Specific over vague**: avoid "streamline," "optimize," "innovative"
   as unsupported claims
3. **Active over passive**: "we generate reports," not "reports are
   generated"
4. **Confident over qualified**: cut "almost," "very," "really"
5. **Show over tell**: describe the outcome, not adjectives about it
6. **Honest over sensational**: fabricated statistics or testimonials
   erode trust and create legal liability; never invent proof

Quick check before moving on: jargon that could confuse an outsider?
Sentences trying to do too much? Passive voice? Exclamation points (cut
them)? Buzzwords without substance?

### Hidden notes, placeholders and headings (all page types)

- **Editor notes are comments, not copy.** The file has two audiences: people reading the finished page and
  people editing the source. Everything meant for editors and for AI is an HTML comment in the same
  file: the implementation brief, a component tag above each section, `confirm` and `verify` notes,
  `PROOF NEEDED` notes, headline alternatives, the reasoning behind choices, and the closing
  `<!-- Skills run: ... -->` line. Nothing editor-facing may be visible when the page is rendered.
- **Questions and doubts go in the file, as comments.** Anything you would otherwise ask the editor
  becomes a comment next to the line: `<!-- QUESTION: ... -->`. A statement you cannot call about 90%
  likely and cannot check against the sources is written in its most cautious supported form, or left
  out, and gets `<!-- UNSURE: ... needs judging by the person operating the chat -->`. Collect every
  `QUESTION`, `UNSURE`, `PROOF NEEDED` and `confirm` note in one `<!-- OPEN ITEMS: ... -->` block at the
  end of the file, so the editor and the marketing director find them in one place. The page itself
  stays clean.
- **The chat reply is the file plus at most two sentences.** Do not repeat the open items, the edit-pass
  summary or the framework reasoning outside the file: they live in its comments. Navigation and
  button rows show the labels only, never instructions in parentheses outside a comment.
- **Component tags.** When the site has a component library, put the exact component name in a comment
  above each section (`<!-- COMPONENT: 3-up problem cards -->`). Reuse the existing components and
  introduce none. A form modal is not a page component. Never use numbers or labels like "Section 1".
  With no component library, skip the tags.
- **Missing proof becomes Lorem Ipsum.** When a section needs proof (a quote, a logo strip, a metric, a
  case card) and the brief, the brand kit and the product files do not supply it, fill that slot with
  Lorem Ipsum in the exact form the real proof will take, so the layout and the need are visible, and add
  a comment `<!-- PROOF NEEDED: customer quote, role, company -->`. Never invent a customer, a figure or
  a logo.
- **Neutral headings until proof exists.** A heading must not imply proof that is not there. Use "Where it
  runs", "References" or "Proof", not "Trusted by", "Customers like you" or "Used by teams like yours",
  until real proof fills the section.

### Page-type guide (defaults, adjust to the brief)

These are common practices, not rules. Practitioner sources agree on the broad shape and differ on the
details, so follow the brief and the brand kit first.

| Page type | Core sections | Proof | FAQ |
|---|---|---|---|
| Landing page (paid) | Hero, problem, plan, proof, objections, closing CTA; one goal, no site navigation | Close to the CTAs | 3 to 6 objection questions from this traffic source |
| Product page | Hero, features framed as use cases, how it works, proof, pricing path | Named, specific; near CTAs | Optional, 3 to 6, on fit and set-up |
| Solution page | Hero, the situation, use cases by role or industry, how it works, proof, related products | Close to the CTAs; case studies linked | 4 to 8, on roles, integration and replacing what exists |
| Feature page | One feature, one use case, visual, path to try | Light | Optional, 3 to 5 |
| Homepage | Value proposition, routes by audience, proof, one clear next step | Logos and one or two headline results | Usually none |
| Pricing page | Plans tied to buyer segments, a recommended plan, comparison grouped by outcome, billing toggle if relevant | Next to the decision point | 4 to 8 last-minute hesitations (billing, contract, support, security) |
| About page | Why the company exists, what it believes, who is behind it, a CTA | Light | None |
| Blog post | Answer-first hook, sections of one topic each, takeaways | Sources and examples | 3 to 5 |
| Pillar page / hub | Answer to the broad question, a map of subtopics, a link out to every spoke | Sources | 3 to 6; every spoke links back |
| Comparison page | Decision rule first, side-by-side table, when to choose each, what can stay | Sources, no vendor attacks | 3 to 5 |
| Glossary | Definitions with stable anchors, grouped by theme | None | None |

Keep spokes distinct in search intent and do not publish thin spokes to add volume.

### Blog post template (Informational, per Step 1)

Apply the AEO architecture from
`content-references/references/seo-aeo-optimization.md` (atomic chunking,
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
[H2 sections]         Each = one atomic topic, 40–120 words per paragraph
[Key Takeaways box]   Bulleted; bold the most citable sentence per section
[Comparison table]    For any "A vs B" angle
[FAQ section]         Min. 3 questions, 40–60 word standalone answers
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

Run the information-gain audit from `seo-aeo-optimization.md` before
finalizing.

### Landing / product / solution / feature page template (Transactional, per Step 1)

**Above the fold:**
- Headline: single most important message, specific over generic.
  Formulas: "{Achieve outcome} without {pain point}," "The {category} for
  {audience}," "Never {unpleasant event} again," or a direct question
  naming the main pain point. A precise number beats a vague superlative
  ("Cut onboarding to 11 days" beats "Faster onboarding"). Lead with
  whichever number or comparison should anchor the visitor's judgment for
  the rest of the page.
- Subheadline: expands the headline, adds specificity, 1–2 sentences max
- Primary CTA; states what they get: "Start Free Trial," not "Sign Up"

**Implementation brief** (hidden HTML comment at the top of the page): URL, traffic source or ad
group, negative keywords for paid traffic, the framework chosen in Step 2 and why, the ONE conversion
goal, form fields, meta title and description, and schema (Organization, BreadcrumbList,
SoftwareApplication or Product, FAQPage). Every primary CTA on the page opens the same action; a
secondary path (a one-pager, say) is visibly smaller and lower contrast, there to catch someone who is
not ready.

**Core sections** (map onto Step 2's chosen framework, StoryBrand's
Problem/Guide/Plan/Success or PAS's Problem/Agitate/Solution):

| Section | Purpose |
|---|---|
| Social proof | Build credibility: logos, stats, testimonials. Lorem Ipsum placeholders until real cases are approved (see Step 4) |
| Problem/pain | Show you understand the visitor's situation (StoryBrand's Problem / PAS's Problem+Agitate) |
| Solution/benefits | Connect to outcomes, 3–5 key benefits (StoryBrand's Plan / PAS's Solution) |
| How it works | Reduce perceived complexity, 3–4 steps |
| Objection handling | FAQ with the question count from the page-type guide, taken from the objections this traffic source arrives with (replace a system? another console? we already have X?), comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

**CTA copy:** avoid "Submit," "Sign Up," "Learn More," "Click Here,"
"Get Started." Use the formula [Action verb] + [what they get] +
[qualifier if needed], "Start My Free Trial," "Get the Complete
Checklist," "See Pricing for My Team."

**Reduce reactance** near any CTA implying commitment: "no credit card
required," "cancel anytime," "no obligation" next to the button removes
the felt pressure that causes hesitation.

**Frame availability/scarcity toward the desired reading, only when
true**: "12 spots left this month" reads as genuine and socially
confirming; "availability limited" reads as vague hedging. Never fabricate
scarcity.

**Page-type specifics:**

- **Homepage**: serve multiple audiences without going generic; lead with
  the broadest value proposition; provide clear paths for different
  visitor intents
- **Landing page**: single message, single CTA; match the headline to the
  ad/traffic source; complete the argument on one page
- **Product page**: feature → benefit → outcome; show use cases; clear
  path to try or buy
- **Solution page**: same as product page, usually broader and more
  strategic in framing; often the page that needs the fullest StoryBrand
  arc since the visitor is earlier in the decision
- **Pricing page**: help visitors choose the right plan, address "which
  is right for me" anxiety, make the recommended plan obvious. Consider a
  premium tier above the one you actually want to sell: a higher anchor
  makes the middle tier look sensible by contrast (extremeness aversion).
  Lead with the reference price you want anchoring the comparison.
- **Feature page**: connect feature → benefit → outcome; show use cases
  and examples; clear path to try or buy
- **About page**: tell the story of why the company exists, connect
  mission to customer benefit, still include a CTA. Natural home for one
  honest, specific limitation or early mistake ("we spent a year building
  the wrong thing before we found this"): a real admitted flaw from an
  otherwise competent narrative increases trust and likeability (the
  pratfall effect). One instance, genuinely true, not a hedge on every claim.

### Behavioral-science layer (all page types)

Apply the relevant rows from
`content-references/references/behavioral-psychology.md`. Blog/
Informational pages lean on precision numbers, concreteness, and fluency;
Transactional pages get the fuller treatment: anchoring, framing,
reactance reduction, extremeness aversion, and the pratfall effect where
the template above calls for it.

### Visual & layout cues (for briefing designers)

This step produces copy, not layouts, but flag these when handing a draft
to design:
- Isolate the primary CTA visually (contrast, whitespace, size): the
  isolated element is disproportionately noticed (von Restorff effect)
- Keep the same colour/shape/iconography system across every page rather
  than a fresh look each time: recognition compounds from consistently
  reused distinctive assets (Ehrenberg-Bass)
- Never sacrifice contrast or type legibility for aesthetics on any page
  with a conversion goal
- Pair any process or comparison claim with a real diagram or screenshot,
  not decorative stock (picture superiority)

Full detail: `content-references/references/behavioral-psychology.md`.

### Keyword integration (all page types, weighted by intent)

Per the placement table in `seo-aeo-optimization.md`. Blog posts apply
this heavily; landing/product/solution pages apply it lightly: keyword in
title/H1, first 100 words, and meta description is usually sufficient,
since the page's job is conversion, not ranking breadth.

### Internal linking (all page types, weighted by intent)

Per `content-references/references/internal-linking.md`: 3–10 contextual
links scaled to post length, descriptive anchor text (never "click here"
or "read more"), at least one link in the first 2–3 paragraphs, and a link
to the pillar page early in any supporting article. Blog posts apply this
heavily; landing/product/solution pages apply it lightly: one or two
links to a relevant blog post or case study is usually enough, since
these pages aren't trying to rank on link breadth.

### Step 4 output

Deliver: the full draft organized by section. The 2–3 headline/title options with
rationale, the meta content (page title, meta description) and the brief annotations on which
principle each key choice applies go in hidden comments, per the rules above.

### E-E-A-T Quality Gate

Run `content-references/references/seo-aeo-optimization.md`'s E-E-A-T
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

## Step 5: Copy Edit

**Not optional, and not done from memory.** Invoke the `copy-editing` skill (Seven Sweeps) through the Skill tool on the Step 4 draft. Two
cross-checks layer on top of that skill's own process:

- **Clarity sweep** also flags AEO violations on blog posts: an unclear
  pronoun is usually the same issue as a floating pronoun breaking entity
  consistency for citation.
- **Zero Risk sweep**: CTA strength must match the Content Bucket from
  Step 0 and the page type from Step 1, a blog post's CTA should stay
  soft even after this sweep; a landing page's shouldn't.

---

## Step 6: Humanize

**Not optional.** Invoke the `ai-content-cleaner` skill through the Skill tool. Use
**BALANCED mode** for blog posts and any page with FAQ/comparison-table
structure worth protecting; **CLEAN mode** is fine for a short landing
page with no structured elements to preserve. Before handoff, note which
structures are intentional (bolded inline headers, declarative Hook
openings, comparison tables) so nothing gets stripped by mistake.

Worth reaching for during this pass: one honest, specific limitation,
stated once, after the page has established competence (the pratfall
effect). Different from hedging, which the humanizing pass will still
flag and remove.

**Deliver only after Steps 5 and 6.** End the file with a hidden line naming the skills you ran
(`<!-- Skills run: copy-editing, ai-content-cleaner -->`). If either is missing from that line, go back and call it. There is no inline substitute.

### Final output

Deliver: final page copy, the Cleaned/Preserved breakdown (BALANCED mode)
or change list (CLEAN mode), and confirmation that intentional structure
survived.

---

## Voice and Tone (fallback: only if Step 3 found no brand kit)

If a `[brand]-brand-kit` skill was found in Step 3, its voice rules apply
instead of this section. This is the generic fallback for brands without
one yet: establish formality level (casual / professional-friendly /
formal-enterprise) and brand personality (playful or serious, bold or
understated, technical or accessible). Maintain consistency but adjust
intensity: headlines can be bolder, body copy should be clearer, CTAs
should be action-oriented throughout.

---

## Full Checklist (One-Page Summary)

### Step 0–3: Setup
- [ ] Content Bucket classified
- [ ] Page type classified
- [ ] Structural framework chosen and noted
- [ ] Brand identified and matching `[brand]-brand-kit` skill checked for and loaded (or its absence flagged)
- [ ] Requirements gathered (product-marketing-context checked first)

### Step 4: Writing
- [ ] Voice follows the loaded brand kit (or the fallback Voice and Tone section if none exists)
- [ ] Writing style rules applied (simple, specific, active, confident, show don't tell, honest)
- [ ] Correct template used for the page type (blog AEO structure vs. conversion-page structure)
- [ ] CTA copy follows the formula; reactance-reducing phrase present if commitment implied
- [ ] Behavioral-science layer applied per Content Bucket
- [ ] Visual & layout cues flagged for design
- [ ] Keyword integration weighted correctly for page type
- [ ] Internal linking applied (3–10 contextual links, descriptive anchors, pillar link where relevant)
- [ ] Information gain audit passed (blog posts)
- [ ] E-E-A-T quality gate run (full weight blog/Informational, lighter Transactional)

### Step 5: Copy Editing
- [ ] Seven Sweeps run via `copy-editing`
- [ ] CTA strength verified against Content Bucket + page type

### Step 6: Humanizing
- [ ] `ai-content-cleaner` run (BALANCED or CLEAN, matched to structure)
- [ ] Breakdown reviewed
- [ ] Intentional structure verified intact
- [ ] Voice still matches the brand kit after humanizing: a de-AI pass can flatten brand-specific phrasing if run carelessly

---

## Related Skills

- `copy-editing`: Step 5 applies this skill directly
- `ai-content-cleaner`: Step 6 applies this reference directly; also directly invocable standalone
- `seo-audit`: full technical SEO audit of an existing, already-published page
- `[brand]-brand-kit`: a brand-specific skill following this naming pattern, loaded in Step 3 when one exists for the brand/client in question
- **social-copywriting**: planned, not yet built; will cover social posts, which this skill explicitly excludes

## Reference Docs (content-references shared library)

- `content-references/references/content-intent-framework.md`
- `content-references/references/communication-frameworks.md`
- `content-references/references/seo-aeo-optimization.md`
- `content-references/references/behavioral-psychology.md`
- `content-references/references/internal-linking.md`
- `ai-content-cleaner` (humanising pass)
