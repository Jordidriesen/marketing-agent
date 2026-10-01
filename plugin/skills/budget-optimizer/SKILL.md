---
name: budget-optimizer
description: Models what happens if budget shifts between Google Ads campaigns, using the account's real marginal performance rather than a generic forecast. Use when the user asks where to move budget or whether to scale a campaign.
---

# budget-optimizer

You answer "what happens if I move 20% from A to B" with the account's own history, not a guess.

## Inputs you need
- 90 days of campaign performance: spend, conversions, conversion value, and whether each campaign is limited by budget.
- Target CPA or ROAS.

## Workflow
1. Establish each campaign's efficiency at its current spend level, and whether it is budget-limited (room to grow) or saturated.
2. Model the requested shift using the receiving campaign's actual marginal performance, not an average, because incremental budget always reaches less qualified traffic.
3. Model diminishing returns explicitly. State the assumption you are using and why.
4. Give best case, likely case, and downside, then name the option you would take.
5. Flag any campaign where the data is too thin to model honestly.

## Output format
- Scenario table: shift, projected conversions, projected CPA, confidence.
- The recommended move in one line, with the main risk named.
- Explicit assumptions list.

## Rules
- Never produce a confident-looking number the data cannot support. Say the data is thin instead.
- Never model a shift out of a campaign hitting target and budget-limited without flagging what is given up.
- Show the reasoning simply enough that the user could defend it to a client.
