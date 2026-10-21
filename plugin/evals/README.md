# Evals in plain language

These evals check one thing: does the agent use the skill and follow it, and does the copy stay believable. Each case runs the same prompt several times, because one run proves little.

Client material is never stored here. Cases in this folder use a fictional company (Acme Access). A case built from a real client brief lives outside the repository and is run locally.

## How results are read

Objective checks (the skill fired, Steps 5 and 6 ran, no em dashes, no competitor names) are scored automatically. Judgement checks (is a claim plausible, does the page follow its framework) are better read as three states. `tools/judge3.py` re-judges a result file as PASS, FAIL or UNSURE: UNSURE means the person operating the chat decides, and the marketing director asks "Can we publish this as is?" with the open items listed.

## What every case checks

- **The skill fired.** The agent called the skill. If it does not, none of the skill's rules can apply.
- **No em dashes** in the reply.

## landing-page-guidelines

**The prompt:** a paid-search landing page written from an implementation brief, the way a real page is specced: URL, ad group, negative keywords, one conversion goal, a short form, and a fixed list of site components. The framework is left to the skill. The brief gives product facts, marks two facts as not confirmed, and says there is no customer proof yet.

**What is checked:**
- `web-content-pipeline` was used, and so were `copy-editing` and `ai-content-cleaner` (Steps 5 and 6).
- **Structure:** a hidden implementation brief at the top, a hidden component tag above every section, one primary action everywhere, a smaller secondary path, a 3 to 6 question objection FAQ, missing proof as Lorem Ipsum with a hidden note, neutral headings, and nothing editor-facing visible on the rendered page.
- **Framework applied:** the page follows the framework it names (any fitting one, not necessarily StoryBrand).
- **Claims plausible:** plausible claims are allowed when the brief supports them. Unconfirmed ones need a hidden `confirm` note. Statistics, customers, quotes, awards, certifications and prices are never invented.

## customer-story

A story from a short brief with one quote and one result. Checks that `customer-story-writer` was used and that nothing beyond the brief appears: no added context, scenes or consequences.

## sdr-needs-input and sdr-cold-email

Both call the `sdr-specialist` agent.
- **needs-input:** the brief is missing the product, audience and sender. The agent should come back with questions and write no email.
- **cold-email:** a complete brief. Checks that `cold-email-sequence` ran, the compliance gate is respected, claims stay inside the brief, the closing `Skills run:` line is present, and no LinkedIn text appears.

## routing-*

Twelve realistic requests that name no agent, each checking that the right specialist is called. Used to test that shorter agent descriptions still route correctly.

## social-linkedin, press-release, newsletter, rsa

Check that the skill fires and that its follow-up skills (`copy-editing`, `ai-content-cleaner`) are actually called through the Skill tool, and for the LinkedIn post that the platform rules are followed.

## emi-sizing

Forces `european-market-intelligence` on a market sizing request and checks which reference files are read.

## solution-page

A trigger check only: does `web-content-pipeline` fire on a request for a solution page.

## cleaner-short-en, cleaner-short-nl and cleaner-long

Check the `ai-content-cleaner` paths. The short cases (English and Belgian Dutch LinkedIn posts) check that the AI tells are gone and that the price, the quote and the URL are untouched. The long case checks that `references/long-form.md` is read and that the text keeps its meaning.

## emi-trigger

A trigger check only: does `european-market-intelligence` fire on a plain "how big is the market" request.

## cro-audit, ab-test-plan and ab-test-infeasible

`cro-audit` gives a page with three planted flaws (vague button, buried proof, a six-field newsletter form) and checks that `cro-auditor` fired, that its checklist was read, that all three flaws are found and that no lift or benchmark is invented. `ab-test-plan` checks the computed sample size and duration for 2% baseline, 10,000 sessions and a 20% minimum effect (about 21,000 per variant, about 18 weeks) and an honest verdict. `ab-test-infeasible` gives 0.1% on 800 sessions and expects a clear "do not run".

## ga4-audit and attribution

`ga4-audit` is run on a seeded export (the goal event has zero counts, UTMs in several conventions) and checks that both are ranked at the top and that the evidence is labelled honestly. `attribution` is a GA4 against Google Ads gap where the planted cause is the counting method (every against once per session, plus a refreshed thank-you page); the cause must rank first and the figures must stay within the numbers given.

## meta-plan, meta-trigger and linkedin-plan

`meta-plan` and `linkedin-plan` check that the build plan is complete and honest: no invented cost per lead, CPM, CPC or audience size, the 300 member account minimum and a size verdict for the 40 account LinkedIn list, and the statement that the channel is not connected so the output is a plan. `meta-trigger` checks that a plain "set up a Facebook campaign" request reaches `meta-ads-manager`. These cases go through the `performance-marketer` agent.

## ai-vis

Two seeded rounds of citation counts; the report must name the right mover and engine (Perplexity), call ChatGPT and Google AI Overviews flat, state the small sample and invent no score.

## routing-meta, routing-measure, routing-cro and routing-aivis

Plain requests that name no agent. The expected agents are `performance-marketer`, `performance-reporter`, `content-writer` and `seo-geo-specialist`.

## Not covered

- The marketing director cannot delegate when it is called as a subagent, so its ask-first behaviour needs a main-agent test that this harness does not offer.
- LinkedIn outreach and reply handling are parked, so there are no cases for them.
