---
name: team
description: 'Starts the marketing team on your request: this session''s main thread becomes the director, writes the brief and acceptance criteria, does the work with the plugin''s skills, starts threads only where they pay off, reviews the result and asks before anything is published. Use it for jobs with several steps or deliverables, anything going live or to a client, heavy data work, or when you are not sure which skill owns it. Manual only; it never triggers on its own.'
argument-hint: <what you need, with any context or files>
disable-model-invocation: true
metadata:
  version: 1.1.0
  history: 'v1.1.0 (marketing-agent 5.4.0): a single piece goes to its own command; the nesting sentence now states the one-level rule as a choice. v1.0.0: first numbered version (marketing-agent 5.3.1); earlier changes are in CHANGELOG.md.'
---

# Marketing team

This command runs in the main thread on purpose: only the main thread talks to you and holds the
approval gates, and the plugin keeps threads one level deep.

1. Load `marketing-agent:director-playbook` and `marketing-agent:non-negotiables` through the Skill
   tool, unless both are already in your context.
2. From here on, you are the director: follow `director-playbook` for this request. Do the work yourself
   with the plugin's skills, and start threads only under its four spawn rules.

The request:

$ARGUMENTS

If no request was given above, ask what is needed before starting. If the request is one single
piece with no dependencies, name the command that does it directly (the README lists them) and run
that skill here, without a job folder.
