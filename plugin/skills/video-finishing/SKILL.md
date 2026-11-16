---
name: video-finishing
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Finishing for footage the user supplies or a render that already exists: subtitles, loudness, trims, cut-downs, reframes to 9:16 and 1:1, Shorts from long-form, platform exports and poster frames, with ffmpeg on a copy and never on the original."
description: 'Finishes existing video: subtitles (SRT and burnt-in), loudness normalisation, trims, cut-downs, reframes to 9:16 and 1:1, Shorts or Reels cut from a long-form video, platform exports, poster frames. Works on a copy with ffmpeg. Use for "add subtitles", "cut this into Shorts", "make a vertical version", "fix the audio levels", "export for LinkedIn". New videos: launch-video.'
argument-hint: <the video file(s), what to produce, platforms, language of the speech, transcript if there is one>
---

# Video finishing

You take a video that already exists (the user's own footage, an edit they exported, a render from
`launch-video`) and make it ready for the places it will run. You never touch the original file.

**Required skill calls.** Burnt-in text, subtitle files and captions are reader-facing: run
`ai-content-cleaner` (CLEAN) on any text you wrote (titles, captions, lower thirds), never on the
speaker's transcribed words, which stay verbatim apart from obvious transcription errors. Run `brand-review`
on anything that makes a claim. End the reply with one line: `Skills run: ...`.

## Step 0: Get the files and look at them

- Files on the user's computer: with a device shell, work there next to the source in a new
  `finished/` folder; otherwise stage them into the workspace. Uploaded files: copy them into the working
  directory first. Large files: say how big they are before moving them.
- Probe every input: `ffprobe -v error -show_entries format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels -of default=nw=1 input.mp4`.
- Extract a few frames (`ffmpeg -ss <t> -i input.mp4 -frames:v 1 frame-<t>.jpg`) at the start, middle and
  end, and look at them: framing, where the subject sits, burnt-in text already present.
- Load the `[brand]-brand-kit` for caption styling (`references/design.md`) and any on-screen wording
  (`references/voice.md`).

Ask only what changes the work: which platforms, and for a cut-down, which moments if the user has a view.

## Step 1: Pick the jobs

| Job | Reference |
|---|---|
| Subtitles: SRT file, burnt-in captions, or both | `references/subtitles.md` |
| Loudness and audio clean-up | `references/ffmpeg-recipes.md` (Loudness) |
| Trim, cut out a section, join clips | `references/ffmpeg-recipes.md` (Cutting) |
| Reframe to 9:16 or 1:1 | `references/ffmpeg-recipes.md` (Reframing) |
| Shorts or Reels from a long-form video | Step 2 below, then the recipes |
| Platform exports and poster frame | `references/ffmpeg-recipes.md` (Exports) |

## Step 2: Shorts and cut-downs from long-form

1. Get a transcript with timestamps (see `references/subtitles.md`).
2. Propose 3 to 5 candidate moments in a table: start, end, length, the hook line it opens with, why it
   stands on its own, and the frame where it starts. A good moment opens on a claim, a question or a
   result, needs no earlier context, and ends on a landed line, not mid-thought.
3. Wait for the user to pick, unless they said to choose.
4. Cut each, reframe to 9:16 (check the subject stays in frame across the whole clip: extract a frame
   every few seconds and look), add burnt-in captions, normalise loudness, export.

Check each platform's current maximum length for Shorts and Reels before promising a length; it changes.

## Step 3: Render

- Work on copies; write each output to a temporary name ending in `.mp4` and rename it when ffmpeg exits 0.
- Drafts: `-preset veryfast`. Final delivery: `-preset slow` only when the user asked for best quality.
- Do not re-encode what does not change: trims on keyframes and audio-only fixes can use `-c:v copy`.
- After every render, probe the result (duration, size, streams) and look at a frame from each output.

## Step 4: Deliver

```
finished/
  [name]-16x9.mp4, [name]-9x16.mp4, [name]-1x1.mp4   what was asked for
  [name].srt (and [name].[locale].srt)               subtitle files
  [name]-poster.jpg                                  a settled frame
  finishing-notes.md                                 what was done, settings, open items
```

Say where the files are, what changed, and what was not checked (for example the subtitles were not
proofread by someone who knows the speaker's terms).

## Rules

- Never modify or overwrite the original. Never delete anything.
- Never upload footage or audio to a third-party service (transcription, AI editing) without a yes for
  that service.
- The speaker's words are theirs: no rewording in subtitles beyond fixing clear transcription errors.
- No em dashes in any text you add. No black text on an orange background in captions or titles.
- Music only when the user supplied it and is licensed to use it.

## Related Skills

- `launch-video`: builds new short videos; its render can come here for exports and cut-downs.
- `video-script-storyboard`: the shot list marks the vertical cut before filming.
- `content-translate`: translated subtitle files.
- `social-content-writer`: the posts that carry each cut.
- `ai-content-cleaner`, `brand-review`: the gates on added text.
