---
name: 0-localise
description: "Menu shortcut: runs the localization-specialist agent on your request. Pick it from the plugin menu when you want localisation work done by that specialist, for producing Dutch, French, German or Spanish versions of finished, approved content. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:localization-specialist
---

# Localisation (agent shortcut)

Handle this request as the localization-specialist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
