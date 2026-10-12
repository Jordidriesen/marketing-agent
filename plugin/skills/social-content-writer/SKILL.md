---
name: social-content-writer
description: "Always use for any organic social post, however short: LinkedIn, Instagram, X or Reddit, with hook, structure, hashtags and CTA per platform. Use for \"LinkedIn post\", \"company post\", \"caption\", \"tweet\". Not paid ads (ad-creative-matrix)."
metadata:
  version: 1.2.1
  history: "v1.2.1: required skill calls stated up front; the follow-up skills are called through the Skill tool, never imitated inline. v1.2.0: platform rules moved to references/ (one file per platform), read on demand in Step 6. v1.1.0: content-references files renamed and merged; references to them updated."
---

# Social Content Writer

Drafts ready-to-post social copy, one platform at a time or several at once, in the right brand voice: built around Instagram, LinkedIn, Reddit, and X, since each has its own algorithm behavior, format expectations, and (for Reddit especially) its own social contract around self-promotion.

**Required skill calls.** After drafting, call `copy-editing` and `ai-content-cleaner` through the Skill tool, in that order, and never imitate them with an inline edit. A reply that skips either is not finished. End the reply with one line: `Skills run: ...`.

**Scope:** A single post or a short batch of posts for one topic/announcement. Not paid ads (`ad-creative-matrix` writes those). Not a content calendar (`campaign-plan` plans that) and not the underlying web content being promoted (`web-content-pipeline` / `customer-story-writer` write that).

**Core rule when several platforms are requested:** re-architect per platform, don't reformat the same text four ways. Instagram's own 2026 algorithm update explicitly deprioritizes recycled cross-platform content, and a LinkedIn post pasted into Reddit reads as an ad and gets removed. Steps 1–4 (brand, requirements, angle, framework) are shared; Step 6 is not.

## Step 0: Choose the Platform(s)

Before gathering anything else, ask which platform(s) this post is for. If the user already named the platform(s) in their request, skip straight past this and confirm briefly instead of asking again.

Use a multi-select question (via the elicitation tool if available):

- **Instagram**
- **LinkedIn**
- **Reddit**
- **X** (Twitter)
- **Not sure, help me pick**, ask one follow-up about the goal (reach, community trust, thought-leadership authority, quick engagement) and recommend one or two platforms based on the answer

If the user picks more than one, proceed through Steps 1–4 once with shared inputs, then run Step 6 separately per platform.

## Step 1: Identify the Brand

Same pattern as `web-content-pipeline`: determine which brand/client this post is for (from the brief, existing conversation context, or by asking if unclear), check for a matching `[brand]-brand-kit` skill, and load it if found, its voice rules override the generic tone guidance below. If no brand kit exists, ask for tone or default to clear/professional and note that a brand kit is worth building if this becomes recurring work.

## Step 2: Gather Requirements

| Field | Input |
|---|---|
| Brand/client | Determines which brand kit applies |
| Platform(s) | Carried from Step 0 |
| Topic/announcement | What the post is about |
| Key message | The one thing the reader should take away |
| Link or asset | URL, image, or video the post points to, if any: note per Step 6 that LinkedIn and X both penalize in-post links heavily |
| Goal | Engagement, traffic, awareness, community, authority |

If any field is missing and the platform choice materially changes the format, ask before writing.

## Step 3: Research the Angle

Before writing, research the topic for: data points or statistics that support the angle, a contrarian take or surprising fact, a real example or case, or a common misconception to challenge. If the angle isn't already obvious from the brief, present 2-3 angle options (each with a one-line description of the hook it enables) and let the user pick before drafting.

## Step 4: Choose a Structural Framework

Per `content-references/references/content-briefing.md`, structure follows objective, not habit:

| Objective | Framework | Why |
|---|---|---|
| Driving urgency / a click | **PAS** (Problem → Agitate → Solution) | Loss aversion: the most reliable structure for short conversion copy |
| A personal story with a takeaway | **Story → Lesson → Advice** (the social-native cousin of Sparkline: widen the gap between "what was" and "what is," then close it) | Matches how personal-transformation posts actually land: tension before resolution |
| Stating a take with authority | **BLUF** (Bottom Line Up Front) | State the take in sentence one; let the rest support it: fastest to read, matches how LinkedIn's algorithm rewards specificity in the first line |
| A how-to or listicle | **Numbered steps** | Scannable, save-worthy: the format Instagram/LinkedIn algorithms both reward for saves |

Default by platform if the user has no preference: LinkedIn → BLUF or PAS; Instagram → Story→Lesson→Advice or numbered steps; X → PAS (compressed) or a numbered thread; Reddit → none of these, see Step 6's Reddit section, which uses a different logic entirely.

## Step 5: Generate Hook Options

Offer 2-3 hook angles from this menu, adapted to what each platform's algorithm currently rewards (see the platform files, LinkedIn now penalizes engagement bait, Reddit penalizes anything that reads like a hook at all):

- **Number-led**: open with a specific metric or count
- **Contrarian**: state a common belief, then flip it
- **Personal transformation**: before vs. after, with a concrete detail
- **Named reference**: a tool, person, or event the audience recognizes
- **Admission**: a mistake, loss, or "I got this wrong"
- **Prediction**: a forward-looking, specific claim

Every hook should be specific (a number, name, or concrete detail beats an abstraction): this is what LinkedIn's and X's 2026 algorithms both reward, and it's also just better writing.

## Step 6: Write to Platform Format

**Read the platform file for each platform you chose in Step 0, now, before drafting** (use the Read tool; these files are not loaded for you). Load only the platforms you need. Paths are relative to this skill's folder.

- Instagram: `references/instagram.md`
- LinkedIn: `references/linkedin.md`
- X (Twitter): `references/x.md`
- Reddit: `references/reddit.md`

### Other platforms

If the user needs a platform outside these four (Facebook, TikTok, YouTube Community, etc.), apply the universal structure, hook, body, one clear CTA, and ask for any platform-specific constraints (character limits, tone norms) the user knows, since this skill's researched depth is scoped to the four above.

## Step 7: Copy Edit and Humanize

Run `copy-editing` (Seven Sweeps) on each platform's draft, then `ai-content-cleaner` in CLEAN mode (social posts rarely have structure worth preserving in BALANCED mode). Confirm the voice still matches the loaded brand kit afterward, and that nothing in Step 6's platform rules got softened back into what the sweep would normally recommend (e.g. don't let a generic "add urgency" edit reintroduce LinkedIn engagement bait or a Reddit sales pitch).

## Step 8: Self-Check Before Output

Before presenting, verify against the rules in the platform file(s) you read in Step 6: hook is specific (not generic), no in-post link where the platform penalizes it, hashtag count matches platform norms (heavy on Instagram, light on LinkedIn, none on X or Reddit), and, for Reddit specifically, the draft reads like a person, not an ad.

## Output

For each platform requested, present in a plain code block (ready to paste, with line breaks exactly as they should appear):

- 2-3 hook options used or considered
- Full post copy
- Hashtag suggestions (platform-appropriate; none for X or Reddit)
- Note on brand voice/tone and framework applied
- For Reddit: a reminder to confirm the target subreddit's current self-promotion rules before posting

Ask: "Would you like this adapted for another platform, a variant to test, or should I check it against your brand's compliance rules?" (Route the last option to `brand-review`.)

## Related Skills

- `[brand]-brand-kit`: a brand-specific skill following this naming pattern, loaded in Step 1 when one exists
- `content-references/references/content-briefing.md`: Step 4's framework choices
- `copy-editing` / `ai-content-cleaner`: Step 7
- `brand-review`: voice and compliance gate before publishing
- `web-content-pipeline`: for the web page a social post might link to
- `customer-story-writer`: for a case study a social post might summarize
- `content-creation`: the gateway skill; routes here when the content type is social
- `ad-creative-matrix`: for paid social and video ads (hooks, bodies, CTAs, test plan). This skill is organic only
