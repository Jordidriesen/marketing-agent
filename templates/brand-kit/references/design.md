# Design: [Client Name]

Visual identity. Load with `context.md`; add `voice.md` when the asset carries copy.

**Source and date.** [Where these tokens come from (brand guidelines PDF, the live site's CSS, a
Figma library) and when they were checked. Never fill this in from memory: read the source.]

---

## Colour

| Token | Hex | Role |
|---|---|---|
| `accent` | [#000000] | [what it signals, where it's used] |
| `background` | [#000000] | [page or slide background] |
| `text` | [#000000] | [body text] |

[Usage rules: how much accent, what never to combine, colours that appear on the site but are
not brand colours.]

---

## Typography

| Use | Font | Settings |
|---|---|---|
| Body | [font] | [size, weight] |
| Headings / display | [font] | [size, weight, letter spacing] |

[Fallback for tools without the brand font, and any licence restriction.]

---

## Layout and components

| Token | Value |
|---|---|
| Container widths | [ ] |
| Spacing scale | [ ] |
| Buttons | [colour, radius, height] |

---

## Verification

The values `frontend-design` measures a page against (`references/verification.md`). Fill from
the source above, never from memory. A blank row is reported as `Not verified`, not guessed.

| Item | Value |
|---|---|
| Viewports to test (name, width, height, phone-class or not) | [ ] |
| Performance budgets (LCP, layout shift, page weight) | [ ] |
| What must be visible without scrolling (selectors) | [ ] |
| Smallest touch target | [ ] |
| Analytics and ad hosts to record but not send | [ ] |
| Tag hosts that must fire, and that must not | [ ] |

Design rules to measure, one per line, each with the selectors and colours it needs (for example
"primary buttons are always filled", "call to action sits at the bottom of its card"):

[ ]

---

## Logo and distinctive assets

[Logo versions, clear space, minimum size, what never to do with it; taglines, handles, any
asset that should repeat unchanged.]

---

## Imagery

[Photography style, illustration rules, what to avoid.]

---

## Tokens as CSS custom properties

```css
:root {
  --[brand]-accent: [#000000];
  --[brand]-background: [#000000];
  --[brand]-text: [#000000];
  --[brand]-font-body: "[font]", sans-serif;
}
```

---

## Do and don't

[Short lists.]

If visual identity isn't documented yet, say so plainly at the top of this file rather than
leaving it silently empty.
