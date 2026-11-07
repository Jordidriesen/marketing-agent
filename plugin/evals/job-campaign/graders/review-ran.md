---
type: llm
---
PASS if the reply reports a cold review at tier `full-opus` (the director-playbook default for this kind of job) that actually ran on the deliverables, and every finding it raised was either fixed or passed to the user. Also PASS if the user's prompt set another tier and that tier ran. FAIL if no review ran, if the tier was lower without a stated reason, or if the reply claims a review it did not run.
