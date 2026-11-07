# Sequence patterns and the compliance checklist

Working structures for `cold-email-sequence`. Nothing here is a claim, a statistic or a benchmark.
Every pattern is filled with the user's own verified facts.

## Touch 1: relevance and a reason

Shape: why you, why now, what it is for, one small ask.

```
Subject: [plain subject about their situation]

Hi {first_name},

[One sentence: the specific reason I am writing to you, sourced: {trigger}.]
[One sentence: what we do for people in your position, as an outcome.]
[One sentence: a small, easy question or offer.]

[Sender name]
[Role, company]
[Opt-out line and company identity as the local rules require]
```

If there is no `{trigger}`, use a segment-level reason ("teams in [situation] often face [problem]")
and mark the email tier 2.

## Touch 2: a different angle

New information. Not "just following up". A second outcome, a short observation about their
situation, or a relevant change in the market. Keep the same ask size.

## Touch 3: proof

One verified result or customer, used with permission, tied to the reader's situation. If there is no
proof the user can back, replace this touch with a question or a resource, and say so.

## Touch 4: something useful

A short resource, a checklist, a relevant article or a one-line question the reader can answer without
a call. It should be worth reading even if they never reply.

## Touch 5: the close

Short, polite, easy exit. Say this is the last email in the sequence. Leave the door open. No guilt,
no false scarcity.

## Subject lines

- Plain and specific beats clever.
- No fake "Re:" or "Fwd:". No false urgency. No claim the body does not support.
- Write two variants per touch and change one thing between them.

## Send gaps

A starting point: a few working days between touches, widening as the sequence goes on. The sender
adjusts to their market and tool. Sequences stop on any reply, unsubscribe or bounce.

## Personalisation fields

| Field | Source | Fallback | Skip the prospect when |
|---|---|---|---|
| {first_name} | The user's list | none (use a neutral greeting) | the name is uncertain |
| {company} | The user's list | none | the company is uncertain |
| {trigger} | A sourced signal | segment-level reason, tier 2 | the signal is older than the sender is comfortable citing |
| {trigger_source} | URL or note | none | missing |

## Compliance checklist (answers go at the top of the deliverable)

- [ ] Recipient type known (named business contact, generic address, sole trader).
- [ ] Recipient country or countries known.
- [ ] Lawful basis written down, and who confirmed it.
- [ ] Address source documented and fair (not purchased, not scraped personal data).
- [ ] Every email identifies the sender and the company.
- [ ] Every email has a working opt-out, honoured immediately and logged.
- [ ] Suppression list in place and checked before every send.
- [ ] Legal or data protection contact has confirmed the above. This skill cannot.

## Deliverability checklist (the sender confirms, the skill does not state figures)

- [ ] Sender domain authentication is set up (SPF, DKIM, DMARC).
- [ ] The mailbox is warmed up as the sending tool requires.
- [ ] Daily volume follows the tool's guidance and the sender's own reputation, not a number from
      this skill.
- [ ] Bounces are removed, and hard bounces never re-sent.
