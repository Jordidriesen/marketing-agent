---
name: creative-brief
metadata:
  version: 1.2.0
  history: >
    Built for the marketing plugin's creative-specialist agent. Structures
    a brief plus a deliverables table with real format/dimension specs,
    loads the brand kit for visual direction, and hands off to
    canva-workflow or figma-weavy-workflow for production. v1.1 adds an
    accessibility section (contrast, min sizes, alt text, localisation
    text expansion).
description: "Writes a creative brief: concept, art direction, mood, do and don't, and an asset table with formats and sizes. Use for \"creative brief\", \"art direction\", \"moodboard\", before design production."
argument-hint: "<what needs designing, and for which campaign or brand>"
---

# Creative Brief

You give a designer, or a design tool, enough to start without a second meeting. A brief that says "make it modern and clean" is not direction. Every line below should be specific enough that two different people would produce recognisably the same thing.

## Step 0: Load the brand's visual identity

Determine which brand or client this is for and load the matching `[brand]-brand-kit` skill.

- **Has visual guidelines** (palette, type, imagery style, logo rules, grid): quote the actual tokens in every section below. Not "brand blue" but the hex; not "our font" but the family and weight.
- **Voice-only so far**: say so, work from any style guide, template or approved asset you were given, and keep direction conservative. Note that adding visual identity to the brand kit is worth doing.
- **Source files exist** (style guide PDF, moodboard, prior assets): read them and derive direction from what is there, not from general taste.

## The brief

Use this structure. Keep it tight; this is a launchpad, not a document.

### 1. The ask
One sentence: what is being made, for what, by when.

### 2. Objective
What the creative has to achieve, tied to the campaign goal. "Stop the scroll and get a click to the launch page," not "raise awareness."

### 3. Audience
Who sees this and in what context (feed, inbox, print, event screen). Their state of mind at that moment matters more than demographics.

### 4. The one message
The single idea the visual must land, in the viewer's terms. Everything in the design serves this. If there are three messages, there are three assets.

### 5. Art direction
- **Concept**: the visual idea in one or two sentences. What is the hero element, what is the visual metaphor if any.
- **Style**: photography / illustration / 3D / type-led / data-led. Reference 2–3 existing pieces (links or named examples) that are close to the target.
- **Composition**: focal point, reading order, where the logo and CTA sit, how much breathing room.
- **Colour**: which brand tokens, in what roles (ground, accent, text). Note any deliberate deviation and why.
- **Typography**: which brand faces, which weights, hierarchy from headline to caption.
- **Imagery**: subject, treatment, crop, what to avoid.
- **Motion** (if any): what moves, how long, whether reduced-motion needs a static fallback.

### 6. Do and don't
A short bulleted list of the specific traps for this brand and this asset. Pulled from the brand kit's banned/required list where one exists.

### 6b. Accessibility
State the non-negotiables: minimum text/background contrast (4.5:1 for body, 3:1 for large text), minimum on-asset font size for the channel, no meaning carried by colour alone, and the alt text for each image deliverable. Localised versions: note where translated copy runs ~30% longer (German, French) and the layout has to breathe for it.

### 7. Deliverables
A table, one row per asset:

| Asset | Channel / use | Format | Dimensions | Safe area / notes | Copy source |
|---|---|---|---|---|---|

Fill real numbers. Common ones: LinkedIn feed image 1200×627, LinkedIn carousel 1080×1080 (or 1080×1350), Instagram feed 1080×1350, IG story/Reel 1080×1920, X post 1600×900, YouTube thumbnail 1280×720, email hero 600px wide (2×), OG image 1200×630, A4 print 210×297mm at 300dpi. If the platform's current spec differs, use the current spec and say so.

### 8. Copy
Exact text that appears in each asset, headline, sub, CTA, taken verbatim from the approved `content-writer` or `social-media-specialist` piece, or written here and flagged for `brand-review`.

### 9. Production route
For each deliverable, which tool and skill: `canva-workflow` for template-based and bulk assets, `figma-weavy-workflow` for generated or composited imagery and design-system components, the Adobe for creativity connector for edits to existing images (background removal with `image_remove_background`, crop and resize to each format with `image_crop_and_resize`, tone correction with `image_apply_auto_tone`), PDF work (for example `pdf_to_markdown` to read a client's brand guideline) and font sourcing (`font_search`, `font_recommend`) when the brand kit leaves type open. Canva stays the default for template work; Adobe Express is used only when the user asks for it. Edits to real photos stay edits: no generative fill or expand on a photo of the client's actual product, people or projects.

## Related Skills

Hand the finished brief to `canva-workflow` or `figma-weavy-workflow` for the build steps. If the creative needs new copy, that comes from `content-writer` or `social-media-specialist` first (for paid social and video ads, `ad-creative-matrix` supplies the winning hooks, bodies and CTAs to brief against), and any copy written into a layout passes `brand-review`. For the campaign context this creative serves, see `campaign-plan`.

## Output

Present the brief with the numbered headings above. The deliverables table is the part people act on: make it complete. No mood-setting prose; if a section would just be adjectives, cut it and add a reference instead.

Conciseness note: any chat framing around this deliverable stays short, a sentence or two. It never applies to the deliverable itself, which is produced at the full length and detail the structure above requires.
