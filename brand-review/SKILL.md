---
name: brand-review
description: "Review content against brand voice and screen it for legal/compliance risk — unsubstantiated claims, missing disclaimers, comparative claims, testimonial issues — before it ships. Automatically identifies the brand and loads its `[brand]-brand-kit` skill, if one exists, so the review applies that brand's actual voice rules rather than generic guidelines. Use when checking a draft before it ships, auditing copy for voice consistency, or screening for compliance risk. For structural/persuasion editing of copy that already reads correctly for the brand, see copy-editing instead."
---

# Brand Review

Reviews content against brand voice and flags legal/compliance risk. This is a gate before publishing, distinct from `copy-editing` (which improves craft and persuasion) — a piece can pass copy-editing's Seven Sweeps and still fail brand-review on voice drift or an unsubstantiated claim.

## Step 1 — Identify the Brand and Load Its Kit

Same pattern as `web-content-pipeline`: determine which brand/client the content is for (from the brief, conversation context, or by asking if unclear), check for a matching `[brand]-brand-kit` skill, and load it if found.

- **If found:** apply its voice, terminology, and banned-language rules as the standard for this review — they override the generic Voice Attribute framework below.
- **If not found:** fall back to the generic review below, and note that documenting this brand's voice as a `[brand]-brand-kit` skill is worth doing if review requests for it recur — see the "Brand Kit Pattern" section of an existing `[brand]-brand-kit` skill for the shape to follow, if you have one.

## Step 2 — Review Dimensions

### With a brand kit loaded
Evaluate against that kit's actual pillars/attributes, its banned-language list, its terminology table, and its quality checklist directly — do not substitute a generic framework when a specific one exists. Flag any sentence that fails one of the kit's own "Do/Don't" examples.

### Without a brand kit (generic fallback)

**Voice and Tone** — consistent formality and personality throughout; no jarring shifts.

**Terminology and Language** — consistent terms (no synonym-switching); jargon level appropriate to audience; product/feature names capitalized correctly.

**Clarity and Professionalism** — main message clear in the first paragraph; free of typos and awkward phrasing; claims are supported.

## Step 3 — Legal and Compliance Flags (always checked, brand kit or not)

- **Unsubstantiated claims** — superlatives ("best," "fastest," "only") without evidence or qualification
- **Missing disclaimers** — financial, health, or guarantee claims that may need one
- **Comparative claims** — competitor comparisons that could be challenged
- **Testimonial issues** — quotes or endorsements without attribution or disclosure
- **Copyright concerns** — content closely paraphrased from another source

## Output Format

### Summary
Overall assessment, biggest strength, most important improvement — 1-2 sentences each.

### Detailed Findings

| Issue | Location | Severity | Suggestion |
|---|---|---|---|

Severity: **High** (contradicts brand voice, compliance risk, or undermines messaging), **Medium** (inconsistent with guidelines, not damaging), **Low** (minor style/preference).

### Revised Sections
Before/after for the top 3-5 highest-severity issues.

### Legal/Compliance Flags
Listed separately with recommended action.

## After Review

Ask: "Would you like me to revise the full content with these suggestions applied, focus on just the high-severity issues, or review another piece against the same brand?"

## Related Skills

- `[brand]-brand-kit` — a brand-specific skill following this naming pattern, loaded in Step 1 when one exists; defines the actual standard this review checks against
- `copy-editing` — for structural/persuasion editing once voice and compliance are confirmed clean
- `web-content-pipeline`, `social-content-writer`, `newsletter-writer`, `press-release-writer`, `customer-story-writer` — the content skills whose output this reviews before publishing
- `content-creation` — the gateway skill that produces the content this reviews