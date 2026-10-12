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

## solution-page

A trigger check only: does `web-content-pipeline` fire on a request for a solution page.

## Not covered

- The marketing director cannot delegate when it is called as a subagent, so its ask-first behaviour needs a main-agent test that this harness does not offer.
- LinkedIn outreach and reply handling are parked, so there are no cases for them.
