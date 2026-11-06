---
name: 0-design
description: "Menu shortcut: runs the graphic-designer agent on your request. Pick it from the plugin menu when you want design work done by that specialist, for fixed-format visuals: briefs, social and ad visuals, email templates, print, logos, short launch or demo videos, in Canva, Affinity, Figma Weave or Adobe. Manual only; it never triggers on its own."
argument-hint: "<what you need, with any context or files>"
disable-model-invocation: true
context: fork
agent: marketing-agent:graphic-designer
---

# Design (agent shortcut)

Handle this request as the graphic-designer agent, following your own instructions and your skill suite:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, and
list anything you could not verify.
