---
name: competitor-teardown
description: Breaks down competitor ads to find the angles everyone claims, the angles nobody claims, and what to test first. Use when the user shares competitor ad copy or creative, mentions a rival's ads, or asks how to differentiate paid messaging. For a competitor's organic footprint, ranking keywords, or page content, see competitor-analysis instead.
---

# competitor-teardown

You read competitor ads the way a poker player reads a table: what they're showing, what it means, and where the open seat is.

This looks at paid ad copy and messaging angles only. For a competitor's organic search footprint, ranking keywords, and actual page content, use `competitor-analysis` instead. Different material entirely: this reads what they say to win a click, that reads what actually ranks.

## Inputs you need

- Competitor ad copy: pasted text, screenshots, or transparency-center exports. The more competitors the better, 3+ makes patterns visible.
- The user's own offer, one line.

## Workflow

1. Per competitor: identify the lead angle. Price, speed, trust/social proof, outcome, fear, convenience. One line each.
2. Build the table-stakes list: claims everyone makes. The user must match these or look inferior, but matching them wins nothing.
3. Find the open positioning: angles nobody claims. This is the whole point of the teardown. Cross-reference against the user's offer to find which open angles they can honestly own.
4. Recommend the 3 angles to test first, each with a written example headline, ranked by how defensible the claim is for this specific user. Before writing the example headlines, pull `content-references/references/behavioral-psychology.md` (Ehrenberg-Bass distinctiveness, Cialdini) to judge whether an "open" angle is open because it's genuinely undifferentiated ground or just untested and weak; the reference is what separates the two.
5. Note structural tells if visible: who's pinning headlines, who's using price in copy (usually means they're filtering clicks), who's running emotional vs rational appeals.

## Output format

- Competitor-by-competitor angle summary.
- Table stakes list.
- Open positioning list, marked for which the user can claim.
- 3 test angles with example headlines.

## Rules

- The analysis is a snapshot. Say when the data was pulled and that rotations change.
- Don't infer competitor performance from copy alone. An ad running isn't an ad working. Flag this.
- Only recommend angles the user can truthfully claim. Ask before assuming they can match a guarantee or price point.
