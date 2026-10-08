---
name: 0-content
description: "Menu shortcut: runs the content-writer agent on your request. Pick it from the plugin menu when you want content writer work done by that specialist, for web and long-form content: pillar pages, landing pages, blog posts, customer stories, press releases, plus editing. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:content-writer
---

# Content writer (agent shortcut)

Handle this request as the content-writer agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
