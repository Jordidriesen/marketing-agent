---
name: abm-plan
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Account-based marketing plan for a set of named accounts: tiers, selection criteria, buying committee by role, plays per tier across outreach, paid social, content and events, coordination with sales, and account-level measurement.\n"
description: "Plans an account-based marketing programme for named accounts: tiers, buying committee, plays per tier across outreach, LinkedIn and Meta audiences, content and events, sales handover, account-level measurement. Use for \"ABM\", \"target account plan\"."
argument-hint: "<the brand, the goal, the account list or how to build it, the period, the budget and who in sales works the accounts>"
---

# ABM plan

Account-based marketing treats a short list of companies as markets of one. It only works when sales
and marketing agree on the list, every channel speaks to the same accounts at the same time, and
success is measured by account, not by lead. This skill writes that plan.

## Inputs you need

- **The brand** and the offer, from the `[brand]-brand-kit` and its product files.
- **The goal**: meetings, opportunities, expansion in existing accounts, entering a new vertical.
- **The accounts**: a supplied list, a list from the scraper suite when installed, or the criteria to
  build one. No list and no criteria means ask before planning.
- **Period and budget**, and which channels are available (outreach, LinkedIn Ads, Meta, events,
  content, direct contact by sales).
- **Who in sales** owns the accounts, and how warm leads reach them.

If the goal or the account list is missing, ask one question before planning.

## Step 0: Load the brand

Load the `[brand]-brand-kit`: `context.md` for ICP and markets, the personas module for the buying
committee, `products/<slug>.md` for what is offered, and the product marketing brief when one exists.

## Step 1: Selection and tiers

Write the selection criteria (fit against the ICP, intent or trigger signals, existing relationship,
deal size potential) and place every account in a tier:

| Tier | Typical size | Treatment |
|---|---|---|
| **1: one-to-one** | A handful | An `account-brief` each, tailored outreach per role, tailored content, sales involved from the start |
| **2: one-to-few** | Small clusters sharing a trait (vertical, region, trigger) | One brief per cluster, cluster-specific messaging and content |
| **3: one-to-many** | The rest of the list | Segment-level messaging, paid audiences, light-touch outreach |

The tier sizes are a starting point the user sets with sales, not a rule. Mark every placement that
rests on inference.

## Step 2: Buying committee

Per tier, map the committee by role from the personas module: who decides, uses, signs and can block,
and what each needs to hear. Named people only from public, professional sources.

## Step 3: Plays per tier

For each tier, which channels run, in which order, with what message:

- **Outreach**: `cold-email-sequence` and `linkedin-outreach`, coordinated, sent by a person.
- **Paid audiences**: LinkedIn matched audiences (company lists) and Meta custom audiences where the
  brand uses Meta. Hand the list and the message to the paid social owner; this plan does not build
  campaigns.
- **Content**: which existing pieces fit each role, and the gaps to commission from `content-writer`.
- **Events and direct contact**: invitations, meetings, sales touches.

Lay the plays out as a week-by-week sequence over the period, so channels warm an account before
outreach arrives rather than colliding.

## Step 4: Sales handover

Agree in writing: what counts as an engaged account, how it reaches sales, how fast sales follows up,
and how sales feeds back what happened. Use `reply-triage` handover notes as the format for individual
replies.

## Step 5: Measurement

By account, not by lead: accounts reached, accounts engaged (by the agreed definition), meetings,
opportunities and pipeline value per tier, plus coverage of the buying committee. Name the data source
for each measure and say plainly which ones the current connectors cannot supply. No industry
benchmarks.

## Output

1. Goal, period, budget and channels.
2. Selection criteria and the tiered account table (account, tier, reason, inference flag).
3. Buying committee per tier.
4. Plays per tier and the week-by-week sequence.
5. Sales handover agreement.
6. Measurement plan.
7. **Needs decision** and **Could not verify** lists.

Deliver as a document in the run folder when one is in use, otherwise in the reply.

## Rules

- **Never invent** accounts, contacts, triggers, budgets or results.
- Paid and outreach parts are plans and drafts; nothing goes live without approval, per `security-policy`.
- Legal points on outreach stay open until confirmed, as in `cold-email-sequence`.
- No em dashes. Dutch is Belgian Dutch.

## Related Skills

- `account-brief`: briefs for tier 1 accounts and tier 2 clusters.
- `cold-email-sequence`, `linkedin-outreach`, `reply-triage`: the outreach and its replies.
- `ad-creative-matrix`: ad creative for the paid audiences.
- `campaign-plan`: for broad campaigns without named accounts.
- `european-market-intelligence`: sourcing accounts from registries and tenders.
