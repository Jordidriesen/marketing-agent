# Changelog

All notable changes to this skill library are documented here. Individual skills may also carry their own `metadata.version` in their `SKILL.md` frontmatter for finer-grained history.

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
