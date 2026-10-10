---
name: canva-workflow
metadata:
  version: 2.0.0
  history: >
    v1 wrote a manual click-by-click Canva build checklist. v2 adds the
    full Canva MCP execution path (generate / brand-template / import →
    convert → transactional per-page edit → export) and keeps the manual
    checklist as the fallback when the connector isn't connected.
description: "Produces Canva assets (social, one-pagers, decks, printables, bulk variants) through the Canva connector, or gives a build checklist without it. Use for \"make this in Canva\"."
argument-hint: "<the asset or brief to build in Canva>"
---

# Canva Workflow

You either build the asset through the Canva MCP and hand back a link to the finished design, or, if the connector isn't there, hand back a checklist precise enough that a person builds it without a single creative decision left to make.

## Step 0: Load the brand and the brief

Load the matching `[brand]-brand-kit` skill and the `creative-brief` output for this asset. You need: palette hex values, brand fonts, logo files and clear-space rules, and the deliverable's exact dimensions. If any are missing, get them before starting.

Then check whether the **Canva MCP connector is connected**. If its tools are available, follow the Execution path. If not, skip to the Manual path.

---

## Execution path (Canva MCP connected)

### 1. Brand kit and route

- `list-brand-kits` → note the `brand_kit_id` for this brand. If the call returns a missing-scope error (`brandkit:read`), tell the user to disconnect and reconnect the Canva connector, then stop.
- Choose the route:

| Situation | Route |
|---|---|
| A brand template exists for this asset | **Template route** |
| Same asset, many data-driven variants (per product, per locale, per name) | **Autofill route** |
| No template; the layout is generated from a description | **Generate route** |
| The source is an existing file or URL (PDF, PPTX, DOCX, a public HTML page, an agent-generated HTML) | **Import route** |

### 2a. Template route

- If you weren't given a template ID (starts with `BTM`), `search-brand-templates` to find one. If you have the ID, skip search.
- `get-brand-template-dataset` with the template ID → the autofill field schema (text and image fields). An empty object means the template has no autofill fields; fall back to `create-design-from-brand-template` and edit it manually in step 3.
- `create-design-from-brand-template` (template ID, optional `page_numbers`) → a new `design_id` (starts with `D`).

### 2b. Autofill route (variants)

- `get-brand-template-dataset` → the field names and types.
- For each variant, call `autofill-design` with the template ID and a data object mapping field name → value (text string, or an asset ID for image fields). Each call returns its own `design_id`. This is the API equivalent of Canva's Bulk Create.

### 2c. Generate route

- Ask the user once whether they want it on-brand; if yes, pass `brand_kit_id`.
- `generate-design` (or `create-design` if that's the name shown) with a detailed `query` (subject, style, composition, colour named as brand hex, mood, what to exclude), the right `design_type` (e.g. `instagram_post`, `poster`, `flyer`, `email`, `doc`, `presentation`), `brand_kit_id`, and any `asset_ids` to place. It returns **design candidates** and a `job_id`.
- Pick the best candidate (show the user if there's genuine ambiguity), then `create-design-from-candidate` (`job_id`, `candidate_id`) → an editable `design_id`.

### 2d. Import route

- `import-design-from-url` with a **public HTTPS URL** and `intended_design_type`. For an agent-generated HTML page, add `data-document-role="page"` to each element that should be a Canva page, `data-label` for a page title, `data-speaker-notes` for notes. Never publish a private or local file to a public host to get a URL, if there's no already-public URL, stop and tell the user.

### 3. Bring in brand assets

For any logo, product shot, or image to place: `upload-asset-from-url` with an **already-public HTTPS URL** and a name → an `asset_id`. Use it in `generate-design`'s `asset_ids`, or in an `update_fill` / `insert_fill` edit operation.

### 4. Edit in a validated transaction

1. `read-design` with `open_transaction: true` and `filter.fields: ["thumbnails"]` → the `transaction_id`, each page's `locator_id`s, the `isEditable` / `type` flags, and the **before-thumbnail**.
2. `edit-design` with `transaction_id`, `page_index` (1-based), `operations: [...]`, `finalize: "keep_open"`. **One page per call.** Useful operations:
   - Text: `replace_text` / `find_and_replace_text` (use exact approved copy), `add_text`, `format_text` (`color` hex, `font_size`, `font_weight`, `text_align`, list markers), `update_text_anchoring`.
   - Image: `update_fill` (swap the image in a frame to an `asset_id`), `insert_fill` (place a new image at x/y/w/h), `crop_media`, `flip_media`.
   - Colour and shape: `recolor_element` (hex), `insert_shape` (SVG path, only `M/L/H/V/C/S/A/Z`, no `Q`/`T`), `replace_shape`, `update_stroke_properties`.
   - Layout: `position_element`, `resize_element` (text: width only; image: one dimension if `preserve_aspect_ratio`), `layer_element` (front/back), `group_elements`, `add_page`, `reorder_page`, `update_opacity`, `delete_element`.
   - `update_title` for the design name; `update_autofill_field` to wire an element to an autofill field (fixed-page designs only).
3. After each `edit-design` call: compare the returned after-thumbnail against the before-thumbnail and inspect the returned `document`. Fix anything wrong with another `keep_open` call.
4. When every page is right: `edit-design` with `finalize: "commit"` and an empty `operations` array. **This is irreversible.** If it went wrong, `finalize: "cancel"` instead.

### 5. Variants by size

`resize-design` (`design_id`, preset `presentation`/`whiteboard`, or custom `width`/`height`) creates a resized copy per channel. Re-open a transaction on each copy to fix any elements the resize shifted.

### 6. Export

- `get-export-formats` for the design **first**: it lists what this design actually supports. Never guess.
- `export-design` (`design_id`, `format`: `{type, export_quality, size, pages, transparent_background, width, height}` as relevant). PNG for flat graphics, `transparent_background: true` for logos and overlays, `pdf` + `size` + `export_quality: pro` for print, `pptx` for decks.
- Show the returned download URL to the user.

### 7. Make it reusable (optional)

`create-brand-template-draft` then `publish-brand-template` turns the finished design into a reusable brand template with autofill fields for future variant runs.

### Execution guardrails

- `commit` is permanent: always validate thumbnails first.
- One page per `edit-design` call; don't batch operations across pages.
- `get-export-formats` before every `export-design`.
- Never publish a private/local file to a public host to satisfy `upload-asset-from-url` or `import-design-from-url`.
- Canva silently substitutes missing fonts, after commit, export a preview and check the type rendered in the brand face.

---

## Manual path (no connector)

### A. Setup
Canva design type and custom dimensions (from the brief). Which brand template or Brand Kit to start from. Note whether the brand has a Canva Brand Kit set up (fonts, colours, logos uploaded in Canva), if not, say that setting one up once removes most of the manual styling below.

### B. Generative steps (if Magic Design or Magic Media is used)
For each, the **exact prompt text**, ready to paste: subject, style, composition, colour (brand hex), mood, and exclusions. State the aspect ratio to set. Flag that generated output needs a brand pass: Canva's models don't know the brand.

### C. Build checklist
Numbered steps in Canva's own terms: "Apply the brand template," "Replace the headline frame with: [exact copy]," "Set the headline to [brand font] [weight] [size]," "Recolour the shape to [hex]," "Place the logo top-left, clear space = logo height ÷ 2," "Position the CTA button [where], label: [exact copy]." Cover the whole asset.

### D. Variants (if Bulk Create is used)
The CSV column headers, one example row filled, and which text/image frames each column maps to.

### E. Export
Format (PNG flat, PDF Print with bleed for print, MP4 for motion) and any per-channel note (compress under the platform's file-size cap).

### F. Brand check
The 3–5 things to verify before shipping: logo clear space, colour accuracy, font substitution, text legibility at display size, safe-area margins.

---

## Related Skills

The brief comes from `creative-brief`. Copy in the asset comes from `content-writer` or `social-media-specialist` and, if written here, passes `brand-review`. For imagery Canva can't produce well (generated hero shots, composited scenes, design-system components), use `figma-weavy-workflow` and place the result as an image. For a quick edit to a real photo before it goes into the design (cut out the background, crop to the format, correct the tone), use the Adobe for creativity connector (`image_remove_background`, `image_crop_and_resize`, `image_apply_auto_tone`), then import the result. Call `adobe_mandatory_init` once first, as that connector requires.

## Output

**Execution path:** a short log of what was generated/edited/exported and the final download URL(s), plus the brand-check result. **Manual path:** the workflow, sections A–F, with every prompt and every piece of copy written out in full.

Conciseness note: any chat framing around this deliverable stays short, a sentence or two. It never applies to the deliverable itself, which is produced at the full length and detail the structure above requires.
