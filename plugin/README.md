# Marketing Agent

A marketing plugin built by [Jordi Driesen](https://github.com/Jordidriesen) for use with [Cowork](https://claude.com/product/cowork) and Claude Code — campaign planning, competitive messaging research, and performance reporting.

**Scoped for this workspace.** Content drafting, brand review, email sequences, and SEO auditing are handled by dedicated account skills instead of duplicating them here:

| For this kind of work | Use |
|---|---|
| Writing content (blog posts, social, email, press releases) | `content-creation` (account skill, gateway) routing to `web-content-pipeline`, `customer-story-writer`, `social-content-writer`, `newsletter-writer`, and `press-release-writer` |
| Brand voice / compliance review | `brand-review` (account skill), which loads a `[brand]-brand-kit` skill automatically when one exists |
| Lifecycle email sequences | `email-sequence-hubspot-brevo` (account skill) |
| SEO research and auditing | `content-research-orchestrator` (keyword research, clustering, competitive landscape, competitor analysis, content gap mapping) plus the account's own technical `seo-audit` skill |

The three skills below remain in this plugin because no account skill covers the same ground; each includes a "Related Skills" note pointing to the account skills that pick up where it leaves off. Each also opens with a Step 0 that identifies the brand and loads its `[brand]-brand-kit` skill automatically, when one exists, so output comes out in the right voice without being told each time.

## Installation

Add this repository as a plugin source in Claude Code or Cowork, then install `marketing-agent` from it. (Exact steps depend on your Claude Code version — see the [plugin documentation](https://docs.claude.com) for the current marketplace/plugin-source syntax.)

## Commands

| Command | Description |
|---|---|
| `/campaign-plan` | Generate a full campaign brief with objectives, channels, content calendar, and success metrics |
| `/competitive-brief` | Research competitor messaging and positioning and generate a comparison, content gap analysis, and sales battlecard |
| `/performance-report` | Build a marketing performance report with key metrics, trends, and optimization recommendations |

## Skills

| Skill | Description |
|---|---|
| [`campaign-plan`](skills/campaign-plan) | Campaign frameworks, channel selection, content calendar creation, budget allocation, and success metrics |
| [`competitive-brief`](skills/competitive-brief) | Messaging/positioning research methodology, content gap analysis, positioning maps, and battlecard creation |
| [`performance-report`](skills/performance-report) | Key metrics by channel, reporting templates, trend analysis, attribution modeling, and optimization frameworks |

## Example Workflows

### Planning a Campaign

```
> /campaign-plan
Goal: Drive 500 signups for our new product launch
Audience: Technical decision-makers at enterprise companies
Timeline: 6 weeks
Budget range: $20,000-$30,000
```

Claude will produce a campaign brief covering objectives, audience segmentation, key messages, channel strategy, a week-by-week content calendar, and KPIs to track. Individual content pieces from the calendar are then handed off to the relevant account skill (see `campaign-plan`'s Related Skills note).

### Researching a Competitor's Messaging

```
> /competitive-brief
Competitor: [name]
```

Claude researches the competitor's positioning, messaging, and content strategy via web search and produces a comparison, content gap analysis, opportunities/threats, and an optional sales battlecard. For SEO-grounded competitor research instead (organic footprint, ranking keywords), use the account's `competitor-analysis` or `competitive-landscape` skill.

### Building a Performance Report

```
> /performance-report
Report type: Overall marketing report
Time period: Last quarter
```

Claude builds a report with key metrics, trend analysis, wins and misses, and prioritized recommendations. For the Google Ads-specific components, see the account's `report-writer` and `metric-detective` skills.

## Configuration

Configure your brand voice, style guide, and target personas in a local settings file for personalized output where a command references it, or rely on a `[brand]-brand-kit` account skill for automatic brand identification.

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Slack** — Share drafts, reports, and briefs with your team
- **Canva** — Create and edit design assets
- **Figma** — Access design files and brand assets
- **HubSpot** — Pull campaign data, manage contacts, and track marketing automation
- **Amplitude** — Pull product analytics and user behavior data for performance reporting
- **Notion** — Access briefs, style guides, and campaign documents
- **Ahrefs** — SEO keyword research, backlink analysis, and site audits
- **Similarweb** — Competitive traffic analysis and market benchmarking
- **Klaviyo** — Draft and review email marketing sequences and campaigns
- **Supermetrics** — Pull marketing data from multiple platforms for analytics and reporting
