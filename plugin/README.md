# Marketing Agent

A marketing plugin built by [Jordi Driesen](https://github.com/Jordidriesen) for use with [Cowork](https://claude.com/product/cowork) and Claude Code. It's a team of subagents, not a single skill: a director dispatches marketing requests to the right specialist (competitive intelligence, SEO/GEO, campaign strategy, content, social, email, paid media, reporting), sequencing multi-discipline campaigns in dependency order rather than running everything at once.

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

## Agents

Talk to `marketing-director` for anything that spans more than one discipline; it decides which specialist(s) to run and in what order. For a single, clearly-scoped task, call the relevant specialist directly.

Dispatch order for a full campaign: intelligence and research first, strategy second, execution third (these run in parallel against each other), reporting last.

| Order | Agent | Role |
|---|---|---|
| — | [`marketing-director`](agents/marketing-director.md) | Entry point. Breaks a request down, delegates to the right specialist(s), assembles one result. |
| 1 | [`competitive-intel-analyst`](agents/competitive-intel-analyst.md) | Positioning, competitor moves, market intelligence, ad teardown, PR outlet mapping. |
| 1 | [`seo-geo-specialist`](agents/seo-geo-specialist.md) | Organic search and generative-engine (AI answer engine) visibility, treated as one discipline. |
| 2 | [`campaign-strategist`](agents/campaign-strategist.md) | Turns a goal, plus the intelligence/research above, into a full campaign brief and channel plan. |
| 3 | [`content-writer`](agents/content-writer.md) | Web and long-form content: pillar pages, clusters, landing pages, case studies, press releases. |
| 3 | [`social-media-specialist`](agents/social-media-specialist.md) | Platform-native social posts. |
| 3 | [`email-marketer`](agents/email-marketer.md) | Newsletters and lifecycle/automation sequences (HubSpot or Brevo). |
| 3 | [`performance-marketer`](agents/performance-marketer.md) | Paid media, Google Ads end to end. |
| 4 | [`performance-reporter`](agents/performance-reporter.md) | Cross-channel results reporting, once execution is live. |

Not built yet: a creative/design specialist (Canva/Figma, creative best practice). No dedicated skill exists for this yet, so it's deliberately left out rather than half-built.

## Skills

Each agent above delegates to these skills rather than duplicating their content; the skills can also be called directly.

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
