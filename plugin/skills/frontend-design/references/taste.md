# Taste: direction, settings and AI tells

Design direction for `frontend-design`. Adapted from Leonxlnx's
[taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), cut down to what applies to this
library's work (landing pages, marketing sites, WordPress block themes, HTML artifacts) and
rewired so the brand kit always wins.

**Precedence, before anything below.** Every rule in this file is a default for when the brand
hasn't decided. A loaded brand kit's `references/design.md` (or `visual-identity.md`) outranks all
of it: if the brand uses a cream background, a serif, a dark theme or a particular accent, that is
the brand, not an AI tell. Several of the "generic" palettes and fonts listed here are some real
brand's identity. Apply these rules to the choices the brand leaves open.

**Scope.** Landing pages, marketing sites, portfolios, blog and editorial layouts, redesigns. Not
dashboards, data tables, multi-step forms or app UI: say so and use only the parts that apply.

---

## 1. Read the brief before designing

Read these signals first:

1. **Page kind:** landing (B2B, consumer, agency, event), portfolio, editorial or blog, redesign.
2. **Vibe words** the user used: "minimal", "calm", "premium", "playful", "serious B2B",
   "editorial", "brutalist".
3. **References:** URLs, screenshots, named products or competitors.
4. **Audience:** a procurement panel, a design-conscious consumer, a local customer looking for a
   contractor. The audience picks the aesthetic, not taste.
5. **Existing brand assets:** logo, colours, type, photography. Starting material, never optional.
6. **Quiet constraints:** accessibility-first audiences, public sector, regulated industries,
   trust-first commerce. These override aesthetic preference.

Then state one line before building:

> Reading this as: *page kind* for *audience*, with a *vibe* language, built on *stack*.

If the read genuinely forks (for example calm editorial versus experimental agency), ask one
question. If it doesn't, state the read and proceed.

---

## 2. Three settings

Set three values from 1 to 10 after the design read, and let them drive layout, motion and density.

| Setting | 1 to 3 | 4 to 7 | 8 to 10 |
|---|---|---|---|
| **Variance** (layout) | Symmetrical grid, equal padding, centred | Offsets and overlaps, mixed image ratios, left-aligned headers | Asymmetric grids, masonry, large empty zones |
| **Motion** | Hover and active states only | CSS transitions, staggered entrances, `transform` and `opacity` | Scroll-driven reveals, pinned sections, choreography |
| **Density** | Gallery: generous section gaps | Standard site spacing | Packed data: hairline separators, tabular figures |

Starting points:

| Brief | Variance | Motion | Density |
|---|---|---|---|
| Minimal, calm, editorial | 5 to 6 | 3 to 4 | 2 to 3 |
| Premium consumer | 7 to 8 | 5 to 7 | 3 to 4 |
| Agency, experimental | 9 to 10 | 8 to 10 | 3 to 4 |
| B2B landing page | 6 to 7 | 4 to 6 | 4 to 5 |
| Trust-first, public sector, local services | 3 to 4 | 2 to 3 | 4 to 5 |
| Redesign, preserve | match the existing site | +1 | match |
| Redesign, overhaul | +2 | +2 | match |

Rules that go with them:

- Above variance 4, asymmetric layouts collapse to a single column under 768px. Declare that
  fallback per section.
- **Motion claimed, motion shown.** Above motion 4, the page has to move (entrances, reveals,
  hover feedback). If working motion doesn't fit the scope, drop to 3 and ship a clean static page.
- **Motion must be motivated:** hierarchy, sequence, feedback or a state change. "It looked cool"
  is not a reason.
- Anything above motion 3 honours `prefers-reduced-motion`; loops, parallax and pinned scroll
  collapse to static.

---

## 3. Defaults to reach past

Unless the brief or the brand asks for them:

- Purple-to-blue "AI gradient" heroes, neon glows, gradient text on large headings.
- Centred hero over a dark mesh; three equal feature cards in a row.
- Inter as the safe default face; a serif chosen only because the brief says "premium" or
  "creative". If a serif is justified, emphasise within one family (italic or bold of the same
  face) rather than dropping a different font into a headline.
- The warm cream, brass and espresso palette as the reflex for anything premium.
- Pure `#000000`; oversaturated accents; more than one accent colour on a page.
- Cards everywhere. Use a card only when elevation means something; otherwise group with space,
  a rule or a background tint. Tint shadows towards the background hue.
- Custom cursors.

---

## 4. Locks: one of each per page

- **Theme lock.** One theme for the whole page. No single section flipping from light to dark
  mid-scroll unless it is a deliberate, one-off composition. Dark mode is built when the brand or
  the brief calls for it; when it is built, tokens are defined for both modes and tested.
- **Colour lock.** One accent, used identically everywhere. No blue button in section seven of an
  orange page.
- **Shape lock.** One corner-radius system (sharp, soft or pill), or a documented rule such as
  "buttons pill, cards 16px, inputs 8px" applied everywhere.
- **CTA lock.** One label per intent. "Get in touch", "Contact us" and "Let's talk" on one page is
  three labels for one action: pick one.

---

## 5. Layout discipline

- **Hero fits the first viewport:** headline at most 2 lines on desktop, subtext at most about
  20 words, CTA visible without scrolling. If it doesn't fit, reduce the type scale or cut copy.
- **Hero holds at most four text elements:** an optional eyebrow, the headline, the subtext,
  one primary and at most one secondary CTA. Trust logos, pricing teasers and feature bullets go
  in the section below.
- **Navigation on one line at desktop**, about 64 to 80px tall.
- **Eyebrows are rationed:** at most one small uppercase label per three sections. The headline
  usually does the job alone.
- **No layout family twice.** A page with eight sections uses at least four different layouts.
  At most two image-and-text zigzag sections in a row.
- **Bento grids:** exactly as many cells as there is content, no empty tile; at least two or three
  cells with real visual variation.
- **Long lists:** more than five items get a better component (grouped columns, cards, tabs,
  horizontal scroll) instead of a long list with a rule under every row.
- **Content density:** short headline, one short paragraph, one visual or one CTA per section
  by default. Testimonials at most three lines, attributed with name and role.
- Use `min-height: 100dvh` rather than `100vh` for full-height sections.

---

## 6. Images

- Follow the brand kit's imagery rules first. For the personal brand that means real photos over
  stock; for a contractor it means real projects, never a generated image presented as their
  work.
- Without real assets, leave clearly labelled placeholder slots (for example
  `<!-- placeholder: hero photo of a finished floor, 1600x1200 -->`) and list them at the end for
  the user. Neutral placeholder services are fine for mock-ups that are labelled as such.
- Generated imagery is for mood, texture and illustration, and only when the user is told it is
  generated. Never generate an image that could pass as the client's real product, team,
  customer or project.
- No fake product screenshots built from styled divs. Use a real screenshot, a real component,
  or editorial photography.
- Logo walls: real logos only, with permission to show them, nothing printed underneath.

---

## 7. Content and data: placeholders, never inventions

- **Live pages never carry invented figures, quotes, customers, dates or credentials.** Every
  number, testimonial and logo traces to the brief, the brand kit or a source the user gave. If
  the page needs a figure that doesn't exist yet, leave a marked gap and say so; `brand-review`
  will flag invented claims anyway.
- **Mock-ups and prototypes** may use sample content, but it must be visibly marked as sample
  (a comment, "Example" label, or the user's explicit go-ahead) so it can't ship by accident.
- Avoid the obvious placeholders ("John Doe", "Acme", lorem ipsum) in mock-ups: they read as
  unfinished. Use plausible, local sample names marked as samples.
- Copy in the layout comes from the approved piece (`web-content-pipeline`, `content-writer`),
  not invented here. Before shipping, re-read every visible string: anything broken, vague or
  cute-but-meaningless gets rewritten plainly or sent back.
- No em dashes anywhere visible: headlines, labels, buttons, captions, alt text, quotes.

---

## 8. AI tells to remove in review

Flag these when reviewing, and avoid them when building, unless the brief asks for them:

- Version labels in a marketing hero ("V0.6", "BETA") outside a real launch.
- Section-number eyebrows ("001 · Capabilities", "06 / how it works") and "01 / 4" counters on
  images.
- Middle dots as the separator for everything; decorative status dots on nav items and lists.
- Poetic micro-labels ("Field notes", "Quietly trusted by", "Currently on the bench").
- Decorative text strips across the bottom of the hero ("BRAND. MOTION. SPATIAL.").
- Scroll cues ("Scroll to explore") and locale or weather strips that aren't relevant.
- Tags or pills overlaid on photos; fake photo-credit captions.
- Version footers ("v1.4.2", "last sync 4s ago") on marketing pages.
- Split section headers with a tiny explainer paragraph floating top-right.
- Progress bars with filled grey tracks used as comparison visuals on a landing page.
- Generic step labels ("Stage 1", "Phase 01") instead of the step itself ("Install").

---

## 9. Pre-flight check (build mode)

- [ ] Design read stated; settings chosen and reasoned.
- [ ] Brand kit loaded; every colour, font and radius traces to it or to a stated decision.
- [ ] Theme, colour, shape and CTA locks hold across every section.
- [ ] Hero fits the first viewport; at most four text elements; nav on one line.
- [ ] No layout family repeated; eyebrows rationed; no empty bento cells.
- [ ] Every CTA, form field, label and placeholder passes contrast (4.5:1 body, 3:1 large text).
- [ ] No CTA label wraps on desktop.
- [ ] Motion motivated, reduced-motion handled, nothing animates `top`, `left`, `width` or
      `height`.
- [ ] Images real, or placeholders labelled and listed. Nothing generated that could pass as
      the client's real work.
- [ ] No invented figures, quotes, customers or dates on anything that could go live.
- [ ] No em dashes in visible text.
- [ ] The interface checklist's non-negotiables pass (`interface-checklist.md`).
