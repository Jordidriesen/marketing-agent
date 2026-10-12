---
name: frontend-design
metadata:
  version: 2.1.0
  history: >
    v1.0: synthesised Anthropic's frontend-design skill (anti-generic
    philosophy, two-pass plan and critique) and vercel-labs'
    web-interface-guidelines (MIT), wired to the [brand]-brand-kit pattern.
    v2.0: folded in Leonxlnx's taste-skill and redesign-skill (MIT) as
    references/taste.md (design read, three settings, locks, AI tells,
    pre-flight check) and references/redesign-protocol.md (mode detection,
    audit, never-change-silently list, fix order), both rewired so the brand
    kit outranks their defaults and so no figure or image is ever invented
    for a live page. Refreshed references/interface-checklist.md against the
    current upstream guidelines as a pinned copy instead of fetching rules at
    review time. Loads modular brand kits' references/design.md.
    v2.1: added references/type-and-colour.md (adapted from jakubkrehel's
    better-typography and better-colors, MIT), references/motion.md (from
    emil-design-eng and better-ui, MIT), references/layout-and-accessibility.md
    (from better-layout, better-accessibility and better-ui, MIT). taste.md
    gained asset dependence and brand fidelity reads, a brand-assets-first rule
    and critique dimensions (from web-design-engineer, MIT). The em dash
    punctuation advice in better-typography was dropped to keep the library's
    no em dash rule.
description: "Designs, builds or reviews web UI in the brand's visual identity: landing page layouts, sites, WordPress pages and themes, components, accessibility. Use for \"design this page\", \"review my UI\". Page copy: web-content-pipeline."
---

# Frontend Design

You design and build front-end interfaces that look like a specific brand made a deliberate
choice, not like a template with the colours swapped. Three jobs:

- **Build mode:** produce a new page, component or design system.
- **Redesign mode:** upgrade an existing site or page without breaking what works.
- **Review mode:** audit existing UI and report fixes, without rewriting.

All three run on the same foundation: the brand's real tokens, a stated design read, and the
references:

| Reference | Use it for |
|---|---|
| `references/taste.md` | The design read, the three settings (variance, motion, density), the locks, the AI tells, the build pre-flight check |
| `references/redesign-protocol.md` | Redesign mode: mode detection, audit, what never changes silently, fix order |
| `references/interface-checklist.md` | The build and review rule set: accessibility, focus, forms, motion, performance, theming, copy |
| `references/type-and-colour.md` | Type scale, line-height, measure, wrapping, punctuation; colour ramps, semantic tokens, contrast measurement, dark mode |
| `references/motion.md` | Whether and how to animate: frequency, easing, durations, entrances and exits, reduced motion, hover on touch |
| `references/layout-and-accessibility.md` | Grouping, alignment, responsive structure, translation growth, surfaces and icons, WCAG 2.2 criteria and ARIA additions |

---

## Step 0: Load the brand's visual identity

Determine which brand or client this is for and load its `[brand]-brand-kit` skill (same
pattern as `web-content-pipeline`).

- **Modular kit:** load `references/design.md` (and `references/context.md` for audience and
  channels). Older kits keep visual identity in `references/visual-identity.md` or inline.
- **Has a visual identity:** pull the actual tokens. Quote the hex, name the font family and
  weights, use the real spacing scale and radius. Every colour and type decision downstream
  traces to a token there.
- **Voice only so far:** say so. Build a minimal token system (Part 1), keep the direction
  conservative, and note that a design module for the kit is worth doing. When the type choice
  is open, the Adobe for creativity connector can propose and check pairings (`font_recommend`,
  `suggest_type_palettes`, `font_preview`); confirm the font's web licence before it ships.
- **No kit at all:** build the token system from the subject, and flag that a
  `[brand]-brand-kit` should be created if this brand recurs.

**Precedence.** The brand kit outranks every default in this skill and its references. A brand
whose identity is a cream background, a serif or a dark theme keeps it: the "generic" lists in
`taste.md` describe defaults to avoid when nothing has been decided, not brands to correct.

---

## Step 1: State the design read and the mode

Following `taste.md` section 1, state in one line what this is, for whom, in which language, on
which stack. Then set the three settings (section 2).

Decide the mode: new build, redesign (preserve or overhaul, per `redesign-protocol.md`), or
review. If the read or the mode genuinely forks, ask one question; otherwise proceed.

**Work with the existing stack.** A WordPress site gets theme settings, block patterns or the
site's own MCP (for example NovaMira), not a React rebuild. If the site is managed in WP Umbrella,
read its installed plugins, theme and performance there first (`list_plugins`, `list_themes`,
`get_performance`); that is read-only and needs no approval. A Claude artifact gets one
self-contained HTML file. A framework project keeps its framework and styling system.

---

## Part 1: Plan before building

Do not open a file until the plan exists. Two passes.

### Pass 1: Draft a compact token system

- **Colour:** 4 to 6 named hex values with roles: `ground`, `surface`, `ink`, `muted`, `border`,
  `accent`, plus semantic `good`, `warn`, `critical` kept separate from the accent. Take them from
  the brand kit wherever it has them.
- **Type:** one or two families, clearly distinct if two. A display face used with restraint, a
  body face, a mono face only if data or code needs it. A set type scale with intentional weights
  and letter-spacing (`type-and-colour.md`). Body measure 60 to 75 characters.
- **Layout:** the concept in one sentence, plus a rough ASCII wireframe of the main view. State
  alignment as a decision.
- **Motion:** what moves, when, why (the motivation rule in `taste.md`; values in `motion.md`),
  and the reduced-motion fallback.
- **The one risk:** a single place to be bold. Everything around it stays quiet.

### Pass 2: Critique the plan against the brief

Read each token and layout choice back against the brief and the brand. Revise anything that
reads as the generic default you'd produce for any similar page: check it against `taste.md`
sections 3 to 5 (defaults to reach past, the four locks, layout discipline).

**Also confirm:**
- **Hero first:** the opening frame is the most characteristic thing in this brand's world,
  sized to what it holds, and it fits the first viewport.
- **Structure encodes information:** numbering, dividers, eyebrows and rules each say something
  true about the content, or they come out.
- **One bold move:** if two things fight for attention, quiet one down.

Only once the plan survives this pass do you write code.

---

## Part 2: Build

Build to the plan, pulling the relevant categories from `references/interface-checklist.md`, and
the type, colour, motion and layout rules from the other references as the page needs them. A
static landing page doesn't need the virtualisation or hydration rules; an app does.

The non-negotiables, applied without being asked:

- **Semantic HTML first:** `<button>` for actions, `<a>` for navigation, real `<label>`s,
  `<table>` for tabular data. ARIA only after semantics run out.
- **Visible keyboard focus** on every interactive element; never `outline: none` without a
  replacement.
- **Theme-aware tokens:** the full palette on `:root`; dark mode only when the brand or brief
  calls for it, and then redefine tokens only (`prefers-color-scheme` plus a `[data-theme]`
  override); explicit `background` on `body`.
- **Motion:** honour `prefers-reduced-motion`; animate `transform` and `opacity` only; never
  `transition: all`.
- **Contrast:** 4.5:1 body text, 3:1 large text and meaningful UI, including every button and
  form field; never carry meaning by colour alone.
- **Layout stability:** `width` and `height` on `<img>`; `min-height: 100dvh` rather than
  `100vh`; wide content scrolls in its own container, never the page body.
- **Locale:** `Intl` formats for dates and numbers; `translate="no"` on brand names.
- **Content:** copy comes from the approved piece. No invented figures, quotes, customers or
  images that could pass as the client's real work (`taste.md` sections 6 and 7). No em dashes
  in visible text.

Take a screenshot mid-build, critique it once, adjust. Run the pre-flight check in `taste.md`
section 9 before handing over. Before shipping, remove one thing.

---

## Part 3: Redesign mode

Follow `references/redesign-protocol.md`: detect the mode, audit before touching, respect the
never-change-silently list (URLs, navigation labels, form fields, logo, legal copy, FAQ and
other structured content), then fix in priority order and stop when the brief is satisfied.
Hand back the audit, the changes in order, and the decisions left for the user.

On a live site, change a staging copy or drafts and ask before publishing.

---

## Part 4: Review mode

When handed existing UI to audit, don't rewrite it: report. Review only what the user pointed
you at. For each finding:

```
path/to/file.tsx:42  <div onClick> used for a nav action; use <a> so Cmd-click and
middle-click work
```

Group by category (Accessibility, Focus, Forms, Type, Colour, Layout, Motion, Performance,
Content, Design), most severe first. Cite the WCAG 2.2 criterion for accessibility findings
(`layout-and-accessibility.md`); anything without one is a recommendation, never `HIGH`. Say
`Not verified` for any check you could not run, and do not approve what you did not inspect.
Flag the anti-patterns at the end of `interface-checklist.md` and the AI tells in
`taste.md` section 8 explicitly. If the user gave no files or URL, ask which to review rather
than guessing.

---

## Composition

- **`[brand]-brand-kit`:** Step 0, supplies the tokens. This skill defines structure and
  behaviour, not the brand.
- **`creative-brief`:** upstream direction when a campaign needs design and there's no art
  direction yet. Its deliverables table feeds this skill's build.
- **`web-content-pipeline`:** writes the copy that goes into the layout; take approved text
  verbatim.
- **`canva-workflow`, `figma-weavy-workflow`:** raster and vector assets that sit in the UI, not
  the coded interface itself.
- **`dataviz`:** any chart, plot or dashboard visualisation.
- **`brand-review`:** the voice and compliance gate for any copy baked into the design.
- **`seo-audit`:** before a redesign that touches templates, URLs or structured data.

## Output

**Build mode:** the design read and settings in one line each, the token system (as CSS custom
properties or the project's format), then the code, then a one-line note on the deliberate risk
taken and what was cut. **Redesign mode:** the audit, the changes in fix order, open decisions.
**Review mode:** the grouped findings list, nothing else.
