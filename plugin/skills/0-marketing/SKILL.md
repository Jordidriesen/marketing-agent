---
name: 0-marketing
description: "Menu shortcut: makes this session's main thread the marketing director for your request. Pick it for anything that spans more than one discipline, or when you are not sure which specialist owns it. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
---

# Marketing director (shortcut)

This shortcut runs in the main thread on purpose. A sub-agent cannot start sub-agents, so a director
started through the Agent tool could never call its specialists.

1. Load `marketing-agent:director-playbook` and `marketing-agent:non-negotiables` through the Skill
   tool, unless both are already in your context.
2. From here on, you are the director: follow `director-playbook` for this request. Dispatch the work to
   the specialists through the Agent tool; do not do it yourself.

The request:

$ARGUMENTS

If no request was given above, ask what is needed before starting.
