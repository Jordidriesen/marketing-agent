# Evals in plain language

These evals check one thing: does the agent use the skill and follow it, and does the copy stay believable. They are small on purpose. Each case runs the same prompt several times, because one run proves little.

Nothing here has been run since the reset to the original skill text. Please review the cases below before they are run.

## What every case checks

- **The skill fired.** The agent called the skill. If it does not, none of the skill's rules can apply.
- **No em dashes** in the reply.

## landing-page-guidelines

**The prompt:** write landing page copy for a fictional visitor management product, with a complete brief (four product facts, a free 20-minute demo as the action, Google Ads traffic, no brand kit). The agent is not allowed to ask questions, because the brief is complete.

**What is checked:**
- `web-content-pipeline` was used.
- `copy-editing` and `ai-content-cleaner` were called (Steps 5 and 6 of the pipeline). Before the reset, the agent skipped both.
- **Framework applied:** the copy starts from the audience's problem, shows the cost of it, and presents the product as the answer (PAS or StoryBrand). Labels are not needed.
- **Claims plausible:** every product statement is at least about 90% likely to be true from the brief. Statistics, customers, quotes, awards, certifications, prices and invented mechanics are not allowed. The call to action may promise what the product is meant to fix.

## customer-story

**The prompt:** write a 400 word customer story from a short brief that holds one quote and one result.

**What is checked:**
- `customer-story-writer` was used.
- **Claims plausible:** only the supplied quote and result appear. Added context is allowed only where it is highly likely to be true. No invented events, numbers, people or implementation details.

## solution-page

A trigger check only: does `web-content-pipeline` fire on a request for a solution page. Its prompt still contains the line "I cannot answer follow-up questions", which does not matter for this check.

## Parked

The LinkedIn cases were removed with the `linkedin-outreach` skill. Outreach will come back as its own project.
