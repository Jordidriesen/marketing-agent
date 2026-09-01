---
name: email-sequence-hubspot-brevo
description: Design and draft multi-email sequences (onboarding, lead nurture, re-engagement, win-back, product launch) built specifically for HubSpot Workflows or Brevo Automation, including full copy, timing, branching logic, exit conditions, and a platform-specific build checklist in the tool's actual menu/step names. Opens by asking which platform to build for. Use whenever building an email sequence, drip campaign, nurture flow, or automation for HubSpot or Brevo, or when the user says "email sequence," "workflow," "automation," "drip campaign," or names either platform.
---

# Email Sequence Builder — HubSpot & Brevo

Design and draft complete email sequences with full copy, timing, branching logic, and performance benchmarks — then translate the whole thing into the exact steps, menu names, and terminology of either **HubSpot Workflows** or **Brevo Automation**, so it can be built in the platform without re-interpreting anything.

## Trigger

User asks to create, design, build, or draft an email sequence, drip campaign, nurture flow, onboarding series, or automation/workflow, especially when HubSpot or Brevo is mentioned.

## Step 0: Choose the Platform

Before gathering anything else, ask which platform this sequence is being built for. If the user already named the platform in their request, skip straight past this and confirm it briefly instead of asking again.

Use a single-select question (via the elicitation tool if available):

- **HubSpot** — Marketing Hub Workflows
- **Brevo** — Automation workflows
- **Not sure — help me pick** — give a 3-4 line comparison (see below) and let them choose

If the user picks "not sure," a quick honest comparison:
- **HubSpot**: deeper branching (nested if/then, property + engagement + AI-suggested triggers), native A/B testing on automated emails (Pro/Enterprise), tightly bound to CRM data (lifecycle stage, deal/ticket objects) — better fit when the sequence needs to read or write CRM properties.
- **Brevo**: simpler visual builder, multi-channel steps in one workflow (email → SMS → WhatsApp), conditional splits and A/B split steps, but shallower nesting and no automatic A/B winner selection — better fit for straightforward lifecycle sequences without complex branching.

Check whether a HubSpot or Brevo MCP connector is already available in this conversation. If one is, mention that the sequence can be built directly in the account once drafted, not just handed over as instructions.

## Inputs

Gather the following. If not provided, ask before proceeding:

1. **Sequence type** — Onboarding, Lead nurture, Re-engagement, Product launch, Event follow-up, Upgrade/upsell, Win-back, or Educational drip.
2. **Goal** — what the sequence should achieve.
3. **Audience** — who receives it, what stage, any segmentation detail (role, industry, behaviour trigger, lifecycle stage).
4. **Number of emails** (optional) — otherwise recommend a count from the templates below.
5. **Timing/cadence** (optional) — e.g. "every 3 days," "weekly," "aggressive first week then taper."
6. **Brand voice** — apply automatically if configured locally; otherwise ask, or default to clear, conversational, professional.
7. **Additional context** (optional) — offers/discounts, CTAs or landing pages, existing content assets, features to highlight, competitor angles.

## Process

### 1. Sequence Strategy
- **Narrative arc** — the story across all emails, emotional/logical progression start to finish.
- **Journey mapping** — map each email to a buyer/user journey stage (awareness, consideration, decision, activation, expansion).
- **Escalation logic** — how urgency/value builds email to email.
- **Success definition** — the specific action that means the sequence has done its job and the contact should exit.

### 2. Individual Email Design

For each email, produce:

- **Subject line** — 2-3 options, varying curiosity/benefit/urgency/personalisation/question angles, under 50 characters where possible.
- **Preview text** — 40-90 characters, complements rather than repeats the subject.
- **Purpose** — one sentence on why this email exists.
- **Body copy** — full draft, hook/body/CTA structure, short paragraphs, scannable, personalisation tokens where relevant.
- **Primary CTA** — button text and destination; one primary CTA, secondary only if the stage warrants it.
- **Timing** — days after trigger or previous email; note any engagement-based adjustment.
- **Segment/condition notes** — who gets it, who skips it, and why.

### 3. Sequence Logic

- **Branching conditions** — e.g. "if opened email 2 but didn't click, send 2b instead of 3"; "if clicked in email 1, skip to email 3."
- **Exit conditions** — what conversion means for this sequence, and when a contact leaves.
- **Re-entry rules** — can someone re-enter, and under what condition.
- **Suppression rules** — don't send if already in another active sequence, unsubscribed, or recently contacted support.

### 4. Performance Benchmarks

| Metric | Onboarding | Lead Nurture | Re-engagement | Win-back |
|--------|-----------|--------------|---------------|----------|
| Open rate | 50-70% | 20-30% | 15-25% | 15-20% |
| Click-through rate | 10-20% | 3-7% | 2-5% | 2-4% |
| Conversion rate | 15-30% | 2-5% | 3-8% | 1-3% |
| Unsubscribe rate | <0.5% | <0.5% | 1-2% | 1-3% |

Adjust for industry/audience if context is available.

## Sequence Type Templates

**Onboarding (5-7 emails, 14-21 days):** Welcome and set expectations → Quick win → Core feature deep dive → Advanced feature/integration → Social proof and community → Check-in and feedback → Upgrade prompt or next steps

**Lead Nurture (4-6 emails, 3-4 weeks):** Value-first educational content → Pain point identification → Solution positioning with proof → Social proof and results → Soft CTA → Direct CTA

**Re-engagement (3-4 emails, 10-14 days):** "We miss you" → Value reminder → Incentive/exclusive offer → Last chance with deadline

**Win-back (3-5 emails, 30 days):** Friendly check-in → What's new → Special offer → Feedback request → Final goodbye

**Product Launch (4-6 emails, 2-3 weeks):** Teaser → Launch announcement → Feature spotlight → Social proof → Limited-time offer → Last chance

**Event Follow-up (3-4 emails, 7-10 days):** Thank you with takeaways/recordings → Resource roundup → Related offer → Feedback survey

**Upgrade/Upsell (3-5 emails, 2-3 weeks):** Usage milestone → Feature gap they're hitting → Upgrade benefits with proof → Limited-time incentive → Plan comparison

**Educational Drip (5-8 emails, 4-6 weeks):** Introduction → Lesson 1 (foundational) → Lesson 2 (intermediate) → Lesson 3 (advanced) → Practical application → Resource roundup → Graduation/next steps

## Platform Build Guide

Once the sequence is drafted, translate it into the chosen platform's actual build steps. Don't just say "set up branching" — name the exact HubSpot or Brevo feature being used.

### If HubSpot was chosen

- **Where to build it**: Automation → Workflows → Contact-based workflow (or the relevant object — deal/ticket-based if the sequence needs to react to pipeline or support data).
- **Enrollment trigger**: form submission, list membership, property change, or an AI-suggested trigger based on historical data.
- **Emails**: create each one under Marketing → Email → Create email → Automated, then add via the workflow's "Send email" action.
- **Branching**: use the **If/then branch** action (the `+` icon in the workflow) for each conditional split — e.g. branch on "opened email 2," "clicked link X," job title, lifecycle stage, or lead score. Branches can be nested for multi-level personalisation, but note a contact only travels down the *first* branch it matches — split into a second workflow if more parallel paths are needed.
- **Delays**: fixed intervals ("wait 3 days") or event-based waits ("wait until page visited").
- **Personalisation tokens**: `{{ contact.firstname }}`, `{{ contact.jobtitle }}`, `{{ company.name }}`, or custom tokens (Enterprise) — usable in the email body, subject, and CTAs.
- **A/B testing**: enable it in the email editor *before* publishing the automated email (Marketing Hub Pro/Enterprise); HubSpot distributes the 50/50 split gradually as contacts enroll and reports a winner. For testing anything beyond email content (e.g. timing, path), use a **Random split by percentage** branch instead.
- **Exit**: set unenrollment triggers and goals so contacts leave once they convert.
- **Re-entry**: configurable per workflow — decide if churned/returning contacts can re-enter.

### If Brevo was chosen

- **Where to build it**: Automation → Workflows → create workflow (drag-and-drop visual canvas).
- **Entry trigger**: contact creation/import, website/page-visit behaviour, custom event, form submission, tag or attribute change, or a date trigger (birthday/anniversary).
- **Steps available on the canvas**: Send Email, Time Delay (wait), Conditional Split (if/else), A/B Split, Update Contact, Add/Remove from List, Send SMS/WhatsApp, Webhook.
- **Branching**: drag a **Conditional Split** onto the canvas, add a filter (e.g. Email → Link Clicked, or a contact attribute), then build different actions down each path. Note Brevo's conditions are simpler than HubSpot's — no complex AND/OR nesting, so keep branches to single conditions or chain sequential splits.
- **A/B testing inside a workflow**: add an **A/B Split** step, which sends an even, alternating 50/50 split down two paths. Unlike HubSpot, **Brevo does not pick a winner automatically** — check Automations → Workflows → View Stats and compare the two paths against the sequence's goal manually.
- **Personalisation**: merge tags like `{{ contact.FIRSTNAME }}`, plus conditional content blocks to show/hide sections by segment.
- **Multi-channel**: a single workflow can chain Email → SMS → WhatsApp steps, which HubSpot handles as separate tools.
- **Re-entry**: a toggle in workflow Settings controls whether contacts can re-enter.
- **Exit**: no dedicated "goal" object like HubSpot — build exit logic as a Conditional Split that routes converted contacts to an end point or removes them from the triggering list.

### If no platform tool is connected in this conversation

Note this to the user, then deliver everything in copy-paste-ready format plus the build checklist above for their chosen platform, so they can follow it inside the tool directly.

## Output

### Sequence Overview Table

| # | Subject Line | Purpose | Timing | Primary CTA | Condition |
|---|-------------|---------|--------|-------------|-----------|

### Full Email Drafts
Each email with subject line options, preview text, purpose, body copy, CTA, timing, segment notes.

### Sequence Flow Diagram
Text-based diagram showing the flow, branches, and exits, e.g.:

```
[Trigger] --> Email 1 (Day 0)
                |
          Opened? --Yes--> Email 2 (Day 3)
                |              |
                No        Clicked CTA? --Yes--> [EXIT: Converted]
                |              |
                v              No
          Email 1b (Day 2)     |
                |              v
                +--------> Email 3 (Day 7)
                               |
                               v
                          Email 4 (Day 10)
                               |
                          [EXIT: Sequence complete]
```

### Platform Setup Checklist
A step-by-step list in the chosen platform's own terminology (drawn from the Platform Build Guide above), mapping every generic step in the flow diagram to the actual action/feature name.

### Branching Logic Notes
All conditions, exits, and suppressions as a reference list.

### A/B Test Suggestions
2-3 recommended tests (subject line, CTA, send time, length), what to split, how to measure the winner — noting whether the platform auto-picks a winner (HubSpot) or requires a manual check (Brevo).

### Metrics to Track
Primary conversion metric, per-email metrics (open, CTR, unsubscribe), sequence-level metrics (conversion rate, time to conversion, drop-off points), and a recommended review cadence.

## After the Sequence

Ask: "Would you like me to:
- Revise the copy or tone for a specific email?
- Add a branching path for a specific scenario, written out in [HubSpot if/then / Brevo conditional split] terms?
- Build a variant of this sequence for a different segment?
- Draft the A/B test variants for the subject lines?
- Build a companion sequence (e.g. a post-purchase follow-up once this one converts)?"
