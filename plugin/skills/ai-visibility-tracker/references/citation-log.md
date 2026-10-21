# Citation log

Loaded by `ai-visibility-tracker` in Step 3. One row per answer. Keep the log in a spreadsheet or a CSV
in the run folder; rounds are appended, never overwritten.

## Columns

| Column | Meaning |
|---|---|
| round | Round number (1, 2, ...) |
| date | Date of the check (YYYY-MM-DD) |
| engine | ChatGPT, Perplexity, Google AI Overviews, AI Mode, Gemini, Copilot, Claude, other |
| mode | Search or browsing on or off, logged in or out, location, language |
| prompt_id | Id from the prompt set, and the set version |
| run | Run number for this prompt in this round (1, 2, ...) |
| brand_mentioned | yes or no: the brand is named in the answer text |
| brand_cited | yes or no: a URL of the brand is listed as a source |
| brand_position | Order among the brands mentioned (1 = first), blank if not mentioned |
| competitors_mentioned | Names, in order |
| competitors_cited | Names whose URLs are listed as sources |
| pages_cited | The brand URLs cited |
| note | Anything odd: answer refused, no sources shown, wrong facts about the brand |

## Round summary (what the report is computed from)

Per engine, per round: answers checked (prompts x runs), brand_mentioned count, brand_cited count,
and the same for each competitor. Percentages are only ever these counts divided by the answers
checked, and are shown beside the counts. Nothing else is called a score.

## Wrong facts

When an answer states something wrong about the brand (a price, a feature, a location), log it in `note`
and list it under Needs decision: it is a content or source problem to fix, not a ranking.
