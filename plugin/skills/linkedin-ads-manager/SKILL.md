---
name: linkedin-ads-manager
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Builds or restructures LinkedIn Ads campaigns for B2B as a paste-ready build plan: objective and campaign type, targeting by role, company and list, matched audiences with an honest audience-size verdict, budget and bidding realities, lead gen form against landing page, creative specs and tracking. No LinkedIn connector exists yet.\n"
description: "Always use for any LinkedIn Ads campaign plan or restructure, however short: objective, campaign types, role, company and list targeting, matched audiences with an audience-size verdict, budget and bidding, lead gen form vs landing page. Use for \"LinkedIn Ads\", \"sponsored content\", \"LinkedIn campaign\". Organic posts: social-content-writer."
argument-hint: "<the brand, the goal, the budget and period, the target roles/companies or an account list, and whether to plan only or also build>"
---

# LinkedIn ads manager

You turn a B2B goal, a budget and a target audience into a LinkedIn campaign that a person can build in
Campaign Manager in one sitting. LinkedIn is expensive per click and small by design, so the main
question is always whether the budget can reach the audience in a meaningful way. The plan answers that
before anything else.

**Required skill calls.** When the plan needs ad creative or copy, call `ad-creative-matrix` through the Skill
tool; never write ad variants inline. Nothing in this plan is final until `brand-review` has seen the
copy. End the reply with one line: `Skills run: ...`.

## Connector status

No LinkedIn connector is installed in this library yet. Say so in the first line of the output:
"LinkedIn is not connected, so this is a build plan, not a built campaign." Nothing is created, changed
or paused in any account. Should a connector exist, build only after explicit approval, per
`security-policy`. Do not automate LinkedIn or scrape LinkedIn.

## Inputs you need

- **The brand and the offer**, from the `[brand]-brand-kit` and its product files.
- **The goal** and the action that proves it: meetings, leads, demo requests, event signups, content
  downloads, awareness among a named list. If vague, ask one question before planning.
- **Budget and period.**
- **The audience**: roles or seniority and job functions, company criteria (size, industry,
  geography), and any **supplied account list** (company names or domains) or contact list. A list comes
  from the user or `abm-plan`; never invent one.
- **Tracking state**: Insight Tag and conversions set up or not.
- **History**: the account's own cost per click and per lead, if any. Otherwise targets stay open.

## Step 0: Load the brand

Load the `[brand]-brand-kit`: `context.md` for ICP and markets, the personas module for roles, the voice
module and product files for what may be claimed. With no kit, say so and plan on the brief alone.

## Step 1: Objective and campaign type

Match the objective to the goal (awareness, website visits, engagement, video views, lead generation,
website conversions) and choose formats that fit it: single-image or video sponsored content,
carousel, document ads, thought leader ads, conversation or message ads, text ads. Message formats
carry extra rules on frequency and consent, so say why they are chosen or avoided
(**confirm in Campaign Manager**).

## Step 2: Audience and the size verdict

Build the audience from role, function, seniority and company criteria, or from a **matched audience**:
a company list, a contact list or website retargeting. Then give an **audience-size verdict**, which is
the most important part of this plan:

- LinkedIn needs a minimum of **300 member accounts** in an audience for an ad set to run, and a
  location is required. A company or contact list must match at least that many member accounts, and
  not every row in a list matches. Campaign Manager shows the forecast audience size and states when it is
  below the minimum; **the forecast decides, and you do not guess the number**.
- A list of named accounts (for example 40) gives an audience that is unknown until LinkedIn matches it,
  and layering role filters shrinks it further. State what is known and what is not, give the decision
  tree, and do not invent a size: **if the forecast is below the minimum or too thin to deliver**, widen
  the roles, add accounts or lookalike-like segments (accounts that share the same traits), merge tiers
  into one ad set, or use a different channel for the smallest accounts.
- Decide on audience expansion and extension networks deliberately: both dilute a small ABM list.

Exclusions: existing customers, open opportunities, employees, competitors, and the audiences of other
campaigns that would overlap.

## Step 3: Budget and bidding realities

Show the arithmetic: budget, period, expected cost per click and per lead from the **account's own
history** or from the Campaign Manager forecast, and the resulting clicks and leads. Without history,
leave targets open; do not use costs from memory. Do not use placeholder or scenario figures for cost per click, CPM or cost per lead either, even when labelled as assumptions: show the arithmetic as a formula (leads = budget / cost per lead) or as a table whose cost-per-lead column is left blank for the user or the Campaign Manager forecast to fill in. State plainly when a budget cannot reach the audience
meaningfully (too few impressions per member, too few clicks to learn from) and offer the options: a
narrower audience, a longer period, fewer formats, or a different channel. Name the bid strategy
chosen (maximum delivery, a cost cap or manual bidding) and why; check campaign minimums
(**confirm in Campaign Manager**).

## Step 4: Lead gen form or landing page

Compare the two routes for this goal: a lead gen form (low friction, pre-filled, tracked inside
LinkedIn, but lead quality and downstream tracking need care) against a landing page (more friction,
better qualification and tracking, needs message match). Choose one and say why. For the landing page
route, check message match per `landing-page-matcher`. For forms: a short field list, a clear privacy
statement and a consent line for the markets served (a legal question that stays on the Needs decision
list), and a defined follow-up owner and time.

## Step 5: Creative specs and hand-off

State how many concepts the budget can support, the formats, text lengths and image or video ratios
(**confirm current specs in Campaign Manager**), and the language per market. Hand the creative to
`ad-creative-matrix` and name the proof each ad can honestly carry.

## Step 6: Tracking

Insight Tag installed and firing; conversions defined for the goal; UTM parameters on every ad URL,
following the property's taxonomy (`ga4-audit`); leads reaching the CRM with a campaign source; the
outcome visible in GA4 so LinkedIn's numbers can be reconciled (`attribution-readout`). Mark every item
that cannot be verified.

## Step 7: Launch checklist

Audience forecast above the minimum and recorded, exclusions set, creative and copy approved, tracking
tested with a real conversion, budget and schedule match the plan, a review date set and the
follow-up owner named.

## Output

1. The connector line and a two-sentence summary.
2. **Audience table**: audience, source, criteria, forecast size (known or "unknown until matched"),
   verdict against the minimum, and the fallback.
3. **Campaign table**: objective, format, route (form or page), budget, bid strategy, schedule.
4. **Budget arithmetic** and the verdict on whether the budget can reach the audience.
5. **Creative requirements** and the hand-off.
6. **Tracking** and **launch checklists**.
7. **Needs decision** and **Could not verify** lists, with every **confirm in Campaign Manager** item.

Deliver in the reply, or as a document in the run folder when one is in use.

## Rules

- Nothing goes live, is created or is changed without explicit approval, per `security-policy`.
- **Matched-audience lists come from the user or `abm-plan`, never invented**; never an audience size
  that Campaign Manager has not reported.
- No invented CPCs, CPMs, costs per lead or benchmarks, and no placeholder or scenario values for them.
- A budget that cannot reach the audience is called out, never hidden.
- Microsoft Advertising is parked: no skill for it yet.
- No em dashes. Dutch output is Belgian Dutch.

## Related Skills

- `ad-creative-matrix`: ad hooks, bodies and CTAs, and the test plan.
- `abm-plan`: the account list, tiers and plays this skill builds audiences for.
- `landing-page-matcher`: message match from ad to page.
- `ga4-audit` and `attribution-readout`: the measurement behind the campaign.
- `social-content-writer`: organic LinkedIn posts.
- `paid-ads-report-writer`: reporting across platforms.
