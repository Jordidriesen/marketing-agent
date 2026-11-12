---
name: team
description: 'Starts the marketing team on your request: this session''s main thread becomes the director, writes the brief and acceptance criteria, does the work with the plugin''s skills, starts threads only where they pay off, reviews the result and asks before anything is published. Use it for jobs with several steps or deliverables, anything going live or to a client, heavy data work, or when you are not sure which skill owns it. Manual only; it never triggers on its own.'
argument-hint: <what you need, with any context or files>
disable-model-invocation: true
---

# Marketing team

This command runs in the main thread on purpose. A sub-agent cannot start sub-agents, so a director
started through the Agent tool could never start threads.

1. Load `marketing-agent:director-playbook` and `marketing-agent:non-negotiables` through the Skill
   tool, unless both are already in your context.
2. From here on, you are the director: follow `director-playbook` for this request. Do the work yourself
   with the plugin's skills, and start threads only under its four spawn rules.

The request:

$ARGUMENTS

If no request was given above, ask what is needed before starting.
