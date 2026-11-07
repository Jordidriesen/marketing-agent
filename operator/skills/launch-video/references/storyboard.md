# Plan and storyboard template

`video-plan.md`: one focused page, the creative reference for the whole video. It says what the video must
communicate and what product material must be used. It does not prescribe animation code.

```markdown
# Video plan: [Product name]

## Type, format, duration
[Launch teaser / Continuous-take demo / Logo sting]. [Landscape / vertical / square], [width]x[height]. [N] seconds.

## What is this?
[One sentence: what it does and what makes it worth showing.]

## The angle
[The creative premise. What makes this video specific to this product.]

## Hook (first 2 to 3 seconds)
[The opening moment. Works with the sound off.]

## User flow worth showing
[Entry, key action, result. Or "none, landing page only".]

## Key moments
[2 or 3 specific moments from the product, as bullets.]

## Outro
[The final line and the beat before the logo.]

## Tone
- Direction: [from the brand kit's voice; one sentence]
- Pacing: [from the table below]

## Visual identity (exact values)
- Background / Accent / Text: [values from the brand kit or the product's CSS]
- Display font / Body font: [names, and whether the licence allows video use]
- Logo file: [path, or none]
- Strongest visual element from the product: [what]

## Stand-in data used
[Any fictional names, figures or content substituted for real ones.]

## Audio
[Silent / user-supplied licensed track: name and licence / none.] Role and intensity in one line.

## Caption (draft)
[One to three sentences, postable as is.]

## Storyboard

### Scene 1: [name] ([duration] s)
On screen: [what appears, the exact text, the product material used]
Action: [sequential reveal, simulated click or swipe, typed text, or none]
Reading time check: [words or labels, and the floor they need]
Carry or transition into scene 2: [the carried element, or the cut type]

### Scene 2 ...

Total: [sum] s. Target: [N] s.
```

## Tone and pacing

Tone comes from the brand kit's voice. These pacing shapes are starting points.

| Tone | Scenes | Pacing and feel |
|---|---|---|
| Polished, premium | 3 to 4 | Long holds, slow crossfades or slides, confidence through restraint |
| Playful | 4 to 5 | Comfortable rhythm, short punchy phrases, clean wipes |
| Deadpan | 3 to 4 | Very long holds, empty space, one idea at a time |
| Cinematic | 4 to 5 | Big type, wide framing, dramatic reveals |
| Clean product (app-store feel) | 4 to 6 | Feature cards, smooth slides, no mess |
| Urgent, high energy | 6 to 8 | Fast cuts, some scenes under 2 s. Only where the brand voice supports it |

Presets are defaults. A specific direction from the user ("quiet premium film") refines or overrides them.
A B2B or regulated brand defaults to polished or clean product unless its kit says otherwise.

## Reading time

- Short label or 1 to 3 word line: about 0.8 s settled (fully in, not yet leaving).
- Headline or sentence: about 0.3 s per word, minimum about 1.2 s. The hook line gets the most.
- Entrances and transitions stay snappy (about 0.3 to 0.6 s). A line can slam in and then hold.
- A 4 s scene carries roughly two or three short reads, not six.
- Sequential text snapped to a fast beat is too quick to read: hold each item to the floor, or reveal them
  quickly and hold the full set afterwards.

These are working rules from the `brag` project, not measured reading speeds. Check them against the real
frames.

## What to show, in order of preference

1. A recreated working-app moment from the real source.
2. A recreated UI element in HTML (a card, a meter, a stat block).
3. The core concept animated, grounded in the product's idea.
4. A text-forward sequence, when the copy is the product.

Never fill scenes with abstract patterns or generic motion.
