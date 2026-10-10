---
name: newsletter-writer
description: "Draft a single, one-off marketing email or newsletter, announcement, update, promotion, or roundup, with subject line options, preview text, and a clear body structure, in the right brand voice. Use for \"write a newsletter,\" \"draft an email,\" \"announcement email,\" \"promo email,\" or \"email update.\" Not for a multi-email lifecycle sequence (see email-sequence-hubspot-brevo) and not for web page copy (see web-content-pipeline)."
metadata:
  version: 1.1.0
  history: >
    v1.1: added a structural-framework step (Step 3) citing
    content-references/references/communication-frameworks.md, a one-off
    email still needs a deliberate PAS / BLUF choice by purpose rather
    than a default body shape. CTA guidance points at
    behavioral-psychology.md.
---

# Newsletter Writer

Drafts one standalone marketing email, not a lifecycle sequence.

**Scope:** A single send: an announcement, product update, promotion, or content roundup. For a multi-email onboarding/nurture/re-engagement/win-back flow with branching logic, use `email-sequence-hubspot-brevo` instead.

## Step 1: Identify the Brand

Same pattern as `web-content-pipeline`: determine the brand/client, check for a matching `[brand]-brand-kit` skill, load it if found (its voice overrides the generic tone below). If none exists, ask for tone or default to clear/conversational/professional.

## Step 2: Gather Requirements

| Field | Input |
|---|---|
| Brand/client | Determines which brand kit applies |
| Purpose | Announcement, update, promotion, roundup, re-send of existing content |
| Audience/list | Who receives this send, and what they already know |
| Key message | The one thing this email needs to communicate |
| Primary CTA | The one action the email should drive |
| Offer/incentive | Discount, deadline, or exclusive access, if any |

## Step 3: Pick a Structural Framework

The body shape follows the purpose, not habit. Definitions are in `content-references/references/communication-frameworks.md`; the choice for a one-off email:

| Purpose | Framework | Why |
|---|---|---|
| Promotion / deadline / drive a click | **PAS** (Problem → Agitate → Solution) | Loss aversion: the reliable structure for short conversion sends |
| Announcement / product update | **BLUF** (inverted pyramid) | The news in sentence one; detail in descending importance: matches how people skim an inbox |
| Content roundup / digest | **Numbered / scannable list** | No persuasion arc; each item earns its own line and link |

For the CTA itself, button verb, framing, risk reduction near the ask, see `content-references/references/behavioral-psychology.md`.

## Step 4: Write the Email

- **Subject line**: 2-3 options, under ~50 characters where possible, varying curiosity/benefit/urgency
- **Preview text**: 40-90 characters, complements (does not repeat) the subject line
- **Greeting**: personalization token if available
- **Body**: 2-3 scannable sections following the Step 3 framework, each with a bold intro sentence; short paragraphs
- **Primary CTA**: one clear, visually distinct action; button text follows [action verb] + [what they get]
- **Sign-off**
- **Footer**: unsubscribe link, company info, social links

Mobile-first: assume most opens are on a phone. Test-worthy elements: subject line, send time, CTA copy.

## Step 5: Copy Edit and Humanize

Run `copy-editing` (Seven Sweeps), then the humanising pass, `ai-content-cleaner`, in BALANCED mode if the email has structured sections worth preserving, CLEAN mode for a short promotional send.

## Output

- Subject line options (2-3) with a one-line rationale each
- Preview text
- Full email body, ready to paste into any ESP
- Note on brand voice and structural framework applied

Ask: "Would you like a version for a different segment, or should this become the first email in a sequence?" (If the latter, hand off to `email-sequence-hubspot-brevo`.)

## Related Skills

- `[brand]-brand-kit`: loaded in Step 1
- `content-references` (`communication-frameworks.md`, `behavioral-psychology.md`): Step 3; `ai-content-cleaner`: Step 5
- `email-sequence-hubspot-brevo`: for a multi-email flow instead of a single send
- `copy-editing` / `ai-content-cleaner`: Step 5
- `content-creation`: the gateway skill; routes here when the content type is a one-off email/newsletter
