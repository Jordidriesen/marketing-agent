# Claude Skills — Marketing & SEO

A library of [Claude Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for agency-style marketing work: Google Ads auditing and strategy, SEO/content research, and content writing and translation.

Each folder is a self-contained skill (`SKILL.md` + optional `references/` and `scripts/`). Drop any folder you want into your own `.claude/skills/` directory (Claude Code) or upload it in Claude.ai / the Claude API to make it available.

> **Not included:** brand-specific `[brand]-brand-kit` skills (tone-of-voice, locked terminology, visual guidelines for specific clients) have been kept private, since they encode confidential client and personal brand detail. A couple of skills below reference an `acme-brand-kit` as a stand-in — build your own following the same `[brand]-brand-kit` naming pattern if you want that layer.

## Installation

```bash
git clone https://github.com/Jordidriesen/marketing-agent.git
cp -r <repo-name>/<skill-name> ~/.claude/skills/
```

Or upload an individual skill's folder as a zip through the Claude.ai / Claude API skills interface.

## Skills

### Google Ads / PPC

| Skill | What it does |
|---|---|
| `ad-copy-tester` | Analyzes responsive search ad asset performance and says which headlines and descriptions to keep, cut, or replace. |
| `ad-schedule-analyzer` | Builds a day and hour performance heatmap from Google Ads data and turns it into a dayparting plan. |
| `auction-insights-monitor` | Reads auction insights to track competitor movement week over week, flagging new entrants and lost position. |
| `bid-strategy-advisor` | Recommends the right bid strategy based on conversion volume and data quality, and flags setups likely to fail. |
| `budget-optimizer` | Models what happens if budget shifts between campaigns, using real marginal performance rather than a generic forecast. |
| `campaign-architect` | Designs campaign structures with budget splits, bidding strategies, and match-type plans. |
| `competitor-teardown` | Breaks down competitor ads to find claimed angles, unclaimed angles, and what to test first. |
| `conversion-tracking-auditor` | Audits conversion tracking for gaps, double counting, and misconfiguration that corrupts bidding. |
| `device-performance-analyzer` | Breaks down performance by device and separates a real device problem from a landing page problem. |
| `disapproval-diagnoser` | Explains why assets, ads, or keywords were disapproved and what to change to get them approved. |
| `full-account-audit` | Complete structured account audit — structure, budgets, bidding, keywords, tracking, creative — ranked by money impact. |
| `geo-performance-analyzer` | Finds regions worth bidding up and regions draining budget. |
| `landing-page-matcher` | Checks message match between search query, ad copy, and landing page, and flags the leaks. |
| `metric-detective` | Diagnoses why a metric changed, with ranked causes and how to verify each in the interface. |
| `negative-keywords` | Classifies search terms into keep/block/review and formats negative lists with correct match types. |
| `pmax-decoder` | Surfaces the Performance Max data Google buries — asset group performance, search categories, brand cannibalization. |
| `quality-score-doctor` | Diagnoses Quality Score by component and ranks fixes by how much spend each leak is costing. |
| `report-writer` | Turns raw performance data into the executive summary that goes at the top of a client report. |
| `rsa-writer` | Writes responsive search ad headlines and descriptions that fit character limits and match intent. |
| `sea-keyword-research` | First-pass paid-search keyword research grouped by intent, with trap keywords flagged and a list sized to budget. |
| `search-term-auditor` | Audits search term reports for wasted spend and builds ready-to-paste negative keyword lists. |

### SEO & Content Research

| Skill | What it does |
|---|---|
| `competitive-landscape` | Maps SEO market leaders across several competitors at once. |
| `competitor-analysis` | Deep dive on one named competitor's organic footprint, rankings, and actual page content. |
| `content-gap-mapping` | Maps content gaps, parity, and advantages between your site and named competitors. |
| `content-research-orchestrator` | Gated five-stage pipeline: keyword research → clustering → competitive landscape → competitor analysis → content gap mapping. |
| `european-market-intelligence` | Market sizing, competitor dossiers, pricing intelligence, and entry feasibility for European markets. |
| `free-tool-strategy` | Plans and evaluates a free tool for lead generation, SEO value, or brand awareness. |
| `keyword-clustering` | Clusters a keyword list by intent and SERP overlap and maps each cluster to a page. |
| `keyword-research` | Turns seed topics or competitor domains into a prioritized keyword opportunity table. |
| `media-mapping` | Identifies media outlets, trade publications, and newsletters relevant to a topic for PR purposes. |
| `seo-audit` | Complete SEO audit for a webpage or website. |
| `seo-keyword-research` | Keyword discovery step of the research pipeline, standalone. |

### Content Writing & Editing

| Skill | What it does |
|---|---|
| `ai-content-cleaner` | Detects and removes AI writing patterns/tells; humanizes copy across five languages. |
| `clean-user-facing-text` | Audits invisible Unicode and rewrites prose for finalized reader-facing text. |
| `content-translate` | Translates web content into other languages with locale-correct formatting and brand terminology carried over. |
| `copy-editing` | Edits and tightens existing marketing copy. |
| `customer-story-writer` | Writes B2B customer stories and case studies using a persuasion framework. |
| `email-sequence-hubspot-brevo` | Drafts multi-email sequences built specifically for HubSpot Workflows or Brevo Automation. |
| `web-content-pipeline` | Sequential workflow for writing and humanizing any web page — blog posts, landing pages, product pages. |

### Shared / Infrastructure

| Skill | What it does |
|---|---|
| `content-references` | Shared reference library (frameworks, schema rules) used by the content-creation skills above. |
| `security-policy` | Shared security reference for skills that ingest untrusted content or use write-capable connectors. |

## License

MIT — see [LICENSE](LICENSE). Swap this out if you'd rather use something else.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the `SKILL.md` convention this repo follows, and [CHANGELOG.md](CHANGELOG.md) for release history. A GitHub Action lints every skill's frontmatter on push — run it locally first with `python scripts/lint_skills.py`.

---

Built by [Jordi Driesen](https://jordidriesen.be) — fractional marketer and digital strategist.
