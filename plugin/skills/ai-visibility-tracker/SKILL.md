---
name: ai-visibility-tracker
metadata:
  version: '1.0.0'
  history: "v1.0.0: new skill. Measures and tracks a brand's visibility in AI answers as a repeatable protocol: a versioned prompt set, a dated check protocol per engine, a citation log, a read of Search Console's generative AI report and AI-referred traffic in GA4, and a round-over-round movement report with stated limits. A protocol, not an automated score.\n"
description: "Always use for any request to measure or track a brand's visibility in AI answers, even a first check: builds a repeatable prompt set, runs the check protocol, logs citations and mentions per engine, reads AI traffic in Search Console and GA4, and reports movement with stated limits. Use for \"AI visibility\", \"are we cited in ChatGPT\", \"GEO report\". Writing for citations: seo-aeo-core."
argument-hint: "<the brand, competitors to track against, the market languages, and how many rounds of checking already exist>"
---

# AI visibility tracker

You measure whether a brand appears in AI answers, and you do it as a protocol that can be repeated:
the same questions, asked the same way, logged the same way, round after round. AI answers vary from run
to run and engine to engine, so one check is an anecdote and a movement needs at least two rounds.
This skill never produces a score the log cannot support.

## Inputs you need

- **The brand** and its main URLs, and **competitors** to track against (named by the user, or from
  `competitor-analysis` or `competitive-landscape`).
- **The markets and languages** the brand sells in. Each language is its own prompt set.
- **Existing rounds**: a citation log from earlier checks, if there is one. With none, this is round 1
  and the report says it has no movement to show.
- **How checks are run**: by a person in each engine, or through a connected tool. Without a tool, the
  protocol is manual and you say so; never pretend to automate it.

If the brand, the competitors or the languages are missing, ask one question before starting.

## Step 0: Load the brand

Load the `[brand]-brand-kit`: `context.md` for the buyers, markets and competitors, and the product
files for the topics the brand should be found for. With no kit, say so and build from the brief.

## Step 1: Build the prompt set

Read `references/prompt-set.md` now. Write buyer questions, the way a buyer would ask an assistant, not
marketing phrases, across funnel stages, in each language, with ids, and store the set as a versioned
list (v1 with a date). Change a prompt and the set becomes v2; movement is only compared between
rounds that used the same version. Suggested minimum: five prompts per funnel stage and language, so
one odd answer does not decide the picture; the user may choose more.

## Step 2: The check protocol

Per round, run every prompt in every chosen engine (typically ChatGPT, Perplexity, Google AI Overviews
or AI Mode, Gemini, Copilot, Claude) under the same conditions: the same location and language, logged
out or in as stated, search or browsing mode on as stated. Run each prompt the same number of times
every round (state the number; answers vary). Record every observation with its **date**. Do not
assist the engines: no prompt stuffing, no leading questions that name the brand, and no hidden text or
other tricks to influence what an engine cites. That is out of scope and refused.

## Step 3: Log citations and mentions

Use the log template in `references/citation-log.md`. Per answer, record: engine, mode, date, prompt id,
whether the brand is **mentioned** in the text, whether a brand URL is **cited** as a source, the
position among mentioned brands, which competitors are mentioned or cited, and which of the brand's
pages were cited. Quote nothing beyond a short excerpt.

## Step 4: Read the measured traffic

- **Search Console.** Google has launched generative AI performance reports for Search and Discover,
  rolling out to a subset of sites, showing impressions, pages, countries, devices and dates for AI
  features such as AI Overviews and AI Mode. They show impressions, not clicks, and the same data also
  stays inside the main performance report. Check whether the property has the report; if not, say so
  and move on. `seo-audit` covers the rest of Search Console.
- **GA4.** Sessions that arrive from AI assistants appear as referral sources; list the referrers the
  property actually shows rather than assuming a list, and note that some AI visits arrive without a
  referrer and land in Direct, so the number is a floor. `ga4-audit` checks the tagging.

Report these as measured traffic, separate from the logged answers: they are different evidence.

## Step 5: The movement report

Nothing is reported as movement before round 2. From round 2: per engine, the brand's cited and
mentioned counts out of the answers checked, round over round, the same for the named competitors, and
the pages that earned the citations. Say the sample plainly (prompts, engines, runs per prompt, dates).
Call a change a movement only when it is larger than the variation between repeat runs; otherwise
call it noise. Do not claim a cause.

## Output

One page:

1. **Round and sample**: set version, dates, engines, prompts, runs per prompt.
2. **Citation table**: engine by brand and competitors, cited and mentioned counts out of answers checked,
   with the previous round beside them from round 2.
3. **Movement**: the biggest mover and the engine, stated with the counts, and what is only noise.
4. **Pages that earn citations**, and the gaps (topics where competitors are cited and the brand is not).
5. **Measured traffic** from Search Console and GA4, or what could not be read.
6. **Fixes** handed to `seo-aeo-core` (structure for citation), `web-content-pipeline` (the pages)
   and `seo-audit`.
7. **Needs decision** and **Could not verify** lists. Deliver in the reply, or as a document in the run folder.

## Rules

- No invented scores: only ratios and counts the log supports. No "visibility score" or projected figure.
- Sample size, dates and engine settings are always stated.
- No citation-gaming tricks: no hidden text, prompt stuffing or fake mentions. Refuse and say why.
- Never state that a page was cited unless the log shows it.
- No em dashes. Dutch output is Belgian Dutch.

## Related Skills

- `seo-aeo-core`: how to write and structure pages so they are cited.
- `web-content-pipeline`: the pages themselves.
- `seo-audit`: Search Console and technical checks.
- `ga4-audit`: the tagging behind AI-referred sessions.
- `competitor-analysis`: who to track against.
