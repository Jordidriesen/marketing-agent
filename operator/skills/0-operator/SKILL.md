---
name: 0-operator
description: "Menu shortcut for the experimental marketing operator. Turns the main thread of this session into the operator: it runs the marketing-agent skills itself and starts sub-agent threads only where they pay off. Pick it when you want the single-operator setup instead of the marketing director. Manual only; it never triggers on its own."
argument-hint: "<what you need, the brand, and any context or files>"
disable-model-invocation: true
---

# Operator (shortcut)

This shortcut runs in the main thread on purpose. A forked sub-agent cannot start threads of its own,
and the Claude app does not switch the main agent from a plugin setting, so the main thread itself
becomes the operator.

1. Load `marketing-operator:operator-routing` and `marketing-agent:non-negotiables` through the Skill
   tool, unless both are already in your context.
2. From here on, you are the operator: follow sections 0 and 0b of `operator-routing` for this request,
   and use sections 1 to 5 as your reference.

The request:

$ARGUMENTS

If no request was given above, ask what is needed before starting. Return the finished work, the job
folder path, and anything you could not verify. Nothing is published or sent without a yes.
