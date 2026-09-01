---
name: social-content-writer
description: "Draft social media posts for Instagram, LinkedIn, Reddit, or X (Twitter) with a platform-selection gate up front, then platform-specific structure, hook, hashtag, and format guidance tuned to each platform's current algorithm behavior — including Reddit's community-first self-promotion norms, which are fundamentally different from the other three. Use for \"write a LinkedIn post,\" \"social post,\" \"Twitter/X post,\" \"Instagram caption,\" \"Reddit post,\" or \"social media content.\" Not for a full content calendar (see campaign-plan) and not for web pages (see web-content-pipeline) or lifecycle email flows (see email-sequence-hubspot-brevo)."
---

# Social Content Writer

Drafts ready-to-post social copy, one platform at a time or several at once, in the right brand voice — built around Instagram, LinkedIn, Reddit, and X, since each has its own algorithm behavior, format expectations, and (for Reddit especially) its own social contract around self-promotion.

**Scope:** A single post or a short batch of posts for one topic/announcement. Not a content calendar (`campaign-plan` plans that) and not the underlying web content being promoted (`web-content-pipeline` / `customer-story-writer` write that).

**Core rule when several platforms are requested:** re-architect per platform, don't reformat the same text four ways. Instagram's own 2026 algorithm update explicitly deprioritizes recycled cross-platform content, and a LinkedIn post pasted into Reddit reads as an ad and gets removed. Steps 1–4 (brand, requirements, angle, framework) are shared; Step 6 is not.

## Step 0 — Choose the Platform(s)

Before gathering anything else, ask which platform(s) this post is for. If the user already named the platform(s) in their request, skip straight past this and confirm briefly instead of asking again.

Use a multi-select question (via the elicitation tool if available):

- **Instagram**
- **LinkedIn**
- **Reddit**
- **X** (Twitter)
- **Not sure — help me pick** — ask one follow-up about the goal (reach, community trust, thought-leadership authority, quick engagement) and recommend one or two platforms based on the answer

If the user picks more than one, proceed through Steps 1–4 once with shared inputs, then run Step 6 separately per platform.

## Step 1 — Identify the Brand

Same pattern as `web-content-pipeline`: determine which brand/client this post is for (from the brief, existing conversation context, or by asking if unclear), check for a matching `[brand]-brand-kit` skill, and load it if found — its voice rules override the generic tone guidance below. If no brand kit exists, ask for tone or default to clear/professional and note that a brand kit is worth building if this becomes recurring work.

## Step 2 — Gather Requirements

| Field | Input |
|---|---|
| Brand/client | Determines which brand kit applies |
| Platform(s) | Carried from Step 0 |
| Topic/announcement | What the post is about |
| Key message | The one thing the reader should take away |
| Link or asset | URL, image, or video the post points to, if any — note per Step 6 that LinkedIn and X both penalize in-post links heavily |
| Goal | Engagement, traffic, awareness, community, authority |

If any field is missing and the platform choice materially changes the format, ask before writing.

## Step 3 — Research the Angle

Before writing, research the topic for: data points or statistics that support the angle, a contrarian take or surprising fact, a real example or case, or a common misconception to challenge. If the angle isn't already obvious from the brief, present 2-3 angle options (each with a one-line description of the hook it enables) and let the user pick before drafting.

## Step 4 — Choose a Structural Framework

Per `content-references/references/communication-frameworks.md`, structure follows objective, not habit:

| Objective | Framework | Why |
|---|---|---|
| Driving urgency / a click | **PAS** (Problem → Agitate → Solution) | Loss aversion — the most reliable structure for short conversion copy |
| A personal story with a takeaway | **Story → Lesson → Advice** (the social-native cousin of Sparkline: widen the gap between "what was" and "what is," then close it) | Matches how personal-transformation posts actually land — tension before resolution |
| Stating a take with authority | **BLUF** (Bottom Line Up Front) | State the take in sentence one; let the rest support it — fastest to read, matches how LinkedIn's algorithm rewards specificity in the first line |
| A how-to or listicle | **Numbered steps** | Scannable, save-worthy — the format Instagram/LinkedIn algorithms both reward for saves |

Default by platform if the user has no preference: LinkedIn → BLUF or PAS; Instagram → Story→Lesson→Advice or numbered steps; X → PAS (compressed) or a numbered thread; Reddit → none of these — see Step 6's Reddit section, which uses a different logic entirely.

## Step 5 — Generate Hook Options

Offer 2-3 hook angles from this menu, adapted to what each platform's algorithm currently rewards (see Step 6 — LinkedIn now penalizes engagement bait, Reddit penalizes anything that reads like a hook at all):

- **Number-led** — open with a specific metric or count
- **Contrarian** — state a common belief, then flip it
- **Personal transformation** — before vs. after, with a concrete detail
- **Named reference** — a tool, person, or event the audience recognizes
- **Admission** — a mistake, loss, or "I got this wrong"
- **Prediction** — a forward-looking, specific claim

Every hook should be specific (a number, name, or concrete detail beats an abstraction) — this is what LinkedIn's and X's 2026 algorithms both reward, and it's also just better writing.

## Step 6 — Write to Platform Format

### Instagram

- **Caption**: front-load the hook — Instagram truncates around the first ~125 characters before "more." Keep it concise; pose a question or clear CTA to prompt replies.
- **Keyword-rich over hashtag-heavy**: Instagram's own social-SEO indexing now weighs the caption's actual words more than hashtag volume. Use a handful of genuinely relevant hashtags, not a wall of 30.
- **Format choice matters more than caption polish**: Reels (under 90 seconds, ideally 15-30s, hook in the first 3 seconds, loop-friendly) reach furthest; carousels (first slide must earn the swipe) are best for save-worthy educational content; single-image posts are least prioritized by the algorithm unless they're distinctly save/share-worthy.
- **Never recycle another platform's content unedited** — the 2026 algorithm explicitly rewards original, platform-native content and suppresses obvious cross-posts.
- If the post is for a Reel or carousel, flag the visual/shot sequence briefly for whoever builds the asset (this skill writes the caption/script, not the image).

### LinkedIn

- **Format hierarchy** (2026): document/PDF carousels outperform everything else for dwell time (each slide swipe extends watch time); native video (30-90s, always captioned — most watch muted) is next; then well-structured text. If the content is a framework, tutorial, or before/after, recommend a document carousel over a text post.
- **Hook**: the first ~150 characters (before "see more") decide whether the post gets wider distribution — the algorithm tests every post on 2-5% of the author's network first. Lead with a data point, a contrarian take, or a specific problem. "Excited to share insights" is a distribution killer, not a hook.
- **Structure**: short paragraphs (3-4 lines max), a blank line between thoughts — this isn't just a style choice, it's what keeps dwell time and scannability high on mobile.
- **No in-post links** — they carry roughly a 60% reach penalty. Put any link in the first comment instead, and say so in the post if relevant ("link in comments").
- **No engagement bait** ("Agree? Comment 👇") — flagged and suppressed since the March 2026 authenticity update. Write for saves and shares, not reflexive likes.
- **Hashtags**: 1-2 inline, never stacked at the bottom — the algorithm reads the actual text now, not a hashtag block.
- **Skip polls** — engagement on LinkedIn polls collapsed after the March 2026 update.

### X (Twitter)

- **Native media beats links**: the algorithm favors video, images, GIFs, and polls; a post with an external link in the body typically sees a 50-90% reach reduction. If a link is essential, put it in a reply rather than the main post, or use a native long-form Article for anything link-worthy.
- **Write for reposts and bookmarks, not likes**: a repost is worth roughly 20x a like, a reply roughly 13.5x, a bookmark roughly 10x. A post built to be shared or saved (a stat worth quoting, a list worth revisiting) outperforms one built to be liked.
- **Hook**: front-load the sharpest word or number — the character budget doesn't leave room to bury it. Use a thread for anything that needs more than one post's worth of room.
- **Reply fast**: engaging with replies in the first 2-3 hours compounds the algorithm's recency weighting.

### Reddit

Reddit is not a broadcast channel — treat it as a fundamentally different skill, not a fourth caption format.

- **The 90/10 rule (some communities enforce closer to 99/1)**: be a community member first, a marketer a distant second. This skill can draft the post itself, but the account posting it needs a real history of genuine, non-promotional participation in that subreddit — flag this to the user if it's a cold account.
- **No corporate voice**: cut every word a marketer would use and a redditor wouldn't — "revolutionary," "game-changing," "best-in-class," any polished CTA. Write like a peer describing a real experience: "I ran into this problem and built something because nothing else worked" reads true; a pitch reads as spam and gets removed by the community's anti-spam filters within minutes.
- **The title is the hook** — Reddit is title-led, not caption-led. Specific and honest beats clever: describe what the post actually is, don't tease it.
- **Disclose, don't hide**: if there's any commercial connection, say so plainly ("full disclosure: I built this") — disclosed self-interest reads as more trustworthy on Reddit than a post that pretends to be neutral and gets found out.
- **Lead with value, mention the product last, if at all**: answer the actual question or tell the actual story first. Acknowledge competing alternatives where relevant — it reads as more credible, not less.
- **No hashtags** — Reddit doesn't use them functionally; including them is itself a tell.
- **Always flag before publishing**: subreddit rules on self-promotion vary enormously (some subs welcome it in designated threads, some ban it outright, some are fine with founder stories but not product links) and change per-community. Tell the user to check the target subreddit's current sidebar/rules before posting — this skill can draft the post but can't verify a specific subreddit's current policy.

### Other platforms

If the user needs a platform outside these four (Facebook, TikTok, YouTube Community, etc.), apply the universal structure — hook, body, one clear CTA — and ask for any platform-specific constraints (character limits, tone norms) the user knows, since this skill's researched depth is scoped to the four above.

## Step 7 — Copy Edit and Humanize

Run `copy-editing` (Seven Sweeps) on each platform's draft, then `ai-content-cleaner` in CLEAN mode (social posts rarely have structure worth preserving in BALANCED mode). Confirm the voice still matches the loaded brand kit afterward, and that nothing in Step 6's platform rules got softened back into what the sweep would normally recommend (e.g. don't let a generic "add urgency" edit reintroduce LinkedIn engagement bait or a Reddit sales pitch).

## Step 8 — Self-Check Before Output

Before presenting, verify against Step 6's rules for the platform(s) used: hook is specific (not generic), no in-post link where the platform penalizes it, hashtag count matches platform norms (heavy on Instagram, light on LinkedIn, none on X or Reddit), and — for Reddit specifically — the draft reads like a person, not an ad.

## Output

For each platform requested, present in a plain code block (ready to paste, with line breaks exactly as they should appear):

- 2-3 hook options used or considered
- Full post copy
- Hashtag suggestions (platform-appropriate; none for X or Reddit)
- Note on brand voice/tone and framework applied
- For Reddit: a reminder to confirm the target subreddit's current self-promotion rules before posting

Ask: "Would you like this adapted for another platform, a variant to test, or should I check it against your brand's compliance rules?" (Route the last option to `brand-review`.)

## Related Skills

- `[brand]-brand-kit` — a brand-specific skill following this naming pattern, loaded in Step 1 when one exists
- `content-references/references/communication-frameworks.md` — Step 4's framework choices
- `copy-editing` / `ai-content-cleaner` — Step 7
- `brand-review` — voice and compliance gate before publishing
- `web-content-pipeline` — for the web page a social post might link to
- `customer-story-writer` — for a case study a social post might summarize
- `content-creation` — the gateway skill; routes here when the content type is social