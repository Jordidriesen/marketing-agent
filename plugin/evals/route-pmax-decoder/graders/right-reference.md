---
type: llm
---
PASS if the reply works from the `pmax-decoder` task of the `google-ads-analyse` skill (its Skills run line names `google-ads-analyse` with `pmax-decoder`, or the reply clearly follows that task) and does not answer the request from general knowledge without the skill. A Needs input block that asks for the missing data in that task's terms also passes. FAIL otherwise.
