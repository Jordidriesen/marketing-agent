# Type and colour

Rules for typography and colour systems in `frontend-design`. Adapted and rewritten from
jakubkrehel's [better-typography and better-colors](https://github.com/jakubkrehel/skills) (MIT),
cut down to marketing sites, landing pages and WordPress block themes.

**Precedence.** A loaded brand kit's `references/design.md` outranks every rule here. These are
defaults for what the brand has not decided. A brand with a light display weight, a serif body or a
specific accent keeps it. Never propose a new typeface unless the task asks for a type change.

**Measured, not preferred.** Some values are exact and are findings when missed: unitless
line-height, weight 400 or heavier below 18px, a capped measure, 16px inputs on iOS, tabular
figures on changing numbers. Letter-spacing, pairing and scale ratios are heuristics: report them
only where they break the project's own scale.

---

## Type

### Fonts, sizes, weights

- Rarely more than three font families; a marketing page can carry more than an app. Hierarchy
  comes from size and weight, so every extra weight dilutes it.
- Pair for contrast. A serif headline over a sans body reads as deliberate; two near-identical
  sans-serifs read as a mistake.
- Below 18px use weight 400 or heavier. Weights 100 to 300 belong at 28px and up, and are checked
  against the background even there.
- Load every face the design uses. Browsers fake a missing weight or italic and distort the face.
  Check the fallback stack before switching synthesis off.

### Properties over raw tags

- `font-weight: 650`, not `font-variation-settings: "wght" 650`.
- `font-variant-numeric: tabular-nums`, not `font-feature-settings: "tnum" 1`.
- Leave `font-optical-sizing` on `auto`. Raw tags are for custom axes and features that have no
  property.

### Scale and hierarchy

- Define a small type scale and deviate from it as little as possible. Pair each size with its
  line-height and weight so a role is one decision.
- Heading levels map to descending steps. A subordinate heading never outweighs its parent and no
  heading is smaller than body text, except a deliberate overline. Where the scale runs out of
  steps, deep levels may share a size if weight or tracking keeps them distinct.
- Size floors: long-form body starts at 16px and moves only for a reason you can name. UI text can
  go smaller (inputs and menus 14px, captions 13px), rarely below 12px. Set sizes in `rem` so the
  reader's browser setting still applies.

### Spacing in text

| Role | Line-height | Letter-spacing |
|---|---|---|
| Display | 1.1 | -0.01em to -0.02em at 24px and up |
| Headings | 1.2 to 1.3 | -0.01em to -0.02em at 24px and up |
| Body | 1.5 to 1.6 | 0 |
| Uppercase labels, 14px or smaller | 1.4 or more if they wrap | 0.05em |

- Line-height is unitless so it scales with the font size.
- Anything that wraps to three or more lines needs at least 1.4, even in a height-constrained card.
- Tracking is in `em`, never `px`. Never turn kerning off as a fix.
- Cap long-form measure at 60 to 75 characters per line, in any unit.

### Wrapping and truncation

- `text-wrap: balance` on headings and short descriptions, never on paragraphs.
- `text-wrap: pretty` on paragraphs to keep a lone word off the last line.
- `overflow-wrap: break-word` where a long word, link or ID could escape its container.
- `white-space: nowrap` on labels and badges where a line break looks broken.
- Interface text stays `text-align: start`. Justified text only in a specific editorial layout.
- Tabular figures on timers, counters, prices and numeric table columns. Figures in prose stay
  proportional.
- Truncated text always has a way back to the full value (expand, detail view or a keyboard
  reachable tooltip). Never truncate numbers, prices or dates.

### Punctuation and text details

- Store text in natural case and set case with `text-transform`, so a redesign never means
  rewriting copy.
- Rendered text uses typographic characters: `…` not `...`, curly quotes, an en dash for ranges
  (`10–20`), non-breaking spaces in `10 MB` and `⌘ K`. Code keeps straight quotes.
- **No em dashes in visible text in this library.** Where a typographic rule elsewhere suggests an
  em dash for a pause, use a comma, colon, full stop or brackets instead.
- Underlines: `text-underline-position: from-font` and `text-decoration-thickness: from-font`, or
  tune offset and thickness by hand.
- Inputs are 16px on mobile or iOS Safari zooms the page. Two fixes hold 16px and look different
  (size the input up on mobile, or keep 16px and scale the rendering), so ask which the design
  wants.
- `-webkit-font-smoothing: antialiased` once on the root, not per component.
- Set `lang` on the document and on switched-language passages (this library serves NL, FR, DE
  and ES pages). Wrap mixed-direction values in `<bdi>`; never reorder digits by hand.
- Build drop caps, gradient text and text shadows in CSS so the text stays selectable and
  searchable. Keep text selectable; `user-select: none` only on drag or gesture surfaces.

### Type review table

| Pattern | Fix |
|---|---|
| `font-weight` value with no matching loaded face | Load the face or use a weight the family ships |
| `font-variation-settings: "wght"` or `"opsz"` | `font-weight`; drop `"opsz"` |
| `font-feature-settings: "tnum"` | `font-variant-numeric: tabular-nums` |
| `line-height` in `px` or `rem` | Unitless value |
| Tight `line-height` on anything that can wrap | 1.4 or more |
| `letter-spacing` in `px` | Same value in `em` |
| Body `font-size` in `px` | `rem` |
| Weight 100 to 300 on text under 18px | 400 or heavier |
| `text-wrap: balance` on a paragraph | `text-wrap: pretty` |
| `text-align: justify` in interface text | `text-align: start` |
| `-webkit-line-clamp` without `display: -webkit-box` and `-webkit-box-orient: vertical` | Add both |
| Timer, counter, price or numeric column without `tabular-nums` | Add it |
| `...` or a hyphenated range in rendered strings | `…` and an en dash |
| `<input>` at 14px with no mobile override | One of the 16px fixes |
| Mixed-direction value without `<bdi>` | Wrap it |

---

## Colour

Never report a contrast value you did not measure, and never estimate a colour you could compute.
Notation, a tinted neutral and a gradient's interpolation space are project choices, not findings.
A broken role mapping, a failing pair and an out-of-gamut step are findings. "Perceived lightness"
below means OKLCH `L`, 0 to 1.

### A system is ramps with jobs

- One neutral ramp, one accent ramp, and only the status ramps the product renders. A `warning`
  ramp nothing uses is maintenance for zero pixels.
- A second accent hue earns its place only when two things must be told apart at a glance.
  Otherwise use more steps of the one accent.
- Every step exists because a role needs it: page background, hover, border, solid fill, body
  text. Do not generate steps no role consumes.
- A ramp holds one hue end to end, peaks in vividness mid-ramp and steps more finely at the light
  end (about 0.04 to 0.05 `L` per step). Build it with a colour library, not by eye. Use the same
  proportion of each hue's own maximum chroma, not one chroma number copied across hues.
- For a new system `oklch()` is the best default. In an existing project, reuse its notation: a
  consistent hex system beats hex with `oklch()` scattered through it.

### Tokens

- **Primitives** name a value by hue (`--blue-600`) and are never used in components.
  **Semantic tokens** name a job (`--color-text-secondary`), point at a primitive, and are the
  only tier components reference.
- Use a token only in its role. A separator token used as a text colour breaks the day borders get
  lighter. If a role has no token, add one.
- Semantic names carry no hue and no component (`--color-accent-solid`, not
  `--color-blue-button`). Call the brand colour `accent` so it does not collide with
  `text-primary`.
- One colour, one meaning across the whole interface. Anything within 15° of OKLCH hue counts as
  the same colour. A status hue closer than 15° to the accent needs moving or a distinct treatment
  for destructive actions.
- Never let colour be the only carrier of meaning: pair it with an icon or a label.

### Emphasis

- Fill exactly one action per view. Peers stay neutral. Put the colour on the background, not the
  label: a filled button reads as primary across the room, accent text on a neutral button reads
  as a link.
- Several coloured backgrounds are fine when they encode distinct states or categories rather than
  competing as peers.

### Contrast

- Measure the foreground against the background it actually renders on, including opacity and any
  image beneath, in light and dark.
- Thresholds: 4.5:1 text, 3:1 large text (24px, or 18.67px bold) and meaningful UI shapes.
- When a pair fails, report the pair, its measured ratio and the threshold, then leave the colours
  alone unless asked. They are a design decision. Remeasure after a change.
- A contrast fix changes lightness, the channel contrast responds to, not hue.
- White text on a mid-ramp fill often fails 4.5:1. Measure it, and move the fill a step darker.
- Text on a colour with alpha (`/50`, `rgba(`, `color-mix` with `transparent`): measure the
  rendered result or use a solid token.

### Dark mode and gamut

- Dark tokens are not the light ramp in reverse. Lower the accent's chroma, widen the dark end and
  remeasure every pair.
- Pick one switching mechanism for colour tokens and use it throughout. This library's pattern is
  `prefers-color-scheme` plus a `[data-theme]` override (see `interface-checklist.md`).
- `prefers-contrast: more` gets its own increased-contrast value per appearance.
- A chroma beyond sRGB declares the sRGB value first, then the vivid one inside
  `@media (color-gamut: p3)`.
- Gradients: default to `in oklab`; use `in oklch` when a two-hue gradient goes grey in the middle.

### Colour review table

| Pattern | Fix |
|---|---|
| Hex, `rgb(` or `oklch(` literal in a component where a token exists | Reuse or add the role token |
| One `oklch(` in a codebase written in hex | Match the established notation |
| `var(--blue-600)` or `bg-blue-600` in a component | Point a semantic token at it |
| `--color-primary` and `--color-text-primary` both defined | Rename the brand token `accent` |
| `hsl(` ramp that differs only in lightness | Rebuild in OKLCH with constant hue |
| Dark tokens equal to the light ramp reversed | Rework chroma and the dark end, remeasure |
| Tokens set under both `prefers-color-scheme` and a `.dark` class | One mechanism |
| Contrast fix that changes hue but not lightness | Change lightness |
| `text-white` on a mid-ramp fill | Measure; likely move the fill darker |

---

## Reporting a review

Group findings under the principle they break, most severe first, one row per root cause listing
every place it appears. `HIGH`: text unreadable, body or control text failing its ratio, meaning
carried by colour alone, content truncated with no way back, or text clipped at 320px or 200%
zoom. `MEDIUM`: breaks the type or colour system. `LOW`: isolated polish.

| Severity | Location | Before | After | Why |
|---|---|---|---|---|

Say `Not verified` for any check you could not run (no browser, no computed values). Never approve
coverage you did not inspect.
