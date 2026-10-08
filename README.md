# Marketing Agent: a Claude marketing team

A marketing team for Claude in one install: a director, eleven specialist subagents, and the 57 skills they run on. Built for agency-style work across Google Ads, paid social, SEO and GEO research, content, email, creative and localisation, on a budget-conscious stack (OpenSEO instead of Ahrefs or Semrush, the ad platforms' own connectors instead of a paid data aggregator).

You act as the operator: ask `marketing-director` for anything that spans disciplines, or call a specialist directly for a single task.

## Repository layout

```
plugin/                    the installable plugin
  .claude-plugin/          plugin manifest
  agents/                  marketing-director and eleven specialists
  skills/                  every skill the agents use (57)
  .mcp.json                connectors with a public endpoint
  CONNECTORS.md            which connector each discipline uses, and the data-source rule
templates/brand-kit/       blank modular brand kit: router + context, voice, design
archive/                   retired skills kept for reference, not installed
scripts/lint_skills.py     frontmatter lint, run in CI
```

**Brand kits are not in this repo.** Each client gets a private `[brand]-brand-kit` skill (identity, voice, design) installed separately in your Claude account. Every content, review and design skill looks for one by that naming pattern and loads it automatically. Start from [`templates/brand-kit`](templates/brand-kit).

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

This installs the agents and all skills together, so they can't drift apart. Update later with `claude plugin marketplace update marketing-agent`.

To use a single skill without the plugin, copy its folder from `plugin/skills/` into `~/.claude/skills/` or upload it as a zip in Claude settings.

Connect the tools you use in Claude's connector settings; see [`plugin/CONNECTORS.md`](plugin/CONNECTORS.md). Skills say plainly when a connector they need isn't there rather than estimating data.

## Agents

See [`plugin/README.md`](plugin/README.md) for each agent's role and the order a full campaign runs in: intelligence and research, then strategy, then execution, then localisation, then reporting.

## Skills

### Paid search and Google Ads

| Skill | What it does |
|---|---|
| `ad-copy-tester` | Keep, cut or replace RSA headlines and descriptions from asset performance |
| `ad-creative-matrix` | 50 hooks, 5 bodies and 3 CTAs for paid social and video ads, screened, tagged and test-planned |
| `ad-schedule-analyzer` | Day-and-hour heatmap and a dayparting plan |
| `auction-insights-monitor` | Competitor movement in auction insights, week over week |
| `bid-strategy-advisor` | The right bid strategy for the conversion volume and data quality |
| `budget-optimizer` | Models budget shifts between campaigns on real marginal performance |
| `campaign-architect` | Campaign structure, budget splits, bidding and match types |
| `competitor-teardown` | Angles competitors' ads claim, angles nobody claims, what to test |
| `conversion-tracking-auditor` | Gaps, double counting and misconfigured conversion actions |
| `device-performance-analyzer` | Device performance and bid adjustments |
| `disapproval-diagnoser` | Why something was disapproved and what to change |
| `full-account-audit` | Complete account audit ranked by money impact |
| `geo-performance-analyzer` | Regions to bid up and regions draining budget |
| `google-ads-tool-map` | Shared reference: Google Ads connector tools and parameters |
| `landing-page-matcher` | Message match between query, ad and landing page |
| `metric-detective` | Why a metric moved, with ranked causes and how to verify each |
| `pmax-decoder` | Performance Max asset groups, search categories, brand cannibalisation |
| `quality-score-doctor` | Quality Score by component, fixes ranked by spend at risk |
| `rsa-writer` | RSA headlines and descriptions within character limits |
| `sea-keyword-research` | Paid search keyword list by intent, sized to budget |
| `search-term-auditor` | Wasted spend, keep/block/review classification and paste-ready negative lists with match types |

### Paid media reporting

| Skill | What it does |
|---|---|
| `paid-ads-report-writer` | Client-ready reports for any paid platform, search and social: executive summary, per-platform sections, a normalised cross-platform view. Replaces `report-writer` |

### SEO, GEO and research

| Skill | What it does |
|---|---|
| `competitive-landscape` | SEO market leaders across several competitors |
| `competitor-analysis` | Deep dive on one competitor's organic footprint and content |
| `content-gap-mapping` | Gaps, parity and advantages against competitors per cluster |
| `content-research-orchestrator` | Gated pipeline: keywords, clustering, landscape, competitor, gaps |
| `european-market-intelligence` | Market sizing, competitor dossiers and entry feasibility for European markets |
| `free-tool-strategy` | Plans a free tool for leads, links or awareness |
| `keyword-clustering` | Clusters keywords by intent and SERP overlap and maps them to pages |
| `media-mapping` | Media outlets, trade press and newsletters for PR |
| `seo-audit` | Technical and on-page SEO audit |
| `seo-keyword-research` | Prioritised organic keyword opportunities |

### Strategy and planning

| Skill | What it does |
|---|---|
| `campaign-plan` | Full campaign brief from a goal and a timeline |
| `lead-magnets` | Plans a lead magnet: format, gating, landing page, delivery, measurement |

### Sales enablement and outreach

| Skill | What it does |
|---|---|
| `battlecard` | One-page sales card on one competitor: where we win and lose, landmines, objection responses, source-tagged |
| `cold-email-sequence` | Cold B2B email sequence drafted for a person to send, with a compliance gate, personalisation fields and a reply guide |
| `linkedin-outreach` | LinkedIn connection notes, messages and follow-ups drafted for manual sending |

### Content writing and editing

| Skill | What it does |
|---|---|
| `ai-content-cleaner` | Final cleaning pass: AI-pattern removal in five languages (Belgian Dutch included), protected spans, invisible-Unicode script. Absorbs `clean-user-facing-text` |
| `brand-review` | Brand voice and compliance check before anything ships |
| `content-creation` | Router for content requests that span formats |
| `content-translate` | Translation and localisation with locked brand terminology |
| `copy-editing` | Seven Sweeps edit of existing copy, honouring a brand's Voice Lock |
| `customer-story-writer` | B2B customer stories and case studies |
| `email-sequence-hubspot-brevo` | Multi-email sequences for HubSpot Workflows or Brevo Automation |
| `newsletter-writer` | One-off marketing emails and newsletters |
| `press-release-writer` | Press releases in standard PR format |
| `social-content-writer` | Platform-specific posts for LinkedIn, Instagram, X and Reddit |
| `web-content-pipeline` | Any web page, from brief to humanised draft |

### Creative and design

| Skill | What it does |
|---|---|
| `creative-brief` | Art direction and an asset table with real formats and dimensions |
| `canva-workflow` | Builds assets in Canva, or a manual checklist when Canva isn't connected |
| `figma-weavy-workflow` | Figma Weave graphs for generated or composited imagery and video |
| `launch-video` | Short product teaser, continuous-take demo or logo sting: storyboard, Hyperframes build, poster frame, caption |
| `logo-design` | Logos, wordmarks, app icons and favicons as clean SVG: brief, concepts, tests, checkpoint, then the full kit |
| `frontend-design` | Builds, redesigns or reviews front-end UI in a brand's visual identity: design read and settings, anti-generic rules, redesign protocol, interface checklist |

### Shared infrastructure

| Skill | What it does |
|---|---|
| `content-references` | Shared frameworks and SEO/AEO rules for the content skills |
| `mcp-efficiency` | How to call any connector without flooding the context |
| `security-policy` | Untrusted content and write-capable connectors: what needs approval |

## Attribution

`brand-review`, `content-creation`, `newsletter-writer`, `press-release-writer` and `social-content-writer` started from Anthropic's marketing plugin and were substantially reworked. `lead-magnets` is adapted from a generic lead-magnet skill (see its `metadata.history`). `european-market-intelligence` is a Europeanised merge of two ID8Labs skills. `content-translate` is adapted from a third-party translate module. `logo-design` is adapted from kaankiziltug's `logo-design-skill` (MIT; its trademarked reference logo library is not included). `launch-video` adapts parts of latent-spaces' `brag` (MIT) and is inspired by feitangyuan's `onetake`, which is not bundled because it is licensed PolyForm Noncommercial. `ad-creative-matrix` writes up the 50-5-3 ad method in its own words. `frontend-design` synthesises Anthropic's `frontend-design`, vercel-labs' `web-interface-guidelines` (MIT) and Leonxlnx's `taste-skill` and `redesign-skill` (MIT). See each skill's `metadata.history` where present.

## Licence

MIT, see [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). A GitHub Action lints every skill's frontmatter on push; run it locally first with `python scripts/lint_skills.py`.

---

Built by [Jordi Driesen](https://jordidriesen.be), fractional marketer and digital strategist.
