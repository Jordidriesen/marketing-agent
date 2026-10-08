---
name: battlecard
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. A one-page, sales-facing competitor card built from verified inputs, with every claim source-tagged, an honest where-they-win column, landmine questions, objection responses and a review date.\n"
description: "Builds a one-page sales battlecard for one named competitor: how they position, where we win, where they win, landmine questions to ask a prospect, traps to expect, objection responses and proof points, with every claim tagged by source and confidence. Use for \"battlecard\", \"how do we beat X\", \"competitive cheat sheet for sales\", \"objection handling against a rival\" or \"sales comparison sheet\". Not for researching the competitor (competitor-analysis, competitive-landscape, european-market-intelligence), analysing their ads (competitor-teardown) or customer-facing comparison pages (web-content-pipeline)."
argument-hint: "<our product, the competitor, and any win/loss notes or sources you can share>"
---

# Battlecard

You write the card a salesperson opens ten minutes before a call: short, honest, usable under
pressure. A battlecard that oversells loses the sales team's trust the first time a prospect checks it.

This skill **compiles and sharpens** what is known. It does not do the competitor research. If the
facts are thin, run `competitor-analysis`, `competitive-landscape` or `european-market-intelligence`
first, or ask the user for the sources. For a European competitor where registry-verified facts matter (legal name, seat, legal form), run `european-market-intelligence` first and carry its "Registry-verified facts" line to the top of the card.

**A battlecard is internal.** It is not a customer-facing document. Anything that will be shown to a
prospect is a different piece (a comparison page, a one-pager) and passes `brand-review`.

## Inputs you need

- **Our product or solution**, in the user's own words: what it does, who it is for, real limitations.
  Take it from the brand kit's `references/context.md`, and from a product file if the kit has one.
- **The competitor**: one per card. Several competitors means several cards.
- **Sources**: the competitor's own site, public pricing, public reviews, analyst pages, and anything the
  sales team has heard first-hand. Pasted or fetched, never recalled from memory.
- **Win and loss notes** from sales, if any. They are the best evidence on the card.
- **Proof points we may use**: customer names and results with permission to use them.

If our own limitations are unknown, ask. A card with no honest weaknesses is not credible.

## Step 0: Load the brand

Load the brand's `[brand]-brand-kit` (`references/context.md` for audience and markets,
`references/voice.md` for locked terms and tone). The kit's locked terminology and banned list
outrank everything here. With no kit, say so and write plainly.

## Step 1: Source-tag every claim

Before writing anything, list each fact about the competitor with:

| Claim | Source (URL or "sales call, date") | Date seen | Confidence |
|---|---|---|---|

Confidence is one of: **verified** (primary source, public), **reported** (secondary or sales
hearsay), **inference** (our reading). Only verified and reported claims may appear on the card, and
reported ones are marked. Inferences go in a separate "to check" list. **Never invent a competitor
feature, price, customer or weakness.** If it is not in a source, leave it out or mark it unknown.

Do not use confidential or leaked competitor material. Public sources and the team's own first-hand
experience only.

## Step 2: Write the card

Use `references/battlecard-template.md`. The sections, in order:

1. **Snapshot**: who they are, who they sell to, how they position, in three lines.
2. **Where we win**: the real differences that matter to our buyer, each with its proof.
3. **Where they win**: honestly. Sales needs to know before the prospect says it.
4. **Parity**: what both do, so nobody wastes breath on it.
5. **Landmines**: questions a salesperson can ask the prospect that surface our strengths, without
   attacking the competitor. They must be fair questions a prospect can answer for themselves.
6. **Traps**: what the competitor's team will likely say about us, and the honest response.
7. **Objection responses**: the three to five most common, each with acknowledge, reframe and proof.
8. **Proof points**: customer evidence with its permission status.
9. **When not to compete**: the prospects where the competitor is the better fit. Say so.
10. **Card control**: owner, review date, sources, open items.

## Step 3: Check

1. Re-read every claim against the source table. Remove anything unsourced.
2. Run `ai-content-cleaner` in CLEAN mode on the card.
3. Run `brand-review` on anything that makes a comparative claim. Comparative advertising rules in the
   EU and the national rules that apply have conditions. This skill does not give legal advice. For
   anything that may leave the building, have a lawyer confirm.
4. Tell the user which claims are the weakest and what would firm them up.

## Output

Deliver the card as a document the sales team can open quickly (a Docs artifact, or markdown if no
document route exists), one page for the card and an appendix for the source table and "to check"
list. Chat framing stays short. Offer to hand the card to `creative-brief` and `canva-workflow` if the
team wants a designed version.

## Rules

- No invented facts about the competitor or about us.
- No disparagement. State differences, not insults.
- Every claim is dated. Competitors change, so the card carries a review date and an owner.
- Never promise a price comparison without a public, dated source.
- No em dashes. No superlatives we cannot prove.
- Do not name a prospect or customer without permission.

## Related Skills

- `competitor-analysis`, `competitive-landscape`, `european-market-intelligence`: upstream research.
- `competitor-teardown`: how the competitor sells in paid ads. Its open angles can feed the landmines.
- `customer-story-writer`: supplies proof points with customer approval.
- `cold-email-sequence`, `linkedin-outreach`: outreach that can use the card's reframes.
- `brand-review`, `ai-content-cleaner`: the gates before delivery.
