---
name: personal-brand-reviews
description: >
  Write review posts for any of the four personal blog series on
  jordidriesen.be: On the Bar (coffee), The Bottle Log (fragrances), On the
  Wrist (watches), and Pocket Science (EDC: pens, knives, wallets, small
  tools). Trigger on: "write a review," "new blog post," "On the
  Bar/Bottle Log/On the Wrist/Pocket Science post," "review this
  coffee/watch/fragrance/pen/knife," "review my wallet," "EDC review,"
  "new bag in the grinder," "I've been wearing/carrying this," "new EDC
  item," or wanting to write about a coffee, fragrance, watch, or EDC item.
  Applies the personal-brand-kit voice by default, a copy-editing quick
  sweep, and a CLEAN-mode ai-content-cleaner humanizing pass. Publishes
  with visible H2 headers and a closing Pro's & Con's block — confirmed
  against the live site for fragrance, adapted for coffee, watches, and
  EDC. No keyword research needed; personal blog series, not commercial
  content.
metadata:
  version: 1.1.0
  history: "Renamed from jordi-blog-reviews to personal-brand-reviews, to
    match personal-brand-kit's naming. Same four series, same pipeline,
    same structure — identifier only."
---

# jordidriesen.be — Blog Review Skill

Four personal blog series, one skill. All share the same voice, the same
light-touch SEO approach, and the same story-first philosophy. The series
differs; the standards don't.

---

## Pipeline

```
1. Series selection + inputs   (Step 1 below)
2. Draft                       (per-series Structure — personal-brand-kit voice applied by default)
3. Copy edit — quick sweep     (copy-editing skill: Clarity, Voice & Tone, Specificity)
4. Humanize                    (ai-content-cleaner skill, CLEAN mode)
        ↓
   Published post, in the Output Format below
```

This is the same pipeline shape `web-content-pipeline` and
`customer-story-writer` use, built on the same `content-references` shared
library — just scoped to what a personal narrative review needs. Of the five
`content-references` modules, four don't apply here: `content-intent-framework`,
`communication-frameworks`, and `behavioral-psychology` exist to classify and
structure persuasion or informational copy, and `seo-aeo-optimization` exists
to structure content for ranking or AI citation. These posts are a formed
opinion with a fixed narrative shape already defined per series below — not
persuasion copy, not a keyword play. Only the fifth module,
`ai-content-humanizing.md`, is relevant, and it's used in its
directly-invocable form: the `ai-content-cleaner` skill (see below).

---

## Step 1 — Series Selection

If the subject is not already clear from context, ask:

> "Which series is this for — On the Bar (coffee), The Bottle Log (fragrance),
> On the Wrist (watches), or Pocket Science (EDC items)?"

If the subject is obvious from what Jordi says ("I want to review the beans I
just bought" / "write up the Mido" / "Bottle Log post for the Lattafa" / "new
pen I've been carrying" / "review my pocket knife"), skip the question and
proceed directly to input collection for the right series.

Once the series is confirmed, jump to that section below.

---

## Shared Standards (All Series)

These apply regardless of which series is active.

### Voice

Apply `personal-brand-kit` in full, by default, without asking — register,
rhythm, the four pillars, banned language, the quality checklist. There's only
one voice for this blog, so there's no voice question to raise with Jordi.
That skill is the single source for this voice; nothing further to restate
here.

### SEO — Light Touch Only

Personal blog series. No keyword targets. Apply these basics and move on:

- **Title:** `[Series Name]: [Subject]` (exact format defined per series below)
- **Slug:** lowercase, hyphenated, follows title pattern
- **Meta description:** 150–160 characters, human-first, one hook from the review
- **H1:** matches title exactly
- **Internal links:** suggest 1–2 cross-links to other posts in the same series
  once more than one entry exists; suggest 1 cross-series link where natural
- **First edition of any series:** no internal links needed

No keyword density targets, no FAQ sections, no structured data required.

### Copy Edit — Quick Sweep

After drafting, run a lightweight pass with the `copy-editing` skill: its
Quick-Pass Editing Checks (word-, sentence-, and paragraph-level), plus these
three sweeps from the full framework —

- **Clarity (Sweep 1):** every sentence immediately understandable, no
  sentence trying to do too much, pronouns have clear references
- **Voice & Tone (Sweep 2):** consistent with `personal-brand-kit`
  throughout, no jarring shifts, reads well aloud
- **Specificity (Sweep 5):** vague words replaced with concrete ones,
  generic statements made specific, filler removed

Skip **So What, Prove It, Heightened Emotion, and Zero Risk**. Those four
sweeps exist to move a reader toward a purchase decision or pre-empt an
objection. A personal review isn't persuasion copy — it doesn't need a
benefit bridge, substantiated claims, or an objection-handling close.

### Humanize — AI Content Sweep

Run a **CLEAN mode** pass with the `ai-content-cleaner` skill — the
directly-invocable form of `content-references/references/ai-content-humanizing.md`.
CLEAN, not BALANCED: BALANCED mode exists to protect intentional SEO/AEO
structure (inline-header lists, rule-of-three, title-case headings), and
this content doesn't carry any of that — no keyword targets, no FAQ blocks,
no structured data to preserve. A full CLEAN pass is safe here.

One thing to protect through the sweep regardless of mode: the deliberate
short/long sentence rhythm that's the core of `personal-brand-kit`'s
Rhythmic pillar. That's a voice trait, not an AI tell — don't let the
cleaner flatten it while it's removing genuine AI patterns.

### Output Format (All Series)

**Confirmed pattern — The Bottle Log (fragrance) only.** Section headers are
published, not internal scaffolding — this is checked directly against the
live site, not a guess: [Hema X Fugazzi HDP](https://jordidriesen.be/perfume/hema-x-fugazzi-hdp/).

1. **Opening.** Sections 1–2 ("The Fragrance," "How It Got Here") merge
   into flowing, unheaded prose. There's no "## The Fragrance" in the
   published post.
2. **Named H2s.** "On the Skin," "Performance," "The Verdict" — each
   publishes as a visible `## H2`, titled exactly as given in the
   Structure below.
3. **Pro's & Con's.** A closing block after the last H2, titled exactly
   `## Pro's & Con's`. 2–4 pros and 1–3 cons, each a short fragment
   (roughly 3–8 words, not a full sentence) drawn from points already
   made in the review — a scan aid, not a place to introduce a new claim.

**Adapted pattern — On the Bar, On the Wrist, Pocket Science.** The same
shape extends naturally to the other three series, but nothing live on the
site confirms it the way Hema X Fugazzi confirms the fragrance one — the
one watch post published today (Mirexal Superautomatic) predates this
template entirely and uses one-off evocative headers instead of a fixed
set. Treat this as a considered adaptation, not a locked spec:

- **Opening** merges the first two Structure sections below, same
  mechanic as fragrance.
- **Named H2s** use each series' own section names, not fragrance's —
  "In the Cup" for coffee, "On the Wrist" / "What Bothers Him" for
  watches, "In the Pocket / In the Hand" / "What Bothers Him" for Pocket
  Science. A watch doesn't have "performance" the way a fragrance does;
  "what bothers him" is the more honest second axis for anything worn or
  carried rather than worn on skin.
- **Closing block** stays `## Pro's & Con's` for consistency across the
  blog, unless a published post in that series later shows the live site
  does something else at the close.

The first time On the Bar, On the Wrist, or Pocket Science actually
publishes under this structure, check the live post against this section
and correct anything that doesn't match — the same way this section was
written by checking the fragrance post directly rather than assuming.

Deliver in this order:

1. **Post title** (H1)
2. **Full post** — unheaded opening, named H2 sections, closing Pro's &
   Con's block, as above
3. **Slug**
4. **Meta description** (with character count)
5. **Sweep note** — one line confirming the copy-edit and humanizing passes
   ran, flagging anything notable either one changed

---

## Series A — On the Bar (Coffee)

**What it is:** Short, opinionated reviews of coffee beans currently in the
grinder. One post per new bag, written after enough pulls to have a real opinion.

**Word count:** 300–500 words.

**Title format:** `On the Bar: [Roaster] [Coffee Name]`
**Slug:** `/on-the-bar/[roaster-coffee-name]`

### Inputs

| Field | Required? | Notes |
|---|---|---|
| Roaster name | Yes | Full name as on the bag |
| Roaster location | Yes | City / country |
| Coffee / blend name | Yes | Exact as labeled |
| Origin(s) | Yes | Country, region if known |
| Roast level | Yes | Light / medium / dark or roaster's own descriptor |
| Processing method | If known | Washed / natural / honey / experimental |
| Intended for | Yes | Espresso / filter / both |
| Price / grammage | Optional | Adds context for the verdict |
| Official tasting notes | If known | Used as a foil, not as structure |
| Jordi's tasting notes | Yes | What he actually tastes. This is the post. |
| Milk performance | If tested | How it holds in a flat white or lungo |
| How he found it | Preferred | Keeps it personal |
| Verdict | Yes | Would he buy again? |

If Jordi gives rough notes, expand them. If he gives nothing but the roaster
and his verdict, ask for the tasting notes before writing.

### Structure

Sections 1–2 merge into the unheaded opening. Sections 3–4 publish as
visible H2 headers, titled exactly as below (adapted pattern — see Output
Format).

**1. The Bean**
One paragraph. Roaster, origin(s), roast level, processing if known. The
passport: who made it, where it came from, what was done to it. Factual,
brief, no marketing language from the bag.

**2. Why This One**
One paragraph. How it ended up in his grinder. A tip, a local roaster he
walked past, a limited release he'd been tracking. If there's no story, one
sentence is fine, but there must be something.

**3. In the Cup**
One to two paragraphs. Aroma, first impression, tasting notes (his, not the
bag's), mouthfeel, finish, how it behaves across the shot window. If he pulled
milk drinks, note how it holds. Specific over comprehensive: "dark chocolate
that drops bitterness fast and doesn't linger" not "chocolate." If his notes
contradict the bag's claims, say so.

**4. The Verdict**
One or two sentences. Would he buy it again. No hedging. Conditional answers
("yes, but only as filter") are fine. Vague ones aren't.

### Title Examples
- `On the Bar: Andes Espresso Blend`
- `On the Bar: Tim Wendelboe Finca El Suelo`
- `On the Bar: Coffee Collective Ethiopia Yukro`

---

## Series B — The Bottle Log (Fragrance)

**What it is:** Story-first, opinionated reviews of fragrances Jordi has worn
long enough to have a real opinion on. Not first impressions, not sample vials.

**Word count:** 400–600 words.

**Title format:** `The Bottle Log: [House] [Fragrance Name]`
**Slug:** `/the-bottle-log/[house-fragrance-name]`

### Inputs

| Field | Required? | Notes |
|---|---|---|
| House / brand | Yes | Full name as on the bottle |
| Fragrance name | Yes | Exact, including flanker designation |
| Perfumer | If known | Credit where it's due |
| Concentration | Yes | EDP, EDT, extrait, parfum, etc. |
| Release year | If known | Relevant for reformulations |
| Fragrance family / character | Yes | Jordi's read, not the brand's classification |
| Acquisition story | Yes | How and why it ended up in his collection |
| How long he's been wearing it | Preferred | Grounds the "formed opinion" angle |
| Opening, his experience | Yes | What he actually smells, not the pyramid |
| Dry-down, his experience | Yes | How it evolves |
| Base, his experience | Yes | What it settles into, what lingers |
| Official notes / pyramid | If known | Used as a foil where relevant |
| Longevity | Yes | Honest hours on skin |
| Projection / sillage | Yes | How far it travels, how long the trail lasts |
| Occasion / season fit | Yes | His read on when it works |
| Verdict | Yes | When he'd reach for it and why |
| Price / format | Optional | Bottle size, where bought, rough cost |

If the acquisition story is missing, ask. It's the anchor of the post.

### Structure

Sections 1–2 merge into the unheaded opening. Sections 3–5 publish as
visible H2 headers, titled exactly as below (confirmed pattern — see
Output Format) — this is the exact shape of [Hema X Fugazzi HDP](https://jordidriesen.be/perfume/hema-x-fugazzi-hdp/):
"On the Skin," "Performance," "The Verdict."

**1. The Fragrance**
One paragraph. House, perfumer if known, concentration, release year if
relevant. Factual, brief, no marketing language. Passport, not press release.
Middle Eastern or niche houses get the same treatment as any other. No special
framing, no exoticism, no "surprisingly good for the price" condescension.

**2. How It Got Here**
One to two paragraphs. The acquisition story. The rabbit hole, the
recommendation, the decant that became a bottle, the blind buy. Honest is
enough. It doesn't need to be dramatic.

**3. On the Skin**
One to two paragraphs. Opening, dry-down, base: as a wearing experience, not
a notes pyramid. What he noticed the first time versus the fifth. Whether the
official notes match what he actually smells. Specific over comprehensive:
"a dry oud that reads more like cedar with ambition" not "oud." Where his
experience diverges from the official story, say so.

**4. Performance**
One paragraph. Longevity in honest hours. Projection: does it announce itself
or stay close? Sillage: what does the trail look like later? Skin chemistry
caveat if relevant. No rating system.

**5. The Verdict**
When he'd reach for it. Season, occasion, mood, context. Not a buy-again
binary. Paint a picture of where it sits in his actual rotation. If that place
is nowhere, say so and say why.

### Avoid (Fragrance-Specific)
- No Fragrantica-style note pyramids in prose form
- No orientalist framing for Middle Eastern houses
- No "olfactory journey," "symphony of notes," "multifaceted"

### Title Examples
- `The Bottle Log: Lattafa Oud for Glory`
- `The Bottle Log: Maison Margiela Replica Jazz Club`
- `The Bottle Log: Swiss Arabian Shaghaf Oud Aswad`

---

## Series C — On the Wrist (Watches)

**What it is:** Story-first, opinionated reviews of watches Jordi has worn long
enough to have a real opinion on. Not unboxing impressions, not first strap
changes.

**Word count:** 500–700 words.

**Title format:** `On the Wrist: [Brand] [Model]`
**Slug:** `/on-the-wrist/[brand-model]`

### Inputs

| Field | Required? | Notes |
|---|---|---|
| Brand | Yes | Full name as on the dial |
| Model / reference | Yes | Exact name and reference number if known |
| Year / era | Yes | Production year or decade if vintage |
| Movement | Yes | Calibre if known, manual / auto / quartz |
| Case material | Yes | Steel, gold, bronze, etc. |
| Case size | Yes | Diameter and lug-to-lug if known |
| Dial description | Yes | Colour, texture, indices, complications |
| Bracelet / strap | Yes | What it came on, what he's running now |
| Condition | If vintage | Original, restored, service history if known |
| Acquisition story | Yes | How and why it ended up on his wrist |
| How long he's been wearing it | Preferred | Grounds the "formed opinion" angle |
| Wearability notes | Yes | How it sits, how it wears across a day |
| What he uses it for | Yes | Daily wear, dress, sport, occasions |
| What he likes | Yes | Specific, not generic |
| What bothers him | Yes | Every watch has something |
| Verdict | Yes | Where it sits in his rotation and why |
| Price paid / current market | Optional | Adds context, especially for vintage |

If the acquisition story is missing, ask. It's the anchor of the post.

### Structure

Sections 1–2 merge into the unheaded opening. Sections 3–5 publish as
visible H2 headers, titled exactly as below (adapted pattern — see Output
Format).

**1. The Watch**
One paragraph. Brand, model, reference if known, year or era, movement type,
case material and size. Enough to orient a reader who doesn't know the
reference, without becoming a spec sheet. No "legendary," no "iconic."

**2. How It Got Here**
One to two paragraphs. The acquisition story. The years of wanting it, the
Chrono24 find at 11pm, the inheritance, the impulsive purchase that turned
out right. There must be something beyond "I bought it."

**3. On the Wrist**
The wearing experience. How it sits: case presence, lug comfort, bracelet
or strap feel across a day. Dial legibility in different light. What wearing
it actually feels like versus what he expected. What it pairs with and what
it doesn't. Any quirks that only surface with time. This is not a spec
recitation. That's what section 1 is for.

**4. What Bothers Him**
One paragraph. Every watch has something: the clasp that pinches, the lume
that disappoints, the crown that digs in, the size that's slightly off. Be
honest. A review without a criticism is an ad. If there's genuinely nothing,
say that and note why it's notable.

**5. The Verdict**
Where it sits in his rotation. What occasions it owns. Daily wearer or
specific-context piece. What it replaced or what it competes with. Whether
he'd buy it again at the price he paid. One to two sentences.

### Avoid (Watch-Specific)
- No watch-journalism clichés: "horological," "timepiece" (use watch),
  "tool watch" unless earned, "iconic," "legendary," "grail"
- No unboxing energy. This series is about wearing, not acquiring.
- Specs only where they explain the experience, not to be complete
- On vintage: honest about condition and originality, no romanticising patina

### Title Examples
- `On the Wrist: Mido Commander 1959`
- `On the Wrist: TAG Heuer Autavia CY2111`
- `On the Wrist: Seiko SKX007`

---

## Series D — Pocket Science (EDC)

**What it is:** Story-first, opinionated reviews of everyday carry items Jordi
has used long enough to have a real opinion on. Pens, pocket knives, wallets,
small tools, keychains, notebooks: anything that lives in a pocket, bag, or
on a desk and gets handled daily. Not unboxing reactions, not first-week
impressions.

**Word count:** 400–600 words.

**Title format:** `Pocket Science: [Brand] [Model]`
**Slug:** `/pocket-science/[brand-model]`

### Inputs

| Field | Required? | Notes |
|---|---|---|
| Brand | Yes | Full name as on the item |
| Model / line | Yes | Exact name, include variant if relevant (colour, material, size) |
| Category | Yes | Pen / pocket knife / wallet / notebook / tool / other |
| Material | Yes | Aluminium, titanium, leather, brass, carbon fibre, etc. |
| Dimensions / weight | Optional | Relevant when size is part of the story (EDC = pocketability matters) |
| Condition | If secondhand or vintage | Where acquired, what state it was in |
| Acquisition story | Yes | How and why it ended up in his pocket or on his desk |
| How long he's been carrying / using it | Preferred | Grounds the "formed opinion" angle |
| Carry / use context | Yes | What pocket, bag, or situation it lives in; what he uses it for |
| What he likes | Yes | Specific, not generic |
| What bothers him | Yes | Every EDC item has something |
| EDC fit | Yes | Does the form factor actually work for daily carry? |
| Collector vs. user angle | Optional | Shelf piece or gets handled daily. Say which. |
| Verdict | Yes | Where it fits in his carry and why |
| Price paid / current market | Optional | Adds context, especially for premium or niche items |

If the acquisition story is missing, ask. It anchors the post.

### Structure

Sections 1–2 merge into the unheaded opening. Sections 3–5 publish as
visible H2 headers, titled exactly as below (adapted pattern — see Output
Format).

**1. The Item**
One paragraph. Brand, model, category, material, key specs that affect the
carry experience. Enough to orient a reader who doesn't know the reference,
without becoming a spec sheet. Factual, brief. No "premium," no "iconic,"
no "ergonomic."

**2. How It Got Here**
One to two paragraphs. The acquisition story. The rabbit hole, the gift, the
impulse buy at a stationery or knife shop, the thing he'd been tracking for
months. There must be something beyond "I bought it."

**3. In the Pocket / In the Hand**
The carry and use experience. How it lives in a pocket or bag: does it add
bulk, does it disappear, does it snag? How it feels when you actually use it.
For a pen: grip, weight, line quality. For a knife: blade deployment, edge
feel, lock confidence. For a wallet: card access, bulk when loaded, wear over
time. Specific over comprehensive. Any quirks that only surface after sustained
daily carry.

**4. What Bothers Him**
One paragraph. Every EDC item has something: the clip that marks the pocket,
the edge that needs frequent touching up, the wallet that's too stiff for the
first month, the pen that's just slightly too short. Be honest. A review
without a criticism is a product listing. If there's genuinely nothing, say
that and note why it's notable.

**5. The Verdict**
Where it sits in his carry. Daily use or occasional. What it replaced or
competes with. Whether the price is justified by how much he reaches for it.
One to two sentences.

### Avoid (EDC-Specific)
- No gear-culture clichés: "premium," "tactical," "EDC-ready," "built to last"
- No unboxing energy. This series is about using, not acquiring.
- Pocketability and real-world carry always beat specs on paper
- Specs only where they explain the carry or use experience

### Title Examples
- `Pocket Science: Kaweco AL Sport Gel`
- `Pocket Science: Victorinox Cadet`
- `Pocket Science: Bellroy Note Sleeve`

---

## Cross-Series Linking

All four series live on the same blog. Where a natural connection exists,
suggest a cross-series link:
- A Pocket Science pen reviewed alongside another EDC item carried at the same time
- A fragrance reviewed alongside a watch worn in the same context
- A coffee reviewed from a roaster visited on a cycling trip also mentioned
  in another post
- A Pocket Science item that was on the desk or in the pocket during a
  journaling session that also mentions a fragrance or watch

Don't force it. One natural link is worth more than three obvious ones.

---

## Related Skills

- **personal-brand-kit** — the voice this skill applies by default; see
  that skill for the full pillars, banned language, and quality checklist
- **copy-editing** — the quick-sweep pass (Clarity, Voice & Tone,
  Specificity) run after drafting
- **ai-content-cleaner** (CLEAN mode) — the humanizing pass run last, before
  delivery; also the directly-invocable form of `content-references`'
  `ai-content-humanizing.md` module
- **content-references** — the shared library this skill's humanizing step
  draws from; see the Pipeline section above for which of its five modules
  apply here and which don't
