# Marketing Agent: a Claude marketing team

A marketing team for Claude in one install: the `team` command, which turns the main thread into a director, six thread profiles it can start, and the 50 skills they run on. Built for agency-style work across Google Ads, paid social, SEO and GEO research, content, email, outbound and sales, graphic design, web development and localisation, on a budget-conscious stack (OpenSEO instead of Ahrefs or Semrush, the ad platforms' own connectors instead of a paid data aggregator).

Run `/marketing-agent:team` for jobs with several steps or deliverables, anything going live or to a client, or heavy data work: the main thread becomes the director, does the work with the skills, starts threads only where they pay off, reviews and asks before publishing. For a single task, just ask: the right skill triggers on its own.

## Repository layout

```
plugin/                    the installable plugin
  .claude-plugin/          plugin manifest
  agents/                  six thread profiles: data-puller, researcher, drafter, graphic-designer, web-developer, cold-reviewer
  skills/                  the 50 skills, plus the `team` command
  CONNECTORS.md            which connector each discipline uses, and the data-source rule
templates/brand-kit/       blank modular brand kit: router + context, voice, design
archive/                   retired skills kept for reference, not installed
scripts/lint_skills.py     frontmatter lint, run in CI
scripts/sync_shared_refs.py  keeps shared reference copies in step with their source
```

**Brand kits are not in this repo.** Each client gets a private `[brand]-brand-kit` skill (identity, voice, design) installed separately in your Claude account. Every content, review and design skill looks for one by that naming pattern and loads it automatically. Start from [`templates/brand-kit`](templates/brand-kit).

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

This installs the profiles and all skills together, so they can't drift apart. Update later with `claude plugin marketplace update marketing-agent`.


To use a single skill without the plugin, copy its folder from `plugin/skills/` into `~/.claude/skills/` or upload it as a zip in Claude settings.

Connect the tools you use in Claude's connector settings; see [`plugin/CONNECTORS.md`](plugin/CONNECTORS.md). Skills say plainly when a connector they need isn't there rather than estimating data.

## Team and thread profiles

See [`plugin/README.md`](plugin/README.md) for when to use `/team`, the six thread profiles, and the order a full job runs in: intelligence and research, then strategy, then execution, then localisation, then reporting.

## Skills

### Paid search and Google Ads

Since 4.0.0, related Google Ads tasks live in three family skills. Each holds the former skills as references and still answers to their trigger phrases.

| Skill | What it does |
|---|---|
| `google-ads-build` | Planning and setup. References: `campaign-architect` (structure, budget splits, bidding, match types), `sea-keyword-research` (keywords by intent, sized to budget), `bid-strategy-advisor` (bid strategy for the conversion volume), `budget-optimizer` (budget shifts on real marginal performance) |
| `google-ads-analyse` | Diagnosis on live data. References: `full-account-audit`, `search-term-auditor` (wasted spend, paste-ready negatives with match types), `quality-score-doctor`, `pmax-decoder`, `geo-performance-analyzer`, `device-performance-analyzer`, `ad-schedule-analyzer`, `auction-insights-monitor`, `conversion-tracking-auditor`, `disapproval-diagnoser`, `landing-page-matcher` |
| `google-ads-ads` | Ad copy. References: `rsa-writer` (RSA headlines and descriptions within character limits), `ad-copy-tester` (keep, cut or replace assets from performance) |
| `ad-creative-matrix` | 50 hooks, 5 bodies and 3 CTAs for paid social and video ads, screened, tagged and test-planned |

The Google Ads connector reference (`google-ads-tool-map`) is a shared reference inside the three families.

### Paid social campaigns

| Skill | What it does |
|---|---|
| `meta-ads-manager` | Meta (Facebook and Instagram) campaign build plan: objective, Advantage+ or manual, audiences and exclusions, budget, tracking and consent checklist. Plan only until a Meta connector exists |
| `linkedin-ads-manager` | LinkedIn Ads build plan for B2B: targeting, matched audiences with an honest audience-size verdict, budget realities, lead gen form or landing page. Plan only until a LinkedIn connector exists |

### Conversion and testing

| Skill | What it does |
|---|---|
| `cro-auditor` | Heuristic conversion audit of one page: findings ranked by expected impact, with fixes and what to test first |
| `ab-test-planner` | A/B test design with a hypothesis, one variable, computed sample size and duration, stop rules and a do-not-run verdict |

### Measurement

| Skill | What it does |
|---|---|
| `measurement` | Family skill. References: `metric-detective` (why a metric moved, ranked causes and how to verify each), `ga4-audit` (GA4 setup from exports or a connector, ranked by decision impact), `attribution-readout` (why GA4 and platform numbers differ, and which test would settle it) |

### Paid media reporting

| Skill | What it does |
|---|---|
| `paid-ads-report-writer` | Client-ready reports for any paid platform, search and social: executive summary, per-platform sections, a normalised cross-platform view. Replaces `report-writer` |

### SEO, GEO and research

| Skill | What it does |
|---|---|
| `ai-visibility-tracker` | Repeatable protocol to track a brand's citations and mentions in AI answers: prompt set, citation log, round-over-round movement |
| `competitive-research` | Family skill. References: `competitor-analysis` (one competitor's organic footprint), `competitive-landscape` (SEO market leaders across competitors), `content-gap-mapping` (gaps, parity and advantages per cluster), `competitor-teardown` (angles competitors' ads claim and leave open) |
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

### Graphic design (graphic-designer)

| Skill | What it does |
|---|---|
| `creative-brief` | Art direction and an asset table with real formats and dimensions |
| `canva-workflow` | Builds assets in Canva, or a manual checklist when Canva isn't connected |
| `figma-weavy-workflow` | Figma Weave graphs for generated or composited imagery and video |
| `launch-video` | Short product teaser, continuous-take demo or logo sting: storyboard, Hyperframes build, poster frame, caption |
| `logo-design` | Logos, wordmarks, app icons and favicons as clean SVG: brief, concepts, tests, checkpoint, then the full kit |
| `affinity-workflow` | Scripted layout, vector, photo and batch work in Affinity by Canva through its local connector, verified with renders, or a manual checklist |
| `email-design` | Email templates and email visuals for Brevo, HubSpot or Canva: modular layout, bulletproof buttons, dark mode, Outlook-safe HTML |

### Web development (web-developer)

| Skill | What it does |
|---|---|
| `frontend-design` | Builds, redesigns or reviews front-end UI in a brand's visual identity: design read and settings, anti-generic rules, redesign protocol, interface checklist |
| `astro-site` | Astro sites: structure, content collections, islands, images, i18n, SEO and schema, build checks |

WordPress page building and plugin work come from the separate `wordpress-development` plugin (`wordpress-page-build`, `wordpress-plugin-development`), which the director and the `web-developer` profile call with the plugin prefix.

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
