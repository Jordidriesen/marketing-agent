---
name: 0-social
description: "Menu shortcut: runs the social-media-specialist agent on your request. Pick it from the plugin menu when you want social media work done by that specialist, for platform-native posts for LinkedIn, Instagram, X and Reddit, and paid social creative sets. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:social-media-specialist
---

# Social media (agent shortcut)

Handle this request as the social-media-specialist agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
