# Changelog

All notable changes to this skill library are documented here. Individual skills may also carry their own `metadata.version` in their `SKILL.md` frontmatter for finer-grained history.

## [Unreleased]

## [2.6.0]

Phase 2 of the web content library clean-up: restructure for load efficiency. Measured before and after with the new `evals/tools/loadreport.py`; no new capability.

- **`web-content-pipeline` 1.6.0 is orchestration only** (31.9 kB to 16.2 kB). Steps 0 to 2 are one router table (page type, intent, default framework, core sections, proof, FAQ count, template). The page templates moved out, and Step 4 now requires reading exactly one template file.
- **Page templates** live in `content-references/references/`: `page-templates-article.md` (blog, pillar or hub, comparison, glossary) and `page-templates-conversion.md` (landing, product, solution, feature, homepage, pricing, about). Two files, not one per brief: a file read loads the whole file, so one file with a section per page type would load every template.
- **`content-briefing.md`** merges the intent and framework references into one decision path (12.9 kB to 6.3 kB). **`seo-aeo-core.md`** and **`seo-aeo-scorecard.md`** split the SEO/AEO reference (the 100-point scorecard is on demand). **`internal-linking-drafting.md`** and **`internal-linking-audit.md`** split the linking reference (the audit is on demand). The four old files are deleted and every inbound reference updated.
- **One rule each** for sourcing (at least one sourced statistic per 500 words, minimum four, every material claim mapped to a source), chunk size and CTA strength, replacing three conflicting statistic thresholds and the "apply whichever is stricter" instruction. The E-E-A-T gate now has six additive checks.
- **`content-references` index** gets a dependency map (who loads which file and when) and a one-line provenance note; the pique-effect clause is removed from `behavioral-psychology.md`.
- Skills that cited the renamed files carry a minor version bump and a history line.

## [2.5.3]

Phase 1 of the web content library clean-up: corrections only, no new capability.

- **`content-references` index is truthful.** It counts its modules correctly (five) and describes `seo-aeo-optimization.md` only by what the file contains. It no longer promises off-page signals or a Who/How/Why pre-gate, which the file never had.
- **Canonical honesty rule** now lives once, in the `content-references` index. The reference files point at it and never into a generation skill; the `web-content-pipeline` claim test is its operational form. Hard-coded module counts ("the other four modules") removed.
- **Personal content removed from the shared library** (`behavioral-psychology.md`, `communication-frameworks.md`); the mappings are kept as a pattern in `templates/personal-context.md` (not installed).
- **Pointer file `ai-content-humanizing.md` deleted**, and the stale mentions in the history notes of `copy-editing`, `customer-story-writer`, `email-sequence-hubspot-brevo`, `press-release-writer` and `ai-content-cleaner` now name `ai-content-cleaner`.
- **`copy-editing` 1.2.1:** removed the reference to the missing Plain English Alternatives file.
- **`web-content-pipeline` 1.5.2:** the empty Step 3 input cells now cross-reference Steps 0, 1 and 2.
- **`security-policy`:** the scope list in `SECURITY.md` names `seo-keyword-research` and `sea-keyword-research` (it named two skills that do not exist); last-reviewed date updated.
- **`scripts/lint_skills.py`** now also fails on a description longer than 500 characters or a malformed `metadata.version`, and warns (without failing) about skills with no version, since Claude Code ignores it at runtime. Correction to the 2.5.2 notes: the lint does check `plugin/skills/`.
- Touched skills carry a bumped `metadata.version` and a one-line history entry.

Noticed, not fixed here: `security-policy/SKILL.md` and `SECURITY.md` still name the owner personally.

## [2.5.2]

Fixes why the content skills stopped running, and tightens how the agents follow them. Found by comparing 2.4.0 and 2.5.1 in evals: landing page copy and LinkedIn outreach scored lower, and `web-content-pipeline` did not run at all in the landing page runs.

- **Skill descriptions rewritten (all 58 skills).** Claude Code caps the skill listing at about 1% of the context window. From 2.2.0 to 2.4.0 the library grew from 52 to 69 skills and the descriptions from about 24,000 to about 33,000 characters, so every skill after `european-market-intelligence` was listed by name only and never triggered. Descriptions are now front-loaded and total about 14,700 characters. The core writers (`web-content-pipeline`, `customer-story-writer`, `social-content-writer`) start with "Always use for ...". Frontmatter descriptions only; skill bodies are unchanged except where listed below. Across all installed plugins the listing can still exceed the budget; `skillListingBudgetFraction: 0.02` in Claude Code settings is one option.
- **`web-content-pipeline` 1.5.1.** The body is the 1.1.0 text plus:
  - A **claim test**: write what is at least about 90% likely to be true from the brief, brand kit or product file; unconfirmed but plausible claims carry a hidden `confirm` note; numbers, customers, logos, quotes, awards, certifications and prices always need a source. A call to action may promise what the offering is meant to fix.
  - **Required skill calls**: `copy-editing` and `ai-content-cleaner` are invoked through the Skill tool, with no inline substitute. Before this, the agent made one skill call and wrote the page directly.
  - **Editor notes are hidden HTML comments**, never visible copy: implementation brief, a component tag above each section, `QUESTION` and `UNSURE` notes (the latter "needs judging by the person operating the chat"), collected in one `OPEN ITEMS` block. Missing proof becomes Lorem Ipsum in the form the proof will take, with a hidden `PROOF NEEDED` note; headings stay neutral until proof exists.
  - The skill chooses the framework (StoryBrand is a common default, not a requirement), plus a **page-type guide** (landing, product, solution, feature, homepage, pricing, about, blog, pillar or hub, comparison, glossary) with core sections, proof placement and FAQ counts, and an ask-first gate when the brand, action, audience or product facts are missing.
- **`customer-story-writer` 1.2.0.** Strict no-fabrication kept, with inferred context and consequences now covered explicitly. Source fidelity overrides the 12-section structure and any length target, the clean pass is invoked through the Skill tool, a sentence-by-sentence source check runs first, and editor notes move into a hidden `OPEN ITEMS` comment.
- **`cold-email-sequence`:** ask-first gate. If the segment, offer or sender is missing it replies with 2 to 4 questions and drafts nothing. It now belongs to `sdr-specialist`.
- **Agents.** All twelve specialists return a **Needs input** block instead of guessing when information is missing (checked before any skill runs) and end with a **Skills run** line. `marketing-director` stops the chain on those questions, asks the user once, passes deliverables through unchanged, and before anything is published lists the open items and asks "Can we publish this as is, or should anything change?".
- **`sdr-specialist` refocused** on research and audience building (target lists, `account-brief`, `abm-plan`) and, on request, cold email sequences. LinkedIn outreach and reply handling are parked.
- **Removed `linkedin-outreach`** and moved **`reply-triage`** to `archive/`, with references updated. Outreach returns as its own project. The plugin now has 58 skills (plus 13 shortcuts).
- **Evals (`plugin/evals/`).** Cases for the landing page (written from an implementation brief), customer story, solution page trigger, and the SDR agent (asks when information is missing; cold email). `evals/README.md` explains each case in plain language and `evals/tools/judge3.py` re-judges subjective checks as PASS, FAIL or UNSURE. Real client briefs are never stored in the repo.
- **Eval results, 3 runs each, on the branch against 2.5.1 (before the last wording changes):** the pipeline fired in 3/3 landing page runs against 0/3 on both 2.4.0 and 2.5.1; `copy-editing` and `ai-content-cleaner` ran 3/3 in one round against 0/3 on 2.5.1, then only 1/3 and 2/3 in the next round, before the required-call wording was added (single runs on the final wording ran both); the SDR agent asked first when information was missing 3/3 against 0/3 and ended with its `Skills run` line 3/3 against 0/3; the customer story skill fired 3/3 against 0/3 on 2.5.1. Quality scores on claims and page structure stayed low (0/3) under an LLM judge that is too literal on judgement calls. They are not a pass. The final wording (1.5.1) was sampled in single runs, which showed one remaining visible editor line in a navigation row. The marketing director cannot delegate when called as a subagent, so its ask-before-publishing step has not been tested.
- **Manifest:** `marketplace.json` now lists 2.5.2 and the twelve-specialist description (it still said 2.4.0 and eleven).

Known issues, not addressed here: `scripts/lint_skills.py` skips `plugin/`; `free-tool-strategy/references/tool-types.md` and `copy-editing/references/plain-english-alternatives.md` are referenced but missing; `content-references` still names the retired `blog-content-pipeline` and `seo-content-writer`; the `scraper-*` suite that `sdr-specialist` routes to when installed is not in this repository.

## [2.5.1]

- **No em dashes anywhere in the repo.** All 1,133 em dashes across 91 files (skills, references, agents, scripts, READMEs, changelog and archive) replaced with a colon, comma or semicolon depending on context: colons for labels, headings and explanations, commas for parenthetical pairs and before linking words. No skill logic changed. Frontmatter still parses and the Python scripts still compile.

## [2.5.0]

- **`sdr-specialist` (new agent) and the `0-sdr` shortcut.** Outbound pipeline in one place: target account lists, account briefs, cold email and LinkedIn outreach drafts for a person to send, reply triage and ABM plans. Drafts and prepares only: it never sends, schedules, imports contacts or scrapes LinkedIn. It routes to the `scraper-*` suite for account lists when that suite is installed; the suite is not in this repo yet, so until it is, the agent works from a supplied list or asks for one.
- **`account-brief`, `reply-triage` and `abm-plan` 1.0.0 (new).** `account-brief`: one page per target account with sourced, dated trigger events, the buying committee by role, ICP fit, the angle and the first touch. `reply-triage`: classifies real replies (adds data-rights requests, bounces, hostile and unclear to the cold email reply guide), drafts answers, lists stops, suppressions and resume dates, and writes handover notes for warm leads. `abm-plan`: tiers (one-to-one, one-to-few, one-to-many), buying committee, plays per tier across outreach, paid audiences, content and events, sales handover and account-level measurement.
- **`sales-enablement-specialist` narrowed** to battlecards and material that equips the sales team. `cold-email-sequence` and `linkedin-outreach` move to `sdr-specialist`; the skills themselves are unchanged apart from two Related Skills lines each. `0-sales` description updated.
- **`marketing-director`** routes outbound to `sdr-specialist`, runs `competitive-intel-analyst` first when accounts still need sourcing, and passes the account list to paid social. `content-creation` routing table split into outbound and battlecard rows.
- Skill count is now 60 (plus 13 shortcuts) and the agent count twelve specialists plus the director.

## [2.4.0]

- **Agent shortcuts in the plugin menu (12 new `0-` entries).** The Claude Desktop `/` menu lists a plugin's skills alphabetically and does not list its agents, so each agent now has a manual shortcut skill that sorts above the rest: `0-marketing` (director), `0-paid-ads`, `0-seo`, `0-content`, `0-social`, `0-email`, `0-creative`, `0-sales`, `0-intel`, `0-campaign`, `0-localise` and `0-report`. Each takes your request as its argument and runs it through the matching agent (`context: fork` with `agent:`). They are `disable-model-invocation: true`, so they never trigger on their own, and the 57 skills stay visible and auto-loadable. `0-marketing` does not fork: it tells the main thread to hand the request to the director. **Unverified:** menu sort order, digit-leading skill names, forking onto a plugin-scoped agent name, and a forked director dispatching specialists. Test after updating and report back.

## [2.3.0]

- **`frontend-design` 2.1.0:** three new references. `type-and-colour.md` (type scale, line-height, measure, wrapping, punctuation, colour ramps, semantic tokens, measured contrast), `motion.md` (frequency table, easing, durations, entrances and exits, reduced motion, hover on touch) and `layout-and-accessibility.md` (grouping, responsive structure, translation growth, surfaces and icons, WCAG 2.2 criteria and ARIA additions). `taste.md` gains asset dependence and brand fidelity reads, a brand-assets-first rule and critique dimensions. Adapted from jakubkrehel/skills, emilkowalski/skills and ConardLi/garden-skills (all MIT). The em dash punctuation advice in better-typography was deliberately dropped. `interface-checklist.md` stays an unmodified pinned copy. Stress testing (break-ui) was not added.

- **Brand-kit template: optional product files.** `references/products.md` (index) and `references/products/_product-template.md` (one file per product: what it is, who it is for, features, limitations, integrations, pricing model, proof with permission, competitors, open questions). Terminology stays at brand level in `voice.md`; product files never carry their own. Router table and `context.md` updated.

## [2.2.0]

- **`battlecard`, `cold-email-sequence` and `linkedin-outreach` 1.0.0 (new)** and the **`sales-enablement-specialist`** agent. Drafts only: nothing sends, schedules or scrapes. `cold-email-sequence` opens with a compliance gate and states that the legal position is unverified; `linkedin-outreach` assumes manual sending and flags LinkedIn's rules and character limits as unverified. `battlecard` source-tags every claim and compiles verified inputs without doing the competitor research. `marketing-director` routes to the new agent. Agent count is now eleven and the skill count 57.
- **`negative-keywords` merged into `search-term-auditor` 2.0.0.** The two skills ended in the same paste-ready negative list. The auditor now also classifies terms as keep, block or review, sets match types and placement, supports a pre-launch exclusion mode and reads the account's existing negatives. `negative-keywords` moved to `archive/`; `performance-marketer` routing, README and CONTRIBUTING updated.
- **`ad-creative-matrix` 1.0.0 (new):** the 50-5-3 method (50 hooks, 5 bodies, 3 CTAs) for paid social and video ads, with a hook screening rubric, a compatibility check, tagged assembly and a test plan sized to budget. References: `angle-library.md`, `platform-limits.md`.
- **Back pointers to `ad-creative-matrix`:** added to `rsa-writer`, `ad-copy-tester`, `competitor-teardown`, `social-content-writer`, `creative-brief`, `content-creation` (new routing rows for paid social and RSA), the `social-media-specialist` agent and `european-market-intelligence` (replaced a stale "no LinkedIn ad skill" line). `rsa-writer`, `ad-copy-tester` and `competitor-teardown` gained a Related Skills section.
- **`logo-design` 1.0.0 (new):** logo and brand-mark design from discovery brief to production SVG files, with a concept checkpoint, critique, redesign and asset modes. Adapted from `logo-design-skill` by kaankiziltug (MIT, licence notice in the skill folder). The 1,400-logo reference library and the scripts that depended on it were removed because those logos are third-party trademarks. `svg_audit.py` and `preview_sheet.py` were patched to run without it.
- **`launch-video` 1.0.0 (new):** short product and brand videos in three types (launch teaser, continuous-take demo, logo sting), planned from the product's source and the brand kit, built with Hyperframes, with reading-time floors, a poster frame baked in as frame 0 and a share caption. Adapted in part from `brag` by latent-spaces (MIT, licence notice in the skill folder). Inspired by `onetake`, which is PolyForm Noncommercial and is not bundled or copied. No audio is bundled. Rendering was not tested in the build environment (Chrome for Hyperframes could not be installed there).
- **`creative-specialist`** now routes to `logo-design` and `launch-video`; `figma-weavy-workflow` points video-teaser requests to `launch-video`.

## [2.1.0]

New connectors wired in: WP Umbrella, Adobe for creativity, G2, Tally.so, vidIQ, Google Drive, Make and Zapier, plus OpenSEO's newer tools (local, rank tracking, near-miss pages, index status, saved keywords, reports).

- **`mcp-efficiency`:** description lists the whole stack. New rule 9 (the identity call per connector, checked against the live tools) and rule 10 (OpenSEO credits, WP Umbrella billing and irreversible actions, Adobe routing, draft-only connectors). Rule 2 now covers loading deferred tools in one search.
- **`CONNECTORS.md`:** rows for local search, G2, Adobe, vidIQ, Tally.so, WP Umbrella, Make and Zapier, Google Drive; a connection-status note (HubSpot's connection is unfinished).
- **`security-policy`:** scope and the confirmation list cover the new write-capable connectors (WP Umbrella actions, Tally forms, Make and Zapier, Adobe sharing and Stock, OpenSEO scheduled trackers, Brevo and Typefully sending).
- **`seo-audit` 1.3.0:** a live-data table (OpenSEO audit, `inspect_urls`, `get_search_opportunities`, rank tracker, local tools; WP Umbrella read-only health). Removed the paid-tool line for Ahrefs and Semrush.
- **`seo-keyword-research`:** uses `get_search_opportunities` for existing sites and offers `save_keywords`; the stale "no Search Console, backlinks or local data" gap note is corrected.
- **`content-gap-mapping`:** OpenSEO's own Search Console route, `get_search_opportunities` for Parity clusters, and `inspect_urls` so an unindexed page isn't called a content gap.
- **`competitor-analysis`, `competitive-landscape`:** local competitors via Google Business Profile, reviews and the Maps rank grid, with cost guidance; G2 for B2B software.
- **`performance-reporter`:** rank tracker, near-miss pages, Brevo or HubSpot results, WP Umbrella uptime and performance as context, optional `save_report`.
- **Creative:** `creative-specialist`, `creative-brief` 1.2.0 and `canva-workflow` route image edits, PDF work and font sourcing to Adobe for creativity. Canva stays the default, Express only when asked, and no generative fill on real photos.
- **`frontend-design`:** WP Umbrella baseline before a redesign and a post-launch check; Adobe font tools when the brand leaves type open.
- **`lead-magnets`, `free-tool-strategy`:** Tally.so for forms; Make or Zapier as the fallback to Brevo or HubSpot; all approval-gated.
- **`creative-specialist`:** the `tools` allowlist is removed so the agent inherits MCP tools; with it, Canva, Figma and Adobe calls were blocked inside the agent.
- **`openseo-tool-map`:** a reference table of the OpenSEO tools used outside the research pipeline, with credit notes.

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
- **`frontend-design` 2.0.0:** folded in Leonxlnx's `taste-skill` and `redesign-skill` (MIT) as `references/taste.md` (design read, variance/motion/density settings, locks, AI tells, pre-flight check) and `references/redesign-protocol.md` (mode detection, audit, never-change-silently list, fix order), both rewired so the brand kit outranks their defaults, the site's existing stack is kept, dark mode follows the brand, and nothing invented (figures, quotes, generated images passing as real work) reaches a live page. New redesign mode. `references/interface-checklist.md` refreshed against the current upstream web interface guidelines as a pinned copy; vercel-labs' `web-design-guidelines` skill not added, because it fetches and follows remote rules at review time.
- `competitive-brief` and `performance-report` moved to `archive/`: no agent calls them since 1.7.0. Root and plugin READMEs rewritten.

**Migration.** After installing 2.0.0, remove the standalone account copies of every skill that now ships in the plugin, plus `report-writer`, `clean-user-facing-text` and (once the modular personal kit is uploaded) `personal-brand-tone-of-voice`, so no skill name exists twice.

## [1.7.0]

- Fixed `seo-audit`: its References and Related Skills sections pointed at six skills that don't exist in this library (`ai-seo`, `programmatic-seo`, `site-architecture`, `schema-markup`, `page-cro`, `analytics-tracking`) and one dead file link. Now points at what actually exists (`content-references`'s `seo-aeo-optimization.md`, `ai-content-cleaner`, `seo-keyword-research`/`keyword-clustering`); description updated to match and bumped to 1.2.0.
- Fixed `plugin/agents/performance-reporter.md` and `plugin/agents/competitive-intel-analyst.md`: both called skills (`performance-report`, `competitive-brief`) that belong to a different, unpublished plugin and don't exist standalone here. `performance-reporter` now builds its own report structure from `report-writer` + `metric-detective`; `competitive-intel-analyst`'s battlecard/positioning case folds into `competitor-analysis` instead of calling a skill that isn't there.
- Shortened `plugin/.claude-plugin/plugin.json`'s `description` from 535 to 457 characters: over Cowork's 500-character plugin-install validation limit, which broke installs from this repo.
- Removed `keyword-research` (the DataForSEO-backed version): dead weight superseded by `seo-keyword-research` (OpenSEO-backed); the two had near-duplicate trigger descriptions.
- Added `brand-kit-template/SKILL.md`: a generic, placeholder-only starting point for a new `[brand]-brand-kit` skill, mirroring the structure real brand kits use (identity, language standards, voice pillars, customer-hero framework, audience/channel calibration, banned language, quality checklist, visual identity) without any real brand's content.

## [1.6.0]

- **Plugin restructured into a full agent team.** `plugin/agents/` now holds `marketing-director` plus ten specialists (competitive-intel-analyst, seo-geo-specialist, campaign-strategist, content-writer, social-media-specialist, email-marketer, creative-specialist, performance-marketer, localization-specialist, performance-reporter). The director dispatches by discipline and sequences a full campaign in dependency order instead of running everything at once.
- Added `localization-specialist`: target-language versions (NL/FR/DE/ES) of signed-off source content via `content-translate`, run after execution and before reporting. `content-writer` no longer calls `content-translate` directly.
- Added `creative-specialist` and the new `frontend-design` skill (design/review front-end UI in a brand's visual identity, plan/critique method from Anthropic's `frontend-design`, interface rule set adapted from vercel-labs' `web-interface-guidelines`, MIT). `chape-braspenning-brand-kit` referenced a `frontend-design` skill before one existed; it does now.
- `campaign-plan`, `competitive-brief`, and `performance-report` moved back out of `/plugin` to the repo root: they're account skills like any other and nothing about them was plugin-specific. The plugin's agents call them by bare name, unaffected.
- Wired five content skills into `content-references` instead of re-implementing its rules: `copy-editing` (dropped duplicated persuasion/lexical tables and four dead skill links, kept the Seven Sweeps process), `customer-story-writer` (framework definitions now cite the hub, kept its fixed structure and framework-to-section mapping), `press-release-writer` (added a humanizing pass it was missing), `newsletter-writer` (added a structural-framework step), `email-sequence-hubspot-brevo` (per-email copy now cites the hub).
- Added `.claude-plugin/marketplace.json` at the repo root so the plugin installs via `claude plugin marketplace add Jordidriesen/marketing-agent` + `/plugin install marketing-agent@marketing-agent`, with `claude plugin marketplace update` for syncing later.

## [1.3.0]

- Moved `campaign-plan`, `competitive-brief`, and `performance-report` out of the flat skill list into [`/plugin`](plugin), packaged as a proper installable Claude Code / Cowork plugin (`.claude-plugin/plugin.json`, `.mcp.json`, its own README/LICENSE/CONNECTORS.md). Content unchanged from the 1.2.0 versions, only the packaging moved.
- Checked `.mcp.json` specifically for credentials before publishing: contains only public, standard MCP endpoint URLs and one non-secret OAuth client ID (Slack), clean.
- Resolved: `european-market-intelligence` and `content-translate` keep their existing third-party attribution (ID8Labs skill merge, and an unnamed third-party translate module respectively) rather than being reattributed solely to Jordi, content in both is independently written beyond shared use of standard frameworks, but the attribution stays as documentation of that transformation. See the Attribution note above the skill tables.

## [1.2.0]

- Adopted cleaner, fully-generic anonymization and a frontmatter bug fix from a newer export across 8 skills (`competitive-landscape`, `competitor-analysis`, `content-references`, `content-research-orchestrator`, `content-translate`, `european-market-intelligence`, `seo-audit`, `web-content-pipeline`).
- Added 8 new skills: `campaign-plan`, `competitive-brief`, `performance-report` (built specifically for the marketing plugin; brand-kit check added, reference tables split out, house style applied) and `brand-review`, `content-creation`, `newsletter-writer`, `press-release-writer`, `social-content-writer` (started from Anthropic's marketing plugin, substantially reworked, added as-is). See the Attribution note above the skill tables. 49 skills total.

## [1.1.0]

- Removed the four personal/lifestyle skills (`middle-eastern-fragrance-explorer`, `personal-brand-reviews`, `supermarkt-prijsanalyse`, `weekmenu-planner`): out of scope for this repo's marketing/SEO/PPC focus. 41 skills remain.

## [1.0.0]: Initial public release

- 45 skills published across Google Ads/PPC, SEO & content research, content writing/editing, shared infrastructure, and personal-use categories.
- Client-specific brand kits (`primion-brand-kit`, `personal-brand-kit`) kept private; a small number of skills reference a generic `acme-brand-kit` placeholder as a stand-in for the `[brand]-brand-kit` pattern.
- Client name mentions anonymised throughout (`Client A`, `Client B`).
- `personal-brand-reviews` retained as the current name; the superseded `jordi-blog-reviews` (identical, pre-rename) was not carried over.
