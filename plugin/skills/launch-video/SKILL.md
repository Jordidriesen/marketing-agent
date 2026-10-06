---
name: launch-video
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. An original workflow for short product and brand videos (teaser, continuous-take feature demo, logo sting), written in this library's terms with the brand kit as the source of voice, colour and type. Structure and several rules (project inspection rubric, reading-time floors, poster frame as frame 0, share copy) are adapted from latent-spaces/brag (MIT, see LICENSE-brag.txt). The continuous-take idea is inspired by feitangyuan/onetake, which is licensed PolyForm Noncommercial and is therefore neither bundled nor copied. No audio files are bundled.\n"
description: "Plans and produces a short (10 to 30 second) product or brand video from the product's own source or brand kit: picks the video type (launch teaser, continuous-take feature demo, logo sting), writes the storyboard with reading-time floors, builds it as an HTML composition rendered with Hyperframes, then picks a poster frame and writes the share caption. Use for \"launch video\", \"product teaser\", \"feature demo video\", \"turn this into a video\", \"logo animation\", \"brag video\" or \"announce this with a video\". Not for logo design (logo-design), static campaign art direction (creative-brief), social graphics (canva-workflow) or video ad copy and hooks (ad-creative-matrix)."
argument-hint: "<what to show, video type if known, format (landscape, vertical, square), duration, tone, brand>"
---

# Launch video

You make short videos that show a real product doing a real thing, in the brand's own voice. The
video is built from the product's actual screens, copy and claims, so it could not belong to any other
company. If a scene could be swapped into a competitor's video unchanged, rewrite it.

## What to state up front

- **Rendering depends on the machine.** The renderer is
  Hyperframes (`npx hyperframes`, Apache-2.0, needs Node 22 and FFmpeg). Check it works with
  `npx hyperframes doctor` before promising a file. If it does not, deliver the plan, the storyboard and the
  composition source, and say a render is still to be done.
- **No music or sound effects ship with this skill.** Use a track the user supplies and is licensed to use,
  or deliver silent. Never pull audio from a source whose licence you have not read.
- A video that will be posted publicly is a public claim. Everything on screen passes `brand-review`.

## Step 0: Load the brand

Load the `[brand]-brand-kit` skill: `references/voice.md` for tone and locked wording,
`references/design.md` for colour, type and logo rules, `references/context.md` for audience and channels.
The kit outranks everything below, including the tone defaults. With no kit, read the colours and fonts
from the product's own CSS and say so. If the brand has an approved logo (`logo-design` output), use that
file as supplied and never redraw it.

## Step 1: Pick the video type

Ask one question only if the choice is genuinely open. Otherwise choose and say which.

| Type | The video is | Use it when | Length |
|---|---|---|---|
| **Launch teaser** | Hook, reveal, two or three sharp highlights, punchline and outro | A launch, a release, a feature announcement to share on social | 15 to 25 s |
| **Continuous-take demo** | One flow shown as a single unbroken move: each beat grows out of the one before it | A feature or workflow where the sequence of steps is the story | 15 to 40 s |
| **Logo sting** | The mark builds or resolves, then holds | An intro or outro for other videos, or a logo reveal after `logo-design` | 3 to 8 s |

`references/video-types.md` holds the structure, the rules and the failure modes for each. Types can
chain: a logo sting can close a teaser.

## Step 2: Inspect the product

Read the project directly. No live URL and no screenshots are needed. Priority order:

1. The main page (`index.html` or the main route): title, hero headline, tagline, section headings,
   CTA text and claims. This is the product's own voice.
2. The stylesheet: colour custom properties, font families, backgrounds. They become the video's visual
   identity unless the brand kit says otherwise.
3. `README.md` and `package.json`: name and one-line description.
4. The **user flow**: routes, key components, state steps, example folders. The strongest material is the
   product in use: entry, key action, result.
5. `public/` or `assets/`: logos and icons that can appear on screen.

Skip build output, lock files, tests, `.git`, `.env*`, keys and credentials.

**Nothing secret leaves this step.** Anything read can end up on screen in a public video. Never carry
secrets, tokens, internal hostnames, real customer names, email addresses or personal data into the plan,
the composition, the render or the caption. Substitute plausible fictional stand-ins and say so in the plan.

Then answer in writing: what the product is, the one claim or moment that earns a reaction, what real UI
should be shown, the shortest satisfying length, the tone, the audio posture (including "silent"), the
draft caption, and the 2 or 3 beats of the user flow. If there is no app, only a landing page, say so and use
the strongest visual instead.

## Step 3: Write the plan and storyboard

Write `video-plan.md` in the output folder, using
`references/storyboard.md`: the angle, the hook, the beats, the outro, the visual identity (exact values),
scene by scene with durations, on-screen text, what real product material is used and the transition
into the next scene.

Hard rules for every type:

- **The hook is the first 2 to 3 seconds.** Plan it first. It must work with the sound off.
- **Show the thing.** At least one scene shows actual UI, copy or a key visual from the product. No
  abstract filler, colour washes or generic motion graphics.
- **No generic SaaS language.** Use the product's actual copy and claims. Never invent a number, a
  customer, a result or a feature. Every claim on screen traces to the source or to something the user said.
- **Reading time.** Pace comes from motion and cuts, never from pulling text away before it can be read.
  A short label needs about 0.8 s settled, a sentence about 0.3 s per word with a minimum of about 1.2 s.
  If a scene carries more text than its length allows, cut copy or split the scene. Do not speed it up.
- **Sequential text** (list items, stat rows) holds each item to those floors, even if the music beat
  is faster.
- Scene durations must sum to the target. Count them.

**Checkpoint.** Show the plan and storyboard and wait for the user's go-ahead before building. A
storyboard is cheap to change and a composition is not. Skip the pause only if the user said not to check in.

## Step 4: Build the composition

Hand a focused composition brief to Hyperframes. Your plan owns the angle, the source material, the
storyboard, the tone and the delivery. Hyperframes owns the animation mechanics and structure.

```bash
npx hyperframes doctor          # confirm Node, FFmpeg and Chrome are present
npx hyperframes init            # scaffold the composition inside <output-dir>/composition/
npx hyperframes docs            # read its current guidance before writing the composition
```

If Hyperframes' own agent skills are installed in the session, read them before composing. Recreate real
product moments in HTML from the project's own source: the upload screen, the result view, the dashboard
with plausible content. Use the brand's exact colours and fonts. Anything sequential (cards arriving, text
typing, a cursor clicking) is written into the storyboard as an explicit action so it can be animated and
timed.

Audio, only when the user supplied a licensed track: use `npx hyperframes beats` to find beats, use them for
accents and sequential reveals (not for readable text), keep the track quieter than any voice, and fade in and
out. Without a track, deliver silent and say so. Narration is out of scope for this version.

Gate before rendering:

```bash
cd <output-dir>/composition
npx hyperframes check           # lint, runtime validation and layout in one gate; fix every error
npx hyperframes snapshot        # key frames as PNG: open them and look
```

Fix every error, including contrast failures. Open the snapshots and look at them yourself.

## Step 5: Render and deliver

Follow `references/delivery.md`: preview, render, pick a **settled** poster frame (never a fade or a
mid-transition), bake the poster in as frame 0 so every platform's idle thumbnail is the poster, write one
caption in `share-copy.txt`, and report where the files are.

Run `ai-content-cleaner` in CLEAN mode on the on-screen text and the caption, then `brand-review` on
anything that makes a claim. Both come before delivery.

## Output

1. The video type chosen and the assumptions made.
2. `video-plan.md` (plan and storyboard).
3. `composition/` (the HTML project) and the render, `video.mp4`, when rendering worked.
4. The poster `video.jpg` and `share-copy.txt`.
5. Open items: claims needing a source, stand-in data used, audio not licensed, anything not rendered.

Keep chat framing short. The files carry the work.

## Rules

- Never invent product facts, figures, customers or testimonials.
- Never put secrets or personal data on screen.
- Never bundle or fetch audio without a clear licence. Never redraw the brand's logo.
- No em dashes in any on-screen text or caption.
- Do not overwrite earlier runs. Use a new timestamped output folder when one already exists.
- Say what you did not test. If you could not render, say so.

## Related Skills

- `[brand]-brand-kit`: loaded first for voice, colour, type and logo rules.
- `logo-design`: produces the mark used by the logo sting and the outro.
- `creative-brief`: campaign art direction and the deliverables table this video belongs to.
- `ad-creative-matrix`: paid video ads. Its video hooks (spoken line, on-screen text, first shot) can feed
  the first 3 seconds of a teaser.
- `figma-weavy-workflow`: generated or composited imagery, not time-based video.
- `brand-review`, `ai-content-cleaner`: the gates before delivery.
- `social-content-writer`: organic posts that carry the finished video.
