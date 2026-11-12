# Connectors

This plugin is built around a budget-conscious stack: OpenSEO instead of Ahrefs or Semrush, the ad platforms' own connectors instead of a paid data aggregator, and free first-party data (Search Console, GA4, Bing Webmaster Tools) wherever it exists.

The plugin declares no MCP servers of its own (the old `.mcp.json` was removed in 3.0.0, because the same servers were already connected per account and ran twice). Everything below is connected per account in Claude's connector settings, or runs locally on the user's computer through the Claude desktop app; the skills look for a connector by name, load its tools and read the names before calling one, and say plainly when it isn't there, rather than guessing data.

## Which connector each discipline uses

| Discipline | Connector | Used by | If it isn't connected |
|---|---|---|---|
| Keyword, SERP, ranking and backlink data | OpenSEO | SEO research skills, `google-ads-build` (its `sea-keyword-research` reference), competitive intel | Say so; fall back to web research, never estimate figures |
| Site audits, rank tracking, GA4, near-miss pages (`get_search_opportunities`), index status (`inspect_urls`), saved keywords and reports | OpenSEO (needs an OpenSEO project for the domain) | `seo-audit`, `seo-keyword-research`, `competitive-research` (its `content-gap-mapping` reference), the reporting step | See "Data-source rule" below |
| Local search: Google Business Profile, reviews, Q&A, Maps rank grid | OpenSEO (any project; spends credits) | `competitive-research` (its `competitor-analysis` reference), `competitive-research` (its `competitive-landscape` reference), `seo-audit` | Say so; local claims stay organic-only |
| First-party search performance | Search Console, or OpenSEO's Search Console tools | `competitive-research` (its `content-gap-mapping` reference), `seo-keyword-research`, `seo-audit` | See "Data-source rule" below |
| Page content and crawling | Firecrawl | Research and content-gap skills | Use web fetch for single pages |
| Web and company research | Exa | `european-market-intelligence`, research skills | Use web search |
| Google Ads (read-only) | Google Ads | Google Ads skills, `paid-ads-report-writer` | Ask for exports |
| LinkedIn Ads | LinkedIn Ads | `paid-ads-report-writer` | Ask for Campaign Manager exports |
| Competitor B2B ads | LinkedIn Ad Library | `competitive-research` (its `competitor-teardown` reference), `european-market-intelligence` | Ask for screenshots or copy |
| B2B buyer reviews and category position | G2 | `competitive-research` (its `competitor-analysis` reference), `competitive-research` (its `competitive-landscape` reference) | Leave it out and say so |
| AI citations (Copilot) | Bing Webmaster Tools | SEO/GEO work | Ask for the AI Performance CSV export |
| Email | Brevo, HubSpot | `email-sequence-hubspot-brevo`, `newsletter-writer` | Produce copy and a build checklist without live data |
| Design (templates, bulk variants, email and social layouts) | Canva | `canva-workflow`, `email-design` | Hand back a manual build checklist |
| Precise vector, print and layout work, batch edits | Affinity by Canva (local: only while Affinity is open with its MCP server on and Claude runs in the desktop app on that computer) | `affinity-workflow` | Hand back a manual build checklist |
| Generated imagery and video | Figma (Weave tools) | `figma-weavy-workflow` | Hand back the graph spec |
| Design to code, code to design | Figma (Dev Mode and file tools, with the Figma plugin's skills) | `frontend-design`, `web-developer` | Read the frame from screenshots |
| Image edits, PDF work, fonts | Adobe for creativity (Express only when asked) | `graphic-designer`, `creative-brief`, `canva-workflow`, `frontend-design` | Hand back edit instructions |
| Short product and logo videos | HyperFrames by HeyGen, or the Hyperframes CLI | `launch-video` | Deliver the plan, storyboard and composition source |
| UI pattern research (optional) | Mobbin | `creative-brief`, `frontend-design` | Leave it out |
| Social scheduling | Typefully | `social-content-writer` | Hand back finished copy only |
| YouTube, Instagram and TikTok research | vidIQ | Personal channel work (personal-content plugin), `social-content-writer` | Use web research |
| Forms | Tally.so | `lead-magnets`, `free-tool-strategy` | Specify the form for manual build |
| WordPress pages, templates and site parts | The site's own MCP: the page builder's server (for example Elementor or Breakdance), NovaMira, or a managed host's; some run locally through the desktop app | `wordpress-development:wordpress-page-build`, `web-developer` | Hand back copy and markup for manual entry |
| WordPress SEO settings | The site's Rank Math MCP, where one is set up | `seo-audit`, `web-developer` | Ask for the settings or an export |
| Sitemaps and wireframes | Relume | `web-developer`, `frontend-design` | Plan the sitemap by hand |
| WordPress maintenance and health | WP Umbrella (sites in its fleet only) | `seo-audit`, `frontend-design` redesigns, `web-developer`, the reporting step | Ask for the site's plugin list and speed test |
| Automation between apps | Make, Zapier (only when asked) | `lead-magnets`, `free-tool-strategy` | Describe the automation for manual set-up |
| Knowledge base and source files | Notion, Google Drive | Briefs and reference material | Ask for the material |

## Data-source rule for search performance data

Not every brand has an OpenSEO project. Resolve the source once per task, in this order:

1. The brand kit's `references/context.md` lists the data sources for that brand. Use what it says.
2. If the brand has an OpenSEO project, use OpenSEO's Search Console and GA4 tools with that project ID.
3. Otherwise use the standalone Search Console connector for the verified property.
4. Otherwise ask. Never substitute estimated traffic for first-party data without saying so.

Every OpenSEO tool takes a `projectId`, but only the first-party tools (Search Console, GA4) and the site-level tools (site audit, rank tracking) need a project tied to the brand's own domain. Keyword, SERP, ranking and backlink research works against any target from any project, so a brand without its own project can use a general research project instead (`create_project` costs no credits; check `list_projects` first so you don't create a duplicate). Competitor-side research is never blocked by a missing brand project.

## Write actions

Every connector that can publish, send, spend or change an account (Brevo, HubSpot, Typefully, WordPress and page-builder MCPs, WP Umbrella, Tally.so, Make, Zapier, Adobe sharing and Stock licensing, Canva exports, page merges and video generation, Figma Weave runs, Affinity scripts that change or export a document, Google Ads changes, OpenSEO scheduled trackers) is gated by `security-policy`: Claude drafts, then asks before anything goes live. Credit, billing and identity rules per connector are in `mcp-efficiency`.

## Connection status to check

Checked against the account's connector list on 5 Nov 2026:

- **Not finished or needing a reconnect:** HubSpot (connection not finished; HubSpot steps fall back to copy plus a build checklist), WP Umbrella (needs a reconnect), HyperFrames by HeyGen and Breakdance (installed, connection not finished).
- **LinkedIn Ads:** only the LinkedIn Ad Library connector is installed at account level. Campaign data for `linkedin-ads-manager` and `paid-ads-report-writer` comes from a locally configured LinkedIn Ads server, if there is one, or from Campaign Manager exports.
- **Affinity:** a local connector, not in the account list. Install it from the connector directory and switch the MCP server on in Affinity's settings.
- **Not used by this plugin:** dembrandt is referenced in `frontend-design` as a CLI (`npx dembrandt`); its MCP server is optional and not installed. Microsoft Ads and Meta connectors are planned, not yet added.
