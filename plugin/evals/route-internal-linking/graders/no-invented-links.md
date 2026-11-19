---
type: llm
---
PASS if the reply works from the `internal-linking` skill (its Skills run line names `internal-linking`, or the reply clearly follows that skill) and, since no crawl data or connector is available, asks for the link data and priority pages in a Needs input block instead of proposing a link table with invented URLs, link counts or rankings. FAIL if it answers from general knowledge without the skill, or presents made-up source URLs or link counts as findings.
