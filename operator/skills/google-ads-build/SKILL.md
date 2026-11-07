---
name: google-ads-build
description: 'Google Ads planning and setup: campaign structure and ad groups, keyword research by intent with OpenSEO volume and CPC, bid strategy choice, and budget shifts between campaigns. Use for "campaign structure", "restructure the account", "PPC keywords", "which bid strategy", "where should budget go", "should we scale this campaign". A live account''s problems: google-ads-analyse. Ad copy: google-ads-ads.'
metadata:
  version: 1.0.0
  history: 'v1.0.0: new family skill in marketing-operator 0.2.0, generated once from marketing-agent 3.1.2. Absorbs campaign-architect, sea-keyword-research, bid-strategy-advisor, budget-optimizer as references, unchanged apart from names and paths.'
---

# Google Ads Build

One skill for a family of related tasks that share the same inputs and connectors. Each task is a full reference file: pick the row that matches the request, read that file **in full**, and follow it as the skill. Where a request needs two tasks (an audit, then the search terms), run them one after the other, each from its own file.

**Shared reference.** `references/google-ads-tool-map.md` lists the Google Ads connector tools and their parameters. Every task reference points to it; read it before the first live call, and load `mcp-efficiency` for how to call the connector cheaply.

| Task reference | Use it for |
|---|---|
| `references/campaign-architect.md` | Designs Google Ads campaign structure: campaigns, ad groups, budget split, bidding and match types. Use when launching or restructuring an account. |
| `references/sea-keyword-research.md` | Google Ads keyword research by intent with traps flagged and a launch list sized to budget, using OpenSEO volume and CPC. Use for "PPC keywords", planning a new Google Ads campaign. |
| `references/bid-strategy-advisor.md` | Recommends the right Google Ads bid strategy for the conversion volume and goals, and flags strategies set up to fail. Use when choosing or troubleshooting bidding. |
| `references/budget-optimizer.md` | Models Google Ads budget shifts between campaigns from real marginal performance. Use for "where should budget go", "should we scale this campaign". |

If no row fits, say so and name the skill that does fit rather than stretching a reference.

**Required skill calls.** The references name the skills they call (for example `brand-review` or `ai-content-cleaner`); call those through the Skill tool, never imitate them inline. End the reply with one line: `Skills run: ...`, naming this skill and the reference used, for example `Skills run: google-ads-build (campaign-architect)`.
