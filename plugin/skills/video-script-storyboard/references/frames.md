# Storyboard frames

A frame is a picture of a scene at its most important settled moment: what the viewer sees when the
scene's text is fully in. One per scene. Frames exist to be approved, so they show composition, text and
source, not finished polish.

## Sizes

| Format | Sketch (SVG viewBox) | Styled keyframe (PNG) |
|---|---|---|
| Landscape 16:9 | 0 0 1600 900 | 1920x1080 |
| Vertical 9:16 | 0 0 900 1600 | 1080x1920 |
| Square 1:1 | 0 0 1200 1200 | 1080x1080 |

## Level 1: thumbnail sketches

- SVG, greyscale on the brand's background colour, plus at most the brand's one accent colour.
- Subject as simple shapes: a head-and-shoulders silhouette for a presenter, a rounded rectangle for a
  screen, a bottle or watch outline for a product. Label each shape in small text.
- On-screen text set in the brand's display font (or a system fallback, said in the board) at roughly the
  real size, so the amount of text is honest.
- A dashed safe-area guide and, for a planned vertical cut, a dashed 9:16 crop box.
- Scene number and duration in a corner, outside the safe area.

Render to PNG for the board: `rsvg-convert -w 1600 scene-01.svg -o scene-01.png`, or headless Chrome
when `rsvg-convert` is missing. Install what is missing; say so if nothing works and deliver the SVGs.

## Level 2: styled keyframes

- HTML at the full output size, using the brand kit's colour and type tokens exactly, screenshotted with
  headless Chrome (or Playwright) at device scale 1.
- Real material only: screenshots of the real product or site (taken in the browser), the user's own photos,
  the approved logo file as supplied. Never redraw a logo.
- Stand-in data (names, figures) is plausible, fictional and marked in the board.
- When the scene will be built in Hyperframes, write the keyframe as the scene's settled state, so
  `launch-video` can reuse the markup.

## Level 3: generated keyframes

- Only on request, or for a live-action concept that cannot be sketched usefully.
- Through `figma-weavy-workflow` (Route B, one model) or Canva `generate-image`. Quote the credit cost and
  wait for a yes before the first run. Brand assets and text go on afterwards as real layers.
- Never generate a frame that could pass as the brand's real product, a real person, a real customer or
  the user's own photos or belongings. Label every generated frame `concept, generated`.

## Check every frame

Open each PNG and look at it:

- Text readable at phone size (scale the frame to about 360 px wide and still read it).
- Contrast meets WCAG AA for the text size. No black text on an orange background.
- Text and key UI inside the safe area.
- Nothing secret, personal or invented on screen.
- No em dashes in any text.

## Contact sheet

For a quick overview next to the board, tile the frames:

```bash
ffmpeg -y -pattern_type glob -i 'frames/scene-*.png' -vf "scale=480:-1,tile=4x3:padding=12:margin=12:color=white" -frames:v 1 frames/contact-sheet.png
```

Adjust the tile grid to the number of scenes.
