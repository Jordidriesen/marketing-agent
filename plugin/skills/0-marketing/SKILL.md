---
name: 0-marketing
description: "Menu shortcut: runs the marketing-director agent on your request. Pick it from the plugin menu when you want marketing director work done by that specialist, for anything that spans more than one discipline, or when you are not sure which specialist owns it. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
---

# Marketing director (agent shortcut)

Use the marketing-agent:marketing-director agent (the Agent tool) to handle this request, and give it the full request:

$ARGUMENTS

If no request was given above, ask what is needed before starting. The director sequences the
specialists (research before strategy, strategy before execution) and returns one assembled result.
