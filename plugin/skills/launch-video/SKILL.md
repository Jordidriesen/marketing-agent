---
name: launch-video
metadata:
  version: 1.2.0
  history: 'v1.2.0: the script, storyboard and frames come from video-script-storyboard, approved before the build; Step 2 works without a code repo (live site through the browser, screenshots, PDFs, a design system artifact); a locale step for multi-market brands; an ffmpeg fallback render when Hyperframes is not available; the description states the real length range; the poster bake uses a fast preset for drafts. v1.1.0: the HyperFrames by HeyGen connector is the first route when it is connected, the npx CLI stays the fallback; generated live-action clips are pointed to Canva create-video or a Weave video model. v1.0.1: required skill calls stated up front; the follow-up skills are called through the Skill tool, never imitated inline. v1.0.0: new skill. An original workflow for short product and brand videos (teaser, continuous-take feature demo, logo sting), written in this library''s terms with the brand kit as the source of voice, colour and type. Structure and several rules (project inspection rubric, reading-time floors, poster frame as frame 0, share copy) are adapted from latent-spaces/brag (MIT, see LICENSE-brag.txt). The continuous-take idea is inspired by feitangyuan/onetake, which is licensed PolyForm Noncommercial and is therefore neither bundled nor copied. No audio files are bundled.

    '
description: Plans and builds a 3 to 40 second product teaser, continuous-take feature demo or logo sting from the product's real screens, site or brand kit, from an approved storyboard. Use for "launch video", "product teaser", "logo animation".
argument-hint: <what to show, video type if known, format (landscape, vertical, square), duration, tone, brand>
---

# Launch video

You make short videos that show a real product doing a real thing, in the brand's own voice. The
video is built from the product's actual screens, copy and claims, so it could not belong to any other
company. If a scene could be swapped into a competitor's video unchanged, rewrite it.

**Required skill calls.** Before building, call `video-script-storyboard` for the storyboard and frames (Step 3). After drafting, call `ai-content-cleaner` and `brand-review` through the Skill tool, in that order, and never imitate them with an inline edit. A reply that skips either is not finished. End the reply with one line: `Skills run: ...`.

## What to state up front

- **Two ways to render.** First choice: the HyperFrames by HeyGen connector, when it is connected
  in the session. Load its tools and read the names before the first call; never guess one, and treat
  any export or share as a step that needs a yes. Fallback: the Hyperframes CLI (`npx hyperframes`,
  Apache-2.0, needs Node 22 and FFmpeg). Check it works with `npx hyperframes doctor` before promising a
  file. If neither works, use the fallback in `references/delivery.md` (each scene's HTML screenshotted
  and assembled with ffmpeg, as in `video-making` when it is listed), and say the motion is simpler than a
  Hyperframes render. If that fails too, deliver the board and the composition source and say a render is
  still to be done.
- **Not this skill:** a generated live-action clip (a product in a scene, a presenter) goes through
  Canva's `create-video` route in `canva-workflow` or a Weave video model in `figma-weavy-workflow`.
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

Use the best source the job has, in this order, and say which you used:

1. **A local project** (the product's code in a linked folder): the main page (`index.html` or the main
   route) for headline, tagline, CTA and claims; the stylesheet for colour properties and fonts;
   `README.md` and `package.json` for the name and one-liner; routes, components and state steps for the
   **user flow**; `public/` or `assets/` for logos and icons. Skip build output, lock files, tests,
   `.git`, `.env*`, keys and credentials.
2. **The live site or app**, through the browser: read the page text, take screenshots at the output size
   of the screens the video will show, and read the computed colours and fonts. Log-in areas only with the
   user's go-ahead and never with real customer data on screen.
3. **Supplied material**: screenshots, screen recordings, product brochures or datasheets (PDF), a deck.
4. **The brand's design system artifact or brand kit** for tokens when there is no product UI to read.

A brand with no software product (a contractor, a club, a physical product) has no user flow: the
strongest material is the real work, the place, the product, from the user's own photos or footage. Say
so and plan around it rather than inventing UI.

**Nothing secret leaves this step.** Anything read can end up on screen in a public video. Never carry
secrets, tokens, internal hostnames, real customer names, email addresses or personal data into the plan,
the composition, the render or the caption. Substitute plausible fictional stand-ins and say so in the plan.

Then answer in writing: what the product is, the one claim or moment that earns a reaction, what real UI
should be shown, the shortest satisfying length, the tone, the audio posture (including "silent"), the
draft caption, and the 2 or 3 beats of the user flow. If there is no app, only a landing page, say so and use
the strongest visual instead.

## Step 3: Plan, storyboard and frames

Run `video-script-storyboard` through the Skill tool, with the video type, the format, the target length
and the Step 2 answers. It writes the on-screen text (or the A/V script when there is a voice-over), the
storyboard and one frame per scene, and holds the approval checkpoint. Use this skill's
`references/storyboard.md` as the storyboard template inside it, and keep `video-plan.md` in the output
folder (angle, hook, beats, outro, visual identity with exact values, scenes with durations, on-screen
text, real material, transitions). When the user brings an already approved board, skip to Step 4 and
build from it.

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

**Checkpoint.** The board with its frames is approved before building (held by
`video-script-storyboard`). A frame is cheap to change and a composition is not. Skip the pause only if
the user said not to check in.

**Locales.** For a brand that runs several language markets, ask which locales are needed. Translate the
on-screen text with `content-translate` after the source board is approved, recheck every reading floor in
each locale (German and French often run about 30% longer), and lengthen the scene in every locale or cut
words in that locale; never speed the text up. One render per locale, named `video.<locale>.mp4`.

## Step 4: Build the composition

Hand a focused composition brief to Hyperframes. Your plan owns the angle, the source material, the
storyboard, the tone and the delivery. Hyperframes owns the animation mechanics and structure.

```bash
npx hyperframes doctor          # confirm Node, FFmpeg and Chrome are present
npx hyperframes init            # scaffold the composition inside <output-dir>/composition/
npx hyperframes docs            # read its current guidance before writing the composition
```

If Hyperframes' own agent skills are installed in the session, read them before composing. Build each scene from its approved frame. Recreate real
product moments in HTML from the project's own source or the screenshots: the upload screen, the result view, the dashboard
with plausible content. Use the brand's exact colours and fonts. Anything sequential (cards arriving, text
typing, a cursor clicking) is written into the storyboard as an explicit action so it can be animated and
timed.

Audio, only when the user supplied a licensed track: use `npx hyperframes beats` to find beats, use them for
accents and sequential reveals (not for readable text), keep the track quieter than any voice, and fade in and
out. Without a track, deliver silent and say so. A voice-over follows the A/V script from `video-script-storyboard`; it is recorded by the user or a licensed voice they choose, never synthesised from a real person's voice, and the subtitles come from `video-finishing`.

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
2. The approved board from `video-script-storyboard` and `video-plan.md` (plan and storyboard).
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
- `video-script-storyboard`: the script, storyboard, frames and approval checkpoint this skill builds from.
- `video-finishing`: subtitles, loudness, vertical and square cut-downs and platform exports of the render.
- `content-translate`: locale versions of the on-screen text.
- `figma-weavy-workflow`: generated or composited imagery and generated clips, not built motion.
- `brand-review`, `ai-content-cleaner`: the gates before delivery.
- `social-content-writer`: organic posts that carry the finished video.
