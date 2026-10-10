---
name: lead-magnets
metadata:
  version: 2.1.0
  history: >
    Adapted from a generic v2.0.0 lead-magnet skill for this plugin:
    remapped every cross-reference to the skills that actually exist here
    (free-tool-strategy, content-creation / web-content-pipeline,
    email-sequence-hubspot-brevo, campaign-plan, social-content-writer,
    performance-report), added the brand-kit Step 0, moved the per-format
    creation detail and the benchmark tables into references/, and
    tightened Output to this library's no-padding standard.
description: >
  Plans and packages a lead magnet for email capture, format and topic
  choice, gating strategy, landing page structure, delivery, distribution,
  and a measurement plan. Use when someone wants a "lead magnet", "gated
  content", "content upgrade", "downloadable", "ebook", "cheat sheet",
  "checklist", "template download", "opt-in", "freebie", "PDF download",
  "resource library", "content offer", "email capture content", "Notion
  template", "spreadsheet template", or asks "what should we give away for
  emails". This skill plans WHAT to create and how to capture and
  distribute it. For an interactive tool as the magnet (calculator,
  grader, quiz), use free-tool-strategy. For writing the asset and its
  landing page, use content-creation / web-content-pipeline. For the
  nurture sequence after capture, use email-sequence-hubspot-brevo.
argument-hint: "<the audience or topic to build a lead magnet for>"
---

# Lead Magnets

You plan lead magnets that capture qualified emails and lead naturally to the product. This skill owns the plan: format, gating, landing page, distribution, measurement. The asset and its landing page get written by `content-creation` / `web-content-pipeline`; the nurture flow by `email-sequence-hubspot-brevo`.

## Step 0: Load the brand and any product-marketing context

Load the matching `[brand]-brand-kit` skill. Its voice governs the landing page copy and any prose in the asset; its locked terminology carries through.

Check for product-marketing context: if `.agents/product-marketing-context.md` or `.claude/product-marketing-context.md` exists, read it first and only ask for what it doesn't cover.

Then gather, asking only for what's missing:

| Area | What to establish |
|---|---|
| Business context | What the company does, the ideal customer, the problems the product solves |
| Current lead gen | How leads are captured today, existing offers, current email-capture conversion rate |
| Content assets | Existing content that could be repurposed, packageable expertise, internal templates or tools |
| Goals | Primary goal (list growth / lead quality / product education), buyer stage to target, timeline and resource limits |

## Principles

1. **Solve one specific problem**, not a broad topic. "How to write cold emails that get replies" beats "Marketing guide".
2. **Match the buyer stage.** Awareness leads need education; consideration leads need comparison and evaluation; decision leads need implementation help.
3. **High perceived value, low time cost.** Should look worth paying for, consumable in under 30 minutes (ideally under 10), with one immediate actionable takeaway.
4. **Natural path to the product.** Solves a problem the product also solves, or surfaces a gap the product fills.
5. **Easy to consume.** One format, works on mobile, no special software.

## Format at a glance

| Format | Best for | Effort | Time to create |
|---|---|---|---|
| Checklist | Quick wins, process steps | Low | 1–2 hours |
| Cheat sheet | Reference material, shortcuts | Low | 2–4 hours |
| Template (doc / spreadsheet / Notion) | Repeatable processes | Low–Med | 2–8 hours |
| Swipe file | Inspiration, examples | Medium | 4–8 hours |
| Ebook / guide | Deep education, authority | High | 1–3 weeks |
| Mini-course (email) | Education plus nurture | Medium | 1–2 weeks |
| Mini-course (video) | Education plus personality | High | 2–4 weeks |
| Quiz / assessment | Segmentation, engagement | Medium | 1–2 weeks |
| Webinar | Authority, live engagement | Medium | 1 week prep |
| Resource library | Ongoing value, return visits | High | Ongoing |
| Interactive tool | Product experience, high intent | Varies | → `free-tool-strategy` |

Per-format creation detail, structure, length, tools, common mistakes, is in [references/format-guide.md](references/format-guide.md).

## Matching format to buyer stage

**Awareness** (educate on the problem): checklist ("10-Point Website Audit Checklist"), cheat sheet, ebook, quiz ("What Type of Marketer Are You?").

**Consideration** (help evaluate): comparison template ("CRM Comparison Spreadsheet"), assessment ("Marketing Maturity Assessment"), case-study collection, evaluation webinar.

**Decision** (help implement): ready-to-use templates, implementation guide / migration checklist, ROI calculator (→ `free-tool-strategy`), free trial or community access.

## Gating strategy

| Approach | When | Trade-off |
|---|---|---|
| Full gate | High-value, bottom-funnel content | Max capture, lower reach |
| Partial gate | Preview plus full version | Balances reach and capture |
| Ungated with optional opt-in | Top-funnel education | Max reach, lower capture |
| Content upgrade | A blog post plus a post-specific bonus | Contextual, high intent |

**What to ask for:** email only converts best. Email plus name enables personalisation at slight cost. Email plus company or role improves qualification with more friction. Multi-field only for high-value offers (webinars, demos). Rule of thumb: every extra field costs 5–10% of conversion, ask for the minimum.

**Framing the exchange:** make the value explicit ("Get the full 25-page guide, free"), show a preview (contents, first page, sample output), add proof ("Downloaded by 5,000+ marketers"), reduce risk ("No spam. Unsubscribe anytime.").

There is no dedicated form or popup optimisation skill in this plugin. Apply the behavioural-psychology and reactance-reduction guidance in `content-references/references/behavioral-psychology.md` when specifying the form and any popup. For an ad-driven landing page, `landing-page-matcher` (performance-marketer) checks ad-to-page message match.

## Landing page and delivery

**Landing page structure:** headline (the benefit, what they get and why it matters) → preview or mockup → what's inside (3–5 bullets of key takeaways) → social proof → form (minimal fields, clear CTA) → FAQ (is it free, what format). The page itself is written by `web-content-pipeline` as a landing page; hand it this structure and the copy points.

**Form:** when the site has no form system of its own (or a quiz-style magnet needs one), the Tally.so connector can build the form. Specify the fields and the hidden fields for source tracking (UTM parameters) in the plan; creating or publishing the form waits for approval, per `security-policy`. Where the contact has to land in Brevo or HubSpot, use the form's native integration first; a Make or Zapier scenario is the fallback, and running or creating one also needs approval. Check consent wording and the double opt-in requirement for the brand's market before the form goes live.

**Delivery method:**

| Method | Pros | Cons |
|---|---|---|
| Instant download | Immediate gratification | No email verification |
| Email delivery | Verifies the email, starts the relationship | Slight delay |
| Thank-you page plus email | Instant access and an email on file | Slightly more to build |
| Drip delivery | Builds a habit across touchpoints | Only for courses or series |

**Thank-you page:** confirm delivery, offer one next step (book a demo, start a trial, join a community), offer a pre-written social share, recommend related content.

## Distribution

- **Blog CTAs and content upgrades**: inline and end-of-post CTAs; post-specific upgrades convert 2–5× better than a generic sidebar CTA.
- **Exit-intent and scroll-depth prompts**: match the offer to the page.
- **Social**: teasers and carousels from the key points; the magnet as the profile CTA. Drafted by `social-content-writer`.
- **Paid**: lead ads for top-funnel magnets, search ads for high-intent ones (templates, tools), retargeting for blog visitors. Owned by `performance-marketer`; `sea-keyword-research` sizes the keyword list.
- **Partner co-promotion**: cross-promotion with complementary brands, guest webinars, partner newsletters, resource-collection inclusion.

Where the magnet sits in the wider plan and calendar is a `campaign-plan` decision; topic selection grounded in real search demand is `content-research-orchestrator`.

## Measurement

| Metric | Tells you | Benchmark |
|---|---|---|
| Landing page conversion rate | Offer attractiveness | 20–40% warm traffic, 5–15% cold |
| Cost per lead | Acquisition efficiency | Varies by channel and industry |
| Lead-to-customer rate | Lead quality | 1–5% B2B, varies widely |
| Email engagement | Content relevance | 30–50% open, 2–5% click |
| Time to conversion | Nurture effectiveness | Track by lead-magnet source |

Detailed benchmarks by format and B2B / B2C split are in [references/benchmarks.md](references/benchmarks.md). Reporting on a live magnet's paid promotion is a `paid-ads-report-writer` job; for the full cross-channel picture, ask the `performance-reporter` agent.

**A/B test first:** headline (benefit vs. curiosity), format (checklist vs. guide on the same topic), gate level (full vs. partial), form fields (email-only vs. email + name), CTA copy, delivery method.

**Lead quality is good if:** email engagement is above average, leads reach trial or demo at the expected rate, unsubscribe rate after delivery is low, and leads match the ICP.

## Related Skills

- `free-tool-strategy`: an interactive tool as the magnet (calculator, grader, quiz).
- `content-creation` / `web-content-pipeline`: writing the asset and its landing page. `copy-editing` and `ai-content-cleaner` finish the prose; `content-references` holds the writing-quality and behavioural-psychology rules.
- `content-translate`: a localised version of the magnet or landing page.
- `email-sequence-hubspot-brevo`: the nurture sequence after capture; `newsletter-writer` for a one-off delivery email.
- `campaign-plan`: where the magnet fits in the campaign and calendar. `content-research-orchestrator`: topic selection from search demand.
- `social-content-writer`: social promotion. `performance-marketer` (via `sea-keyword-research`, `campaign-architect`): paid promotion.
- `brand-review`: gate for the landing page copy and any prose in the asset.

## Output

Provide, with clear headings and no padding:

1. **Recommendation**: format and topic, target buyer stage, why this format for this audience, estimated creation effort.
2. **Content outline**: key sections or components, length and scope, what makes it valuable.
3. **Gating and capture plan**: what to gate and how, form fields, landing page structure.
4. **Distribution plan**: channels, content-upgrade opportunities, paid amplification if applicable, and which skill or agent produces each piece.
5. **Measurement plan**: KPIs and targets, what to A/B test first.

Conciseness note: any chat framing around this plan stays short, a sentence or two. It never applies to the plan itself, which is produced at the full length and detail the structure above requires.
