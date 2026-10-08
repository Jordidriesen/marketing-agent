---
name: 0-sales
description: "Menu shortcut: runs the sales-enablement-specialist agent on your request. Pick it from the plugin menu when you want sales enablement work done by that specialist, for battlecards, cold email sequences and LinkedIn outreach drafts. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:sales-enablement-specialist
---

# Sales enablement (agent shortcut)

Handle this request as the sales-enablement-specialist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
