---
name: 0-intel
description: "Menu shortcut: runs the competitive-intel-analyst agent on your request. Pick it from the plugin menu when you want competitive intelligence work done by that specialist, for competitor messaging and positioning, organic footprint, paid ad teardown, European market intelligence, PR outlet mapping. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:competitive-intel-analyst
---

# Competitive intelligence (agent shortcut)

Handle this request as the competitive-intel-analyst agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
