# Prompt set

Loaded by `ai-visibility-tracker` in Step 1. A prompt set is a stored, versioned list of questions. It is
the instrument: change it and you can no longer compare with earlier rounds.

## How to write the prompts

- **Buyer questions, not marketing phrases.** Write what a real buyer types or says to an assistant:
  "Which visitor management software works for a warehouse with two gates?", not "best visitor
  management solution". Take them from sales calls, support tickets, search queries and the
  `[brand]-brand-kit` personas, never from the brand's own taglines.
- **Do not name the brand** in non-branded prompts. A branded prompt measures recall of the brand; a
  non-branded one measures discovery. Keep both, labelled, in separate columns of the report.
- **One question per prompt**, in the language and phrasing of the market. Dutch, French and English are
  separate sets; do not translate a prompt and call it the same prompt.
- **Cover the funnel**: problem-aware ("how do I keep track of contractors on site"), solution-aware
  ("what should I look for in visitor management software"), vendor-comparing ("[brand] versus
  [competitor]", "alternatives to [competitor]"), and decision ("is [brand] GDPR compliant", "what does
  [brand] cost" where the answer is public).
- **Suggested minimum** of five prompts per funnel stage and language, so no single answer decides the
  picture. More is better; the cost is the person-time of running them.

## Table to store

| Id | Version | Language | Funnel stage | Branded | Prompt | Added on |
|---|---|---|---|---|---|---|
| P01 | v1 | nl-BE | problem | no | (the question) | (date) |

## Versioning

- v1 is the first set, dated. Adding or removing a prompt creates v2; so does rewording one.
- A round uses exactly one version. The report compares only rounds that share a version, or compares
  the prompts the two versions have in common and says so.
- Never edit a prompt in place after a round has used it.
