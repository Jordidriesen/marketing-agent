---
name: brand-kit-template
description: "TEMPLATE, not a usable skill. Copy the whole brand-kit folder to [client-slug]-brand-kit/, rename the name field, fill every [PLACEHOLDER] in SKILL.md and the three reference modules, then delete this notice. The finished skill is the single entry point for a brand: other skills load [client-slug]-brand-kit and it routes them to context, voice or design. It should trigger on 'write this for [Client]', 'use the [Client] voice', 'review this against the [Client] brand', 'design this in [Client] style', or any [Client] brief."
metadata:
  version: 2.0.0
  history: >
    v2.0: split from one monolithic SKILL.md into a router plus three
    modules (references/context.md, voice.md, design.md), matching the
    personal-brand-kit pilot.
---

# [Client Name] Brand Kit: TEMPLATE

Delete this callout once the kit is filled in. This folder defines the shape every
`[client]-brand-kit` skill follows: a short router (this file) and three modules. Copy the
folder, rename it and the `name:` field to `[client-slug]-brand-kit`, replace every
`[PLACEHOLDER]`, and delete any section that genuinely doesn't apply rather than leaving it
half-filled.

Keep this file short. It decides which module a task needs; the substance lives in the modules.

## Which module, for which task

| Task | Load |
|---|---|
| Any writing or editing for [Client] | `references/context.md` + `references/voice.md` |
| Reviewing or cleaning existing copy | `references/voice.md` (its Voice Lock outranks generic rules) |
| Visual or design work, front-end, Canva or Figma assets | `references/design.md` + `references/context.md` |
| Copy baked into a designed asset | all three |
| SEO, analytics, paid media reporting | `references/context.md` (Data sources, KPIs) |
| Translation or localisation | `references/voice.md` (Locked Terminology) + `references/context.md` (markets) |

## Non-negotiables

[Three to five rules that hold in every module: language variant, banned punctuation or words,
legal must-haves. Repeat them here so a skill that reads only this file still gets them right.]

## Related skills

List the other skills in this plugin that this brand kit should combine with, and
how — e.g. which content-production skill identifies the brand and auto-loads this
kit, which localization skill should carry Locked Terminology across locales, which
skills this kit adds "you-first" language or customer-outcome framing on top of.

## Open items for [Client]

If any part of this kit is Claude's construction rather than a client-confirmed
brand document (a first draft built from a brief, or values inferred rather than
stated), list exactly what still needs sign-off here. Delete this section once
everything is confirmed.
