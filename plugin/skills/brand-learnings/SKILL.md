---
name: brand-learnings
description: "Shows or logs what has worked for a client brand: which angle, headline, audience, offer, format or channel performed, with the numbers, period and confidence, kept in brand/learnings.md in the client's storage. Use for \"what do we know about this brand\", \"what worked last time\", \"log this result\", before a campaign plan. Writes only after a yes."
metadata:
  version: 1.0.0
  history: 'v1.0.0 (marketing-agent 5.4.0): new. The learning loop: results from reports, tests and analyses feed the next brief.'
---

# Brand learnings

One file per brand holds what has been learned, so the next brief starts from it instead of from
zero: `brand/learnings.md` in the storage root (`marketing-jobs/<brand>/brand/` in a linked folder,
`brand/` in the client's repository; see `director-playbook` references/storage.md). It is client
material: it never goes into the plugin repository.

## Show

Load the brand kit, read the file and answer the question asked: what worked for a channel, an
audience, an angle, an offer. Quote the rows with their dates, numbers and confidence. When the
file has nothing on the question, say so; never fill the gap from general knowledge or benchmarks.

## Log

1. Take the result from the user, or from the output of `paid-ads-report-writer`,
   `ab-test-planner`, `google-ads-analyse`, `measurement` or a connector read.
2. Write it as one row in the table below. Numbers come from the source as they are. A result
   without numbers is logged as `stated`, in the user's words.
3. Show the rows and ask: "Log these in learnings.md?" Write only after a yes.
4. Without resolved storage (no linked folder, no client repository), write nothing: give the rows
   in the reply so they can be pasted later.

```markdown
# Learnings: <brand>

| Date | Channel | What was tried or seen | Result (numbers, period, sample) | Confidence | Source |
|---|---|---|---|---|---|
| 20/11/2026 | Google Ads, Search | Headlines naming QR check-in vs generic "visitor software" | CTR 6.1% vs 3.4%, 30 days, about 4,000 impressions each | observed | google-ads-analyse (ad-copy-tester) |
```

- **Confidence:** `tested` (a controlled A/B test with a read-out), `observed` (seen in the data,
  no control), `stated` (the user's or client's judgement, no numbers).
- **Never invent** a figure, a period or a sample size. A row with a gap says so.
- Rows older than 12 months read as `review`, not as current; they are not deleted.

## How the director uses it

When writing a brief, the director copies the rows that touch the job into **What we already
know**. Every thread that writes or plans reads that section. A learning is a reason, not a rule:
a brief that goes against one says why.

End with: `Skills run: brand-learnings`.
