# Video types

Three types. Each has a structure, rules and a failure mode. Pick one per video.

## 1. Launch teaser (15 to 25 seconds)

**Shape:** hook (2 to 3 s), reveal (2 to 4 s), two or three sharp highlights (5 to 12 s), punchline and
outro (2 to 4 s). Adapt it: not every product needs three highlights.

- **Hook:** one word, image or motion that earns the next 20 seconds, readable with the sound off. Plan it
  before anything else.
- **Highlights:** specific moments from the product, never "feature callouts". "The altitude meter counting
  up" beats "real-time analytics".
- **Centrepiece:** when the product has a flow, the middle scenes show that flow (entry, key action,
  result), not landing-page sections. At most one stat card or headline block, used as a frame around the
  flow and not as a substitute for it.
- **Outro:** the product name, then the line the brand would actually say. The last beat before the logo
  should land.

**Failure modes:** a diagram of what the product does instead of the product doing it; three stat cards
copied from the social-proof row; generic motion that could belong to any video.

## 2. Continuous-take demo (15 to 40 seconds)

**Idea:** the whole video feels like one unbroken move through the product. Every beat grows out of the
one before: an element that ends one beat becomes the thing that starts the next, so the viewer's eye
never has to reset. The boundary between two beats is the thing you design, not the beats themselves.

The idea is inspired by the `onetake` skill (feitangyuan/onetake), which is not bundled and not copied
because its licence (PolyForm Noncommercial) does not allow commercial use. Everything below is this
library's own wording of the principle.

**Method:**
1. Write the flow as 3 to 6 beats (entry, steps, result).
2. For each boundary between beats, name the **carry**: the one element that stays on screen and changes
   role (a card that becomes a panel, a cursor that becomes the next click target, a number that becomes the
   next headline). A boundary with no carry is a cut: either design one or accept the cut and say why.
3. Keep one camera idea for the whole video (a steady push, a pan along the flow, a zoom into detail and
   back). Do not mix camera ideas.
4. Hold between moves. Stillness is part of the rhythm: motion, then a settled hold long enough to read,
   then the next move.

**Failure modes:** a stack of scenes joined by crossfades and described as "continuous"; a carry that
changes meaning (a card that was a customer becomes a price); constant motion with no holds, so nothing can
be read.

## 3. Logo sting (3 to 8 seconds)

**Shape:** build or resolve the mark (1 to 3 s), hold the finished lockup (about 1.5 s or more), optional
tagline.

- Use the approved SVG from `logo-design` or the brand kit exactly as supplied. Animate the supplied
  shapes; never redraw them.
- The mark ends in its resting state with clear space as specified in the guidelines.
- If the brand has a one-colour or reversed version, the sting uses the one that fits the background it
  will sit on.

**Failure modes:** effects that outlast the mark (glows, particles) so the logo never settles; a hold so
short that the logo cannot be read; a tagline that is not the brand's locked line.

## Choosing between types

| The user says | Type |
|---|---|
| "announce the launch", "teaser", "something to post" | Launch teaser |
| "show how it works", "walk through the feature", "demo video" | Continuous-take demo |
| "animate our logo", "intro", "logo reveal" | Logo sting |
| "make a video" and nothing else | Launch teaser, and say so |

## Formats

| Format | Size | Use |
|---|---|---|
| Landscape | 1920x1080 | Websites, YouTube, LinkedIn feed |
| Vertical | 1080x1920 | Reels, Shorts, TikTok, stories |
| Square | 1080x1080 | Feed posts |

Keep titles and key UI inside the safe area of the format. Platform interface overlays differ and change,
so check the platform's current specification before relying on a particular margin.
