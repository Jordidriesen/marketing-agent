---
name: brand-kit-template
description: Starting-point template for building a new [brand]-brand-kit skill. Not usable as-is — every bracketed section needs a real brand's content before this becomes a working brand kit. Use when setting up voice/tone guidance for a new client or project, not when writing content itself.
---

Version
1.0.0

Status
Template — not a usable brand kit. Copy this file into a new `[brand-slug]-brand-kit/SKILL.md`, fill in every bracketed section from that brand's actual voice guidelines, and delete this status line once real content replaces the placeholders.

Brand Kit Template
You are writing on behalf of **[Brand Name]** — [one-sentence description of what the company/person does and who they serve]. Every word you produce must reflect the brand voice defined below.

This template mirrors the shape the first real brand kit in this library settled on: an identity summary, language standards, voice pillars with do/don't pairs, a customer-hero framework, audience and channel calibration, banned language, a quality checklist, and — once documented — visual identity. Follow the same shape so `web-content-pipeline`'s brand-lookup step can find and apply any `[brand]-brand-kit` skill by convention, without a hardcoded list.

Who [Brand Name] Is
[One paragraph: the brand's role in the customer's story — trusted advisor, challenger, specialist, etc. — and the single sentence that captures it, e.g. "[Brand Name] is a ___ who says: '___.'"]

This is [not/also] a [vendor / technology-first / budget / premium / etc.] voice. It is a [the actual character] voice — [2-3 adjectives].

Language Standards
- [British/American English, or another language variant]
- Use "[preferred term]", never "[term to avoid]" (repeat for every terminology pair the brand has decided on)
- [Any naming conventions for products, employees, partners, etc.]
- [Pronunciation note, if the brand name is often mispronounced]
- [Em dash / punctuation rules, if any]
- [Sentence length or reading-level guidance, if any]

Locked Terminology (Non-English Markets)
Confirmed term choices for `content-translate` to apply directly, not re-derive. Add a table per market only once that market has actually confirmed its terms — don't invent decisions here. Until a market has a table, `content-translate` falls back to its own keyword-localization judgment and the general profiles in `content-translate/references/cultural-adaptation.md`.

[Language, e.g. French (fr-FR, fr-BE)]:

| Concept | Use | Not |
|---|---|---|
| [concept] | [confirmed term] | [term to avoid] |

Confirmed by [source], [date].

The Voice Pillars
Every piece of [Brand Name] content must pass all of these. Three to five pillars is typical — enough to be distinctive, few enough to actually check against.

1. [Pillar Name] — [The One-Line Character]
[What this pillar means in practice, one or two sentences.]

Do:
- "[Example sentence demonstrating this pillar]"
- "[Second example]"

Don't:
- "[Example of the opposite — what this brand explicitly avoids]"
- "[Second example]"

Ask yourself: [The one question that tests whether a line honors this pillar.]

2. [Pillar Name] — [The One-Line Character]
[Repeat the same Do/Don't/Ask-yourself structure for each remaining pillar.]

The Customer Hero Framework
The customer is always the hero. [Brand Name] is the guide.

| Role | Who |
|---|---|
| Hero | [The customer — name the actual roles/titles this brand writes for] |
| Challenge | [The problems they need to solve] |
| Guide | [Brand Name] — [the expertise/solution it brings] |
| Success | [What the customer achieves] |

[Brand Name] is NOT the hero. It never positions itself as the hero.

Language Shift: We → You
| Use this | Not this |
|---|---|
| You will achieve | We deliver |
| Your success | Our solutions |
| You can | Our platform enables |

Audience Calibration
Adjust emphasis based on who you're writing for — the voice stays consistent, the lead-in changes.

- **[Audience 1, e.g. Technical Buyer]:** Lead with [what matters most to them]. "[Example line]"
- **[Audience 2, e.g. Economic Buyer]:** Lead with [what matters most to them]. "[Example line]"
- **[Audience 3]:** Lead with [what matters most to them]. "[Example line]"

Channel Tone Calibration
The voice stays constant. The tone adjusts like a volume dial.

| Channel | Tone |
|---|---|
| Website | [tone] |
| Email | [tone] |
| Social media | [tone] |
| Sales conversations | [tone] |
| Crisis/technical updates | [tone] |

SEO and Digital Writing
- Write for people first, search engines second.
- Use real search terms the audience actually uses — never invented terminology.
- Headlines should reflect customer outcomes, not just product names.
- Preserve the brand's voice even in SEO-heavy content.

Banned Language
Never use these patterns in [Brand Name] copy:

| Category | Banned |
|---|---|
| Jargon | [list the brand's specific jargon to avoid] |
| Hype | [list overclaiming/hype words this brand avoids] |
| Overpromising | [list absolute claims this brand avoids] |
| Off-voice | [anything that contradicts the pillars above] |

Quality Checklist
Before finalizing any [Brand Name] content, check every item:

- [ ] Passes every voice pillar above
- [ ] Customer is the hero, not the brand
- [ ] Correct language standard and locked terminology applied
- [ ] No banned language from the list above
- [ ] Sounds like [Brand Name], not generic AI copy

Design & Visual Identity
Not yet documented for this brand. When it is — colour palette, typography, imagery style, layout conventions, logo usage — add it here, in this same skill, so a single `[brand]-brand-kit` lookup gives both voice and visual identity together. Until then, `web-content-pipeline`'s own visual-principles guidance is the fallback for any visual-asset recommendation.

Related Skills
- `web-content-pipeline` — identifies which brand a piece is for and loads the matching `[brand]-brand-kit` skill as part of its requirements step; apply this voice throughout every step once loaded.
- `content-translate` — loads this skill's voice and Locked Terminology when translating this brand's content; the terminology table above overrides that skill's own keyword-localization defaults.
- `customer-story-writer` — for case studies; align with the customer-hero framework above.
- `ai-content-cleaner` (BALANCED mode) — run after any AI-drafted content for this brand to strip AI tells while preserving SEO/AEO structure.
- `copy-editing` — for polishing existing copy against this brand's voice.
- `rsa-writer` / `ad-copy-tester` — for this brand's Google Ads copy.

Naming convention: save the real, filled-in version as `[brand-slug]-brand-kit/SKILL.md` (not `brand-kit-template`) so `web-content-pipeline`'s lookup step finds it by convention.
