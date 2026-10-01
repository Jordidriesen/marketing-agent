# Content Intent Framework: Informational / Navigational / Transactional

Classify intent **before** writing, not after. The intent type should determine
structure, proof type, CTA strength, and which behavioral-science levers apply
— not get bolted on at the end as a metadata field nobody uses.

Part of the `content-references` shared library — see
`content-references/SKILL.md` for how generation skills should use this
alongside the other four modules.

For the full effect-by-effect playbook this framework points into, see
`content-references/references/behavioral-psychology.md`.

---

## The three intent types (Broder, 2002 — the standard SEO taxonomy)

### 1. Informational
**Searcher wants:** to understand or learn something. Not ready to act.

**Signals:** how/what/why/guide/tips/meaning/vs (comparison without buy intent),
question-form queries, OpenSEO's `intent = informational` field on
`get_keyword_metrics`/`research_keywords` results.

**Content implication:** blog posts, guides, definitions, FAQ, explainers.
Hand off to `web-content-pipeline`.

**Structural defaults:**
- Direct-answer hook in the first 50–100 words (AEO)
- TOC, FAQ, comparison tables where relevant
- CTA is soft: related content, newsletter, low-commitment next step —
  never a hard "Buy now" or "Request a demo" as the primary ask
- Proof type: citations, data, named expert sources (Cialdini's *authority*
  principle) rather than customer testimonials

**Primary behavioral levers** (see playbook for detail):
curse of knowledge (strip jargon), cognitive fluency (this is the single
highest-leverage lever here — comprehension *is* the goal), concreteness /
picture superiority (diagrams beat prose for process explanation), precision
numbers (sourced stats over vague claims — also raises AEO citation odds),
peak-end rule (end with a clear, single next micro-step).

---

### 2. Navigational
**Searcher wants:** a specific, already-decided destination — a brand, a
login page, a specific product page.

**Signals:** brand name + login/pricing/contact/dashboard/support,
`search_intent = navigational`.

**Content implication:** this is not usually a page you write persuasive
copy for — it's a page that must exist, load fast, and be unmistakably the
right destination. Relevant mainly for site structure, title tags, and
branded page hygiene (branded pages for your clients, Google Business Profile).
Persuasion-heavy treatment here can feel dishonest or slow the visitor down
— they already decided.

**Structural defaults:**
- Minimal friction, fast load, title tag matching the brand query exactly
  (fluency = confirmation the visitor landed in the right place)
- Distinctive brand cues (logo, colour, layout) visible immediately —
  this is the visitor's confirmation signal, not a sales pitch

**Primary behavioral levers:**
distinctive brand assets (Ehrenberg-Bass — consistent, unmistakable visual
identity), processing fluency (arriving instantly at what was expected).
Skip the Seven Sweeps' emotional/proof-heavy treatment here; it's the wrong
tool for a visitor who already chose you.

---

### 3. Transactional (including Commercial Investigation as a subtype)
**Searcher wants:** to act now or soon — buy, sign up, request a quote,
or do the final comparison before buying.

**Signals:** buy/price/quote/near me/best [category]/[brand] vs [competitor],
`intent = transactional`. OpenSEO's `commercial` label (comparison
/ research immediately pre-purchase) should be treated as a Transactional
subtype for content-strategy purposes, even though it's tracked separately
in keyword tables for prioritization.

**Content implication:** landing pages, pricing pages, product pages,
comparison pages, local service pages. This includes a client's Google
Ads landing pages and product/solution pages. Hand off to `web-content-pipeline`.

**Structural defaults:**
- Single message, single CTA
- Objection handling and proof stacked close to the CTA, not buried earlier
- Pricing/value anchor front-loaded

**Primary behavioral levers** (this is where most of the persuasion playbook
concentrates — see the full table):
anchoring & price relativity, charm pricing & extremeness aversion (tiering),
scarcity & social proof (real only — never fabricated, per the web-content-pipeline
skill's honesty rule), framing (loss-averse phrasing, "sold out" not
"unavailable"), reactance reduction ("no obligation," "cancel anytime"),
pratfall effect (one honest caveat late in the page, only once competence is
established), peak-end rule (end on the strongest benefit + easiest action,
not a feature recap).

---

## Quick decision table

| Signal in keyword/brief | Intent | Hand off to |
|---|---|---|
| how / what / why / guide / tips / vs (education) | Informational | `web-content-pipeline` |
| [brand] + login / pricing / contact / dashboard | Navigational | site structure / IA — not a persuasive-copy skill |
| buy / price / quote / near me / best [category] / [brand] vs [competitor] | Transactional | `web-content-pipeline`, paid-ads landing pages |

## Mixed / blended intent

Real queries often blend — "best access control system" is informational-
leaning-transactional (commercial investigation). When blended:
- Default to the **more commercial classification** if the page's business
  goal is conversion.
- Default to **informational** if the business goal is topical authority
  or AEO citation.
- State the choice explicitly in the content brief so downstream skills
  (and Claude sessions) don't disagree on structure mid-pipeline.

## Source

OpenSEO's `get_keyword_metrics` and `research_keywords` return an `intent`
field with one of: `informational`, `navigational`, `transactional`,
`commercial`, `unknown` — same four working labels DataForSEO's older
dedicated `search_intent` tool used, now folded into the keyword-metrics
response instead of a separate call. Map `commercial` to Transactional
(subtype: commercial investigation) for content-strategy decisions, while
keeping it as its own label in keyword tables.
