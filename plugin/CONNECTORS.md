# Connectors

This plugin is built around a budget-conscious stack: OpenSEO instead of Ahrefs or Semrush, the ad platforms' own connectors instead of a paid data aggregator, and free first-party data (Search Console, GA4, Bing Webmaster Tools) wherever it exists.

`.mcp.json` only declares the connectors with a stable public endpoint (Canva, Figma, HubSpot, Notion). Everything else below is connected per account in Claude's connector settings; the skills look for it by name and say plainly when it isn't there, rather than guessing data.

## Which connector each discipline uses

| Discipline | Connector | Used by | If it isn't connected |
|---|---|---|---|
| Keyword, SERP, ranking and backlink data | OpenSEO | SEO research skills, `sea-keyword-research`, competitive intel | Say so; fall back to web research, never estimate figures |
| Site audits, rank tracking, local rank grid, GA4 | OpenSEO (needs an OpenSEO project for the domain) | SEO skills, `paid-ads-report-writer` (landing page context) | See "Data-source rule" below |
| First-party search performance | Search Console, or OpenSEO's Search Console tools | `content-gap-mapping`, `seo-keyword-research`, `seo-audit` | See "Data-source rule" below |
| Page content and crawling | Firecrawl | Research and content-gap skills | Use web fetch for single pages |
| Web and company research | Exa | `european-market-intelligence`, research skills | Use web search |
| Google Ads (read-only) | Google Ads | Google Ads skills, `paid-ads-report-writer` | Ask for exports |
| LinkedIn Ads | LinkedIn Ads | `paid-ads-report-writer` | Ask for Campaign Manager exports |
| Competitor B2B ads | LinkedIn Ad Library | `competitor-teardown`, `european-market-intelligence` | Ask for screenshots or copy |
| AI citations (Copilot) | Bing Webmaster Tools | SEO/GEO work | Ask for the AI Performance CSV export |
| Email | Brevo, HubSpot | `email-sequence-hubspot-brevo`, `newsletter-writer` | Produce copy and a build checklist without live data |
| Design | Canva, Figma | `canva-workflow`, `figma-weavy-workflow` | Hand back a manual build checklist |
| Social scheduling | Typefully | `social-content-writer` | Hand back finished copy only |
| WordPress | The site's own MCP (for example NovaMira) | Content and design work on a live site | Hand back copy and markup for manual entry |
| Knowledge base | Notion | Briefs and reference material | Ask for the material |

## Data-source rule for search performance data

Not every brand has an OpenSEO project. Resolve the source once per task, in this order:

1. The brand kit's `references/context.md` lists the data sources for that brand. Use what it says.
2. If the brand has an OpenSEO project, use OpenSEO's Search Console and GA4 tools with that project ID.
3. Otherwise use the standalone Search Console connector for the verified property.
4. Otherwise ask. Never substitute estimated traffic for first-party data without saying so.

Every OpenSEO tool takes a `projectId`, but only the first-party tools (Search Console, GA4) and the site-level tools (site audit, rank tracking) need a project tied to the brand's own domain. Keyword, SERP, ranking and backlink research works against any target from any project, so a brand without its own project can use a general research project instead (`create_project` costs no credits; check `list_projects` first so you don't create a duplicate). Competitor-side research is never blocked by a missing brand project.

## Write actions

Every connector that can publish, send, spend or change an account (Brevo, HubSpot, Typefully, WordPress, Canva exports, Google Ads changes) is gated by `security-policy`: Claude drafts, then asks before anything goes live.
