# Motion

Motion rules for `frontend-design`, scoped to marketing pages, landing pages and WordPress sites.
Adapted and rewritten from Emil Kowalski's [emil-design-eng](https://github.com/emilkowalski/skills)
and jakubkrehel's [better-ui](https://github.com/jakubkrehel/skills), both MIT. Gestures, springs,
drag and product-app interaction are left out on purpose.

**Precedence.** The brand kit and `taste.md` come first. The motion setting in `taste.md` section 2
decides how much a page moves; this file decides how each movement is built. Where two sources gave
slightly different numbers, one value is picked here. Values are starting points to judge by eye,
not laws.

---

## 1. Decide whether it animates

| How often the user sees it | Decision |
|---|---|
| Every interaction (nav hover, row hover, tab switch, keyboard action) | Instant, or at most 150 ms on `opacity` or `background-color` |
| Several times per visit (menus, accordions, dropdowns) | Short, standard transition |
| Once per visit (hero entrance, section reveal, first load) | Can carry expression |
| Rare moments (success state, empty state, celebration) | Can add delight |

Every animation answers "why does this move?": spatial continuity, a state change, feedback to a
press, or explaining how something works. "It looks cool" on something seen often is not a reason.
Every animated state change also leaves a static cue (colour, icon or label); motion is never the
only feedback. Never animate keyboard-initiated actions.

## 2. Easing and duration

| Case | Easing |
|---|---|
| Entering or exiting | `ease-out` (starts fast, feels responsive) |
| Moving or morphing on screen | `ease-in-out` |
| Hover or colour change | `ease` |
| Constant motion (marquee, progress) | `linear` |
| Default | `ease-out` |

Never `ease-in` for interface motion: it starts slow, and the first moment is the one the user is
watching. The built-in CSS curves are weak, so define project tokens, for example:

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
}
```

| Element | Duration |
|---|---|
| Press feedback | 100 to 160 ms |
| Tooltips, small popovers | 125 to 200 ms |
| Dropdowns, accordions | 150 to 250 ms |
| Modals, drawers | 200 to 500 ms |
| Page-level entrances | up to 400 to 600 ms, once |

Interface transitions stay under 300 ms. Speed changes perceived performance more than the
clock does: a 180 ms menu feels more responsive than a 400 ms one.

## 3. Build rules

- **Transitions, not keyframes, for anything the user can trigger repeatedly or reverse.**
  Transitions retarget mid-flight; keyframes restart from zero. Keyframes are for sequences that
  run once (a hero entrance).
- **Name the properties.** `transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out)`.
  Never `transition: all`.
- **Animate `transform` and `opacity` only.** Never `top`, `left`, `width`, `height`, `margin` or
  `padding`.
- **Never animate from `scale(0)`.** Start at `scale(0.95)` with `opacity: 0`.
- **Press feedback:** `:active` scales the pressable element to 0.96 or 0.97, 150 ms, `ease-out`,
  one value site-wide. A disabled control never scales (`:not(:disabled):active`).
- **Origin-aware popovers** scale from their trigger. Modals stay centred.
- **Enter with `@starting-style`** where browser support allows; otherwise a `data-mounted`
  attribute set after first paint.
- **Blur to hide a rough crossfade:** a small `filter: blur(2px)` while two states overlap reads as
  one object. Under 20 px, and sparingly in Safari.
- **Skip state animations on first render.** The default state of a toggle or tab does not animate
  in on load. An intentional hero entrance does.
- **`will-change` only after you see first-frame stutter,** naming the property (`transform`,
  `opacity`), never `all`.
- **Theme switch:** disable transitions for the swap, force a style flush and restore them next
  frame, or every colour transition fires at once and the switch smears.

## 4. Entrances and exits

- Stagger an entrance only where sequence carries hierarchy (title, description, actions). Split
  content into semantic chunks, 40 to 100 ms apart, each moving 8 to 12 px with `opacity`. Keep
  total stagger short, never block interaction while it plays, never stagger routine interactions.
- Exits are shorter and smaller than entrances: about 150 ms, a small fixed offset and `opacity`,
  not the full container height. Slide fully out only where the destination means something (a
  drawer closing). Remove instantly where motion adds nothing.
- Asymmetry rule: slow where the user is deciding, fast where the system is responding.
- Everything meant to be read is visible at rest. Nothing parked at `opacity: 0` waiting on a
  scroll trigger that may not fire (see the hero rule in `interface-checklist.md`).

## 5. Reduced motion and touch

- Movement, scale and blur run only under `@media (prefers-reduced-motion: no-preference)`. Under
  reduced motion, replace them with an `opacity` crossfade rather than removing the element
  instantly. Reduced does not mean zero: keep fades and colour changes that aid comprehension.
- Parallax, autoplay and looping decoration are off under reduced motion.
- Anything moving, blinking or updating on its own for more than 5 seconds needs a visible pause
  control (WCAG 2.2.2).
- Hover-only styling sits behind `@media (hover: hover) and (pointer: fine)`, otherwise `:hover`
  latches after a tap on touch and reads as a stuck selected state. Set
  `-webkit-tap-highlight-color: transparent` where the control draws its own pressed state.
- Scrollable dialogs, drawers and menus get `overscroll-behavior: contain`.

## 6. Cohesion

Match motion to the brand. A playful brand can be bouncier; a contractor or an enterprise security
company should be crisp and quiet. The easing, duration and visual design should feel like one
decision. Review motion the next day with fresh eyes, and replay it at 10 to 25 percent speed to
spot two states overlapping, a wrong origin or properties out of sync.

## Review table

| Pattern | Fix |
|---|---|
| `transition: all` | Name the properties |
| `scale(0)` entrance | `scale(0.95)` with `opacity: 0` |
| `ease-in` on interface motion | `ease-out` or a project curve |
| Duration over 300 ms on a small interface element | 150 to 250 ms |
| `animation:` on `:hover` or a toggled class | A transition on the same properties |
| `:active` scale below 0.96, or on a disabled control | 0.96 to 0.97, exclude `:disabled` |
| Hover effect with no `@media (hover: hover)` | Wrap it |
| Movement with no `prefers-reduced-motion` guard | Gate it, crossfade under reduced motion |
| Animating `top`, `left`, `width` or `height` | `transform` |
| Colour transitions plus a theme toggle, no suppression | Suppress on switch |
| Content hidden until a scroll animation fires | Visible at rest |
| `will-change: all`, or on an element that never animates | Name the property or delete it |
