---
name: 0-report
description: "Menu shortcut: runs the performance-reporter agent on your request. Pick it from the plugin menu when you want performance reporting work done by that specialist, for cross-channel performance reports with wins, misses and next steps. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:performance-reporter
---

# Performance reporting (agent shortcut)

Handle this request as the performance-reporter agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
