# Component system

How to build components so pages reuse them instead of restyling them. This file holds method
only. Every value (colours, type, spacing, radii, breakpoints, sizes, budgets) comes from the
project's design system or the brand kit's `design.md`, never from here.

The method is adapted in outline from the ideas in the `build-design-system` skill of
`arla6ka/design.how`. No text was copied; that repository states no licence.

## 1. Where a value comes from

In order: the project's own design system or UI rules (`AGENTS.md`, `CLAUDE.md`, a component
library), then the brand kit's `design.md`, then the token system drafted in Part 1 of `SKILL.md`.
If a value is needed and none of these has it, log a gap and ask. Do not fill it from taste, from
this skill, or from a similar site.

## 2. Tokens by role

- Name a token by what it is for, never by what it looks like.
- Pair every surface token with the foreground token that sits on it, so contrast is decided once.
- Every raw value inside a component maps to a token or to a listed exception. A raw colour, size
  or font in a component is a defect, not a shortcut.
- Merging near-identical values is a decision with a tolerance taken from the design system and
  recorded in the handover. Where it states no tolerance, ask.

## 3. Build by family, most used first

1. Count what the project already uses and group it into families (action, field, card, tag,
   navigation, section). Start with the family used most and the text primitives it needs.
2. Each family gets three things before any page consumes it: a registry row (name, variants,
   props or slots, where it is used), a doc, and a showcase entry that renders every state:
   default, hover, focus, disabled, error, loading, empty, long text and translated length.
3. Show the family to the person before other pages depend on it.

## 4. Behaviour and combinations

- **Behaviour table.** For an interactive component, one row per event: what changes, and the
  check that proves it.
- **Tone matrix.** Cross every pressable or row component with each status tone the design system
  defines. An empty cell is logged as a gap or marked unsupported, never left blank.

## 5. Gaps are logged, never patched

A page that needs something the system lacks logs a gap row and the primitive is built. It is not
patched with a one-off rule inside the page. Where the project forbids page-specific styles, this
is how the rule is kept: pages compose components, and components own their styles.

## 6. Checks over reminders

- Turn each rule the system states into a check: a lint rule on code, or a rule in the
  verification config (`verification.md`, rule types) that measures the rendered page.
- A rule counts only after it has been seen failing on a planted violation. The engine's
  `--self-test` proves the rule types; a rule added to a client config is proven on a deliberately
  broken copy or on staging.
- An allowlist of known exceptions may only shrink.
- A fix that recurs twice becomes a check or a script, not another sentence in a skill.

## 7. Stacks

- **Page builders and block themes.** A component is the builder's global widget, block pattern,
  template part or theme component. Pages assemble them; the registry lists them by those names.
- **Component frameworks.** A component is the framework's own unit, following the project's
  conventions.
- **No component layer yet.** Do not add a library or system the project does not have unless the
  user asks (`SKILL.md`, Step 1). Say what a component layer would give, and wait.

## 8. Extracting a system from an existing site

Measure what the site ships (Step 0, dembrandt, or the stylesheet), cluster raw values by role,
and propose tokens. The proposal goes to the design system owner as a decision. Nothing the site
does not already use is invented, and nothing measured is presented as the brand's intent.

## 9. Handover

Report coverage as counts, each tied to the check that produced it: raw values mapped, components
documented, states shown, gaps open, exceptions listed. A number without its source is not
reported.
