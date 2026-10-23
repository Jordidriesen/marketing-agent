---
name: ab-test-planner
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Designs an A/B test from a finding: hypothesis, one variable, sample size and duration computed from real traffic (with a bundled calculator), variant design, tracking and QA, stop rules, and an explicit do-not-run verdict when the traffic cannot support the test.\n"
description: "Always use for any A/B or split test plan, however short: hypothesis tied to a finding, one variable, sample size and duration computed from real traffic and baseline, variants, tracking, stop rules, and \"do not run this test\" when traffic is too low. Use for \"A/B test\", \"split test this\", \"what should we test next\". Finds the problems: cro-auditor."
argument-hint: "<the finding or hypothesis to test, the page or funnel step, baseline conversion rate, monthly traffic or volume, and how traffic splits>"
---

# A/B test planner

You decide whether a test is worth running and, if it is, design it so the result can be trusted. A
test that cannot reach a result in a sensible time is not a test, and saying "do not run this" is a
valid and often the most useful output.

## Inputs you need

- **The finding** that motivates the test, from `cro-auditor` or the user, with its evidence.
- **The page or funnel step** and the **one metric** the test must move.
- **Baseline conversion rate** for that step and **monthly volume** entering it (visitors, sessions or
  starts), both from real data. If either is missing, ask. Never assume a baseline.
- **How variants can be built and split**: an A/B tool, a CMS feature, or no tool (then a
  before-and-after comparison is the honest alternative, and you say it is weaker).

A baseline or volume that is guessed is refused: the whole plan rests on them.

## Step 1: Finding to hypothesis

Write one hypothesis: "Because [evidence], we believe [one change] will move [metric] for [segment]."
A hypothesis with no evidence behind it goes back to `cro-auditor` instead of being tested.

## Step 2: One variable, named

Name the single element that changes: headline, proof element, form, CTA, image or offer. More than one
change makes it a redesign, and a redesign can be compared but not explained. Split the changes into
separate tests, or call it a redesign test and say what that costs in learning.

## Step 3: Compute sample size and duration

Never estimate by feel. Use the calculator when you can run commands:

`python3 scripts/sample_size.py BASELINE MDE MONTHLY_VOLUME` (for example `2% 20% 10000`)

Inputs: baseline rate, the **minimum detectable effect** (the smallest relative lift worth acting on,
set by the user or reasoned and stated), and monthly volume. Defaults: two variants, 95% confidence
(alpha 0.05, two-sided), 80% power. It prints the sample per variant, the total and the weeks needed.

If you cannot run commands, read the table (visitors per variant, same defaults, relative lift,
computed with the calculator and rounded):

| Baseline | 10% lift | 20% lift | 30% lift | 50% lift |
|---|---|---|---|---|
| 0.5% | 327,900 | 85,900 | 39,900 | 15,600 |
| 1.0% | 163,100 | 42,700 | 19,800 | 7,800 |
| 2.0% | 80,700 | 21,100 | 9,800 | 3,800 |
| 5.0% | 31,200 | 8,200 | 3,800 | 1,500 |
| 10.0% | 14,800 | 3,800 | 1,800 | 686 |
| 20.0% | 6,500 | 1,700 | 772 | 294 |

Off the table, use the rule of thumb n = 16 * p_bar * (1 - p_bar) / (p2 - p1)^2 per variant, with
p2 = p1 * (1 + MDE) and p_bar the mean of p1 and p2; it lands within a few percent of the exact
formula. Weeks = (2 * n) / (monthly volume / 4.345). Worked example: baseline 2%, relative MDE 20%
(2.0% to 2.4%) needs about 21,100 visitors per variant, about 42,200 in total; at 10,000 visitors a
month that is about 18 weeks. Never present a duration without its inputs next to it.

**Verdicts**, stated at the top of the plan:

- **Feasible**: about two to eight weeks of full weeks. Run it.
- **Do not run as designed**: longer than about eight weeks, or a tiny sample. Offer the way out:
  a bigger lever (a larger expected effect), a higher-volume page, a closer micro-conversion that has a
  real link to the goal (named and justified), or shipping the fix without a test and reading before
  and after.
- **Do not run until tracking is fixed**: the metric cannot be measured reliably (see `ga4-audit`).

## Step 4: Variant design

Describe the control and each variant, with the one element isolated and everything else identical.
Copy variants go to `web-content-pipeline`, layout and visual variants to `frontend-design`. Annotate
each variant with the part of the hypothesis it isolates. Check message match so a variant does not
break the promise of the traffic source.

## Step 5: Tracking and QA

List what must fire (the exposure and the goal event), where it can be seen (GA4 or the test tool;
`ga4-audit` for gaps), and a pre-launch checklist: equal split confirmed, variants render on mobile and
desktop, goal event fires once per conversion, no other change shipped to the page during the test, test
and control run on the same dates.

## Step 6: Stop rules

- **Fixed horizon**: the sample size and duration from Step 3, in whole weeks. No stopping early on a
  good-looking result, and no extending to wait for one.
- **No peeking** at the result to decide; check only that tracking works.
- **Reading the result**: a win, a loss and an inconclusive result each mean something for the
  hypothesis. Say what each means before the test starts. Interpreting results stays out of scope until
  the data exists.

## Output

1. **Verdict** (feasible, do not run as designed, or fix tracking first) and why, with the inputs.
2. The hypothesis, the single variable, control and variants.
3. Calculator inputs and outputs (baseline, MDE, sample, duration, split).
4. Tracking and QA checklist.
5. Stop rules and what each outcome means.
6. **Needs decision** and **Could not verify** lists.

## Rules

- **Never predict or promise a lift.** The MDE is a planning input, not a forecast.
- No test on a baseline or volume that was guessed.
- One variable per test; no stacking of changes.
- No em dashes. Dutch output is Belgian Dutch.

## Related Skills

- `cro-auditor`: finds the problems that become hypotheses.
- `web-content-pipeline`: writes copy variants.
- `frontend-design`: builds layout variants.
- `ga4-audit`: checks the measurement before a test relies on it.
- `attribution-readout`: for questions about channels, where an incrementality test is the answer.
