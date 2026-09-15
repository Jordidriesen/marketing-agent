---
name: brand-kit-template
description: >
  This is a TEMPLATE, not a usable skill. Copy this file to [client-slug]-brand-kit/SKILL.md,
  replace every [PLACEHOLDER] with the real client's brand details, then remove this
  notice. Once filled in, the resulting skill applies that client's tone of voice —
  and visual/design guidelines once documented — to any content task: website pages,
  landing pages, blog posts, email copy, social media, sales materials, case studies,
  product descriptions, or any other customer-facing or external communication for
  that client. It should trigger when the user says "write this for [Client]," "use
  the [Client] voice," "review this against the [Client] brand," "does this sound
  like [Client]," "apply [Client] tone/brand," or when working on any [Client]
  content brief.
metadata:
  version: 1.0.0
---

# [Client Name] Brand Kit — TEMPLATE

Delete this line and everything in this callout once the kit is filled in: this file
defines the shape every `[client]-brand-kit` skill in this plugin follows. Copy it,
rename the folder and the `name:` field to `[client-slug]-brand-kit`, replace every
`[PLACEHOLDER]`, and delete any section that genuinely doesn't apply to this client
rather than leaving it half-filled.

---

## Identity Summary

One paragraph: what the client does, who they serve, what makes their position
distinctive, and the single sentence that should anchor every tone decision below.
Example shape (not real content): "[Client] is a [industry] company serving
[audience] since [year] — [what makes them different from competitors in one
clause]. Every word or visual decision should reflect [the one thing the client
wants to be known for]."

If this is a first draft rather than a client-confirmed brand document, say so
explicitly here (see `chape-braspenning-brand-kit/SKILL.md` for the wording this
plugin uses when a brand kit hasn't been signed off yet) and list what still needs
confirming in a closing "Open Items" section.

---

## Language Standards

- Which English/Dutch/French/etc. variant and spelling convention applies
  (British English, Belgian Dutch/Flemish, fr-BE vs fr-FR, etc.) — never assume;
  state it explicitly.
- House terms: "customer" vs "client", or any other word the client has a fixed
  preference for.
- Formatting conventions (e.g. no em dashes) if the client or this plugin's general
  house style requires them.

### Locked Terminology

Only include this table if the client has fixed translations or naming for specific
terms across locales — delete the section if not.

| Term | [Locale A] | [Locale B] |
|------|------------|------------|
| [Example] | [Locked translation] | [Locked translation] |

---

## The [N] Pillars

Most brand kits in this plugin use three to five voice pillars. Name them, give each
one a one-line descriptor, then a short do/don't pair so the pillar is checkable,
not just aspirational.

### 1. [Pillar Name] — [One-line descriptor]

**Do:** [A real example sentence written in this pillar's voice]
**Don't:** [The generic or off-brand version of the same sentence]

### 2. [Pillar Name] — [One-line descriptor]

**Do:** [...]
**Don't:** [...]

Repeat for each remaining pillar.

---

## The Customer Hero Framework

(Rename this section if a different protagonist framing fits the client better —
e.g. a homeowner/professional split rather than an enterprise-buyer split.)

| Role | Who |
|------|-----|
| Hero | The customer ([name the actual buyer personas/roles]) |
| Challenge | [The problems they need to solve] |
| Guide | [The client, positioned as advisor rather than hero] |
| Plan | [What the client offers them] |
| Success | [What the customer achieves] |

If the client's default copy tends to centre the company rather than the customer,
include a short before/after table like this one:

| Context | Before (company-focused) | Now (customer-focused) |
|---------|---------------------------|--------------------------|
| [Example] | [Old framing] | [New framing] |

---

## Audience Calibration

How tone shifts by audience segment — e.g. technical buyer vs. budget holder vs.
end user — without breaking the core pillars. One short paragraph or table per
segment is usually enough.

---

## Channel Tone Calibration

How the pillars flex by channel (website vs. email vs. social vs. sales materials).
Note anywhere a channel needs a genuinely different register, not just a shorter
version of the same tone.

---

## SEO / Digital Writing Guidance

If this client has house rules for on-page writing (heading structure, metadata
tone, use of real search terms vs. invented terminology, active voice, etc.), list
them here. Delete if this duplicates general guidance already covered elsewhere in
the plugin and nothing client-specific applies.

---

## Crisis Communication

Optional. Only include if the client has specific guidance for how tone should
change under complaint-handling or crisis conditions.

---

## Banned Language

| Category | Banned |
|----------|--------|
| [e.g. Dismissive] | [Phrases to avoid] |
| [e.g. Timid] | [Phrases to avoid] |
| [e.g. Off-brand vocabulary] | [Specific words the client has flagged] |

---

## Quality Checklist

- [ ] **[Pillar 1 name]**: [what "on-brand" looks like for this pillar]
- [ ] **[Pillar 2 name]**: [...]
- [ ] Locked terminology used correctly for the target locale
- [ ] No banned language present
- [ ] Customer positioned as the hero, not the company

**Quick voice test:** [one fast heuristic a writer can apply without re-reading the
whole kit — e.g. "would [Client] actually say this out loud to a customer?"]

---

## Design & Visual Identity

If visual guidelines exist (colour palette, typography, imagery style, layout
conventions, logo usage, UI component patterns), document them here — either
inline for a short spec, or in a `references/visual-identity.md` file for a full
design-token-level spec (see `chape-braspenning-brand-kit/references/visual-identity.md`
for the shape a full spec takes: design tokens, colour derivation reasoning,
typography, layout/spacing, components).

If visual identity isn't documented yet, say so plainly rather than leaving the
section silently empty — future contributors need to know whether it's missing or
intentionally out of scope.

---

## Related Skills

List the other skills in this plugin that this brand kit should combine with, and
how — e.g. which content-production skill identifies the brand and auto-loads this
kit, which localization skill should carry Locked Terminology across locales, which
skills this kit adds "you-first" language or customer-outcome framing on top of.

---

## Open Items for [Client]

If any part of this kit is Claude's construction rather than a client-confirmed
brand document (a first draft built from a brief, or values inferred rather than
stated), list exactly what still needs sign-off here. Delete this section once
everything is confirmed.
