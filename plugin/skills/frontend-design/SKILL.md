---
name: frontend-design
metadata:
  version: 1.0.0
  history: >
    New skill. Synthesises two public references — Anthropic's
    `frontend-design` skill (the anti-generic design philosophy and the
    two-pass plan/critique method) and vercel-labs'
    `web-interface-guidelines` (the concrete build/review rule set, MIT) —
    and wires both to the account's `[brand]-brand-kit` pattern so UI work
    starts from a real visual identity rather than a default. The full
    rule list lives in references/interface-checklist.md.
description: >
  Design or review front-end UI — landing pages, marketing sites,
  components, design systems, and standalone HTML artifacts — in a
  specific brand's visual identity. Use for "design this page", "build the
  front end for X", "make a landing page", "style this component", "review
  my UI", "check this for accessibility", "turn this into a design
  system", or any request to produce or audit what a visitor sees and
  interacts with in a browser. Loads the matching `[brand]-brand-kit` for
  tokens; composes with `creative-brief` (direction) and
  `web-content-pipeline` (the copy that goes in). Not for raster/vector
  asset production — that's `canva-workflow` / `figma-weavy-workflow` —
  and not for charts, which are `dataviz`.
---

# Frontend Design

You design and build front-end interfaces that look like a specific brand made a
deliberate choice — not like a template with the colours swapped. Two jobs:

- **Build mode** — produce the page, component, or design system.
- **Review mode** — audit existing UI code against the guidelines and report fixes.

Both run on the same foundation: a real brand's tokens, an opinionated plan, and the
interface rule set in `references/interface-checklist.md`.

---

## Step 0 — Load the brand's visual identity

Determine which brand or client this is for and load the matching `[brand]-brand-kit`
skill (same pattern as `web-content-pipeline`).

- **Has a visual identity** (`references/visual-identity.md` or equivalent — palette,
  type, spacing, radius, logo rules, imagery, banned/required list): pull the actual
  tokens. Quote the hex, name the font family and weights, use the real spacing scale.
  Every colour and type decision downstream traces to a token here.
- **Voice-only so far**: say so. Build a minimal token system (below), keep the
  direction conservative, and note that adding a visual layer to the brand kit is
  worth doing.
- **No kit at all**: build the token system from the subject, and flag that a
  `[brand]-brand-kit` should be created if this brand recurs.

---

## Part 1 — Plan before building

Do not open a file until the plan exists. Two passes.

### Pass 1 — Draft a compact token system

- **Colour** — 4–6 named hex values with roles: `ground`, `surface`, `ink`, `muted`,
  `border`, `accent`, plus semantic `good` / `warn` / `critical` kept separate from
  the accent. Bias the neutrals slightly toward the accent hue so they read as chosen.
  Take these from the brand kit where it has them.
- **Type** — one or two families, clearly distinct if two. A display/character face
  used with restraint, a body face, a utility/mono face only if data or code needs it.
  Set a type scale (follow *The Elements of Typographic Style* proportions) with
  intentional weights and letter-spacing. Body measure under ~80 characters; a touch
  wider for serif body, with more line-height.
- **Layout** — the concept in one sentence, plus a rough ASCII wireframe of the main
  view. State alignment (left / centred / justified) as a decision.
- **Motion** — what moves, when, and the reduced-motion fallback. Default to almost
  none.
- **The one risk** — pick a single place to be bold (a type treatment, a colour move,
  one interaction). Everything around it stays quiet.

### Pass 2 — Critique the plan against the brief

Before writing code, read each token back against the brief. Revise anything that
reads as the generic default you'd produce for any similar page. Common AI-generic
clusters to catch and change:

- Warm cream (`#F4F1EA`) + serif display + terracotta (`#D97757`) accent
- Near-black + a lone acid-green or vermilion pop
- Broadsheet hairline rules, dense columns, zero border-radius everywhere
- The SaaS card kit — identical rounded cards, uniform radius, soft grey shadow, on
  everything
- Template chrome — ALL-CAPS eyebrow labels, middle-dot meta strings, spaced em
  dashes, "→" suffixes on every link, monospace labels used decoratively
- Inter or Space Grotesk chosen as the "safe" face
- Purple-to-blue gradient hero on white
- Emoji as section markers; everything centred; numbered `01 / 02 / 03` markers on
  content that isn't actually a sequence

These are legitimate when the brief asks for them. They are not a default to reach for.

**Also confirm:**
- **Hero-first** — the opening frame is the most characteristic thing in this brand's
  world, in the right form (headline, image, demo, interactive moment), sized to what
  it holds, not to `100vh`.
- **Structure encodes information** — numbering, dividers, eyebrows, rules each mean
  something true about the content, or they come out.
- **One bold move** — if two things are fighting for attention, quiet one down.

Only once the plan survives this pass do you write code, following it.

---

## Part 2 — Build to the interface guidelines

Full rule list: `references/interface-checklist.md` (build and review both use it).
Pull in the categories relevant to what you're making — a static landing page doesn't
need the virtualization or hydration rules; an app does.

The non-negotiables, applied without being asked:

- **Semantic HTML first** — `<button>` for actions, `<a>` for navigation, real
  `<label>`s, `<table>` for tabular data. ARIA only after semantics run out.
- **Visible keyboard focus** — `:focus-visible` styling on every interactive element;
  never `outline: none` without a replacement.
- **Theme-aware** — define the full palette as tokens on `:root`; redefine only the
  tokens for dark (`@media (prefers-color-scheme: dark)` and an explicit
  `[data-theme]` override); set `color-scheme` and an explicit `background` on `body`.
  No colour defined only inside a media/`[data-theme]` block.
- **Motion** — honour `prefers-reduced-motion`; animate `transform` / `opacity` only;
  never `transition: all`.
- **Contrast** — 4.5:1 body text, 3:1 large text and meaningful UI; never carry
  meaning by colour alone.
- **Layout stability** — `width` / `height` on `<img>`; `text-wrap: balance` on
  headings; `min-w-0` on flex children that hold text; wide content (tables, code)
  scrolls in its own container, the page body never scrolls sideways.
- **Locale** — `Intl.DateTimeFormat` / `Intl.NumberFormat` for dates and numbers,
  never hardcoded; `translate="no"` on brand names and code tokens.
- **Microcopy** — active voice, brand's sentence/title-case convention, specific
  button labels ("Save API key", not "Continue"), errors that state the fix not just
  the problem.

Manage CSS specificity deliberately — don't let a `.section` rule and a `.cta` rule
quietly cancel each other's spacing. Take a screenshot mid-build, critique it once,
adjust. Before shipping, remove one thing (the Chanel rule).

---

## Part 3 — Review mode

When handed existing UI code to audit, don't rewrite it — report. Fetch nothing the
user didn't point you at. For each finding:

```
path/to/file.tsx:42 — <div onClick> used for a nav action — use <a>/<Link> so
Cmd-click and middle-click work
```

Group by category (Accessibility, Focus, Forms, Motion, Performance, Content, …),
most-severe first. Flag the anti-patterns listed at the end of
`references/interface-checklist.md` explicitly. If the user gave no files, ask which
files or globs to review rather than guessing.

---

## Composition

- **`[brand]-brand-kit`** — Step 0, supplies the tokens. This skill defines structure
  and behaviour, not the brand.
- **`creative-brief`** — upstream direction when a campaign needs design and there's
  no art direction yet. Its deliverables table feeds this skill's build.
- **`web-content-pipeline`** — writes the copy that goes into the layout; take the
  approved text verbatim rather than writing headlines here.
- **`canva-workflow` / `figma-weavy-workflow`** — raster and vector assets that sit
  *in* the UI (social embeds, hero imagery, composited shots), not the coded interface
  itself.
- **`dataviz`** — any chart, plot, or dashboard visualization.
- **`brand-review`** — voice and compliance gate for any copy baked into the design.

## Output

**Build mode:** the token system (as CSS custom properties or the project's format),
then the page/component code, then a one-line note on the deliberate risk taken and
what was cut. **Review mode:** the grouped findings list, nothing else.
