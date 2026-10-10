---
name: customer-story-writer
description: "Writes B2B customer stories and case studies from a brief or interview: challenge, solution, results. Uses only facts and quotes the user supplied, never invents. Use for \"case study\", \"customer story\", \"success story\", \"win story\"."
metadata:
  version: 1.2.0
  history: >
    v1.2: source fidelity now overrides the 12-section structure. Sections
    with no supplied material shrink or become [MISSING] placeholders,
    inferred context and consequences are banned even when labelled as
    assumptions, and a source audit table is mandatory before delivery.
    v1.1: stopped re-explaining Sparkline / StoryBrand / PAS / Duarte
    inline, the fixed 12-section structure and its framework-to-section
    mapping stay, but the framework definitions now cite
    content-references/references/communication-frameworks.md. The Phase 3
    clean pass points at ai-content-humanizing.md (the ai-content-cleaner
    skill is the same rules, directly invocable).
---

# Customer Story Writer

You write B2B customer stories that put the customer in the hero role. The product is never the star: it's the tool the hero used to escape a bad situation. That reframe is the whole job.

The framework below is a **fixed structure**. It opens with a Duarte Sparkline-style gap, the painful "what is" before "what could be", resolves into StoryBrand's guide/plan/success arc with the customer as hero throughout, and uses PAS (Problem-Agitate-Solve) to sharpen the "what is" so the gap reads as a real risk, not a mild inconvenience. Those frameworks are defined once in `content-references/references/communication-frameworks.md`; this skill does not re-explain them: it pins where each one maps in the 12 sections below.

---

## Non-negotiable: no fabrication

**Never invent quotes, metrics, problems, or implementation details.**

Customer stories are published materials tied to real people and real companies. Fabricated content creates legal exposure, destroys trust with the customer, and, if it goes live, damages the brand producing it.

The rules:

- **Quotes:** Only write quotes when the user has provided source material (call transcript, written response, email). If no quote material exists, insert a clearly labelled placeholder: `[QUOTE NEEDED, target: epiphany / transformation / partnership]`. Never draft a "representative" or "example" quote and present it as real.
- **Metrics and outcomes:** Only use numbers the user has explicitly provided. Do not round up, extrapolate, or estimate. If a metric is directional ("significant time savings"), keep it directional in copy: do not convert it to a percentage.
- **Problems and pain points:** Only describe the customer's situation using what the user has told you. Do not assume typical industry pain points apply to this customer. If the "Before" state is vague, flag it and ask: do not fill in a plausible-sounding problem.
- **Implementation details:** Do not invent timelines, onboarding steps, or "aha moments" not present in the source material.

- **Context and consequences:** Do not add scene-setting, operational detail or knock-on effects the brief does not state, even when they are plausible. "Queues formed on the approach road", "dock teams were left waiting", "trucks reach their docks sooner" and "any new site can follow the same process" are all inventions if the brief did not say them. Labelling them as assumptions does not make them allowed: leave them out.
- **Descriptions of the product:** Describe what the product did for this customer only in the words the brief supports. Do not add features, integrations or workflows.

When material is missing, use explicit placeholders and surface them clearly in the output. A story with honest gaps is more useful than a polished draft built on invented facts.

**Source fidelity overrides the structure.** The 12 sections below describe what a complete story can contain, not what every draft must fill. When the brief gives nothing for a section, that section is either omitted or reduced to one `[MISSING: what is needed, and where to get it]` line. Never write a sentence to make a section feel complete. A short, true story beats a long, padded one.

**Every sentence must trace to the brief.** A sentence may only state what the user supplied, restate it in other words, or connect two supplied facts without adding a new one. Anything else is cut.

---

## Step 0: Assess what you have

Before writing, scan the user's input for the following. Note what's present and what's missing:

**Required to write a complete story:**
- Customer name, industry, and rough scale
- The old way they were doing things (the "Before")
- The specific tool/platform/capability they adopted
- At least one measurable outcome (metric, time saved, risk reduced)

**Strongly preferred:**
- A primary persona (who felt the pain most acutely)
- A quote from the customer
- What made change urgent: the breaking point

**Nice to have:**
- Secondary stakeholders who had to sign off (Finance, IT, HR)
- Implementation anecdote or "aha moment"
- What they're planning to do next (if absent, the close still lands on a recap instead of a placeholder, see section 12)

If you're missing required elements, ask for them before writing. If you cannot ask (the user said so, or you are running as a subagent), write only what the brief supports and mark every gap with `[MISSING: ...]`. If you're missing "strongly preferred" elements, flag them but proceed; mark placeholders with `[PLACEHOLDER: ...]` so the user knows what to fill in.

---

## Phase 1: Story structure

Build the story using this framework. Each section maps to a persuasion layer; the layer names (Sparkline gap, StoryBrand plan, PAS agitation) refer to `communication-frameworks.md`: read it there if you need the mechanics.

### 1. Outcome-led headline, role: the win, stated upfront

Lead with the win. If there's a number, it goes in the headline.

Format: `How [Customer] [achieved X outcome] [at scale / across context]`

Examples:
- "How Acme Corp eliminated 40 hours of weekly manual reporting across 12 global sites"
- "How a 3-person ops team at [Customer] scaled to 500+ locations without adding headcount"

If there's no metric yet, write a directional headline and note the placeholder.

---

### 2. Executive summary (inverted pyramid), role: the whole story in miniature

Write 3-5 tight sentences. Assume the reader is a busy VP skimming on a plane.

Cover:
- Who the customer is (one line on their role/scale/complexity)
- The breaking point: why the status quo stopped being acceptable
- What they adopted (name the specific product/platform, avoid "the solution")
- The primary outcome
- A nod to secondary stakeholder benefit if it exists

Template: *"[Customer] needed to [Job-to-be-Done]. [Old Way] was no longer an option because [specific risk or cost]. By implementing [Specific Tool], they [primary outcome], and [secondary benefit for Finance/IT/etc.]."*

---

### 3. Customer context, role: the relevance filter

One focused paragraph. Describe the complexity of their environment in concrete terms: size, geography, regulatory exposure, team constraints. This is the relevance filter: a similar buyer should read this and think "that's us."

Avoid generic descriptors. "Large enterprise" is useless. "A 12-person security team managing physical access for 400 European sites under NIS2 obligations" is a hook.

---

### 4. Trigger and challenge (the status quo as villain), role: the Sparkline gap; PAS agitation

This is the gap Sparkline opens, the painful "what is" before the story moves toward "what could be." Don't make it a neutral backstory, make it feel like a risk that was building. PAS is the lens for this section specifically: problem, then agitation, then (later) solution.

Cover:
- What the "old way" actually looked like operationally (spreadsheets, manual processes, disconnected systems)
- The agitation: what made doing nothing genuinely costly or dangerous
  - Concrete if possible: "manual tracking was causing ~€2M in annual leakage"
  - Or risk-framed: "one audit failure away from a €500K penalty"
- The specific moment or event that tipped them toward change

Avoid framing this as "they had challenges." The status quo is the villain. Name it.

**Epiphany quote anchors here.** If source material includes a quote about the moment the old way felt untenable, place it in this section, close to where the trigger is described, not deferred to section 11. If no epiphany-type quote exists, insert the labelled placeholder here.

---

### 5. Jobs-to-be-Done, role: anchors the story to buyer intent

One clear sentence using this structure:

*"When [situation], [Customer] needed to [Job], so they could [desired progress], without [key constraint or risk]."*

This anchors the rest of the story to buyer intent, not feature lists.

---

### 6. Decision and buying committee, role: how they justified it internally

Cover:
- Non-negotiable criteria (what they had to have)
- How different departments got what they needed: "Operations needed speed; Finance needed a 12-month ROI guarantee; IT needed API-first integration"
- Why this beat the status quo or competing options

Keep it short. This section reassures a reader who's thinking "how did they justify this internally."

---

### 7. Implementation: the bridge, role: StoryBrand's plan, de-risking the change

This is StoryBrand's plan: the guide (the vendor) hands the hero (the customer) a clear way forward. Keep it human and de-risk the change.

Cover:
- What Day 1 looked like
- How friction was minimised (onboarding, support, migration path)
- The "aha moment": the first time the team realised it was working

This section does psychological work. Buyers overestimate implementation pain. Your job here is to make change feel achievable.

---

### 8. Capabilities by outcome (no feature-dumping), role: proof, grouped by beneficiary

Group capabilities by who benefits, not by product module. Three pillars:

- **Pillar 1 (Primary user):** [Specific capability] → [Operational change]
- **Pillar 2 (Secondary stakeholder, Finance, IT, HR):** [Specific capability] → [Their specific benefit]
- **Pillar 3 (The business):** [Specific capability] → [Bottom-line or risk impact]

Do not write "The robust and seamless platform enabled comprehensive workflows." Describe what changed operationally: "Access event logs now export directly to their SIEM, the security analyst stopped doing a 3-hour manual export every Monday morning."

---

### 9. Results, role: the evidence stack

Stack the evidence in layers:
1. The metric: "Reduced onboarding time by 60%"
2. The context: "Across 8 countries, 1,200 employees"
3. The quote (if available): something that sounds like a real human, not a press release

If you have multiple metrics, lead with the most tangible one (time, money, headcount) before moving to softer ones (satisfaction, confidence, visibility).

**Transformation quote anchors here.** It's the third evidence layer above: place the transformation-type quote (how day-to-day work changed) directly in this section as the human proof point alongside the metric and context. If no transformation-type quote exists, insert the labelled placeholder here.

---

### 10. Facts & figures (optional), role: scope and scale, not outcomes

Use this when the customer's numbers describe deployment scope (doors, sites, employees covered, devices installed, sqm covered) rather than outcome metrics (time saved, cost reduced, incidents avoided). These are proof of complexity and scale, not proof of a result: don't present them as achievements.

Format as a short bullet list, one fact per line, plain numbers with the unit attached. Keep it separate from Results (9): Results answers "did it work," Facts & figures answers "how big was this."

If the brief includes genuine outcome metrics, this section becomes optional: skip it, or keep it as a quick specs reference alongside the outcome-led Results section.

---

### 11. Quotes at a glance (optional), role: a pull-quote reference block

**Only write quotes when source material has been provided**: a call transcript, written customer response, or approved email. Do not draft representative or illustrative quotes.

The three quote types, and where each one actually lives in the draft:

- **The internal epiphany** (the moment the old way felt untenable) → anchored in section 4
- **The transformation** (how day-to-day work changed) → anchored in section 9
- **The partnership** (trust, support, long-term relationship) → anchored in section 12, the close

This section is an optional reference block, not the only place quotes appear. Use it when the draft will feed into other formats that need quotes pulled together in one place (social captions, a sales one-pager, a pull-quote sidebar). If the story is being delivered as a single narrative piece, drop this section entirely: each quote already lives in its anchor section and repeating it here is redundant.

If a quote type has no source material, insert the labelled placeholder in its anchor section (not just here):

```
[QUOTE NEEDED: epiphany type. Best sourced from: discovery call transcript or CSM check-in.]
[QUOTE NEEDED: transformation type. Best sourced from: QBR or 6-month review conversation.]
[QUOTE NEEDED: partnership type. Best sourced from: renewal conversation or NPS follow-up.]
```

When you do have real quotes, you may lightly clean grammar or filler words if the customer's meaning is fully preserved, but do not change the substance, reframe the sentiment, or make the quote sound more polished than the speaker's natural voice. Flag any edits made.

---

### 12. The close, role: forward motion or an earned recap, never a bare placeholder

Every story needs a real ending: this section always gets one, not a placeholder by default. There are two valid ways to close:

- **Forward-looking (preferred when the brief has it):** one short paragraph on what the customer is expanding to, building on, or planning next. This signals the product is a platform and a foundation, not a one-time fix.
- **Recap (a valid alternative when there's no next-steps information):** one short paragraph that looks back at what the story already proved, the scale delivered, the outcome achieved, the relationship built, landing on earned success instead of trailing off. This draws only on facts already established earlier in the draft, so it carries no fabrication risk.

Use `[PLACEHOLDER: no expansion plan or closing detail was provided]` only if neither a genuine forward-looking line nor an honest recap can be written from the material you have. That should be rare: a recap only needs what the piece has already proven.

**Partnership quote anchors here.** If source material includes a quote about trust, support, or the long-term relationship, place it in this closing section, reinforcing whichever closing style you used. If no partnership-type quote exists, insert the labelled placeholder here.

---

## Phase 2: Writing rules

Apply these throughout the draft.

**Ban "solution."** It's the most common lazy word in B2B copy. Replace with: platform, tool, workflow, system, dashboard, engine, framework, whatever is accurate.

**Kill adjectives that don't carry data.** "Seamless integration" → "integrated in 4 hours." "Robust reporting" → "custom reports that take 3 clicks, not 3 days."

**Lead with the After.** The win goes in the headline and the first paragraph. Don't make the reader earn it.

**Write for scanners.** Every section gets its own specific, outcome-carrying subheading: short and catchy, headline-length, not paragraph-length. Never publish the generic framework name (Customer context, Results, Trigger and challenge, etc.) as the actual header; the numbered names in Phase 1 are structural roles, not headers to print. A reader who only reads subheadings should understand the arc. Generic label → actual header, by section:

- Customer context → "A 26,000 m² Hub for 200 Branches"
- Trigger and challenge → "No Legacy System, Just 14 Months to Launch"
- Jobs-to-be-Done → "One Partner, Not Five Suppliers"
- Decision and buying committee → "Integration, Speed and Proximity Won the Deal"
- Implementation: the bridge → "Live Before the Doors Opened"
- Capabilities by outcome → "What's Running Today"
- Results → "From 40 Hours of Manual Entry to 15 Minutes" (outcome-led; this is where a real metric belongs)
- Facts & figures → "The Deployment, By the Numbers" (scope-led; use this header here, not on Results, when there's no outcome metric)
- The close, forward-looking → "What's Next for [Customer]"
- The close, recap → "The Deployment That Delivered"

**Cross-functional appeal, when the brief supports it.** Every story needs one moment that speaks to the person holding the budget, not just the person using the product. If Finance or IT has no reason to care, the deal doesn't close.

---

## Phase 2b: Source audit (mandatory)

Before the clean pass, audit the draft line by line:

1. List every factual statement in the draft: numbers, names, roles, places, events, problems, product capabilities, causes and effects.
2. Match each one to the exact words in the brief it comes from.
3. Delete or rewrite every statement with no match. Do not keep it as an "assumption"; remove it.
4. Re-read the remaining draft for sentences that imply something new (a consequence, a feeling, a scale) and cut those too.

Deliver the result as a compact table after the draft: `Statement | Source in brief`. Every row must have a source. If the table has a row with no source, the draft is not finished.

---

## Phase 3: AI content clean pass

After drafting, run `ai-content-cleaner` in **BALANCED** mode.

Customer stories are especially prone to:
- em dashes, collaborative scaffolding, copula avoidance ("serves as a testament to")
- "robust," "seamless," "transformative," "leverage," "streamline," "cutting-edge"
- significance inflation ("marking a pivotal moment in their journey"), promotional language, rule-of-three filler
- "In today's fast-paced business environment," "Furthermore," "It is worth noting that"

Use BALANCED (not CLEAN) to preserve:
- Intentional AEO structures like bolded inline headers (Pillar 1/2/3, decision criteria)
- Deliberate FAQ or structured data patterns for SEO
- Heading capitalisation choices that match brand standards

After the clean pass, run the self-check:
- [ ] Are all quotes sourced from real material provided by the user: no invented or illustrative quotes?
- [ ] Do quotes sit in their anchor sections (epiphany in Trigger and challenge, transformation in Results, partnership in the close) rather than only clustered in Quotes at a glance?
- [ ] Does the close end with real forward motion or an earned recap, not a bare `[PLACEHOLDER]` used as a default?
- [ ] Are all metrics and problems sourced directly from the brief: nothing extrapolated or assumed?
- [ ] Are all gaps marked with explicit `[PLACEHOLDER]` labels rather than filled with plausible-sounding content?
- [ ] Is "solution" gone or used at most once?
- [ ] Is the status quo painted as a real risk, as far as the brief supports it and no further?
- [ ] If the brief names a secondary stakeholder (Finance, IT, HR), do they get a reason to care? If it names none, is that left out or marked `[MISSING]` rather than invented?
- [ ] Does the Bridge section use only supplied implementation detail, or is it omitted or marked `[MISSING]`?
- [ ] Can a reader understand the full story just from the subheadings?
- [ ] Does the copy pass the one-line test: *"This is a story about how [Customer] escaped [Old Way] by using [Specific Tool] to achieve [Outcome], for both [Persona A] and [Persona B]."*

---

## Output format

Deliver the story in this order:

1. **Working headline** (with note if metric placeholder is needed): short and catchy, not a full descriptive sentence
2. **Full draft** using the 12-section structure above. Every section gets its own specific, outcome-carrying subheading, headline-length, never the generic framework name. Quotes sit in their anchor sections (epiphany in section 4, transformation in section 9, partnership in section 12); include Facts & figures (10) when the numbers are scope rather than outcome, and include Quotes at a glance (11) only if a standalone pull-quote block is useful for other formats. Section 12 always closes with forward motion or a recap, never a bare placeholder by default
3. **Source audit table**: `Statement | Source in brief`, every row sourced (Phase 2b)
4. **Missing elements**: brief list of any `[MISSING]` and `[PLACEHOLDER]` items and what would make each one stronger
5. **AI content sweep summary**: brief list of patterns found and removed in the BALANCED clean pass

Never add an "assumptions I made" list that contains invented content. The only assumptions allowed are about format (length, tone, language), never about facts.

If the user provided a complete brief, deliver the full draft in one pass. If significant elements are missing, ask for them first (Step 0 gates this).

---

## Reference file

See `references/brief-template.md` for a standalone intake form to send to customers or internal sales teams when collecting story material.
