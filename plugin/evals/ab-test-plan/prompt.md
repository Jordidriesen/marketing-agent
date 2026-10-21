---
max_turns: 30
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Use the content-writer agent. Plan an A/B test for the demo-request page of Acme Access (a fictional Belgian visitor management company). Finding from our CRO audit: the form button says "Submit" and recordings show visitors hovering over it and leaving. We want to test a button that names the outcome. Data: the page converts at 2% of sessions to a demo request, it gets 10,000 sessions a month, and traffic splits 50/50 between two variants in our A/B tool. We would only act on a lift of 20% or more (relative, so 2.0% to 2.4%). Give me the plan and tell me honestly whether to run it.

Return the agent's reply to me verbatim, including its closing Skills run line. Put the full deliverable in your reply; do not write files.
