---
name: content-creation
description: "Entry point for any \"write marketing content\" request when the content type isn't yet specified, or when a request spans more than one type — e.g. \"turn this launch into a blog post, a LinkedIn post, and a press release.\" Determines which content type(s) are needed and routes each to its specialist skill, collecting shared inputs once rather than asking the same questions per piece. Use for \"create content,\" \"write marketing content,\" \"draft something for the launch,\" or any content request that doesn't already name a specific format skill."
---

# Content Creation

A router, not a writer. This skill classifies a content request by type and dispatches to the specialist skill for each type — it does not draft copy itself.

## Why this exists

Each content type has its own skill, tuned to that format's actual process (web pages get a brand-kit-aware, SEO/AEO-structured, copy-edited, humanized pipeline; a social post gets a much lighter pass). Routing through a single entry point means: shared inputs (brand, topic, key messages, audience) get collected once and passed to every specialist the request needs, instead of each one re-asking; and a multi-format request ("repurpose this across channels") produces a consistent set of pieces from one brief instead of drifting between them.

## Step 1 — Classify the Content Type(s)

| If the user wants... | Route to |
|---|---|
| A blog post, landing page, product/solution/feature page, homepage, pricing page, or about page | `web-content-pipeline` |
| A case study or customer success story | `customer-story-writer` |
| A social media post (LinkedIn, Twitter/X, Instagram, Facebook) | `social-content-writer` |
| A single/one-off marketing email or newsletter | `newsletter-writer` |
| A multi-email lifecycle sequence (onboarding, nurture, win-back, etc.) | `email-sequence-hubspot-brevo` |
| A press release | `press-release-writer` |
| Several of the above from one brief (a launch, a campaign) | Run each relevant specialist in turn, passing the shared inputs from Step 2 to each |

If the type is genuinely unclear from the request, ask directly rather than guessing: "What are we creating — a blog post, a landing page, a social post, an email, a press release, a case study, or a mix?"

## Step 2 — Collect Shared Inputs Once

Before dispatching to any specialist, gather what every content type will need, so the specialists don't re-ask:

| Field | Input |
|---|---|
| Brand/client | Which brand this is for (feeds each specialist's own brand-kit lookup) |
| Topic/announcement | What this content is about |
| Key message(s) | 2-4 main points every piece should communicate |
| Target audience | Who this is for |
| Goal | Awareness, traffic, leads, launch buzz, etc. |

Only ask for fields a chosen specialist actually needs beyond this (e.g. `press-release-writer` needs a quote source; `web-content-pipeline` needs a page type). Don't re-ask what Step 2 already collected.

## Step 3 — Dispatch and Assemble

Run each routed specialist skill with the shared inputs plus its own type-specific requirements. For a multi-format request, present the pieces together, each labeled by type, so the user can review the full set from one brief before requesting a specific piece be regenerated or adjusted.

## Related Skills

This skill's entire job is routing to these specialists — see each for its actual drafting process:

- `web-content-pipeline` — blog posts and all page types
- `customer-story-writer` — case studies
- `social-content-writer` — social posts
- `newsletter-writer` — one-off emails
- `email-sequence-hubspot-brevo` — lifecycle email sequences
- `press-release-writer` — press releases
- `campaign-plan` (marketing plugin) — for planning which pieces a campaign needs before this skill produces them
- `brand-review` — to check any produced piece against brand voice and compliance before it ships