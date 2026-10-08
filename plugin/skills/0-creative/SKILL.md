---
name: 0-creative
description: "Menu shortcut: runs the creative-specialist agent on your request. Pick it from the plugin menu when you want creative work done by that specialist, for visual assets: briefs, social graphics, ad creative, logos, short launch or demo videos. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:creative-specialist
---

# Creative (agent shortcut)

Handle this request as the creative-specialist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
