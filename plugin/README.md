# Marketing Agent (plugin)

A marketing team of subagents for Claude, built by [Jordi Driesen](https://github.com/Jordidriesen) for Cowork and Claude Code. A director dispatches each request to the right specialist and sequences multi-discipline campaigns in dependency order, rather than running everything at once.

**One install, agents and skills together.** As of 2.0.0 the plugin ships its 69 skills (plus 14 `0-` agent shortcuts, see below) in [`skills/`](skills) alongside the agents, so the two can't drift apart. Only client brand kits live outside it: each brand gets a private `[brand]-brand-kit` skill that every content, review and design skill loads automatically (see [`templates/brand-kit`](../templates/brand-kit)).

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

Update later with `claude plugin marketplace update marketing-agent`.

## Agents

Talk to `marketing-director` for anything that spans more than one discipline; it decides which specialist(s) to run and in what order. For a single, clearly scoped task, call the specialist directly.

| Order | Agent | Role | Main skills |
|---|---|---|---|
| · | [`marketing-director`](agents/marketing-director.md) | Entry point. Breaks a request down, delegates, assembles one result | (dispatch only) |
| 1 | [`competitive-intel-analyst`](agents/competitive-intel-analyst.md) | Positioning, competitor moves, market intelligence, ad teardown, PR outlet mapping | `competitor-analysis`, `competitive-landscape`, `competitor-teardown`, `european-market-intelligence`, `media-mapping` |
| 1 | [`seo-geo-specialist`](agents/seo-geo-specialist.md) | Organic search and AI answer-engine visibility as one discipline | `content-research-orchestrator` and its stage skills, `seo-audit`, `ai-visibility-tracker` |
| 2 | [`campaign-strategist`](agents/campaign-strategist.md) | Goal plus research into a campaign brief and channel plan | `campaign-plan` |
| 3 | [`content-writer`](agents/content-writer.md) | Pages, articles, case studies, press releases | `web-content-pipeline`, `customer-story-writer`, `press-release-writer`, `copy-editing`, `ai-content-cleaner`, `brand-review`, `cro-auditor`, `ab-test-planner` |
| 3 | [`social-media-specialist`](agents/social-media-specialist.md) | Platform-native social posts and paid social ad sets | `social-content-writer`, `ad-creative-matrix`, `brand-review` |
| 3 | [`email-marketer`](agents/email-marketer.md) | Newsletters and lifecycle sequences (HubSpot or Brevo) | `newsletter-writer`, `email-sequence-hubspot-brevo`, `brand-review` |
| 3 | [`graphic-designer`](agents/graphic-designer.md) | Fixed-format visuals on approved copy: social, ads, email templates, print, decks, logos, short video | `creative-brief`, `canva-workflow`, `affinity-workflow`, `figma-weavy-workflow`, `email-design`, `logo-design`, `launch-video` |
| 3 | [`web-developer`](agents/web-developer.md) | Pages and sites in WordPress and Astro, redesigns, Figma to code, performance and accessibility | `frontend-design`, `astro-site`, `wordpress-development:wordpress-page-build`, `wordpress-development:wordpress-plugin-development` |
| 3 | [`performance-marketer`](agents/performance-marketer.md) | Google Ads end to end, plus Meta and LinkedIn Ads build plans | the Google Ads skills, `meta-ads-manager`, `linkedin-ads-manager`, `paid-ads-report-writer` |
| 3 | [`sdr-specialist`](agents/sdr-specialist.md) | Audience research and cold email: target account lists, account briefs, ABM plans, cold email sequences. LinkedIn and reply handling parked | `account-brief`, `abm-plan`, `cold-email-sequence`, the scraper suite when installed |
| 3 | [`sales-enablement-specialist`](agents/sales-enablement-specialist.md) | Battlecards and other material that equips the sales team | `battlecard`, `brand-review` |
| 3.5 | [`localization-specialist`](agents/localization-specialist.md) | Target-language versions of signed-off content (NL, FR, DE, ES) | `content-translate`, `brand-review` |
| 4 | [`performance-reporter`](agents/performance-reporter.md) | Cross-channel reporting once execution is live, GA4 audits and attribution questions | `paid-ads-report-writer`, `metric-detective`, `ga4-audit`, `attribution-readout` |

### Models and effort

Each agent names its model and reasoning effort in its frontmatter, so judgement-heavy work (strategy, writing, paid media, code) runs on Opus and high-volume or templated work on Sonnet. Change a value in the agent file to trade cost against quality; `inherit` makes an agent use the session's model.

| Agent | Model | Effort | Max turns |
|---|---|---|---|
| `campaign-strategist` | opus | high | 50 |
| `competitive-intel-analyst` | opus | high | 80 |
| `content-writer` | opus | high | 60 |
| `email-marketer` | sonnet | medium | 40 |
| `graphic-designer` | opus | medium | 60 |
| `localization-specialist` | opus | medium | 40 |
| `marketing-director` | opus | high | none |
| `performance-marketer` | opus | high | 80 |
| `performance-reporter` | sonnet | high | 60 |
| `sales-enablement-specialist` | sonnet | medium | 40 |
| `sdr-specialist` | sonnet | medium | 50 |
| `seo-geo-specialist` | sonnet | high | 80 |
| `social-media-specialist` | sonnet | medium | 40 |
| `web-developer` | opus | high | 100 |

Every agent preloads `marketing-agent:non-negotiables`. Agents that used a fixed `tools` list now use `disallowedTools` instead, so they keep their connector (MCP) tools; only the director keeps an allowlist, because it dispatches and does not do the work.

Dispatch order for a full campaign: intelligence and research first, strategy second, execution third (these run in parallel), localisation once source content is signed off, reporting last.

## Example workflows

### Planning a campaign

Ask `marketing-director` (or `campaign-strategist` directly):

```
Goal: 150 qualified leads for the new product line
Audience: Facility managers at mid-sized companies in Belgium and Germany
Timeline: 8 weeks
Budget: EUR 20,000
```

The director runs competitive and SEO research first, then the brief, then hands each calendar item to the right specialist; localisation follows once each piece is signed off.

### Researching a competitor

Ask `competitive-intel-analyst` with the competitor's name and domain. It uses `competitor-analysis` for organic footprint, content and positioning, `competitor-teardown` for paid ad angles, and `european-market-intelligence` for market-level questions.

### Reporting on paid media

Ask `performance-reporter` (or `performance-marketer` for a Google-Ads-only report):

```
Client: [brand]
Platforms: Google Ads, LinkedIn Ads
Period: September 2026, compared with August
```

`paid-ads-report-writer` pulls live data where the connectors are connected, works from exports for the rest, normalises conversion definitions across platforms, and writes the executive summary plus a section per platform.

## Brand kits

Every content, review, design and localisation skill identifies the brand and loads its `[brand]-brand-kit` skill when one exists. A modular kit is a short router plus three modules: `context.md` (who the brand is, audiences, channels, data sources), `voice.md` (tone of voice and Voice Lock) and `design.md` (colour, type, layout tokens). Start from [`templates/brand-kit`](../templates/brand-kit).

## Agent shortcuts

Open the `/` menu, choose Plugins, then Marketing Agent. The fourteen `0-` entries sort above the skills and each runs your request through one agent. Type your request after the name.

| Entry | Agent |
|---|---|
| `0-marketing` | marketing-director (multi-discipline or unsure who owns it) |
| `0-paid-ads` | performance-marketer |
| `0-seo` | seo-geo-specialist |
| `0-content` | content-writer |
| `0-social` | social-media-specialist |
| `0-email` | email-marketer |
| `0-design` | graphic-designer |
| `0-web` | web-developer |
| `0-sdr` | sdr-specialist |
| `0-sales` | sales-enablement-specialist |
| `0-intel` | competitive-intel-analyst |
| `0-campaign` | campaign-strategist |
| `0-localise` | localization-specialist |
| `0-report` | performance-reporter |

They are manual only (`disable-model-invocation: true`), so Claude never picks them by itself; the 69 skills still load automatically in a normal chat. The shortcuts depend on how the Claude Code and Desktop menus sort and fork, which has not been tested here. If an entry does not sort first or does not run, `@agent-marketing-agent:<name>` still calls the agent directly.

## Connectors

See [CONNECTORS.md](CONNECTORS.md) for which connector each discipline uses, what happens when one isn't connected, and the data-source rule for brands with and without an OpenSEO project.
