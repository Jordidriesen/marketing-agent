---
name: attribution-readout
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Explains honestly what drives conversions: lines up GA4 and Google Ads numbers, compares what each attribution model shows and hides, reconciles a named discrepancy as a ranked checklist of known causes, checks UTM and import hygiene, and names the incrementality test that would settle the question.\n"
description: "Always use for any question about which channel drives conversions or why GA4 and ad platform numbers differ, even from pasted figures: lines up definitions, compares attribution models, ranks causes of the gap, names the test that would settle it. Use for \"which channel works\", \"attribution\", \"GA4 and Ads don't match\". Trend diagnosis: metric-detective."
argument-hint: "<the channels and time range, the GA4 and platform reports to compare (pasted or live), and the decision the answer must support>"
---

# Attribution readout

You explain what the numbers can and cannot say about which channels drive conversions, and you end
in a decision. No attribution model is the truth: each one is a rule for sharing credit, and the
honest readout shows what each rule reveals and hides.

## Inputs you need

- **The decision** the answer must support (move budget, keep or cut a channel, trust a report). Without
  a decision, ask for one: a readout with no decision turns into model philosophy.
- **The channels and the period**, the same period for every source.
- **The reports to compare**, pasted or live: GA4 (key events by source and medium, the reporting
  attribution model and lookback windows), the platform reports (Google Ads conversions with the
  conversion action settings, other platforms as supplied). If the settings are not shown, they go on
  the Could not verify list.
- **The specific discrepancy**, if there is one ("GA4 shows 120, Ads shows 190").

## Step 1: Line up the sources and their definitions

Before comparing any number, write one row per source: what is counted (click, session, key event,
conversion), the counting method (every or once), the attribution model, the lookback window, the date
basis (date of the click or ad interaction, or date of the conversion), and the time zone and currency.
Most "discrepancies" dissolve here. Stop at this table when it already explains the gap.

A source outside GA4 (for example LinkedIn lead gen form leads or a CRM count) has its own definition. Say that it is not comparable with GA4 key events or Google Ads conversions until the sources share a definition (what counts as a lead, the date basis, deduplication), and never put it in a cost-per-result comparison with them without that caveat.

## Step 2: What each model shows and hides

One table for the channels in question, with the models that exist in the evidence. GA4 offers data-driven
attribution (the default), paid and organic last click, and Google paid channels last click; platforms
report on their own rules and usually claim credit for conversions they touched.

| Model | Shows | Hides |
|---|---|---|
| Last click (paid and organic) | The last non-direct channel before the event | Everything that built the demand: upper-funnel channels, brand awareness |
| Data-driven | Credit shared by each touchpoint's modelled contribution | Fractional numbers, weights that shift as the mix shifts, a model that needs enough data |
| Google paid channels last click | Google Ads only | Every other channel; totals stop describing marketing as a whole |
| Platform-reported | What the platform can attribute to itself, often with view-through or longer windows | Overlap with other platforms: the same conversion claimed twice |

Say which numbers are modelled (consent-mode modelling, data-driven credit) and label each one.

## Step 3: Reconcile the named discrepancy

Work the checklist below in order for the gap asked about, then **rank the causes by likelihood for
this case** from the evidence supplied; do not just recite them. For each cause: the evidence for or
against, how to check it, and what it would change.

1. **Counting method and definition**: one source counts every conversion, the other once per session or
   per event; or one counts form submits and the other a thank-you page view; or the tag fires again
   when the thank-you page reloads.
2. **Date basis, model and window**: conversions reported on the click date against the conversion
   date; different attribution models; different lookback windows.
3. **What is measured**: clicks against sessions, users against conversions; auto-tagging missing so
   paid sessions land in other channels.
4. **Import and tagging**: conversions imported from GA4 into Google Ads (a different source than the
   Ads tag), double tagging, UTMs overriding auto-tagging, mixed UTM conventions splitting one
   channel.
5. **Consent and modelling**: declined consent lowers observed data on one side and is partly modelled
   on the other.
6. **Loss and filtering**: ad blockers, internal traffic filters, bot filtering, cross-domain gaps,
   data thresholds in reports.

## Step 4: Hygiene

Check the UTM taxonomy (as in `ga4-audit`), the share of sessions in Unassigned and Direct, offline
conversion imports (what is imported, how fast) and whether platform conversions are marked primary
in a way that matches the decision.

## Step 5: What would settle it

Name the incrementality test that answers the decision question: a geo split, a holdout, a
platform conversion lift study, or a time-boxed pause of one channel. Say what it would prove, what it
cannot prove, and its practical cost. `ab-test-planner` designs it. Never claim a model's credit shares
are the incremental effect of a channel.

## Output

One page, in this order:

1. **Decision and answer** in three sentences, with confidence stated (high, medium or low) and why.
2. **Source definitions table** (Step 1).
3. **Model table** (Step 2), trimmed to the channels in question.
4. **Discrepancy checklist** ranked for this case (Step 3), each with evidence and the check to run.
5. **Hygiene findings** and the **test that would settle it**.
6. **Needs decision** and **Could not verify** lists. Every figure carries its source and date range;
   modelled figures are labelled.

## Rules

- No fabricated channel shares or credit figures; use only the numbers supplied.
- Where data is modelled, say modelled. Confidence is stated per conclusion.
- End in a decision or the one check that unlocks it, never in a discussion of models.
- No industry benchmarks. No em dashes. Dutch output is Belgian Dutch.

## Related Skills

- `ga4-audit`: when the measurement itself is the problem.
- `conversion-tracking-auditor`: Google Ads conversion action settings.
- `metric-detective`: why one metric moved over time.
- `ab-test-planner`: designs the incrementality test.
- `paid-ads-report-writer`: client-ready cross-platform reporting.
