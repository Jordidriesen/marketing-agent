---
name: 0-operator
description: "Menu shortcut for the experimental marketing-operator. Hands your request to the operator when the session's main agent is marketing-operator; otherwise explains how to switch. Manual only; it never triggers on its own."
argument-hint: "<what you need, the brand, and any context or files>"
disable-model-invocation: true
---

# Operator (shortcut)

The operator has to be the session's **main agent**. It is not started as a forked sub-agent on
purpose: a sub-agent cannot start threads of its own, so a forked operator could never spawn the
parallel, background or review threads its design relies on.

**If you are the marketing-operator** (your instructions say "You are the marketing operator"), handle
this request following your own instructions and `operator-routing`:

$ARGUMENTS

If no request was given, ask what is needed before starting.

**If you are any other agent** (for example `marketing-director`), do not attempt the work and do not
imitate the operator. Reply with these steps and stop:

1. In the folder you work in, open or create `.claude/settings.json` and set
   `"agent": "marketing-operator:marketing-operator"`.
2. Start a new session in that folder, then run `/0-operator` again.
3. To go back to the director, remove that line (the marketing-agent plugin makes
   `marketing-director` the default).
