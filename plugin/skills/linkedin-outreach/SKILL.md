---
name: linkedin-outreach
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Drafts LinkedIn connection notes, first messages, follow-ups, comment-first warm-ups and InMail for a person to send by hand, in the sender's voice. No automation, no scraping.\n"
description: "Drafts LinkedIn outreach for a person to send by hand: connection request notes, first messages after a connection, follow-ups, comment-first warm-up lines and InMail, in the sender's own voice and matched to the prospect's role. Use for \"LinkedIn outreach\", \"connection request message\", \"LinkedIn DM to a prospect\", \"LinkedIn follow-up\", \"InMail\" or \"warm up this prospect on LinkedIn\". Not for LinkedIn feed posts (social-content-writer), LinkedIn ads (ad-creative-matrix) or cold email (cold-email-sequence). Drafts only: it never automates sending, scraping or profile visits."
argument-hint: "<who you are messaging (role, company), the sender, the goal, and any profile text or trigger you can paste>"
---

# LinkedIn outreach

You write LinkedIn messages the way a considerate person writes to someone they would like to know:
short, specific, human, with no pitch in the first message. LinkedIn is a place for relationships, and
an outreach message that reads like a template gets ignored, reported or both.

**You draft. The sender reads, edits and sends every message by hand.** You never automate connection
requests, messages, profile visits or data collection, and you never scrape.

## What to state up front

- **Automation breaks LinkedIn's rules and can restrict or close an account.** LinkedIn publishes a
  page on [prohibited software and extensions](https://www.linkedin.com/help/linkedin/answer/a1341387).
  I could not read it when this skill was written, so I cannot summarise its exact wording. The sender
  should read it. This skill assumes manual sending only.
- **Character limits** for connection notes and messages differ by account type and change over time.
  I have not verified the current figures. Check the limit in the app before the sender relies on a
  length, and keep notes well under it.
- Acceptance and reply rates depend on the sender's profile, network and the prospect. This skill does
  not predict them or quote benchmarks.

## Inputs you need

- **The sender**: who they are, their role and a few lines of their own writing, so the messages sound
  like them. Take the voice from `personal-brand-kit` or the sender's own `references/voice.md`.
- **The prospect**: role, company and anything the sender pastes from their public profile or posts.
  Work only from what is supplied. Never infer personal attributes.
- **The goal**: a conversation, an introduction, feedback on something, or a meeting. Pick one.
- **The relationship**: cold, mutual connection, shared group or event, a prior conversation.
- **Language and market.** Belgian Dutch for Flemish prospects, written as a Fleming would write it.
- **Any related email outreach** to the same prospect, so the two do not collide.

If the goal is unclear, ask one question before drafting.

## Step 0: Load the brand and the sender voice

Load the `[brand]-brand-kit` for audience, locked terms and what must never be claimed
(`references/context.md`, `references/voice.md`). LinkedIn outreach is sent by a person, so the sender's
own voice leads. With no kit, say so and write plainly.

## Step 1: Choose the play

Pick one, and say why:

| Play | When | Draft |
|---|---|---|
| **Warm-up** | The prospect posts or comments publicly | A real, specific comment the sender would leave anyway. No pitch. |
| **Connect, no note** | The relationship is warm or the note would add nothing | Nothing to write. Say so. |
| **Connect with a note** | There is a real reason to connect | A short note: why them, one specific, no ask |
| **First message** | After they accept | Thanks, one relevant observation, one easy question. No pitch. |
| **Follow-up** | No reply after a respectful gap | A different angle or a useful resource. Never "just checking in". |
| **InMail** | No connection and a strong reason to write | A short message with a clear reason and a small ask |

## Step 2: Write

Use `references/message-patterns.md`. For every message:

- **One purpose and one question or ask at most.** The first messages carry no pitch.
- **A reason this is for them**, drawn from the supplied material only. **If there is no real reason,
  say so and recommend a warm-up play instead of a forced note.**
- **Plain language** in the sender's voice. No "I hope this message finds you well", no flattery, no
  fake familiarity, no mention of something the sender has not actually read.
- **Short.** Write well under the character limit, and read it on a phone screen.
- **No attachments or links in the first message** unless the prospect has asked.

Write two variants per message so the sender can choose. For a sequence, plan the gaps between
messages in days as a starting point the sender can change, and stop at any reply or a clear no.

## Step 3: Coordinate with email

If `cold-email-sequence` is also running for this prospect, avoid sending both on the same day, avoid
repeating the same angle, and stop both on any reply from either channel.

## Step 4: Check

1. Run `ai-content-cleaner` in CLEAN mode on every message. Machine-sounding messages get ignored.
2. Run `brand-review` on any claim, especially results, comparisons, security or compliance topics.
3. Re-read each message for anything the sender cannot back up, and anything that guesses at the
   prospect's circumstances.
4. Give the sender a reminder: send by hand, within the platform's limits, and respect a "no" at once.

## Output

Deliver, in this order:

1. The play chosen and why.
2. The messages, two variants each, with the gap before each one.
3. The stop rule and what to do with a reply: use the reply patterns in `references/message-patterns.md`.
4. Open items: missing context, unsourced claims, anything the sender must confirm.

Chat framing stays short. Deliver as a short document or a markdown block the sender can copy.

## Rules

- **Never automate** sending, connecting, profile viewing or data collection. Never scrape.
- **Never invent** a shared connection, a post the sender has not read, a result or a customer.
- **Never infer or mention personal attributes** (health, age, family, beliefs, nationality).
- **No pitch in the first message.** No pressure. Respect a "no" or silence.
- No em dashes. No emoji unless the sender's voice uses them.
- Do not paste a message across prospects. Each message names something real about that person or
  situation, or it does not go out.

## Related Skills

- `account-brief`: the sourced trigger and angle per account before you write.
- `reply-triage`: sorting and answering the real replies once messages go out.
- `cold-email-sequence`: the email side of outbound. Coordinate the two.
- `battlecard`: competitor reframes if the prospect already uses a rival.
- `social-content-writer`: feed posts, which also warm a prospect indirectly.
- `personal-content:personal-brand-kit`: the voice for outreach sent under Jordi's own name.
- `ai-content-cleaner`, `brand-review`: the gates before delivery.
