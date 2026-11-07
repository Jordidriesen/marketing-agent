---
name: figma-weavy-workflow
metadata:
  version: 2.1.0
  history: 'v2.1.0: run path rewritten against the live Figma MCP tool names (checked 5 Nov 2026): weave_list_tools, weave_get_tool_inputs, weave_upload_asset, weave_run_tool with its cost gate, weave_get_tool_run_output, weave_cancel_tool_run, plus the direct model route (weave_find_model, weave_run_model, weave_get_model_run_output) that runs one model without a published tool. The MCP still cannot build or edit a graph. v2.0.1: required skill calls stated up front; the follow-up skills are called through the Skill tool, never imitated inline. v1 gave a loose Weavy prompt-chain outline. v2 is built from Figma Weave''s actual node documentation: real node names by category, datatype/colour connection rules, consistency controls, iterators for batching, publishing a graph as a reusable "tool", and the Figma MCP run path (which can run a published Weave tool but not build a graph).

    '
description: 'Designs and runs Figma Weave node graphs for generated or composited imagery and short video: hero images, product shots, batch variants. Templates and text variants: canva-workflow.'
argument-hint: <the imagery or video to build in Figma Weave>
---

# Figma Weave (Weavy) Workflow

Figma Weave is a node canvas: each node is a function with inputs on the left and outputs on the right; you wire an output handle to a compatible input handle and the graph re-runs downstream whenever an input changes. Your job is to specify that graph precisely, then, if the tooling allows, run it.

**Required skill calls.** After drafting, call `brand-review` through the Skill tool, in that order, and never imitate them with an inline edit. A reply that skips it is not finished. End the reply with one line: `Skills run: ...`.

What the Figma MCP **cannot** do: create or edit a Weave graph. It can *run* a graph that has already been built in Weave and published as a "tool" with exposed inputs, and it can run a **single model** directly (one generation or edit, no graph). So the graph spec below is the deliverable whenever the job needs more than one model call, even when a connector is present.

## Step 0: Load the brand, the brief, and references

Load the matching `[brand]-brand-kit` skill and the `creative-brief` output. Collect: palette hex, imagery style and treatment rules, logo files, any reference images or approved prior assets, and the deliverable's dimensions and aspect ratio. Reference images matter more here than adjectives: a model tracks a style image far better than a description.

## Datatypes and wiring

Handles only connect when the datatypes match. Node colour signals the type:

| Colour | Datatype |
|---|---|
| Green | Image |
| Red | Video |
| Purple | Text (prompt) / LoRA |
| Blue | Array / List / 3D |
| Lime | Mask |
| White | Node accepts multiple input types |

Add a node: search the left panel, press **Tab** on the canvas, or right-click the canvas and type the name. Select a node to see its parameters in the right-hand panel. Generative nodes have a **Run** button and cost credits; editing, matte and utility nodes are free.

## Node catalogue

### Inputs and datatypes
- **Image**, **Video**: upload or receive from an upstream node.
- **Text**: the prompt. Also a **Prompt** node, which supports **Variables**: click *Add Variables* to add named input handles, then connect a Text node to each; lets one prompt be assembled from labelled parts.
- **Number**, **Toggle**, **Seed**, **List Selector**: expose a model parameter as a node so it's visible and connectable. Set the Seed once a look is approved so variants stay consistent.
- **Array**: hold several text inputs as separate items (typed, or split from one connected Text node on a delimiter). Feeds List Selector and the text iterator.

### Generative nodes (Run button, cost credits)
- **Text-to-image / Generate**: prompt + aspect ratio + inference steps + guidance scale + seed. Model choice matters: photoreal vs. illustration vs. typographic. Named models available include Flux, Ideogram V3, Imagen, SDXL Turbo, Seedream, Reve, Nano Banana, and GPT image; check the in-app *Image Models Comparison* for the current list.
- **Image-to-image / Edit**: an Image input plus a prompt; changes an existing image.
- **Generate-from-image**: uses one or more reference images to steer style, subject or composition. This is the brand-consistency lever: feed an approved reference at controlled strength.
- **Upscale**: a downstream node that takes output to print resolution. Check *Enhance Images Models Comparison*.
- **Gen Effect**: applies a generative effect to an image.
- **Video**: image or text in, motion prompt, → video (Runway Gen-4, Veo, Kling and others; see *Video Models Comparison*). **Extract Video Frame** pulls a still.

### Editing nodes (free)
**Levels** (shadows/midtones/highlights), **Crop** (preset ratio or custom), **Resize** (stretch to exact dimensions for a model's input requirement), **Blur** (box or Gaussian), **Invert** (often used on a mask), **Channels** (R/G/B/A for advanced compositing), **Painter** (paint a mask or sketch by hand, outputs both an **image** and a **mask**).

### Matte / mask nodes
- **Mask Extractor**: click to auto-segment; Shift adds, Alt+Shift subtracts.
- **Mask By Text**: Image + Text → a mask of whatever the prompt describes.
- **Matte Grow / Shrink**: choke or expand a matte for a clean edge.
- **Merge Alpha**: Image + Mask → an RGBA image (cut-out).
- **Image Describer**: Image → Text. Use it for describe-then-regenerate consistency: describe an approved asset, reuse that text as the prompt.
- **Outpaint**, **Z Depth Extractor**: extend a frame; extract depth for structural conditioning.

### Compositor node
Layer-based composition on the canvas: each input is a layer with blend mode, opacity, position, scale, rotation; add **shape layers** and **live text layers** directly; set a background fill; group layers. Has a timeline for video layers. **This is where brand assets go**: place the real logo/wordmark as its own layer, and set headline/CTA copy as live text layers, rather than letting a model render either.

### Helpers and iterators
- **Sticky Notes**: annotate the graph. **Compare**: A/B two outputs side by side.
- **Text Iterator**: many prompts → one model, batched as separate runs. Accepts an Array node, a Prompt node, or an imported **CSV**.
- **Image Iterator** / **Video Iterator**: many media inputs → one model, batched.
- **Nested iterators**: an outer iterator over categories, an inner over variations, for a full matrix (e.g. 4 products × 3 backgrounds = 12 runs).

### Custom models
**Import Models** and **Import LoRAs** (from a URL) let you load a brand-trained fine-tune so generations sit on-style by default.

## Consistency controls (use all that apply)

1. **Fix the Seed** once a look is approved; feed the same Seed node into every variant generation.
2. **Reference image at controlled strength** into a generate-from-image node: the single strongest lever for brand look.
3. **Image Describer → reuse the text** so re-generations describe the same thing.
4. **Never let a model render the logo or wordmark**: place the real asset in the Compositor.
5. **Keep all copy as live Compositor text layers**, not baked into the image, so it stays legible, editable, and can pass `brand-review`.
6. **Brand colour correction as an explicit final Levels/recolour step**: generative output drifts off-palette.

## Example graphs

**Branded product shot**
`Image (product)` → `Mask By Text ("the product")` → `Merge Alpha` (cut-out) → `Generate-from-image` (scene prompt + brand palette hex, cut-out as reference) → `Compositor` (generated scene as background layer, logo layer top-left, live headline text layer) → `Upscale` → `Crop` iterator (Array of ratios: 1:1, 4:5, 9:16, 16:9) → export per format.

**Character / style consistency across a set**
`Image (approved key visual)` → `Image Describer` → `Text` (edit the description per scene) → `Generate` (fixed `Seed`, style reference wired in) → `Compare` (new vs. key visual) → accept or adjust prompt and re-run.

**Batch variants (per product or locale)**
`Array` (product names or locale strings) → `Text Iterator` (assembles the prompt per item, or pulls a CSV) → `Generate` (fixed Seed, brand LoRA) → `Compositor` (per-item logo + text) → `Image Iterator` export.

**Short social video**
`Generate` or `Image (approved still)` → `Video` node (motion prompt, duration) → `Levels` (brand grade) → `Crop` (9:16 and 1:1) → export.

## Publish as a reusable tool

Expose the inputs a non-technical user should control as **labelled input nodes at the top of the graph**: e.g. "Product Photo", "Headline", "Brand Palette", "Output Ratio". Publish the graph as a Weave **tool**; App Mode auto-generates a simple form UI while keeping the full graph editable. A published tool is what the MCP can run.

## Run path (Figma MCP connected)

Figma Weave runs through the **Figma MCP server** (no separate Weavy MCP). Requires a Figma Weave account on Starter, Pro, Team or Enterprise, the Figma account linked to Weave (*Settings → Profile → Linked accounts* in Weave), and the right Weave workspace active. Load the Weave tools in one tool search; never guess a name. Weave work needs no Figma file, so `create_session` is not part of this path. Every run spends **Weave credits** (not Figma AI credits).

**Route A: a published tool (the normal route for a graph).**
1. `weave_list_tools` (with `search` set to the name, if known) → the tool's `recipeId`. A pasted `app.weavy.ai/tool/<id>` or `/flow/<id>` URL already is the `recipeId`; skip the list and never open a browser for Weave.
2. `weave_get_tool_inputs` → the `version`, the `outputs` summary and the `inputs` list (`nodeId`, `type`, `default`, `required`). Fill every required input; confirm with the user any default the run would silently use.
3. Media: an https URL can go in directly; a local file goes through `weave_upload_asset`, which shows the user a file picker. Pass the whole returned asset object as the value.
4. `weave_run_tool` without `acknowledgedCost` only quotes. Show the user the quoted cost and get an explicit approve or cancel, then call again with `acknowledgedCost` (`-1` for a dynamic-cost graph). Every rerun is quoted and approved again.
5. `weave_get_tool_run_output` with the `runIds` until each run reports the status `COMPLETED`, `FAILED` or `CANCELED` (the API's spelling); download outputs with the curl instructions it returns rather than embedding media. `weave_cancel_tool_run` stops a run and cannot be undone.

**Route B: one model, no graph.** For a single generation or edit (one hero variant, one upscale, one image-to-video clip): `weave_find_model` with the model name → its `id` and input contract; `weave_run_model` (quote, approve, run, same gate as above); `weave_get_model_run_output` with the `predictionIds`. Brand assets still go in afterwards as real layers, so a one-model run is rarely the finished asset: composite it in Canva, Affinity or a Compositor graph.

If no suitable published tool exists and the job needs a graph, hand back the graph spec for someone to build once in Weave, then publish it as a tool for future runs.

## Related Skills

The brief comes from `creative-brief`. Layout-and-template assembly of the pieces can move to `canva-workflow`, precise vector or print layout to `affinity-workflow`. Copy in the final asset comes from `content-writer` or `social-media-specialist` and passes `brand-review`.

## Output

The graph spec, every node in order, every wire, every parameter, every prompt and negative prompt written out, every brand token named, followed by the consistency checklist. If a run path was available and a published tool existed, add the run log and the output URL.

Conciseness note: any chat framing around this deliverable stays short, a sentence or two. It never applies to the deliverable itself, which is produced at the full length and detail the structure above requires.
