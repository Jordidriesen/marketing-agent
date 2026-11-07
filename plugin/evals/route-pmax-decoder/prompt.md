---
max_turns: 12
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Load the marketing-agent:director-playbook skill through the Skill tool and handle this request yourself as the director it describes, in this main thread. Context: Acme Access is a fictional Belgian company selling cloud visitor management and access control. No connectors are available; where data is needed and missing, ask for it rather than inventing it. Return your reply to me verbatim, including the Skills run line.

Request: What is our Performance Max campaign actually spending on? Is it just eating our brand searches?
