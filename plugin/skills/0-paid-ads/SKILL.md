---
name: 0-paid-ads
description: "Menu shortcut: runs the performance-marketer agent on your request. Pick it from the plugin menu when you want paid ads work done by that specialist, for Google Ads work: structure, budgets, bidding, keywords and negatives, ad copy, Performance Max, tracking, disapprovals, auction insights. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:performance-marketer
---

# Paid ads (agent shortcut)

Handle this request as the performance-marketer agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
