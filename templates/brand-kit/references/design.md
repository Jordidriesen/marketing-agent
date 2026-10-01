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
