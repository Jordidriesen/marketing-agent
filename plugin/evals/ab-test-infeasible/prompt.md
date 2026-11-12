---
max_turns: 30
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Handle this request yourself in this main thread with the plugin's skills; do not start a sub-agent. Plan an A/B test for a quote-request page of Acme Access (a fictional Belgian visitor management company). Finding: the headline is vague (it currently reads "Smart access for modern sites"). The page is https://example.com/quote. I only need the test plan and the verdict, not the variant copy; do not ask me questions, list what you could not verify instead. The page converts at 0.1% of sessions to a quote request and gets 800 sessions a month, split 50/50 in our A/B tool. We would act on a lift of 20% or more (relative). Tell me whether to run it.

Return your reply to me verbatim, including a closing Skills run line. Put the full deliverable in your reply; do not write files.
