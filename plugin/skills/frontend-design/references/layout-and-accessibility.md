# Layout, surfaces and accessibility

Additions to `interface-checklist.md` for `frontend-design`. Adapted and rewritten from
jakubkrehel's [better-layout, better-accessibility and better-ui](https://github.com/jakubkrehel/skills)
(MIT). This file only holds what the checklist does not already say; it does not repeat its focus,
form, hit-area, alt-text or reduced-motion basics. `interface-checklist.md` stays a pinned copy of
the upstream Vercel guidelines and is not edited.

**Precedence.** The brand kit, then the project's own spacing scale and tokens. The numbers below
apply only where the project has none. A layout finding needs a failure you can show (a clip, an
overlap, a broken mirror, a misread group), not just a different value.

---

## Layout

- **Group with space, not lines.** Space first, background shapes second, separator lines last and
  only where space cannot carry the structure. The gap between groups is at least twice the gap
  inside one (8 px inside means 16 px or more between).
- **Controls look like controls.** Every interactive element has a background shape, border,
  underline or a consistent zone such as a toolbar. A control styled like the static text beside
  it does not read as one.
- **Align to shared edges.** Pick a few alignment edges and put everything on them. One spacing
  step per level of nesting (16 px is a useful default).
- **Order by importance, and keep DOM order.** The most important content sits near the top and
  the leading edge; within a row, identifying content leads and metadata and actions trail. Visual
  order matches source order: no reordering with `order`, `row-reverse` or grid placement.
- **One primary action per view.** Secondary actions go behind a menu past three. Prefer a short
  view that links deeper over one long view that shows everything. (Colour of the primary action:
  `type-and-colour.md`.)
- **Hint at hidden content.** Anything off-screen or collapsed has a visible cue: the next item
  peeking 16 to 32 px past the scroll edge, or a disclosure control.
- **Borderless controls need clearance.** Without a density system, 12 px between adjacent bordered
  or filled controls and 24 px between the visible glyphs of borderless text or icon controls.
  Hit areas never overlap.
- **Inset full-width buttons** from the layout margins (about 16 px on mobile) unless they follow
  platform chrome and account for safe areas.
- **Content bleeds, controls float.** Backgrounds and media run to the viewport edge; controls and
  text stay inside margins and safe areas. `env(safe-area-inset-*)` is zero unless the viewport
  meta has `viewport-fit=cover`. Content scrolls beneath sticky chrome, so set
  `scroll-padding-block-start` to the sticky header height.
- **Hold structure until it breaks.** Breakpoints come from the content, not device presets. Keep
  the expanded layout until it stops fitting, then collapse. Prefer container queries for
  component-level adaptation and test the smallest and largest sizes first.
- **Logical properties for anything that mirrors.** `margin-inline-start`, `padding-inline-end`,
  `inset-inline-start`, `text-align: start`. Physical left and right only for physical geometry
  such as safe-area insets. Relevant here only if a market needs right-to-left; do not add
  mirroring work to an NL, FR, DE or ES site that will not use it.
- **Plan for growth, because translation grows.** Short strings grow proportionally more, so a
  one-word button label is the riskiest text on the page (Dutch and German run long). Size text
  containers with `min-height` and `max-width`, never a fixed `width` or `height`, and let rows
  wrap. Test with one long-string locale. Never park a critical action where resize, zoom or
  scroll can clip it.

### Layout review table

| Pattern | Fix |
|---|---|
| Grid track `1fr` or flex child holding long text or a wide table, overflowing | `minmax(0, 1fr)` on the track, `min-width: 0` on the flex child |
| `width: 100vw` | `width: 100%` (100vw includes the scrollbar) |
| `height: 100vh` on a full-height mobile section | `min-height: 100dvh` |
| Fixed `height` on a box holding text | `min-height`, or `max-height` with `overflow-y: auto` |
| `@media (max-width)` inside a reusable component | `@container` on the parent |
| `container-type: inline-size` on a shrink-to-fit element with no width | Give it a definite width |
| `env(safe-area-inset-*)` with no `viewport-fit=cover` | Add it, or the inset is 0 |
| `float: left` on UI that mirrors | `float: inline-start` |
| Sticky header with no `scroll-padding-block-start` | Set it to the header height |
| Fixed-width button | Content width with `min-width` |

---

## Surfaces and icons

- **Concentric radii.** Where nested surfaces share an even inset, outer radius = inner radius +
  padding + any border width. Past about 24 px of padding, or with asymmetric padding, treat the
  layers as separate surfaces and keep each one's radius token. (Shape lock: `taste.md`
  section 4.)
- **Optical alignment.** Where geometric centring looks off, nudge by eye: 2 px less padding on a
  button's icon side, a play triangle shifted toward its point. Fix asymmetric glyphs in the SVG
  itself.
- **Shadows for elevation, borders for structure.** Where a border exists only to create depth,
  use layered transparent shadows. Keep borders on dividers, separators, table cells, selected
  states and form inputs (an input boundary needs 3:1 non-text contrast). Forced-colours mode
  removes every `box-shadow`, so keep `border: 1px solid transparent` under a shadow ring so an
  edge still draws.
- **Outline content images** with a 1 px inset outline in pure black or white at 10 percent
  (`oklch(0 0 0 / 0.1)` light, `oklch(1 0 0 / 0.1)` dark), never a tinted neutral or the accent,
  or a coloured fringe shows on the image edge. Skip transparent artwork such as logos.
- **One SVG, recoloured by state.** Icons use `currentColor` and take hover, selected and disabled
  from CSS, never from separate assets. One icon library per surface. Outline is the default
  variant, fill marks the active state. Icon stroke tracks text weight (roughly 1.5 px beside
  weight 400 up to 2.5 px beside 700).
- **Cross-fade a contextual icon swap** (play to pause, copy to copied) on an infrequent state
  change: scale 0.25 to 1, opacity 0 to 1, blur 4 px to 0, about 300 ms, no bounce. A tab icon or
  a row action revealed on hover is high-frequency and does not animate (`motion.md`).

| Pattern | Fix |
|---|---|
| Padded parent and child with the same radius | Outer = inner + padding |
| `box-shadow: 0 0 0 1px` ring with no border beside it | `border: 1px solid transparent` |
| Image outline in a palette grey or hex colour | Pure black or white at 10 percent |
| `fill="#..."` or `stroke="#..."` inside an icon SVG | `currentColor` |

---

## Accessibility: cite the criterion

A finding cites a WCAG 2.2 Level A or AA criterion by number, or a concrete task an
assistive-technology user cannot complete. Anything else (AAA criteria, ARIA practice conventions,
the one-`<h1>` outline, the 44 px and 40 px target sizes) is a recommendation and never `HIGH`.

| Criterion | Rule |
|---|---|
| 1.4.1 Use of colour | Status needs a redundant cue (icon, text or underline) |
| 1.4.3 Contrast (AA) | Text 4.5:1; large text (24 px, or 18.67 px bold) 3:1 |
| 1.4.4 Resize text | Text survives 200 percent resize |
| 1.4.10 Reflow | Reflows at 320 px width with no horizontal scrolling |
| 1.4.11 Non-text contrast | UI boundaries, states and meaningful graphics 3:1 |
| 2.2.2 Pause, stop, hide | Anything moving or updating over 5 seconds has a pause control |
| 2.4.11 Focus not obscured | A focused element is never fully hidden behind sticky chrome |
| 2.5.7 Dragging movements | Every drag has a single-pointer alternative |
| 2.5.8 Target size (AA) | At least 24 by 24 CSS px, or an exception; aim for 44 px on touch |

### Beyond the checklist

- **Native first.** Do not use ARIA when a native element exists; when unsure, remove ARIA rather
  than add it. A real link supports Cmd, Ctrl and middle click.
- **Disabled means unavailable.** Use native `disabled` for genuinely unavailable controls.
  `aria-disabled="true"` only when the control must stay focusable; then block pointer, keyboard
  and form behaviour in code and style the state. A tooltip on a natively disabled control never
  shows, so put the text beside it.
- **Keyboard order.** Only `tabindex="0"` (join the order) and `tabindex="-1"` (programmatic
  focus); never a positive value. Composite widgets use roving tabindex.
- **Dialogs.** Prefer `<dialog>` opened with `showModal()`. A custom overlay sets `inert` on the
  background plus `role="dialog"` and `aria-modal="true"`. Either way, move focus in on open and
  return it to the trigger on close.
- **Client-side route changes** reset nothing: update `document.title` and move focus to the new
  view's `<h1>` or `<main>`.
- **Errors that announce.** Validate on submit; never disable submit until the form is valid. Mark
  failing fields `aria-invalid="true"`, point `aria-describedby` at the inline error, focus the
  first invalid field.
- **Live regions.** `aria-describedby` for field-specific validation; a polite `role="status"` for
  non-urgent updates (toasts, result counts); `role="alert"` only for urgent errors not tied to a
  control. A repeated polite announcement needs a stable empty region rendered before its text
  updates. A toast carrying an action or an error stays until dismissed.
- **Accessible names.** Visible label text appears in the accessible name, so `aria-label` begins
  with it. `aria-hidden` never goes on a focusable element or an ancestor of one.
- **Alt text by purpose.** Decorative `alt=""`; informative describes the meaning; functional
  describes the action, not the picture.
- **Structure is navigation.** Headings that describe their sections, one visible primary
  `<main>`, a "Skip to content" link first when repeated chrome precedes it.
- **Zoom.** Never `maximum-scale=1` or `user-scalable=no`.
- **Focus rings.** A custom ring needs an explicit token and 3:1 against every adjacent colour,
  and preserves system colours in forced-colours mode.

| Pattern | Fix |
|---|---|
| `<div onClick>` or `<span onClick>` | `<button>`, or `<a href>` for navigation |
| `role="button"` or `role="tab"` with no key handler | Native element, or the full keyboard map |
| Positive `tabindex` | Fix the DOM order, use `0` |
| `disabled={!isValid}` on a submit button | Keep enabled, validate on submit |
| `aria-live="assertive"` on a success toast | `role="status"` |
| `aria-label` that omits the visible label text | Start the name with the visible text |
| `maximum-scale=1` or `user-scalable=no` | Remove it |
| Drag handler with no button alternative | Add a single-pointer path |

---

## Reporting a review

Group findings under the principle they break, most severe first, one row per root cause listing
every place it appears. Always `HIGH`: a missing accessible name, a missing focus indicator, a
pointer path with no keyboard path, motion that ignores reduced motion, clipping or overlap at
320 px or 200 percent zoom, content past a scroll edge with no cue, and meaning carried by colour
alone.

| Severity | Location | Before | After | Why (principle or criterion) |
|---|---|---|---|---|

Mark any check you could not run as `Not verified` (no browser, no accessibility tree), and never
approve coverage you did not inspect.
