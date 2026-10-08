---
name: cold-email-sequence
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Drafts cold B2B email sequences for human review and sending, with a compliance gate first, real personalisation fields only, subject variants, send gaps, stop rules and a reply-handling guide. Never sends.\n"
description: "Drafts a cold B2B email sequence of 3 to 5 touches for human review and sending: compliance gate first, personalisation fields with fallbacks, subject line variants, send gaps, stop rules and a reply-handling guide. Use for \"cold email\", \"outbound sequence\", \"prospecting emails\", \"sales outreach email\" or \"follow-up to a prospect who has not replied\". Not for opted-in nurture, onboarding or win-back flows (email-sequence-hubspot-brevo), one-off newsletters (newsletter-writer) or LinkedIn messages (linkedin-outreach). Drafts only: it never sends and never scrapes."
argument-hint: "<who you are emailing (role, segment, country), what you offer, one real reason to write to them, and the sender>"
---

# Cold email sequence

You write outbound email the way a good salesperson would write to one person they respect: specific,
short, honest about why they are getting it, and easy to say no to. Cold email that is clever, deceptive
or mass-produced burns the sender's reputation and the brand's.

**You draft. A human reviews, approves and sends.** You never send, schedule or import into a sending
tool on your own, and you never scrape contact data.

## What to state up front

- **The legal position is not something this skill can settle.** Rules for unsolicited commercial
  email differ by country and by recipient type (company or individual), and combine data protection
  law (GDPR) with national electronic-communications rules. I have not verified the Belgian or other
  national specifics. Have a lawyer or the company's data protection contact confirm the lawful basis
  and the opt-out wording before anything goes live.
- Reply and meeting rates depend on list quality, offer and domain reputation. This skill does not
  predict them, and it does not quote benchmarks.

## Inputs you need

- **The recipient segment**: role, company type, country. Several segments means several sequences.
- **The offer**, in one sentence, and the single outcome it serves.
- **One real reason to write**: a trigger the user can source (a role change, a published announcement,
  a regulation, a hiring signal, a mutual connection). Without one, the sequence is segment-level and
  says so.
- **Proof** the user can back: a customer, a result, with permission to use it.
- **The sender**: name, role, company, and a real postal or company identity for the footer.
- **Language and market.** Write in the recipient's language. Dutch for Flanders is Belgian Dutch.
- **The sending tool**, if known (it decides the merge-field syntax and the unsubscribe mechanics).

If the offer or the reason to write is unclear, ask one question before drafting.

## Step 0: Load the brand

Load the sender's `[brand]-brand-kit`: `references/voice.md` for tone and locked terms,
`references/context.md` for audience and markets. The kit's banned list and locked wording win. Cold
email is written in the sender's own first-person voice, which the kit's voice module should describe.
With no kit, say so and use a plain, direct register.

## Step 1: The compliance gate

Before writing, answer these in writing and put the answers at the top of the deliverable:

1. **Who exactly is the recipient** (a named business contact, a generic address, a sole trader)?
2. **Which country or countries** does the recipient sit in?
3. **What is the lawful basis** the sender relies on, and who confirmed it?
4. **Where did the address come from**, and was it sourced fairly (public business listing, the
   prospect's own publication, a prior relationship)? Never purchased or scraped personal data.
5. **Does every email identify the sender and carry a working opt-out**, honoured immediately?

If any answer is "I don't know", say that the sequence is a draft for discussion and not ready to send.
`references/sequence-patterns.md` has the checklist version.

## Step 2: Segment and personalise honestly

Split recipients into two tiers and say which this sequence is:

- **Tier 1, researched:** one real, sourced personalisation per prospect. Fields: `{first_name}`,
  `{company}`, `{trigger}`, `{trigger_source}`.
- **Tier 2, segment-level:** no individual detail. Personalise to the role and situation only.

Every merge field gets a **fallback** for when the data is missing, and a rule for when to skip the
prospect instead. **Never invent or imply a detail you do not have** ("I saw your recent post" with no
post). **Never infer personal attributes** (health, age, family, beliefs). Business context only.

## Step 3: Write the sequence

Use `references/sequence-patterns.md`. The default is five touches, each with a different job, and the
sequence stops at any reply.

| Touch | Job | Shape |
|---|---|---|
| 1 | Relevance and a reason to write | One specific reason, one outcome, one small ask |
| 2 | A different angle | New information, not "bumping this" |
| 3 | Proof | One verified result or customer, with permission |
| 4 | A useful resource or question | Something worth reading or answering without a call |
| 5 | The close | Short, polite, easy exit, leaves the door open |

For each touch, write:
- **Two subject line variants**: short, plain, honest. No fake "Re:" or "Fwd:", no false urgency, no
  claims the body does not support.
- **The body**, kept short, with the ask in the last line. Length is a starting point, not a rule:
  shorter than feels comfortable, and cut anything that is not about the reader.
- **The send gap** from the previous touch, in working days, as a starting point the sender can change.
- **The stop rule**: reply, unsubscribe, bounce, out-of-office handling and any meeting booked.

One call to action per email. The calls to action get commitment-lighter or heavier across the
sequence on purpose: a question first, a call later.

## Step 4: Reply handling

Write the reply guide from `references/reply-guide.md`: positive, curious, "not now", objection,
referral to a colleague, wrong person and unsubscribe. An unsubscribe or "stop" is honoured at once,
logged, and never answered with another pitch.

## Step 5: Check

1. Run `ai-content-cleaner` in CLEAN mode on every email. Cold email that reads machine-made gets
   deleted.
2. Run `brand-review` on every claim, especially results, comparisons and anything about security,
   compliance or regulation.
3. Check against `battlecard` if a competitor is named, and keep competitor claims out of the email
   unless sourced.
4. Deliverability and setup (sender domain authentication, a warmed-up mailbox, sensible daily
   volume) depend on the sending tool and the domain. List what the sender must confirm. Do not state
   figures for safe volumes.

## Output

Deliver, in this order:

1. The compliance gate answers and any open legal question.
2. The segment, the tier and the personalisation fields with fallbacks.
3. The sequence, touch by touch: subject variants, body, send gap, stop rule.
4. The reply guide.
5. A measurement plan: reply rate, positive reply rate, meetings booked, unsubscribe and bounce rate.
   Judge by the user's own baseline, not by outside benchmarks.
6. Open items: unsourced claims, missing proof, anything legal still to confirm.

Deliver as a document the sender can edit (a Docs artifact, or markdown). Chat framing stays short.

## Rules

- **Never send, schedule or import.** Draft only.
- **Never invent** a personalisation, a customer, a result, a deadline or a mutual connection.
- **No deception**: no fake replies or forwards, no false urgency, no hidden sender, no misleading
  subject.
- **Opt-out is honoured at once** and the address is suppressed.
- No scraped or purchased personal data. Business contact details from fair, documented sources only.
- No em dashes. No exclamation marks unless the brand kit's voice allows them.
- One sequence per segment. Do not reuse one sequence for audiences with different problems.

## Related Skills

- `linkedin-outreach`: the LinkedIn side of the same prospect. Coordinate the two so they do not hit the
  same person on the same day with the same message.
- `battlecard`: competitor reframes and proof points.
- `email-sequence-hubspot-brevo`: lifecycle email to people who have opted in. That is a different job.
- `customer-story-writer`: supplies proof with customer approval.
- `ai-content-cleaner`, `brand-review`: the gates before delivery.
