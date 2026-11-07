---
name: google-ads-ads
description: 'Google Ads ad copy: responsive search ad headlines (30 characters) and descriptions (90) matched to search intent, and reading RSA asset performance to keep, cut or replace assets. Use for "ad copy", "RSA", "Google Ads headlines", "which headlines should go", "this ad underperforms". Paid social and video ads: ad-creative-matrix.'
metadata:
  version: 1.0.0
  history: 'v1.0.0: new family skill in marketing-agent 4.0.0 (built first in the marketing-operator trial). Absorbs rsa-writer, ad-copy-tester as references, unchanged apart from names and paths.'
---

# Google Ads Ads

One skill for a family of related tasks that share the same inputs and connectors. Each task is a full reference file: pick the row that matches the request, read that file **in full**, and follow it as the skill. Where a request needs two tasks (an audit, then the search terms), run them one after the other, each from its own file.

**Shared reference.** `references/google-ads-tool-map.md` lists the Google Ads connector tools and their parameters. Every task reference points to it; read it before the first live call, and load `mcp-efficiency` for how to call the connector cheaply.

| Task reference | Use it for |
|---|---|
| `references/rsa-writer.md` | Writes Google Ads responsive search ad headlines (30 characters) and descriptions (90) that match search intent. Use for "ad copy", "RSA", "Google Ads headlines". Paid social and video ads: ad-creative-matrix. |
| `references/ad-copy-tester.md` | Reads Google RSA asset performance and says which headlines and descriptions to keep, cut or replace. Use when an ad underperforms or asset data is shared. |

If no row fits, say so and name the skill that does fit rather than stretching a reference.

**Required skill calls.** The references name the skills they call (for example `brand-review` or `ai-content-cleaner`); call those through the Skill tool, never imitate them inline. End the reply with one line: `Skills run: ...`, naming this skill and the reference used, for example `Skills run: google-ads-ads (rsa-writer)`.
