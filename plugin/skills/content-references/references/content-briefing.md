# Content Briefing: Intent, Page Type and Structural Framework

Decide three things before writing, in this order: what the reader wants (intent), what kind of page this is (page type), and how the piece is built to deliver it (framework). Intent and framework are separate decisions that correlate, so they share one decision path. State the result in the content brief so every downstream skill builds on the same choice.

## 1. Intent (Broder, 2002: the standard SEO taxonomy)

### Informational
**The searcher wants** to understand something and is not ready to act. **Signals:** how, what, why, guide, tips, meaning, "vs" without buy intent; question-form queries; OpenSEO `intent = informational`.

**Content:** blog posts, guides, definitions, FAQs, explainers, pillar pages.
- Direct-answer hook in the first 50 to 100 words (AEO), TOC, FAQ, comparison tables where relevant.
- CTA per the rule below: related content, a newsletter, a low-commitment next step, never "Buy now" or "Request a demo" as the primary ask.
- Proof is citations, data and named expert sources (Cialdini's authority), not customer testimonials.
- **Levers:** curse of knowledge (strip jargon), cognitive fluency (the highest-leverage lever here), concreteness and picture superiority, sourced precision numbers, peak-end (finish on one clear micro-step).

### Navigational
**The searcher wants** a specific, already-decided destination: a brand, a login, a named product page. **Signals:** brand plus login, pricing, contact, dashboard or support; `intent = navigational`.

**Content:** usually not a page you write persuasive copy for. It must exist, load fast and be unmistakably the right destination. Persuasion-heavy treatment feels dishonest or slows a visitor who has already decided.
- Title tag matching the brand query exactly, distinctive brand cues visible at once.
- **Levers:** distinctive brand assets (Ehrenberg-Bass) and processing fluency. Skip the emotional, proof-heavy Seven Sweeps treatment.

### Transactional (commercial investigation is a subtype)
**The searcher wants** to act now or soon: buy, sign up, request a quote, or make the last comparison. **Signals:** buy, price, quote, near me, best [category], [brand] vs [competitor]; `intent = transactional`. Treat OpenSEO's `commercial` label as Transactional (subtype: commercial investigation) for content strategy, while keeping it as its own label in keyword tables.

**Content:** landing pages, pricing, product and solution pages, comparison pages, local service pages.
- Single message, single CTA. Objection handling and proof stacked close to the CTA. Pricing or value anchor up front.
- **Levers:** anchoring and price relativity, extremeness aversion (tiering), real scarcity and social proof (per the canonical honesty rule in `content-references/SKILL.md`), loss-averse framing, reactance reduction ("no obligation", "cancel anytime"), one honest caveat late in the page (pratfall effect), and ending on the strongest benefit plus the easiest action. Full detail in `behavioral-psychology.md`.

### Mixed intent
Real queries blend: "best access control system" is informational leaning transactional. Default to the more commercial class when the page's goal is conversion, and to informational when the goal is topical authority or AEO citation. State the choice in the brief.

**CTA strength follows intent** (stated here once): Informational soft, Navigational none, Transactional one clear primary action.

## 2. Page type

Page type picks the template, not the framework: blog post, pillar or hub, comparison, glossary, landing, product, solution, feature, homepage, pricing, about. The pipeline's page-type guide lists core sections, proof and FAQ counts for each.

## 3. Structural framework

Not "always Minto". Minto is the strongest framework for logical persuasion (answer first, then MECE support), and its blind spot is the same thing that makes it efficient: it builds no narrative tension. People rarely decide on logic alone, so use the frameworks below when the objective calls for tension, momentum or urgency.

| Goal | Framework | Structure |
|---|---|---|
| Defending a strategy | **Minto Pyramid** | Answer, then grouped MECE logic, then data. Right for executive summaries, strategic reports, recommendations, and any audience already asking "how do we solve this?" |
| Inspiring an audience | **Duarte Sparkline** | Oscillate between "what is" and "what could be", widening the gap before closing it on a "new bliss". For keynotes, launches, vision decks |
| Converting prospects | **StoryBrand** | A character (the customer) has a problem, meets a guide (the brand) with a plan, and is called to action. The brand is the guide, never the hero. For landing pages, nurture, web copy |
| Driving urgency | **PAS** | Problem, agitate until it feels urgent, then solution. Uses loss aversion. For ads, lead-gen emails, short PPC landing pages |
| Internal efficiency | **BLUF** | Bottom line in the first sentence, no supporting pyramid. For status updates and summaries |

**Rule of thumb:** Minto or BLUF when the audience has accepted the problem and wants the answer. Sparkline, StoryBrand or PAS when they do not yet feel a problem worth solving.

**Intent to framework:** Informational usually Minto (the reader wants the answer) or a light Sparkline open (the topic first needs a reason to matter). Navigational uses neither. Transactional is almost always StoryBrand or PAS.

**Practical mapping:** executive content, Minto; launches and keynotes, Sparkline; landing and solution pages, StoryBrand; ad copy and lead-gen sequences, PAS; internal updates, BLUF. Where none fits, do not force one: use the structure the content needs and name it.

### Combining frameworks
They are not exclusive within one document. A customer story can open on a brief Sparkline gap (the before state) and resolve into StoryBrand's plan and success, which is what `customer-story-writer`'s arc does. A long report can use Minto for the summary and BLUF for the daily-update sections. Name the framework per section when mixing.

## Source for intent labels
OpenSEO's `get_keyword_metrics` and `research_keywords` return `intent` as `informational`, `navigational`, `transactional`, `commercial` or `unknown`.
