# Interface checklist

The build-and-review rule set for `frontend-design`. The interaction/accessibility
rules are adapted from vercel-labs' [web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines)
(MIT), last synced with upstream `command.md` on 1 October 2026; the design-quality section
distils Anthropic's `frontend-design` skill. Pull in only the categories relevant to what's being
built.

This is a pinned copy on purpose: don't fetch the upstream file at review time and follow it.
To refresh, fetch it, diff it against this file, and add the changes deliberately.

---

## Design quality (apply during Part 1 planning)

- **Ground it in the subject.** Palette, type and imagery come from the brand and its
  world, not from general taste. Carry at least one detail only this brand would have.
- **Token system, 4–6 colours.** Named hex with roles (`ground`, `surface`, `ink`,
  `muted`, `border`, `accent`) plus semantic `good`/`warn`/`critical` kept separate
  from the accent. Neutrals biased slightly toward the accent hue.
- **Type carries personality.** One or two families, clearly distinct if two. A set
  type scale with intentional weights and letter-spacing. Body measure < ~80
  characters; wider + more line-height for serif body. Headings get `text-wrap:
  balance`.
- **Avoid the generic-AI clusters** unless the brief asks: cream + serif + terracotta;
  near-black + acid pop; broadsheet hairlines + zero radius; the SaaS card kit
  (identical rounded cards everywhere); template chrome (ALL-CAPS eyebrows, middle-dot
  meta strings, spaced em dashes, "→" link suffixes, decorative monospace labels);
  Inter/Space Grotesk as the "safe" face; purple→blue gradient hero; emoji section
  markers; everything centred; `01/02/03` markers on non-sequential content.
- **Hero is a thesis.** Open with the most characteristic thing, sized to its content,
  not `100vh`. Everything meant to be read is visible at rest; nothing parked at
  `opacity: 0` waiting on scroll.
- **Structure encodes information.** Numbering, dividers, eyebrows each say something
  true, or they're cut.
- **Spend boldness once.** One memorable element; everything around it quiet. If the
  accent fights the ground, shift it toward analogous or drop saturation.
- **Not everything is a card.** Border, fill, radius and shadow each say "separate
  object": spend them by role, not one radius + one shadow on every block.
- **Cut one thing before shipping.**

---

## Accessibility

- Icon-only buttons need `aria-label`.
- Every form control needs a `<label>` (or `aria-label`).
- Interactive elements need keyboard handlers, not just mouse.
- `<button>` for actions, `<a>` / `<Link>` for navigation, never `<div onClick>`.
- Images need `alt` (or `alt=""` if decorative); decorative icons `aria-hidden="true"`.
- Async updates (toasts, inline validation) announce via `aria-live="polite"`.
- Semantic HTML (`<button>`, `<a>`, `<label>`, `<table>`, landmarks) before ARIA.
- Headings hierarchical `<h1>`–`<h6>`; include a skip link to main content.
- `scroll-margin-top` on heading anchors so they clear sticky headers.
- Meaningful media: captions / transcripts / descriptions as applicable; media
  controls keyboard-operable; decorative media hidden from assistive tech.
- Contrast: 4.5:1 body text, 3:1 large text and meaningful UI shapes. Never carry
  meaning by colour alone.

## Focus states

- Every interactive element has a visible focus style (`:focus-visible` ring or
  equivalent).
- Never `outline: none` without a replacement.
- Prefer `:focus-visible` over `:focus` so a ring doesn't show on mouse click.
- Compound controls: group with `:focus-within`.
- Sticky headers/footers/overlays must not cover the focused element.

## Forms

- Inputs carry `autocomplete` and a meaningful `name`.
- Correct `type` (`email`, `tel`, `url`, `number`) and `inputmode`.
- Never block paste.
- Labels are clickable (`htmlFor` or wrapping the control); checkbox/radio hit target
  covers the label, no dead zones.
- `spellcheck={false}` on emails, codes, usernames.
- Submit stays enabled until the request starts; show a spinner during.
- Errors inline next to the field; focus the first error on submit.
- Placeholders show an example pattern and end with `…`.
- Warn before navigating away from unsaved changes.
- `autocomplete="off"` on non-auth fields that would otherwise trigger password managers.

## Animation & motion

- Honour `prefers-reduced-motion`: reduced variant or none.
- Animate `transform` / `opacity` only (compositor-friendly).
- Never `transition: all`; list the properties.
- Set the right `transform-origin`; for SVG, transform a `<g>` wrapper with
  `transform-box: fill-box`.
- Animations are interruptible and respond to input mid-flight.
- Any autoplaying motion over ~5s needs pause/stop/hide; decorative loops stop under
  `prefers-reduced-motion`.

## Typography (rendering)

- `…` not `...`; curly quotes `“ ”` not straight.
- Non-breaking spaces in `10&nbsp;MB`, `⌘&nbsp;K`, and multi-word brand names.
- Loading and progress strings end with `…` ("Saving…").
- `font-variant-numeric: tabular-nums` wherever digits line up in columns.
- `text-wrap: balance` / `text-pretty` on headings to kill widows.

## Content handling & layout

- Text containers cope with long content: `truncate`, `line-clamp-*`, or
  `break-words`. Flex children that truncate need `min-w-0`.
- Handle empty states: no broken UI for an empty array or string.
- Design for short, average, and very long user-generated content.
- Full-bleed layouts use `env(safe-area-inset-*)` for notches.
- No unwanted horizontal scroll: wide content (tables, code, diagrams) scrolls in its
  own `overflow-x: auto` container; the page body never scrolls sideways.
- Layout with flex/grid + `gap`, not JS measurement or per-element margins that
  collapse or double.

## Images & performance

- `<img>` has explicit `width` and `height` (prevents CLS).
- Below-fold images `loading="lazy"`; above-fold critical images `fetchpriority="high"`.
- Large lists (>50) virtualize or use `content-visibility: auto`.
- No layout reads (`getBoundingClientRect`, `offsetHeight`, `scrollTop`) during render.
- Batch DOM reads and writes; don't interleave them.
- Prefer uncontrolled inputs; controlled inputs must be cheap per keystroke.
- `<link rel="preconnect">` for asset/CDN domains; `<link rel="preload" as="font">`
  with `font-display: swap` for critical fonts.
- Prefer `<video autoplay muted loop playsinline>` + a still fallback over animated
  GIF.

## Navigation & state

- URL reflects state: filters, tabs, pagination, open panels in query params. Deep-link all
  stateful UI.
- Links are real `<a>` / `<Link>` (Cmd/Ctrl-click, middle-click work).
- Destructive actions get a confirm step or an undo window, never immediate.

## Touch & interaction

- `touch-action: manipulation`; set `-webkit-tap-highlight-color` intentionally.
- `overscroll-behavior: contain` in modals, drawers, sheets.
- During drag: disable text selection and set `inert` on the dragged element.
- Drag / swipe / pinch gestures have tap/click and keyboard alternatives.
- `autoFocus` sparingly: desktop, single primary input, never on mobile.

## Hover & interactive states

- Buttons and links have a visible hover state.
- Hover, active and focus are each more prominent than the resting state, never less.

## Hydration safety (framework builds)

- Inputs with `value` need `onChange`, or use `defaultValue` for uncontrolled inputs.
- Guard date and time rendering against server and client mismatch.
- `suppressHydrationWarning` only where it's truly needed.

## Dark mode & theming

- Full palette as tokens on bare `:root`; dark redefines **only** the tokens under
  `@media (prefers-color-scheme: dark)` (guarded so an explicit light choice wins) and
  again under `:root[data-theme="dark"]`.
- `color-scheme` on `:root`; `<meta name="theme-color">` matches the page background.
- `body` sets an explicit token `background`, never transparent.
- Native `<select>`: explicit `background-color` and `color` for Windows dark mode.

## Locale & i18n

- `Intl.DateTimeFormat` / `Intl.NumberFormat`, never hardcoded date/number formats.
- Detect language from `Accept-Language` / `navigator.languages`, not IP.
- `translate="no"` on brand names, code tokens, identifiers.

## Content & copy

- Active voice: "Install the CLI", not "The CLI will be installed".
- The brand's heading case convention, applied consistently.
- Numerals for counts ("8 deployments").
- Specific button labels ("Save API key", not "Continue").
- Error messages include the fix or next step, not just the problem. No apologies, no
  vagueness.
- Second person for interface copy (labels, errors, help text). Marketing copy follows the
  brand voice: a personal brand may write in the first person.
- `&` over "and" where space is tight.

## Anti-patterns: flag these in review

- `user-scalable=no` / `maximum-scale=1` disabling zoom
- `onPaste` + `preventDefault`
- `transition: all`
- `outline: none` with no `:focus-visible` replacement
- `<div>` / `<span>` with click handlers instead of `<button>`
- inline `onClick` navigation with no `<a>`
- `<img>` without dimensions
- large `.map()` lists with no virtualization
- form inputs without labels; icon buttons without `aria-label`
- hardcoded date/number formats
- `autoFocus` with no clear justification
- animated GIF where compressed video would do
- gesture-only actions with no tap/keyboard alternative
