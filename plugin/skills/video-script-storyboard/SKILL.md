---
name: video-script-storyboard
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. One script, storyboard, shot list and frames workflow shared by launch-video, the YouTube skills and any filmed or voiced video, so a video is approved as pictures and words before anything is built, filmed or rendered."
description: 'Writes the script (spoken or two-column A/V), storyboard, shot list and storyboard frames for any video before it is built, filmed or rendered, with an approval checkpoint on the frames. Use for "video script", "voice-over script", "storyboard", "shot list", "storyboard frames", "keyframes", "what do I film". Builds: launch-video, canva-workflow, figma-weavy-workflow. Own footage: video-finishing.'
argument-hint: <video goal, audience, length, format (landscape, vertical, square), filmed or built, brand, frame level if known>
---

# Video script and storyboard

You decide what a video says and shows before anyone spends time building, filming or rendering it.
The output is approved as words and pictures, scene by scene, so a change costs a line of text, not a
re-render or a reshoot.

**Required skill calls.** After drafting, call `ai-content-cleaner` (CLEAN) on every spoken line and
every on-screen text, then `brand-review` on anything that makes a claim, through the Skill tool, in that
order. Never imitate either inline. End the reply with one line: `Skills run: ...`.

## Step 0: Load the brand and the context

Load the `[brand]-brand-kit` skill: `references/voice.md` for tone and locked terms,
`references/design.md` for colour, type and logo rules (frames use these exact values),
`references/context.md` for audience and channels, and `references/youtube-channel.md` when the video is
for the brand's channel. With no kit, say so and ask for the brand basics or work from the site's own CSS.

Collect, or ask for in one **Needs input** block when missing: the goal (one sentence), the audience, the
one message, the length, the format, where it will run, and the source material (product screens, a
page, a brief, notes, an approved script from `youtube-script`). Never invent a product fact, a figure, a
customer or a quote. A gap is marked `[NEEDS SOURCE]`.

## Step 1: Pick what this video needs

| The video is | Script form | Storyboard | Default frames |
|---|---|---|---|
| Face on camera (YouTube long-form, a Short, a LinkedIn talking head) | Spoken script | Shot list first, storyboard per section | Thumbnail sketches |
| Voice-over over footage, screens or motion (client explainer, demo with narration) | Two-column A/V script | Full storyboard | Styled keyframes |
| Built motion with on-screen text only (teaser, logo sting) | On-screen text list, inside the storyboard | Full storyboard (the `launch-video` template) | Styled keyframes |
| Generated live-action concept (Canva or Weave video) | A/V script | Full storyboard | Generated keyframes, gated |
| Paid video ad | Hook, body, CTA from `ad-creative-matrix`, as an A/V script | Full storyboard | Styled keyframes |

Say which row you chose. The user can override the frame level. Personal-brand work defaults to sketches,
client work to styled keyframes.

## Step 2: Write the script

Follow `references/script-formats.md`.

- **Spoken script.** Written to be said, not read: contractions, short sentences, one idea per sentence.
  Hook in the first 5 seconds, then the promise, re-hooks at each section change, the payoff, one CTA.
  Read every line aloud in your head; rewrite anything you would stumble over. For a YouTube script, when
  the vidIQ connector is connected, call `vidiq_before_scripts_outlines_and_edits` first with the user's
  request verbatim and follow its guidance, and check the length with `vidiq_before_stating_script_length`
  before stating a runtime. Without vidIQ, count words and use 150 words per minute, and say so.
- **Two-column A/V script.** One row per beat: time, visual (left), audio (right: voice-over, on-screen
  text, music or SFX cue). Every visual names its source material. Every row fits its time: about 2.5 spoken
  words per second, and the on-screen text reading floors in `references/script-formats.md`.
- **On-screen text only.** Every line carries its reading-time check.

Timings must sum to the target length. Count them.

## Step 3: Storyboard and shot list

Follow `references/storyboard-and-shots.md`. One entry per scene: number, duration, shot type, framing,
camera move, what is on screen, the script line or text it carries, the transition and the source
material. For anything filmed, also write the shot list: grouped by location and set-up (not by script
order) so it can be filmed in the fewest set-ups, with B-roll, cutaways and pick-ups listed, and the
vertical cut marked when a Short or Reel will be cut from it.

## Step 4: Draw the frames

Follow `references/frames.md`. One frame per scene, drawn before the checkpoint.

- **Thumbnail sketches** (default for own-brand work): SVG frames at the output aspect ratio, greyscale
  plus the one accent, showing subject position, text position and the platform safe area. No credits.
- **Styled keyframes** (default for client work): frames at full output size in the brand's real colours
  and type, with real screenshots or photos where the scene uses them, and the exact on-screen text.
- **Generated keyframes** (on request or for live-action concepts): images through `figma-weavy-workflow`
  or Canva `generate-image`. Quote the credit cost and wait for a yes before the first run. Never generate
  anything that could pass as the brand's real product, a real person or the user's own photos; mark every
  generated frame `concept, generated`.

Render each frame to PNG, look at every one yourself, and fix anything off-brand, unreadable or outside the
safe area before showing it.

## Step 5: The board and the checkpoint

Put it together on one board: per scene the frame, the script line or A/V row, duration and notes. Publish
it as a Docs artifact when the session offers the Docs type (frames as images, one section per scene), so
the user or a client can comment scene by scene; otherwise as one self-contained HTML page, or as
`storyboard.md` plus a `frames/` folder.

**Checkpoint.** Show the board and wait for approval before anything is built, filmed, generated or
rendered. Skip the pause only when the user said not to check in. Record approved changes in the board, not
only in the chat.

## Step 6: Hand over

Write to a new output folder (`video-board/`, or `video-board-YYYY-MM-DD-HHmmss/` when one exists):

```
video-board/
  script.md             spoken or A/V script, with timings
  storyboard.md         scenes, shots, transitions, sources
  shot-list.md          only for filmed work
  frames/scene-01.png   one per scene
  board.html            when no Docs artifact was made
```

Then hand off: `launch-video` builds from the approved board (it skips its own Step 3), Canva
`create-video` or a Weave video model takes the A/V rows as the production spec, a filmed video goes to the
shoot with `shot-list.md` and later to `video-finishing`. For a localised version, run `content-translate`
on `script.md` and recheck every timing in the target language; German and French often run about 30%
longer and break the reading floors.

## Output

1. The row chosen in Step 1 and the assumptions made.
2. The board (link or path), with the script, storyboard, shot list where filmed, and frames.
3. Open items: `[NEEDS SOURCE]` claims, stand-in data, frames not drawn, length not verified with vidIQ.

## Rules

- Never invent product facts, figures, customers, quotes or personal experiences. The user's own opinions
  and anecdotes come from their notes.
- Never put secrets, real customer names or personal data in a frame or a line.
- No em dashes in any script line, on-screen text or frame.
- No black text on an orange background in any frame.
- Do not overwrite earlier boards.

## Related Skills

- `[brand]-brand-kit`: voice, design tokens and the channel profile.
- `launch-video`: builds teasers, demos and stings from the approved board.
- `youtube-script` (personal-content plugin): the full YouTube script, which this skill turns into a shot
  list and board.
- `ad-creative-matrix`: the winning hooks, bodies and CTAs for a video ad.
- `canva-workflow`, `figma-weavy-workflow`: generated video and generated keyframes.
- `video-finishing`: subtitles, loudness, cut-downs and reframes once footage exists.
- `content-translate`: locale versions of the script.
- `ai-content-cleaner`, `brand-review`: the gates before the checkpoint.
