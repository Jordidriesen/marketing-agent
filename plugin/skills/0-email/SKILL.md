---
name: 0-email
description: "Menu shortcut: runs the email-marketer agent on your request. Pick it from the plugin menu when you want email work done by that specialist, for newsletters and multi-email sequences for HubSpot or Brevo. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:email-marketer
---

# Email (agent shortcut)

Handle this request as the email-marketer agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
