---
name: logo-design
metadata:
  version: '1.0.0'
  history: "v1.0.0: adapted from kaankiziltug/logo-design-skill (MIT, see LICENSE-logo-design-skill.txt). Kept the process, references and dependency-free scripts. Removed the 1,400-logo reference library (its logos are third-party trademarks outside the MIT grant) and every script and instruction that depended on it. Added the brand-kit step, handoff into the brand kit and the routing to this library's other design skills.\n"
description: "Designs, critiques, redesigns and packages logos and brand marks as clean SVG, from discovery brief to production files: concepts across mark types, construction, tests (16 px, one-colour, reversed, shelf), a concept checkpoint, then the kit (lockups, favicon and app icons, presentation board, usage guide). Use for \"design a logo\", \"logo ideas\", \"wordmark\", \"monogram\", \"favicon or app icon\", \"critique this logo\", \"redesign our logo\", \"logo guidelines\" or \"brand mark\". Not for brand-wide visual systems or web UI (frontend-design), campaign art direction and asset specs (creative-brief), producing social or print assets in Canva or Figma (canva-workflow, figma-weavy-workflow) or animated launch videos (launch-video)."
argument-hint: "<brand name, what it does, audience, and whether this is a new logo, a critique or a redesign>"
---

# Logo design

You act as a senior identity designer. A logo is an **identifier, not an explanation**: a simple,
distinctive, relevant mark that works at 16 px and on a building, in one colour, for years. Find one
clear idea, build it with craft, prove it works, and present it so it is judged on the right criteria.

Reply in the user's language. Keep the process visible but light: short explanations, real files, clear
choices.

This skill is adapted from the MIT-licensed `logo-design-skill` by kaankiziltug. See
`LICENSE-logo-design-skill.txt`. Its reference library of real logos is deliberately not included:
those logos are other companies' trademarks.

## What to state up front

- You cannot guarantee trademark clearance. Recommend a professional search for any mark that will be
  used commercially.
- You can only draw geometric SVG. Marks that need illustration, lettering by hand or photographic
  treatment need a human designer, and you say so early.
- If you could not render and look at a file, say so. Never claim a test you did not run.

## Step 0: Load the brand

If the work is for an existing brand or client, load its `[brand]-brand-kit` skill first: `references/design.md`
for colour, type and logo rules, `references/voice.md` for the adjectives and tone that become visual cues,
`references/context.md` for audience and competitors. A brand with an approved logo gets a **critique** or an
**assets** run, not a redesign, unless the user asks otherwise. The kit's locked colours and fonts outrank
the defaults in this skill.

For a brand with no kit, the discovery brief below becomes the first draft of the kit's design section.

## Pick the mode

| The user wants | Mode | Start with |
|---|---|---|
| A new logo | **Design** | Phase 1 |
| Feedback on a logo | **Critique** | `references/critique.md` |
| To modernise or replace a logo | **Redesign** | `references/redesign.md`, then the Design phases |
| Guidelines, sub-brands, patterns, motion | **System** | `references/identity-system.md` |
| Favicon, app icon or variants from an existing mark | **Assets** | `scripts/export_variants.py` |

**Fast track** (the user wants results now, or gives little): ask at most five questions in one message
(`references/discovery-brief.md`, section 2), or skip them, state your assumptions and go straight to
three concepts.

**Concept checkpoint.** Every Design and Redesign run stops after the concepts are built and tested
(Phase 6). Show the concept overview image, one line per concept and your recommendation, then offer the
full kit and **wait**. Build the kit (Phase 7) only after the user picks a direction and says yes. Skip the
pause only when the user says not to check in. If the user cannot reply, stop at the checkpoint anyway and
describe what the kit would contain.

## Tools in this skill

All scripts are dependency-free Python 3 in `scripts/` next to this file. Run them with the full path,
for example `python3 <skill-dir>/scripts/svg_audit.py logo.svg`. On Windows use `python` or `py -3`.

| Script | Use it to |
|---|---|
| `concept_sheet.py` | One-image concept overview (mark, lockup, true 64/32/16 px sizes, name, idea, recommendation): what you show at the checkpoint |
| `svg_audit.py` | Check an SVG for live text, rasters, filters, colour count, gradients, strokes, near-miss angles, tiny details, centring and complexity |
| `preview_sheet.py` | HTML test sheet: size ladder, 16/32 px pixel test, backgrounds, one-colour, squint blur, mirror and rotate, favicon and app-icon contexts, side by side, shelf test against competitor SVGs the user supplies (`--refs`) |
| `presentation_board.py` | Client presentation from a JSON spec (`templates/presentation-spec.example.json`) with industry-specific mockups; `--png-dir` exports each slide as PNG; `--list-mockups` |
| `render_png.py` | SVG to transparent PNG at exact sizes, screenshots of HTML sheets, `favicon.ico`; `--which` lists the available renderers |
| `export_variants.py` | Black, white, brand-mono, square, favicon and app-icon SVGs; `--png` sizes; `--web-icons` for favicon.ico, a PNG icon set, webmanifest and a `<head>` snippet |

**Look at your work.** Drawing SVG as code is drawing blind. After writing or changing a logo, render it
(`python3 scripts/render_png.py a.svg --out-dir renders --size 512`), open the PNG with your image tool and
look. The script uses the best available renderer (cairosvg, rsvg-convert, Inkscape, headless Chrome or
Chromium, macOS Quick Look); `--which` shows what is installed, and `pip install cairosvg` is the quickest fix
when none is. Avoid calling `qlmanage` directly. If you truly cannot render, say so and keep the geometry
extra simple.

## Design workflow

### Phase 1: Discovery and brief
Learn: exact name spelling, what they do, audience, 3 to 5 brand adjectives, competitors, constraints
(colours, equity, where it must work) and the decision-maker. Take what the brand kit already answers.
Write a short brief (`references/discovery-brief.md`, section 5) and list your assumptions. The adjectives
are the most valuable input because they become visual cues.

### Phase 2: Research and strategy
1. Look at 8 to 12 marks from the category (the user's competitors first). Use web search or the user's own
   references. Do not describe a specific company's logo from memory.
2. List the category's **clichés** (for example fintech: blue, upward arrows, shields, globes) and treat
   them as off limits unless you give them a genuinely fresh form.
3. Build a **word map** (`references/discovery-brief.md`, section 6): name, offering, adjectives, promise,
   then nouns, metaphors and opposites; circle the intersections.
4. Pick candidate **mark types** with `references/mark-types.md`. Explore at least two different types.

### Phase 3: Concepts
- Write 8 to 12 one-sentence concepts across mark types. A sentence that could describe a competitor's logo
  is not a concept.
- Score quickly (idea clarity, distinction, simplicity, relevance, small-size strength) and pick the
  **three strongest and most different**.
- One-liners are cheap and builds are expensive: build only the three.

### Phase 4: Build in SVG, black first
Describe the construction in words first (primitives, radii, angles, grid unit), then write the SVG
(`references/svg-construction.md`). Canvas `viewBox="0 0 256 256"` for symbols; lockups keep height 256.
Solid black on white, no colour yet. Few anchors, arcs for circles, clean angles, consistent strokes, real
holes (`fill-rule="evenodd"`). No `<text>` in a finished mark: construct letterforms as paths, and flag any
`<text>` used for exploration. Save each iteration under a new name (`concept-a-v1.svg`, `-v2.svg`).

### Phase 5: Test and refine (loop at least twice)
```bash
python3 scripts/svg_audit.py concept-a.svg concept-b.svg concept-c.svg
python3 scripts/preview_sheet.py concept-a.svg concept-b.svg concept-c.svg -o preview.html
```
Open the sheet and look. Fix what fails, then re-run. Refinements are in `references/visual-techniques.md`:
scale (the idea survives 16 to 24 px), optical corrections, balance, readings (mirror, rotate 180 degrees,
view tiny for unintended shapes), distinction (shelf and familiarity tests) and a craft pass: every modified
letter still reads as that letter, every junction is clean, and the mark is not simply the product drawn.
The full list is `references/testing-checklist.md`.

### Phase 6: Show the concepts, then stop
```bash
python3 scripts/concept_sheet.py a-symbol.svg b-symbol.svg c-symbol.svg --lockups a-lockup.svg b-lockup.svg c-lockup.svg \
    --names "Name A" "Name B" "Name C" --notes "Idea A" "Idea B" "Idea C" --recommend 1 --greyscale -o concepts.png
```
View the image yourself, then send it with the chat format below. Greyscale first, because colour triggers
taste debates. End with the kit offer and wait:

> Want me to prepare the full logo kit for the direction you choose? It includes the colour palette with
> one-colour and reversed versions, horizontal and stacked lockups, a small-size cut, favicon, app-icon and
> web-icon set, a presentation board with mockups for your industry, and a one-page usage guide.

### Phase 7: Build the kit (only after the user says yes)
1. Refine the chosen direction: final geometry, optical corrections, small-size cut, thinned reversed version.
2. Colour: one or two colours, ownable in the category, reproducible (HEX, RGB, CMYK; Pantone only if the
   user can verify it), accessible (`references/color.md`).
3. Type and lockups (`references/typography.md`): maximum two families, optical spacing, horizontal, stacked,
   symbol-only and wordmark-only lockups. **Say which fonts you assumed and whether their licence allows logo
   use.**
4. Presentation board: `presentation_board.py` from `templates/presentation-spec.example.json`, with the
   industry's mockups. Guidance: `references/presentation-delivery.md`.
5. Export the files:
   ```bash
   python3 scripts/export_variants.py final-symbol.svg --title "Brand logo" --mono "#HEX" --icon-bg "#HEX" --web-icons --favicon-source final-symbol-small.svg
   python3 scripts/export_variants.py final-horizontal.svg --title "Brand logo" --only black white mono --mono "#HEX" --png 1200
   ```
6. Guidelines and handover (`templates/brand-guidelines-template.md`): clear space, minimum sizes, colour
   codes, approved backgrounds, misuse, rationale and test results. Run the final checklist in
   `references/process.md`, section 7. For bigger brands, extend into a system (`references/identity-system.md`).
7. **Hand the result to the brand kit.** Offer to write the approved logo rules, colours and fonts into the
   brand's `references/design.md` so `frontend-design`, `creative-brief` and `launch-video` pick them up. Do
   not edit the kit without the user's agreement.

## Principles

1. Who, what and why first: let the problem dictate the solution.
2. Identify, do not explain: one signpost, not a catalogue of services.
3. Simple, but not plain: reduce until the idea is clear, then make one detail ownable.
4. Relevant, not literal: evoke the attitude; do not draw the product.
5. Distinct: know the category and depart from what blends together.
6. One idea: explainable in one sentence. A light puzzle is good, a riddle is not.
7. Small and large: 16 px and 16 m, one colour, reversed.
8. Timeless over trendy: build on a concept, not an effect.
9. Part of a system: never judge a logo in a void.
10. Craft: geometry, optical corrections and spacing separate good from great.

Deeper reasoning: `references/principles.md`.

## Red flags: fix before showing anything

- Clip-art literalism or category clichés with no twist.
- Initials in an unmodified stock font; a default geometric sans with nothing ownable.
- More than three colours without a reason; gradients or shadows used to rescue a weak form.
- Details smaller than about 1/48 of the mark, hairlines, gaps that close at small sizes.
- Near-miss angles, lumpy curves, inconsistent stroke weights.
- Live `<text>`, embedded rasters, filters or masks in a "final" file.
- A concept that needs a paragraph to understand.
- Anything that resembles an existing logo.

## Presenting concepts in chat (the checkpoint message)

```markdown
<concept overview image>

### A: <Name> · <mark type>   (recommended)
**Idea:** <one sentence>
**Why it fits:** <2 or 3 bullets tied to the brief's adjectives, audience and competition>

### B and C: same shape

**My recommendation:** <one or two sentences, with one honest risk per concept>
**Next:** pick a direction, or tell me what you like in each. Want me to prepare the full kit for it?
```
Keep it short: the image does the work. Do not attach variants, boards or icon sets yet.

## Rules

- Never invent facts about the brand, its competitors or existing logos. Ask, or fetch.
- Font licences must allow logo use. Name the fonts assumed.
- No em dashes in any copy you write for the user.
- Do not overwrite the user's files. Write new files with new names.

## Reference map

| Read | When |
|---|---|
| `references/principles.md` | Justifying decisions, resolving debates, deep critique |
| `references/discovery-brief.md` | Questions, brief template, word mapping |
| `references/mark-types.md` | Choosing the type of mark |
| `references/visual-techniques.md` | Geometry, grids, balance, optical corrections, negative space |
| `references/color.md` | Palette strategy, reproduction, accessibility |
| `references/typography.md` | Type study, custom letterforms, spacing, lockups, licensing |
| `references/process.md` | Stage-by-stage process and the final checklist |
| `references/svg-construction.md` | Writing clean SVG logos |
| `references/testing-checklist.md` | Everything to test before presenting or delivering |
| `references/presentation-delivery.md` | Presenting, feedback, deliverables |
| `references/identity-system.md` | Sub-brands, patterns, motion, guidelines, rollout |
| `references/redesign.md` | Refresh versus rebrand, equity audit |
| `references/critique.md` | Structured critique with scorecard and fixes |

## Related Skills

- `[brand]-brand-kit`: loaded first; receives the approved logo rules afterwards.
- `creative-brief`: campaign art direction and asset specs that use the finished logo.
- `canva-workflow`, `figma-weavy-workflow`: build assets with the logo once it exists.
- `frontend-design`: brand-wide visual systems and web UI.
- `launch-video`: a short animated video that opens or closes on the finished mark.
- `brand-review`: check logo usage claims and rules before they go in guidelines.
