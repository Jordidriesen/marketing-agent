# Marketing Agent (plugin)

A marketing team of subagents for Claude, built by [Jordi Driesen](https://github.com/Jordidriesen) for Cowork and Claude Code. A director dispatches each request to the right specialist and sequences multi-discipline campaigns in dependency order, rather than running everything at once.

**One install, agents and skills together.** As of 2.0.0 the plugin ships its 55 skills in [`skills/`](skills) alongside the agents, so the two can't drift apart. Only client brand kits live outside it: each brand gets a private `[brand]-brand-kit` skill that every content, review and design skill loads automatically (see [`templates/brand-kit`](../templates/brand-kit)).

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
| 1 | [`seo-geo-specialist`](agents/seo-geo-specialist.md) | Organic search and AI answer-engine visibility as one discipline | `content-research-orchestrator` and its stage skills, `seo-audit` |
| 2 | [`campaign-strategist`](agents/campaign-strategist.md) | Goal plus research into a campaign brief and channel plan | `campaign-plan` |
| 3 | [`content-writer`](agents/content-writer.md) | Pages, articles, case studies, press releases | `web-content-pipeline`, `customer-story-writer`, `press-release-writer`, `copy-editing`, `ai-content-cleaner`, `brand-review` |
| 3 | [`social-media-specialist`](agents/social-media-specialist.md) | Platform-native social posts and paid social ad sets | `social-content-writer`, `ad-creative-matrix`, `brand-review` |
| 3 | [`email-marketer`](agents/email-marketer.md) | Newsletters and lifecycle sequences (HubSpot or Brevo) | `newsletter-writer`, `email-sequence-hubspot-brevo`, `brand-review` |
| 3 | [`creative-specialist`](agents/creative-specialist.md) | Creative direction and assets on approved copy | `creative-brief`, `frontend-design`, `canva-workflow`, `figma-weavy-workflow`, `logo-design`, `launch-video` |
| 3 | [`performance-marketer`](agents/performance-marketer.md) | Google Ads end to end | the Google Ads skills, `paid-ads-report-writer` |
| 3.5 | [`localization-specialist`](agents/localization-specialist.md) | Target-language versions of signed-off content (NL, FR, DE, ES) | `content-translate`, `brand-review` |
| 4 | [`performance-reporter`](agents/performance-reporter.md) | Cross-channel reporting once execution is live | `paid-ads-report-writer`, `metric-detective` |

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

## Connectors

See [CONNECTORS.md](CONNECTORS.md) for which connector each discipline uses, what happens when one isn't connected, and the data-source rule for brands with and without an OpenSEO project.
