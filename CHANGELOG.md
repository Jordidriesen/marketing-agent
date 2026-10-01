# Changelog

All notable changes to this skill library are documented here. Individual skills may also carry their own `metadata.version` in their `SKILL.md` frontmatter for finer-grained history.

## [2.0.0]

Breaking: skills moved and two were renamed or merged. Reinstall the plugin and remove the old standalone copies from your account (see the migration note at the end).

- **One install.** All 52 public skills moved from the repo root into `plugin/skills/`, so the plugin now ships agents and skills together and they can no longer drift apart. `plugin.json` and `marketplace.json` share one description, version 2.0.0.
- **Reconciled the account and repo versions.** Took the newer account versions of `ai-content-cleaner`, `conversion-tracking-auditor`, `quality-score-doctor`, `search-term-auditor`, `full-account-audit` (live Google Ads connector wiring) and `keyword-clustering` (SERP page-type consensus). Kept the repo versions of the content skills (anonymised, wired into `content-references`) and ported the account's Voice Lock precedence into `copy-editing`. Added six skills that existed only in the account: `canva-workflow`, `creative-brief`, `figma-weavy-workflow`, `google-ads-tool-map`, `lead-magnets`, `mcp-efficiency`. Replaced a leftover customer name in `customer-story-writer` with a placeholder.
- **`report-writer` is now `paid-ads-report-writer`** (v2.0.0): covers every paid platform, search and social (Google Ads, Microsoft Ads, LinkedIn Ads, Meta, others via export), with live pulls where connected, a cross-platform normalisation step and a new `references/platform-metrics.md`. Ad group names always shown next to keywords and search terms.
- **`clean-user-facing-text` merged into `ai-content-cleaner`** (v2.0.0): protected spans, the honesty rule, and a working invisible-Unicode pass via the new `scripts/unicode_audit.py` (the old skill referenced scripts that never existed). `ai-content-cleaner` is now the single owner of the humanising rules and language pattern files; the duplicate pattern files in `content-references` are gone and `ai-content-humanizing.md` is a pointer. Every skill that called the humanising pass now names `ai-content-cleaner` directly. Added a Belgian Dutch section to the NL patterns.
- **Brand kits are modular.** `brand-review`, `copy-editing` and `ai-content-cleaner` load a kit's voice module (`references/voice.md`) and still support older kits with a separate tone-of-voice skill. `brand-kit-template` moved to `templates/brand-kit/` and is now a router plus `context.md`, `voice.md` and `design.md`.
- **Connectors.** `.mcp.json` keeps only Canva, Figma, HubSpot and Notion; Slack, Amplitude, Ahrefs, Similarweb, Klaviyo and Supermetrics removed. `CONNECTORS.md` rewritten around the real stack, with a data-source rule for brands with and without an OpenSEO project. `email-marketer` uses Brevo instead of Klaviyo.
- **Stale references fixed.** Removed the `dataforseo:` fallbacks (that connector is gone; `OpenSEO:search_serp_locations` replaces the location lookup). `content-gap-mapping`, `competitor-analysis` and `competitive-landscape` now use OpenSEO's backlink and local SERP tools instead of saying the data isn't available. `european-market-intelligence` uses OpenSEO backlinks instead of Ahrefs. OpenSEO project resolution now checks the brand kit first and asks before creating a client project.
- **Agents.** `performance-reporter` and `performance-marketer` use `paid-ads-report-writer`; `seo-geo-specialist` follows the data-source rule; `creative-specialist` names this plugin's `frontend-design`.
- `competitive-brief` and `performance-report` moved to `archive/`: no agent calls them since 1.7.0. Root and plugin READMEs rewritten.

**Migration.** After installing 2.0.0, remove the standalone account copies of every skill that now ships in the plugin, plus `report-writer`, `clean-user-facing-text` and (once the modular personal kit is uploaded) `personal-brand-tone-of-voice`, so no skill name exists twice.

## [1.7.0]

- Fixed `seo-audit`: its References and Related Skills sections pointed at six skills that don't exist in this library (`ai-seo`, `programmatic-seo`, `site-architecture`, `schema-markup`, `page-cro`, `analytics-tracking`) and one dead file link. Now points at what actually exists (`content-references`'s `seo-aeo-optimization.md`, `ai-content-cleaner`, `seo-keyword-research`/`keyword-clustering`); description updated to match and bumped to 1.2.0.
- Fixed `plugin/agents/performance-reporter.md` and `plugin/agents/competitive-intel-analyst.md`: both called skills (`performance-report`, `competitive-brief`) that belong to a different, unpublished plugin and don't exist standalone here. `performance-reporter` now builds its own report structure from `report-writer` + `metric-detective`; `competitive-intel-analyst`'s battlecard/positioning case folds into `competitor-analysis` instead of calling a skill that isn't there.
- Shortened `plugin/.claude-plugin/plugin.json`'s `description` from 535 to 457 characters — over Cowork's 500-character plugin-install validation limit, which broke installs from this repo.
- Removed `keyword-research` (the DataForSEO-backed version) — dead weight superseded by `seo-keyword-research` (OpenSEO-backed); the two had near-duplicate trigger descriptions.
- Added `brand-kit-template/SKILL.md` — a generic, placeholder-only starting point for a new `[brand]-brand-kit` skill, mirroring the structure real brand kits use (identity, language standards, voice pillars, customer-hero framework, audience/channel calibration, banned language, quality checklist, visual identity) without any real brand's content.

## [1.6.0]

- **Plugin restructured into a full agent team.** `plugin/agents/` now holds `marketing-director` plus ten specialists (competitive-intel-analyst, seo-geo-specialist, campaign-strategist, content-writer, social-media-specialist, email-marketer, creative-specialist, performance-marketer, localization-specialist, performance-reporter). The director dispatches by discipline and sequences a full campaign in dependency order instead of running everything at once.
- Added `localization-specialist` — target-language versions (NL/FR/DE/ES) of signed-off source content via `content-translate`, run after execution and before reporting. `content-writer` no longer calls `content-translate` directly.
- Added `creative-specialist` and the new `frontend-design` skill (design/review front-end UI in a brand's visual identity — plan/critique method from Anthropic's `frontend-design`, interface rule set adapted from vercel-labs' `web-interface-guidelines`, MIT). `chape-braspenning-brand-kit` referenced a `frontend-design` skill before one existed; it does now.
- `campaign-plan`, `competitive-brief`, and `performance-report` moved back out of `/plugin` to the repo root — they're account skills like any other and nothing about them was plugin-specific. The plugin's agents call them by bare name, unaffected.
- Wired five content skills into `content-references` instead of re-implementing its rules: `copy-editing` (dropped duplicated persuasion/lexical tables and four dead skill links, kept the Seven Sweeps process), `customer-story-writer` (framework definitions now cite the hub, kept its fixed structure and framework-to-section mapping), `press-release-writer` (added a humanizing pass it was missing), `newsletter-writer` (added a structural-framework step), `email-sequence-hubspot-brevo` (per-email copy now cites the hub).
- Added `.claude-plugin/marketplace.json` at the repo root so the plugin installs via `claude plugin marketplace add Jordidriesen/marketing-agent` + `/plugin install marketing-agent@marketing-agent`, with `claude plugin marketplace update` for syncing later.

## [1.3.0]

- Moved `campaign-plan`, `competitive-brief`, and `performance-report` out of the flat skill list into [`/plugin`](plugin), packaged as a proper installable Claude Code / Cowork plugin (`.claude-plugin/plugin.json`, `.mcp.json`, its own README/LICENSE/CONNECTORS.md). Content unchanged from the 1.2.0 versions — only the packaging moved.
- Checked `.mcp.json` specifically for credentials before publishing: contains only public, standard MCP endpoint URLs and one non-secret OAuth client ID (Slack) — clean.
- Resolved: `european-market-intelligence` and `content-translate` keep their existing third-party attribution (ID8Labs skill merge, and an unnamed third-party translate module respectively) rather than being reattributed solely to Jordi — content in both is independently written beyond shared use of standard frameworks, but the attribution stays as documentation of that transformation. See the Attribution note above the skill tables.

## [1.2.0]

- Adopted cleaner, fully-generic anonymization and a frontmatter bug fix from a newer export across 8 skills (`competitive-landscape`, `competitor-analysis`, `content-references`, `content-research-orchestrator`, `content-translate`, `european-market-intelligence`, `seo-audit`, `web-content-pipeline`).
- Added 8 new skills: `campaign-plan`, `competitive-brief`, `performance-report` (built specifically for the marketing plugin; brand-kit check added, reference tables split out, house style applied) and `brand-review`, `content-creation`, `newsletter-writer`, `press-release-writer`, `social-content-writer` (started from Anthropic's marketing plugin, substantially reworked, added as-is). See the Attribution note above the skill tables. 49 skills total.

## [1.1.0]

- Removed the four personal/lifestyle skills (`middle-eastern-fragrance-explorer`, `personal-brand-reviews`, `supermarkt-prijsanalyse`, `weekmenu-planner`) — out of scope for this repo's marketing/SEO/PPC focus. 41 skills remain.

## [1.0.0] — Initial public release

- 45 skills published across Google Ads/PPC, SEO & content research, content writing/editing, shared infrastructure, and personal-use categories.
- Client-specific brand kits (`primion-brand-kit`, `personal-brand-kit`) kept private; a small number of skills reference a generic `acme-brand-kit` placeholder as a stand-in for the `[brand]-brand-kit` pattern.
- Client name mentions anonymised throughout (`Client A`, `Client B`).
- `personal-brand-reviews` retained as the current name; the superseded `jordi-blog-reviews` (identical, pre-rename) was not carried over.
