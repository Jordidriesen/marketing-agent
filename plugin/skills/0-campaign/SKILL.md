---
name: 0-campaign
description: "Menu shortcut: runs the campaign-strategist agent on your request. Pick it from the plugin menu when you want campaign strategy work done by that specialist, for turning a goal and a timeline into a full campaign brief. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:campaign-strategist
---

# Campaign strategy (agent shortcut)

Handle this request as the campaign-strategist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
