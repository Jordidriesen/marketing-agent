# Evals in plain language

These evals check one thing: does the agent use the skill and follow it, and does the copy stay believable. Each case runs the same prompt several times, because one run proves little.

Client material is never stored here. Cases in this folder use a fictional company (Acme Access). A case built from a real client brief lives outside the repository and is run locally.

## What every case checks

- **The skill fired.** The agent called the skill. If it does not, none of the skill's rules can apply.
- **No em dashes** in the reply.

## landing-page-guidelines

**The prompt:** a paid-search landing page written from an implementation brief, the way a real page is specced: URL, ad group, negative keywords, StoryBrand, one conversion goal, a short form, and a fixed list of site components. The brief gives product facts, marks two facts as not confirmed, and says there is no customer proof yet.

**What is checked:**
- `web-content-pipeline` was used, and so were `copy-editing` and `ai-content-cleaner` (Steps 5 and 6).
- **Structure:** a hidden implementation brief at the top, every section tagged with an allowed component, one primary action everywhere, a smaller secondary path, a 4 to 6 question objection FAQ, proof as visible placeholders.
- **Framework applied:** StoryBrand with the customer as the hero: problem as a cost, the company as guide, a plan, proof, a call to action.
- **Claims plausible:** plausible claims are allowed when the brief supports them. Unconfirmed ones need a hidden `confirm` note. Statistics, customers, quotes, awards, certifications and prices are never invented.

## customer-story

A 400 word story from a short brief with one quote and one result. Checks that `customer-story-writer` was used and that only the supplied quote and result appear, with added context only where it is highly likely to be true.

## sdr-needs-input and sdr-cold-email

Both call the `sdr-specialist` agent.
- **needs-input:** the brief is missing the product, audience and sender. The agent should come back with questions and write no email.
- **cold-email:** a complete brief. Checks that `cold-email-sequence` ran, the compliance gate is respected, claims stay inside the brief, the closing `Skills run:` line is present, and no LinkedIn text appears.

## solution-page

A trigger check only: does `web-content-pipeline` fire on a request for a solution page.

## Not covered

- The marketing director cannot delegate when it is called as a subagent, so its ask-first behaviour needs a main-agent test that this harness does not offer.
- LinkedIn outreach and reply handling are parked, so there are no cases for them.
