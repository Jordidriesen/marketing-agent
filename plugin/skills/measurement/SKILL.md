---
name: measurement
description: 'Measurement diagnosis: why a Google Ads metric changed, GA4 setup audits (key events, consent mode, UTMs, PII), and attribution (which channel drives conversions, why GA4 and ad platforms disagree). Use for "why did this change", a spike or drop, "GA4 audit", "is my analytics set up right", "GA4 numbers look wrong", "attribution", "GA4 and Ads don''t match", even from pasted figures.'
metadata:
  version: 1.3.0
  history: 'v1.3.0: GA4 consent check can be confirmed with the Chrome DevTools MCP network list. v1.2.0: the GA4 audit measures which tag hosts fire before consent with frontend-design verify.mjs --inventory-only. v1.1.0 (marketing-agent 5.4.0): a diagnosis that found a cause proposes a learning. v1.0.0: new family skill in marketing-agent 4.0.0 (built first in the marketing-operator trial). Absorbs metric-detective, ga4-audit, attribution-readout as references, unchanged apart from names and paths.'
---

# Measurement

One skill for a family of related tasks that share the same inputs and connectors. Each task is a full reference file: pick the row that matches the request, read that file **in full**, and follow it as the skill. Where a request needs two tasks (an audit, then the search terms), run them one after the other, each from its own file.

| Task reference | Use it for |
|---|---|
| `references/metric-detective.md` | Diagnoses why a Google Ads metric changed, with ranked causes and how to verify each. Use for any spike, drop or "why did this change". |
| `references/ga4-audit.md` | Always use for any GA4 or web analytics setup check, even from pasted exports: key events against the funnel, consent mode, UTM taxonomy, filters, cross-domain and PII hygiene, ranked by decision impact. Use for "GA4 audit", "is my analytics set up right", "GA4 numbers look wrong". Google Ads conversion actions: conversion-tracking-auditor. |
| `references/attribution-readout.md` | Always use for any question about which channel drives conversions or why GA4 and ad platform numbers differ, even from pasted figures: lines up definitions, compares attribution models, ranks causes of the gap, names the test that would settle it. Use for "which channel works", "attribution", "GA4 and Ads don't match". Trend diagnosis: metric-detective. |

If no row fits, say so and name the skill that does fit rather than stretching a reference.

**Required skill calls.** The references name the skills they call (for example `brand-review` or `ai-content-cleaner`); call those through the Skill tool, never imitate them inline. End the reply with one line: `Skills run: ...`, naming this skill and the reference used, for example `Skills run: measurement (metric-detective)`.

**Learnings.** A diagnosis that established a cause (not a guess) ends with a proposed learning line for `brand/learnings.md`, written only after a yes; format in `brand-learnings`.
