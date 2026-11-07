---
type: llm
---
PASS if the reply works from the `ga4-audit` task of the `measurement` skill (its Skills run line names `measurement` with `ga4-audit`, or the reply clearly follows that task) and does not answer the request from general knowledge without the skill. A Needs input block that asks for the missing data in that task's terms also passes. FAIL otherwise.
