# Marketing Agent

A marketing plugin built by [Jordi Driesen](https://github.com/Jordidriesen) for use with [Cowork](https://claude.com/product/cowork) and Claude Code. It's a team of subagents, not a single skill: a director dispatches marketing requests to the right specialist (competitive intelligence, SEO/GEO, campaign strategy, content, social, email, creative, paid media, localization, reporting), sequencing multi-discipline campaigns in dependency order rather than running everything at once.

**Scoped for this workspace.** The plugin ships agents only. Every specialist delegates to dedicated account skills for the actual work — content drafting, brand review, email sequences, SEO auditing, campaign planning, competitive research, and reporting are all account skills, not duplicated here:

| For this kind of work | Use |
|---|---|
| Planning a campaign (brief, calendar, channel plan, metrics) | `campaign-plan` (account skill) |
| Competitor messaging / positioning research and battlecards | `competitive-brief` (account skill); `competitor-analysis` / `competitive-landscape` for SEO-grounded data |
| Marketing performance reporting | `performance-report` (account skill); `report-writer` / `metric-detective` for the Google Ads slice |
| Writing content (blog posts, social, email, press releases) | `content-creation` (account skill, gateway) routing to `web-content-pipeline`, `customer-story-writer`, `social-content-writer`, `newsletter-writer`, and `press-release-writer` |
| Brand voice / compliance review | `brand-review` (account skill), which loads a `[brand]-brand-kit` skill automatically when one exists |
| Lifecycle email sequences | `email-sequence-hubspot-brevo` (account skill) |
| SEO research and auditing | `content-research-orchestrator` (keyword research, clustering, competitive landscape, competitor analysis, content gap mapping) plus the account's own technical `seo-audit` skill |
| Creative direction and asset production | `creative-brief` → `frontend-design` (coded UI) / `canva-workflow` / `figma-weavy-workflow` (account skills) |
| Translating finished content into a target market | `localization-specialist` (agent) → `content-translate` (account skill) |

Each account skill opens with a Step 0 that identifies the brand and loads its `[brand]-brand-kit` skill automatically, when one exists, so output comes out in the right voice without being told each time.

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

`Jordidriesen/marketing-agent` is a marketplace ([`.claude-plugin/marketplace.json`](../.claude-plugin/marketplace.json) at the repo root) offering this one plugin, sourced from `/plugin` in the same repo. Update later with `claude plugin marketplace update marketing-agent` — no need to re-add.

The plugin's agents call account skills such as `campaign-plan`, `competitive-brief`, `performance-report`, `content-creation`, `brand-review`, and `content-translate` by name. Those skills live flat in the repo root (see [the main README](../README.md#installation)) and need to be available in the same environment for the agents to work as intended.

## Agents

Talk to `marketing-director` for anything that spans more than one discipline; it decides which specialist(s) to run and in what order. For a single, clearly-scoped task, call the relevant specialist directly.

Dispatch order for a full campaign: intelligence and research first, strategy second, execution third (these run in parallel against each other), localization once source content is signed off, reporting last.

| Order | Agent | Role |
|---|---|---|
| — | [`marketing-director`](agents/marketing-director.md) | Entry point. Breaks a request down, delegates to the right specialist(s), assembles one result. |
| 1 | [`competitive-intel-analyst`](agents/competitive-intel-analyst.md) | Positioning, competitor moves, market intelligence, ad teardown, PR outlet mapping. |
| 1 | [`seo-geo-specialist`](agents/seo-geo-specialist.md) | Organic search and generative-engine (AI answer engine) visibility, treated as one discipline. |
| 2 | [`campaign-strategist`](agents/campaign-strategist.md) | Turns a goal, plus the intelligence/research above, into a full campaign brief and channel plan. |
| 3 | [`content-writer`](agents/content-writer.md) | Web and long-form content: pillar pages, clusters, landing pages, case studies, press releases. |
| 3 | [`social-media-specialist`](agents/social-media-specialist.md) | Platform-native social posts. |
| 3 | [`email-marketer`](agents/email-marketer.md) | Newsletters and lifecycle/automation sequences (HubSpot or Brevo). |
| 3 | [`creative-specialist`](agents/creative-specialist.md) | Creative direction and design assets (Canva, Figma Weave), built on approved copy. |
| 3 | [`performance-marketer`](agents/performance-marketer.md) | Paid media, Google Ads end to end. |
| 3.5 | [`localization-specialist`](agents/localization-specialist.md) | Target-language versions of signed-off source content (NL, FR, DE, ES). |
| 4 | [`performance-reporter`](agents/performance-reporter.md) | Cross-channel results reporting, once execution is live. |

## Example Workflows

### Planning a Campaign

Ask `marketing-director` (or `campaign-strategist` directly):

```
Goal: Drive 500 signups for our new product launch
Audience: Technical decision-makers at enterprise companies
Timeline: 6 weeks
Budget range: $20,000-$30,000
```

The strategist runs the `campaign-plan` account skill and produces a brief covering objectives, audience segmentation, key messages, channel strategy, a week-by-week content calendar, and KPIs. Individual pieces from the calendar are then handed to the relevant specialist — `content-writer`, `social-media-specialist`, `email-marketer`, `creative-specialist` — and, if the campaign targets more than one market, `localization-specialist` produces the translated versions once each piece is signed off.

### Researching a Competitor's Messaging

Ask `competitive-intel-analyst`:

```
Competitor: [name]
```

It runs the `competitive-brief` account skill for positioning, messaging, and content-gap analysis via web search, and `competitor-analysis` / `competitive-landscape` when SEO-grounded organic data is needed.

### Building a Performance Report

Ask `performance-reporter`:

```
Report type: Overall marketing report
Time period: Last quarter
```

It runs the `performance-report` account skill for the cross-channel structure, and leans on `report-writer` and `metric-detective` for the Google Ads-specific components.

## Configuration

Configure your brand voice, style guide, and target personas in a `[brand]-brand-kit` account skill for automatic brand identification, or in a local settings file where a skill references one.

## MCP Integrations

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](CONNECTORS.md).

This plugin works with the following MCP servers:

- **Slack** — Share drafts, reports, and briefs with your team
- **Canva** — Create and edit design assets
- **Figma** — Access design files and brand assets, run Figma Weave graphs
- **HubSpot** — Pull campaign data, manage contacts, and track marketing automation
- **Amplitude** — Pull product analytics and user behavior data for performance reporting
- **Notion** — Access briefs, style guides, and campaign documents
- **Ahrefs** — SEO keyword research, backlink analysis, and site audits
- **Similarweb** — Competitive traffic analysis and market benchmarking
- **Klaviyo** — Draft and review email marketing sequences and campaigns
- **Supermetrics** — Pull marketing data from multiple platforms for analytics and reporting
