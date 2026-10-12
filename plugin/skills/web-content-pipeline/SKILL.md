---
name: web-content-pipeline
metadata:
  version: 1.6.1
  history: "v1.6.1: no-em-dash style rule. v1.6.0: orchestration only. Page templates moved to content-references (page-templates-article, page-templates-conversion), steps 0 to 2 merged into one router table, and the formerly-two-skills note (blog pipeline plus copywriting, merged in 1.0) reduced to this line. Earlier history is in CHANGELOG.md."
description: "Always use for any website copy or copywriting, however short or fully specified: landing pages, homepages, product, solution, feature, pricing and about pages, page design and page copy work, a hero section, benefit blocks, CTAs, SEO or AEO blog posts. Not social posts or ebooks."
---

# Web Content Pipeline

Takes any web page or blog post from brief to publish-ready: classify intent and page type, pick a structural framework, write to the right template, edit, humanize. What differs by page type is the template in Step 4, not the process around it. Web content only: not social posts, not ebooks or whitepapers.

**Required skill calls.** Two other skills are part of this pipeline and must be called through the Skill tool, never imitated with an inline edit: `copy-editing` after the Step 4 draft, and `ai-content-cleaner` after that. If you have a draft and have not called both, call them now, before you reply. A reply that says the edit pass was done inline, or that skips either skill, is not finished.

**Required file read.** Step 4 needs one template file, read with the Read tool before you draft (named in Step 4). Reference files are not loaded for you: if this skill tells you to read one, read it.

---

## Claim test: write what is plausible, never what is invented

This is the operational form of the canonical honesty rule in `content-references/SKILL.md`.

Facts about the product, the offer or the company come from the brief, then the brand kit or the product file (`products/<slug>.md`). Before you write a statement about what the product does or what a visitor gets, ask: given those sources, is this at least about 90% likely to be true? If yes, write it plainly, with no hedge, and let the framework do its work (the problem and agitation steps describe the audience's situation, and outcomes that follow from a stated feature are fine). A plausible claim the sources do not confirm (EU hosting, a walkthrough length, a deployment option) is still written, with a hidden note next to it: `<!-- confirm: EU hosting, check region before publish -->`. If you would be guessing below that level (a specific mechanism, integration, setting or step), use the general version the sources support.

These always need a source, however plausible they sound: numbers and percentages, customer names and logos, quotes, awards and ratings, certifications and compliance claims, and prices. Missing proof is a Lorem Ipsum placeholder in the form the proof will take, with a hidden `PROOF NEEDED` comment (see Step 4). Leave a fact out, with a hidden note, rather than approximate it. A call to action may promise what the offering is meant to fix, as the brief states it.

Do not build selling points on a single fact. "A Belgian company" does not mean "a team in your time zone and language", and "cloud" does not mean a named hosting region. If a benefit rests on something the sources only hint at, leave it out or flag it with a hidden `confirm` note.

---

## Steps 0 to 2: classify, then choose the framework

**Step 0, intent.** Informational (how, what, why, guide: soft CTA, authority proof), Transactional including commercial investigation (buy, price, quote, best, vs: firm CTA, heavy proof), or Navigational (brand plus a page name: clarity and speed, not persuasion). A starting signal, not a rule; state your reasoning if the page type below does not match. CTA strength follows intent (rule in `content-references/references/content-briefing.md`).

**Step 1, page type.** Pick the row below. If it is unclear from the brief, ask: the template in Step 4 depends on it.

**Step 2, framework.** The skill chooses the framework that fits the page type, the traffic source and the goal. StoryBrand is the common default for conversion pages, not a requirement: use PAS, Minto, Sparkline or another when it fits better, and say which in one line with the reason. If the brief names a framework, use it unless it clearly does not fit, and say so. Note the choice: it shapes Step 4.

Defaults (common practice, not rules; the brief and the brand kit come first):

| Page type | Intent | Default framework | Core sections | Proof | FAQ | Template |
|---|---|---|---|---|---|---|
| Landing page (paid) | Transactional | StoryBrand (longer) or PAS (short, ad-driven) | Hero, problem, plan, proof, objections, closing CTA; one goal, no site navigation | Close to the CTAs | 3 to 6 objections from this traffic source | conversion |
| Product page | Transactional | StoryBrand | Hero, features as use cases, how it works, proof, pricing path | Named, specific; near CTAs | Optional, 3 to 6, on fit and set-up | conversion |
| Solution page | Transactional | StoryBrand (fullest arc) | Hero, the situation, use cases by role or industry, how it works, proof, related products | Close to CTAs; case studies linked | 4 to 8, on roles, integration, replacing what exists | conversion |
| Feature page | Transactional | PAS (ad-driven) or StoryBrand (in-app explainer) | One feature, one use case, visual, path to try | Light | Optional, 3 to 5 | conversion |
| Homepage | Navigational-leaning | StoryBrand-lite | Value proposition, routes by audience, proof, one clear next step | Logos, one or two headline results | Usually none | conversion |
| Pricing page | Transactional | Minto-style comparison plus PAS anchoring | Plans tied to buyer segments, a recommended plan, comparison grouped by outcome, billing toggle if relevant | Next to the decision point | 4 to 8 last-minute hesitations | conversion |
| About page | Informational/brand | Sparkline (what was, what is now) | Why the company exists, what it believes, who is behind it, a CTA | Light | None | conversion |
| Blog post | Informational | Minto (answer first) or Sparkline (thought leadership) | Answer-first hook, one topic per section, takeaways | Sources and examples | 3 to 5 | article |
| Pillar page / hub | Informational | Minto | Answer to the broad question, a map of subtopics, a link to every spoke | Sources | 3 to 6; every spoke links back | article |
| Comparison (A vs B) | Informational leaning Transactional | Minto with a table | Decision rule first, side-by-side table, when to choose each, what can stay | Sources, no vendor attacks | 3 to 5 | article |
| Glossary / reference | Informational | None (definition format) | Stand-alone definitions, stable anchors, grouped by theme | None | None | article |

For the reasoning behind intent and framework choices, and edge cases, read `../content-references/references/content-briefing.md` (on demand; not needed when the table above settles it).

---

## Step 3: Gather Requirements

**Check for product marketing context first:** if `.agents/product-marketing-context.md` exists (or `.claude/product-marketing-context.md` in older setups), read it before asking questions. Use that context and only ask for what isn't already covered.

**Identify the brand and load its brand kit.** Each brand or client has its own voice, so there is no single default tone. Before drafting anything:

1. Determine which brand or client this piece is for, from the brief, from context already in the conversation, or by asking if genuinely unclear.
2. Check for a matching `[brand]-brand-kit` skill for that brand (found by the naming pattern, not a hardcoded list).
3. **If found:** load it and apply its voice throughout Steps 4 to 6. Its rules override the Voice and Tone fallback below.
4. **If not found:** flag that no brand kit exists, fall back to the Voice and Tone section, and note that a `[brand]-brand-kit` skill is worth building if this becomes recurring work.

| Field | Input |
|---|---|
| Brand/client | Which brand: determines which brand kit applies |
| Page type (Step 1) | Outcome of Step 1 |
| Content Bucket (Step 0) | Outcome of Step 0 |
| Structural framework (Step 2) | Outcome of Step 2 |
| Primary keyword + secondary keywords | Still relevant for landing, product and solution pages, not just blogs |
| Target audience | Who is the ideal visitor or reader? |
| Primary action | The ONE thing you want them to do |
| Product/offer | What's being sold or explained; what makes it different; proof points |
| Traffic source | Ads, organic, email: shapes how much context the visitor already has |
| Tone (only if no brand kit exists) | professional / casual / technical |
| Competitor URLs or top-ranking posts | If known |

If any field is missing, ask before writing. When the brand, the primary action, the audience or the product facts the page needs are missing from the brief, the brand kit and the product files, stop and reply with 2 to 5 specific questions and nothing else: no draft, no copy with placeholders. Tone, length and language may default; say which default you used.

---

## Step 4: Write to the page-type template

**Read the template file for your page type now, before drafting** (the Template column above):
- `article`: `../content-references/references/page-templates-article.md` (blog, pillar, comparison, glossary)
- `conversion`: `../content-references/references/page-templates-conversion.md` (landing, product, solution, feature, homepage, pricing, about)

Load only the one you need. Load `../content-references/references/seo-aeo-core.md` as well when an article is meant to rank or be cited, and `../content-references/references/behavioral-psychology.md` when a conversion page needs the full persuasion detail. Paths are relative to this skill's folder.

### Writing style rules (every page type)

1. **Simple over complex**: "use" not "utilize," "help" not "facilitate"
2. **Specific over vague**: avoid "streamline," "optimize," "innovative" as unsupported claims
3. **Active over passive**: "we generate reports," not "reports are generated"
4. **Confident over qualified**: cut "almost," "very," "really"
5. **Show over tell**: describe the outcome, not adjectives about it
6. **Honest over sensational**: never invent proof
7. **No em dashes**: use a colon, comma or full stop

Quick check: jargon an outsider could not follow? Sentences doing too much? Passive voice? Exclamation points (cut them)? Buzzwords without substance?

### Hidden notes, placeholders and headings (every page type)

- **Editor notes are comments, not copy.** The file has two audiences: people reading the finished page and people editing the source. Everything meant for editors and for AI is an HTML comment in the same file: the implementation brief, a component tag above each section, `confirm` and `verify` notes, `PROOF NEEDED` notes, headline alternatives, the reasoning behind choices, and the closing `<!-- Skills run: ... -->` line. Nothing editor-facing may be visible when the page is rendered.
- **Questions and doubts go in the file, as comments.** Anything you would otherwise ask the editor becomes a comment next to the line: `<!-- QUESTION: ... -->`. A statement you cannot call about 90% likely and cannot check against the sources is written in its most cautious supported form, or left out, and gets `<!-- UNSURE: ... needs judging by the person operating the chat -->`. Collect every `QUESTION`, `UNSURE`, `PROOF NEEDED` and `confirm` note in one `<!-- OPEN ITEMS: ... -->` block at the end of the file, so the editor and the marketing director find them in one place. The page itself stays clean.
- **The chat reply is the file plus at most two sentences.** Do not repeat the open items, the edit-pass summary or the framework reasoning outside the file. Navigation and button rows show the labels only, never instructions in parentheses outside a comment.
- **Component tags.** When the site has a component library, put the exact component name in a comment above each section (`<!-- COMPONENT: 3-up problem cards -->`). Reuse the existing components and introduce none. A form modal is not a page component. Never use numbers or labels like "Section 1". With no component library, skip the tags.
- **Missing proof becomes Lorem Ipsum.** When a section needs proof (a quote, a logo strip, a metric, a case card) and the brief, the brand kit and the product files do not supply it, fill that slot with Lorem Ipsum in the exact form the real proof will take, so the layout and the need are visible, and add `<!-- PROOF NEEDED: customer quote, role, company -->`. Never invent a customer, a figure or a logo.
- **Neutral headings until proof exists.** A heading must not imply proof that is not there. Use "Where it runs", "References" or "Proof", not "Trusted by", "Customers like you" or "Used by teams like yours", until real proof fills the section.

### Step 4 output

Deliver the full draft organized by section. The 2 to 3 headline or title options with rationale, the meta content (page title, meta description) and the brief annotations on which principle each key choice applies go in hidden comments.

---

## Step 5: Copy Edit

**Not optional, and not done from memory.** Invoke the `copy-editing` skill (Seven Sweeps) through the Skill tool on the Step 4 draft. Two cross-checks layer on top of that skill's own process:

- **Clarity sweep** also flags AEO violations on blog posts: an unclear pronoun is usually the same issue as a floating pronoun breaking entity consistency for citation.
- **Zero Risk sweep**: CTA strength must match the intent and page type (a blog post's CTA stays soft even after this sweep; a landing page's does not).

## Step 6: Humanize

**Not optional.** Invoke the `ai-content-cleaner` skill through the Skill tool. Use **BALANCED mode** for blog posts and any page with FAQ or comparison-table structure worth protecting; **CLEAN mode** is fine for a short landing page with no structured elements to preserve. Before handoff, note which structures are intentional (bolded inline headers, declarative hook openings, comparison tables) so nothing gets stripped by mistake.

Worth reaching for during this pass: one honest, specific limitation, stated once, after the page has established competence (the pratfall effect). Different from hedging, which the humanizing pass will still flag and remove.

**Deliver only after Steps 5 and 6.** End the file with a hidden line naming the skills you ran (`<!-- Skills run: copy-editing, ai-content-cleaner -->`). If either is missing from that line, go back and call it. There is no inline substitute. Deliver the final page copy, the Cleaned/Preserved breakdown (BALANCED) or change list (CLEAN), and confirmation that intentional structure survived.

---

## Voice and Tone (fallback: only if Step 3 found no brand kit)

Establish formality (casual, professional-friendly, formal-enterprise) and personality (playful or serious, bold or understated, technical or accessible). Keep it consistent but adjust intensity: headlines bolder, body copy clearer, CTAs action-oriented throughout.

## Full Checklist

- [ ] Step 0 to 3: intent, page type and framework chosen and noted; brand identified and its kit loaded (or its absence flagged); requirements gathered
- [ ] Step 4: template file read; voice follows the brand kit or the fallback; style rules applied; CTA follows the formula with a reactance-reducing phrase if commitment is implied; keyword and internal linking weighted for the page type; E-E-A-T gate run for articles; visual and layout cues flagged
- [ ] Hidden notes: component tags, `PROOF NEEDED`, `confirm`, `QUESTION`, `UNSURE`, one `OPEN ITEMS` block, nothing editor-facing visible
- [ ] Step 5: Seven Sweeps run via `copy-editing`; CTA strength verified
- [ ] Step 6: `ai-content-cleaner` run; intentional structure intact; voice still matches the brand kit

## Related skills and references

`copy-editing` (Step 5), `ai-content-cleaner` (Step 6), `seo-audit` (an already-published page), `[brand]-brand-kit` (Step 3). The shared references and which skill loads what are mapped in `content-references/SKILL.md`.
