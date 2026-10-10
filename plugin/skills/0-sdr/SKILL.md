---
name: 0-sdr
description: "Menu shortcut: runs the sdr-specialist agent on your request. Pick it from the plugin menu when you want SDR work done by that specialist, for target account lists, account briefs, cold email and LinkedIn outreach drafts, reply triage and ABM plans. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:sdr-specialist
---

# SDR (agent shortcut)

Handle this request as the sdr-specialist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
