# Render and deliver

Commands come from the Hyperframes CLI (`hyperframes` on npm, version 0.8.x when this was written). Flags
change between versions: run `npx hyperframes <command> --help` and use what it reports.

## Validate

```bash
cd <output-dir>/composition
npx hyperframes check       # lint, runtime validation and layout in one gate
npx hyperframes snapshot    # key frames as PNG
```

Fix every error `check` reports, including contrast failures. Open the snapshots and look at them.

## Preview

```bash
npx hyperframes preview
```

Tell the user the preview is running and give them the local address. Invite them to check it before the
final render.

## Render

```bash
npx hyperframes render --output ../video.mp4
```

Use a draft quality for iteration and a high quality for final delivery. The available quality flags are
listed by `npx hyperframes render --help`.

## Pick the poster frame

The poster is the still shown before the video plays. Never leave it to the raw first frame, which often
lands on a fade or a blank intro. You built the composition, so you know its strongest moment: the hook
line, the hero reveal or the final logo. Choose that beat at a **settled** point (text fully in, not yet
leaving) and extract it:

```bash
ffmpeg -ss 3.2 -i ../video.mp4 -frames:v 1 -q:v 2 ../video.jpg
```

Use the timestamp of your strongest settled beat. If the frame lands mid-transition, nudge it by a few
tenths of a second. Look at the frame: it should be postable on its own.

### Bake the poster in as frame 0

Slack, X, Discord and most players show frame 0 as the idle thumbnail and ignore cover-art metadata.
Replace only the first frame with the poster, leaving timing and audio untouched:

```bash
ffmpeg -y -i video.mp4 -i video.jpg \
  -filter_complex "[0:v][1:v]overlay=0:0:enable='eq(n,0)'[v]" \
  -map "[v]" -map "0:a?" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
  -c:a copy -movflags +faststart video.poster.mp4 && mv video.poster.mp4 video.mp4
```

Keep `video.jpg`: it is the custom thumbnail for platforms that accept an upload and the `poster` image for
any `<video>` embed. This technique is adapted from the `brag` project. Check the result plays and has the
same duration before replacing the original.

## Caption

Write `share-copy.txt`: one to three sentences, specific to the product, in the brand's voice from the kit,
postable as is. No "excited to share". Variants for other platforms go in a separate
`share-copy-variants.md`. Run `ai-content-cleaner` and `brand-review` on it.

## Output folder

```
<output-dir>/
  video.mp4              the render (poster baked in as frame 0)
  video.jpg              the poster
  video-plan.md          plan and storyboard
  share-copy.txt         the caption
  composition/           the Hyperframes project
```

Use `video-output/` by default and a timestamped folder (`video-output-YYYY-MM-DD-HHmmss/`) when one
already exists, so earlier runs are never overwritten.

## Telling the user

Say where the video, the poster and the caption are, in one sentence what the video does creatively, and
what was not tested or not licensed. Offer one next step: re-roll a scene, change the tone, or build a
vertical cut.
