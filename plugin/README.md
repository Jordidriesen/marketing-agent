# Marketing Agent (plugin)

A marketing team of subagents for Claude, built by [Jordi Driesen](https://github.com/Jordidriesen) for Cowork and Claude Code. A director dispatches each request to the right specialist and sequences multi-discipline campaigns in dependency order, rather than running everything at once.

**One install, agents and skills together.** As of 4.0.0 the plugin ships its 50 skills (plus 14 `0-` agent shortcuts, see below) in [`skills/`](skills) alongside the agents, so the two can't drift apart. Only client brand kits live outside it: each brand gets a private `[brand]-brand-kit` skill that every content, review and design skill loads automatically (see [`templates/brand-kit`](../templates/brand-kit)).

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

Update later with `claude plugin marketplace update marketing-agent`.

## Agents

Run `/0-marketing` for anything that spans more than one discipline. The main thread becomes the director (`director-playbook`): it writes the brief in a job folder, does the work with the skills itself, and starts a specialist thread only under four rules: parallel work, a noisy data job, a cold review, or a job that needs a profile's own model. The specialists below are those thread profiles. For a single, clearly scoped task you can still call a skill or a specialist directly.

| Order | Agent | Role | Main skills |
|---|---|---|---|
| · | [`marketing-director`](agents/marketing-director.md) | Entry point, in the main thread through `/0-marketing`. Runs the job, starts threads under the spawn rules, owns acceptance and the review tier | `director-playbook` and every skill below |
| · | [`cold-reviewer`](agents/cold-reviewer.md) | Reviews finished deliverables cold against `brief.md` and reports breaches; never edits. Tiers `light`, `full-sonnet`, `full-opus` | none (reads files only) |
| 1 | [`competitive-intel-analyst`](agents/competitive-intel-analyst.md) | Positioning, competitor moves, market intelligence, ad teardown, PR outlet mapping | `competitive-research`, `european-market-intelligence`, `media-mapping` |
| 1 | [`seo-geo-specialist`](agents/seo-geo-specialist.md) | Organic search and AI answer-engine visibility as one discipline | `content-research-orchestrator` and its stage skills, `seo-audit`, `ai-visibility-tracker` |
| 2 | [`campaign-strategist`](agents/campaign-strategist.md) | Goal plus research into a campaign brief and channel plan | `campaign-plan` |
| 3 | [`content-writer`](agents/content-writer.md) | Pages, articles, case studies, press releases | `web-content-pipeline`, `customer-story-writer`, `press-release-writer`, `copy-editing`, `ai-content-cleaner`, `brand-review`, `cro-auditor`, `ab-test-planner` |
| 3 | [`social-media-specialist`](agents/social-media-specialist.md) | Platform-native social posts and paid social ad sets | `social-content-writer`, `ad-creative-matrix`, `brand-review` |
| 3 | [`email-marketer`](agents/email-marketer.md) | Newsletters and lifecycle sequences (HubSpot or Brevo) | `newsletter-writer`, `email-sequence-hubspot-brevo`, `brand-review` |
| 3 | [`graphic-designer`](agents/graphic-designer.md) | Fixed-format visuals on approved copy: social, ads, email templates, print, decks, logos, short video | `creative-brief`, `canva-workflow`, `affinity-workflow`, `figma-weavy-workflow`, `email-design`, `logo-design`, `launch-video` |
| 3 | [`web-developer`](agents/web-developer.md) | Pages and sites in WordPress and Astro, redesigns, Figma to code, performance and accessibility | `frontend-design`, `astro-site`, `wordpress-development:wordpress-page-build`, `wordpress-development:wordpress-plugin-development` |
| 3 | [`performance-marketer`](agents/performance-marketer.md) | Google Ads end to end, plus Meta and LinkedIn Ads build plans | `google-ads-build`, `google-ads-analyse`, `google-ads-ads`, `meta-ads-manager`, `linkedin-ads-manager`, `paid-ads-report-writer` |
| 3 | [`sdr-specialist`](agents/sdr-specialist.md) | Audience research and cold email: target account lists, account briefs, ABM plans, cold email sequences. LinkedIn and reply handling parked | `account-brief`, `abm-plan`, `cold-email-sequence`, the scraper suite when installed |
| 3 | [`sales-enablement-specialist`](agents/sales-enablement-specialist.md) | Battlecards and other material that equips the sales team | `battlecard`, `brand-review` |
| 3.5 | [`localization-specialist`](agents/localization-specialist.md) | Target-language versions of signed-off content (NL, FR, DE, ES) | `content-translate`, `brand-review` |
| 4 | [`performance-reporter`](agents/performance-reporter.md) | Cross-channel reporting once execution is live, GA4 audits and attribution questions | `paid-ads-report-writer`, `measurement` |

### Models and effort

Each agent names its model and reasoning effort in its frontmatter, Opus for the director, the graphic designer (layout, imagery and animation judgement) and the web developer (long tool chains on live sites), Sonnet for every other specialist, all at medium effort. Change a value in the agent file to trade cost against quality; `inherit` makes an agent use the session's model.

| Agent | Model | Effort | Max turns |
|---|---|---|---|
| `campaign-strategist` | sonnet | medium | 50 |
| `cold-reviewer` | opus (set per tier by the director) | high | none |
| `competitive-intel-analyst` | sonnet | medium | 80 |
| `content-writer` | sonnet | medium | 60 |
| `email-marketer` | sonnet | medium | 40 |
| `graphic-designer` | opus | medium | 60 |
| `localization-specialist` | sonnet | medium | 40 |
| `marketing-director` | opus | medium | none |
| `performance-marketer` | sonnet | medium | 80 |
| `performance-reporter` | sonnet | medium | 60 |
| `sales-enablement-specialist` | sonnet | medium | 40 |
| `sdr-specialist` | sonnet | medium | 50 |
| `seo-geo-specialist` | sonnet | medium | 80 |
| `social-media-specialist` | sonnet | medium | 40 |
| `web-developer` | opus | medium | 100 |

These are the profiles' defaults. When the director starts a thread it passes `model` and `effort` from the model table in `director-playbook` (Haiku for bulk data pulls, Sonnet for research and drafting, Opus for visuals, web builds and full reviews), and logs both in the job's `decisions.md`.

Every agent preloads `marketing-agent:non-negotiables`. The specialists use `disallowedTools`, so they keep their connector (MCP) tools; the cold reviewer only has Read, Glob and Grep.

Order for a full campaign: intelligence and research first, strategy second, execution third (independent pieces in parallel threads), localisation once source content is signed off, reporting last, with a cold review at the job's tier before the publish question.

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

Ask `competitive-intel-analyst` with the competitor's name and domain. It uses `competitive-research` (its `competitor-analysis` reference for organic footprint, content and positioning, and its `competitor-teardown` reference for paid ad angles), and `european-market-intelligence` for market-level questions.

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
| `0-marketing` | marketing-director, run in the main thread so it can call specialists (multi-discipline or unsure who owns it) |
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

They are manual only (`disable-model-invocation: true`), so Claude never picks them by itself; the 50 skills still load automatically in a normal chat. The shortcuts depend on how the Claude Code and Desktop menus sort and fork, which has not been tested here. If an entry does not sort first or does not run, `@agent-marketing-agent:<name>` still calls the agent directly.

## Connectors

See [CONNECTORS.md](CONNECTORS.md) for which connector each discipline uses, what happens when one isn't connected, and the data-source rule for brands with and without an OpenSEO project.
