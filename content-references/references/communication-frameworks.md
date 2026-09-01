# Communication Frameworks: Structural Choice by Objective

Intent (`content-intent-framework.md`) tells you what the reader wants.
This reference answers a separate question: once you know that, **how do
you structurally build the piece** to deliver it? "Better" has no fixed
answer here — it depends entirely on the objective. Pick a framework
deliberately; don't default to one out of habit.

Part of the `content-references` shared library.

---

## Why not just always use Minto?

The Minto Pyramid Principle is the strongest framework available for
**logical persuasion** — start with the answer, then defend it with
MECE (Mutually Exclusive, Collectively Exhaustive) supporting arguments.
It's the right default for executive summaries, strategic reporting, and
consulting-style deliverables, and it's efficient precisely because it
front-loads the conclusion.

Its blind spot is exactly what makes it efficient: **it's purely logical
and builds no narrative tension.** People rarely decide on logic alone.
A landing page, an ABM campaign, or a keynote needs emotional resonance —
something Minto is deliberately built to skip. Use the frameworks below
when the objective calls for tension, momentum, or urgency rather than
argument.

---

## The five frameworks

### 1. Minto Pyramid — for defending a strategy

**Structure:** Answer → grouped, MECE supporting logic → data.

**Use for:** executive summaries, strategic reports, consulting
deliverables, internal recommendations — any piece where the audience is
already asking "how do we solve this?" and just needs the argument laid
out efficiently.

**Mechanic:** state the conclusion first, then group supporting arguments
so each one is a genuinely distinct reason (no overlap) and together they
cover the full case (no gaps). Kills narrative tension by design — that's
correct for this objective, wrong for most others.

### 2. Duarte Sparkline — for keynotes and visionary pitches

**Structure:** oscillate between "what is" (the painful status quo) and
"what could be" (the better future), building toward a "new bliss" close.

**Use for:** keynotes, product launches, vision decks — anything where the
goal is to move an audience emotionally toward a future state, not just
inform them of one.

**Mechanic:** repeatedly widen the gap between current reality and the
possible future before finally closing it. The tension Minto avoids is
the entire engine here — the audience stays engaged because the gap
hasn't resolved yet.

### 3. StoryBrand — for B2B marketing and landing pages

**Structure:** a **character** (the customer) has a **problem**, meets a
**guide** (the brand) who hands them a **plan**, and is called to
**action** — resulting in **success** or avoiding **failure**.

**Use for:** landing pages, nurture sequences, web copy — anything where
opening with your own answer (the Minto move) would read as arrogant to a
prospect who hasn't yet been positioned as the hero of the story.

**Mechanic:** the brand is the guide, never the hero. Customer-centric
("here's how you get through this") beats company-centric ("here's our
recommendation") for anything the reader has to be persuaded to want.

### 4. PAS — for copywriting and lead generation

**Structure:** **Problem** → **Agitate** the pain until it feels urgent
→ **Solution**.

**Use for:** short-form conversion copy — ads, lead-gen emails, PPC
landing pages. The most reliable structure available for driving a click
or a form-fill.

**Mechanic:** leverages loss aversion directly — agitating the pain makes
inaction feel costly before the solution is offered as relief. Emotion
drives the action; logic (which Minto would lead with) only gets to
justify it afterward. Minto in a marketing email reads like a whitepaper;
PAS reads like an offer.

### 5. BLUF — for rapid-fire internal efficiency

**Structure:** Bottom Line Up Front — state the decision, action, or
takeaway in the first sentence. No supporting pyramid unless asked.

**Use for:** daily project updates, internal status emails, Slack
summaries — anywhere Minto's full supporting structure is overkill and
the reader's time matters more than the argument.

**Mechanic:** often confused with Minto because both front-load the
conclusion, but BLUF stops there — no MECE grouping, no defended logic
tree, just the takeaway. Faster to write and faster to read.

---

## Decision table

| Goal | Framework | Core mechanic |
|---|---|---|
| Defending a strategy | Minto Pyramid | Answer → grouped logic → supporting data |
| Inspiring an audience | Duarte Sparkline | What is ↔ what could be → the new bliss |
| Converting prospects | StoryBrand | Hero + problem → meets guide → gets plan |
| Driving urgency | PAS | Name the pain → agitate it → offer relief |
| Internal efficiency | BLUF | Bottom line → stop |

**Key rule of thumb:** use Minto or BLUF when the audience is already
asking "how do we solve this?" — they've accepted the problem and want
the answer efficiently. Use Sparkline, StoryBrand, or PAS when the
audience doesn't yet realize they have a problem worth solving — they
need to feel the gap before the answer will land.

---

## Mapping to Content Bucket and to Jordi's actual work

Cross-reference against `content-intent-framework.md` — intent and
framework are separate decisions, but they correlate:

| Content Bucket | Frameworks that usually fit | Example |
|---|---|---|
| Informational | Minto (if the reader already wants the answer) or a light Sparkline open (if the post needs to first establish why the topic matters) | A client guide page that opens with "what is" the current pain before answering |
| Navigational | Neither — wayfinding, not persuasion | N/A |
| Transactional | StoryBrand or PAS, almost always | A client's Google Ads landing pages, product/solution pages |

**Practical mapping for recurring work:**
- A client's executive-facing content (board decks, strategic proposals,
  management presentations) → **Minto**
- A client's product launches, category-defining keynote content → **Sparkline**
- A client's landing pages, solution pages → **StoryBrand**
- A client's Google Ads copy, lead-gen email sequences → **PAS**
- Internal status updates, quick team Slack/email summaries → **BLUF**
- A voice-led personal/lifestyle review series → none of these fit
  cleanly; a verdict-led structure is closer to BLUF in spirit (bottom
  line up front, no defended pyramid) but shouldn't be forced into any
  of the five above

## Combining frameworks

These aren't always mutually exclusive within one document. A client
customer story can open with a brief Sparkline-style gap (the "before"
state) and then resolve into StoryBrand's plan/success structure — that's
exactly what `customer-story-writer`'s existing arc already does, without
having named it. A long report can use Minto for the executive summary and
switch to BLUF for individual daily-update sections within it. Name the
framework being used per section when mixing, so the structural choice is
deliberate rather than accidental.
