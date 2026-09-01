# European Data Sources - Reference

Loaded by `european-market-intelligence` SKILL.md for Workflows 1, 2, and 6. Organized pan-EU first, then country-specific, then commercial/private-data platforms, then compliance.

## Table of Contents
1. Pan-European Official Sources
2. National Statistical Offices & Business Registers (by country)
3. Public Procurement (Government Demand)
4. Company & Funding Intelligence Platforms
5. Marketing / SEO / Ad Intelligence Sources
6. Review & Software Marketplace Platforms
7. Trade Bodies, Chambers of Commerce & Funding Agencies
8. GDPR / OSINT Compliance Reference

---

## 1. Pan-European Official Sources

| Source | What it gives you | Notes |
|---|---|---|
| **Eurostat** (ec.europa.eu/eurostat) | Structural Business Statistics (SBS) by NACE code, country, size class; business demography (births/deaths/high-growth); population, trade, price indices | Primary top-down market-sizing source. Datasets carry DOIs - cite them (e.g. `sbs_sc_ovw`, `bd_size`). Data typically lags 18–24 months; state vintage. |
| **BRIS - Business Registers Interconnection System** (via European e-Justice Portal) | Cross-border company existence check, legal form, seat, branches, cross-border mergers | Verification layer only - no financials, no ownership. Connects all EU/EEA national registers via a single point of access; doesn't replace them. |
| **BORIS - Beneficial Ownership Registers Interconnection System** | Beneficial ownership (who ultimately owns/controls a company) | Live in ~17 of 30 EU/EEA countries as of early 2026 (rolling out; member states had until July 2026 to transpose operational rules, full response-time obligations from November 2026). Treat non-covered countries as "unknown," not "no owner." Public UBO access has been restricted EU-wide since a 2022 CJEU ruling - most countries now require a "legitimate interest" request. |
| **TED - Tenders Electronic Daily** (ted.europa.eu) | All EU public procurement notices above threshold: contract notices, prior information notices, contract award notices | Official RESTful API, anonymous read access, ~740,000 notices/year, updated ~5x/week. Filter by CPV code, country, buyer, value, date. See Section 3. |
| **EU Open Data Portal** (data.europa.eu) | Aggregated open datasets across all EU institutions, including CSV subsets of TED and trade data | Good for one-off pulls without building against the live API. |
| **ECB Statistical Data Warehouse** | Macroeconomic, monetary, exchange-rate, interest-rate data | Use for currency-normalization and macro-context sections of a report. |
| **CORDIS** (cordis.europa.eu) | Horizon Europe / EU-funded R&D projects and participants | Useful for innovation-trend scanning and identifying who's getting EU research funding in a category. |
| **VIES** (VAT Information Exchange System) | VAT-number validation for any EU business | Quick legitimacy check on a named company. |
| **EUIPO** (euipo.europa.eu) | EU trademark and design registrations | Useful signal for product launches and brand activity ahead of public announcement. |

## 2. National Statistical Offices & Business Registers (core working set)

Match this to your existing translation-memory language set (EN/DE/FR/NL/ES) plus the UK as a common comparison market.

| Country | Statistical office | Business/company register |
|---|---|---|
| Belgium | Statbel (statbel.fgov.be) | KBO/BCE (Banque-Carrefour des Entreprises / Kruispuntbank van Ondernemingen) |
| Germany | Destatis (destatis.de) | Handelsregister (via unternehmensregister.de) |
| France | INSEE (insee.fr) | Sirene / INPI Registre National des Entreprises |
| Netherlands | CBS (cbs.nl) | KVK Handelsregister |
| Spain | INE (ine.es) | Registro Mercantil Central |
| Italy | ISTAT (istat.it) | Registro Imprese (via InfoCamere) |
| United Kingdom (non-EU, common comparator) | ONS (ons.gov.uk) | Companies House (free, unusually open filings) |
| Nordics | Statistics Sweden / Statistics Denmark / Statistics Norway / Statistics Finland | Bolagsverket (SE), Virk/CVR (DK), Brønnøysund (NO), PRH (FI) |
| Poland | GUS (stat.gov.pl) | KRS (Krajowy Rejestr Sądowy) |

**Reality check on access:** coverage and cost vary sharply by country - Denmark, Poland, and the UK offer broad free access to filings; Italy, France, and Spain typically charge for full financial filings. Budget accordingly and don't assume EU-wide parity.

## 3. Public Procurement (Government Demand)

TED is the primary source (Section 1). Practical use:

- **Demand signal:** search open/recent contract notices by CPV code + country to size current government demand in a category.
- **Competitor intelligence:** contract *award* notices show winner, awarded value, and buyer - one of the few places European B2B pricing becomes public record.
- **Account targeting:** buyer names and NUTS regions build a target list of active public-sector purchasers.
- **Access:** official API is free and anonymous for reading published notices; several third-party wrappers (Apify actors, RapidAPI listings) exist if a cleaner JSON feed than the native XML/eForms schema is preferred. eForms became the standard schema from November 2022 - make sure any tooling handles both eForms and legacy standard-form notices for historical data.
- Many countries also run below-threshold procurement on national portals not fully mirrored in TED - for deep single-country public-sector work, check the national portal too (e.g. Belgium's e-Procurement, Germany's bund.de/Vergabeportal).

## 4. Company & Funding Intelligence Platforms

**Free-first stack (default).** Use Exa to discover funding/press signals and Firecrawl (or Claude for Chrome where a site needs an interactive search form) to pull structured company data from these:

| Country | Free source | What it gives you | Access notes |
|---|---|---|---|
| Belgium / pan-EU | **Bizzy** (bizzy.org / bizzy.ai) | NACEBEL codes, legal status, Financial Health Score, financials from the National Bank of Belgium, ownership structure, team/roles | Freemium, free trial/limited lookups, no credit card required. Search form is interactive; use Claude for Chrome rather than Firecrawl for this one. |
| Belgium | **Databakkes.be** or **Busibee.be** | Enterprise number, address, NACE codes, establishments, straight from the CBE (Crossroads Bank for Enterprises) | Fully free, scrape-friendly for Firecrawl. Thinner than Bizzy (no financials yet on Databakkes as of 2026) but a clean fast lookup. |
| France | **Pappers.fr** | SIREN/SIRET, legal form, financials, directors, filings, sourced from INPI/INSEE/BODACC | Free since 2020, 22M+ companies, the reference tool for French company data; also has a free-tier API. |
| Germany | **Northdata** (northdata.com) | Handelsregister data, officers, LEI, financials/insolvency events, across 21 European countries | Basic registry lookups are free; deeper financial/network views are paywalled. Good first stop even outside Germany given its multi-country coverage. |
| Netherlands | **KVK Handelsregister** (kvk.nl) | Trade names, legal form, registration status, address | Basic search free; official extracts cost a small fee. |
| United Kingdom (non-EU, common comparator) | **Companies House** | Full filing history, accounts, officers, ownership (PSC register) | Fully free and unusually open, the best single-country register in Europe for depth at zero cost. |
| Spain | **einforma** or the **Registro Mercantil** directly | Basic company facts free; financial extracts typically paid | Weakest link in the free-first chain, budget extra Exa/Firecrawl discovery time to compensate. |

**Optional paid upgrades (not required for this skill to work):**

| Platform | Best for | Note |
|---|---|---|
| **Dealroom** (dealroom.co) | Startup/scaleup funding rounds, ecosystem benchmarking | Purpose-built in Amsterdam for Europe, materially deeper than Crunchbase on early-stage BE/NL/DACH/Nordic data. Roughly €5k-25k/yr, no free tier, use only if a specific engagement's budget justifies it. |
| **Orbis (Moody's / Bureau van Dijk)** | Private-company financials and ownership at scale | Enterprise pricing; the closest thing to a pan-European private-financials database if a client project ever funds it. |
| **Crunchbase** | Broad global lookups | Free tier exists but European (especially early-stage) coverage is thinner than Dealroom's, a secondary check either way. |
| **Statista** | Market-size estimates, consumer/industry statistics | Useful for triangulation; always trace a Statista figure back to its cited original source rather than citing Statista itself as primary. |
| **Kompass** | Exhaustive B2B company-list building in a category/country | Free tier for basic listings, paid for bulk export. |

## 5. Marketing / SEO / Ad Intelligence Sources

Already covered by your existing MCP stack - listed here for completeness within this skill's Workflow 4:

- **OpenSEO** - organic rankings, keyword demand, and SERP data settable per country/language (`locationCode`/`languageCode` on each call, project-scoped, see `content-research-orchestrator/references/openseo-tool-map.md`); the right tool for "how big is search demand for X in Germany vs. France."
- **Ahrefs** - cross-check on backlink/domain-authority signals.
- **LinkedIn Ad Library MCP** - live and historical B2B ad creative and targeting; generally a stronger signal for European B2B competitors than estimated ad spend, since LinkedIn is the dominant paid channel for the category Client A/Client B-type clients compete in.
- **Google Ads MCP** - auction insights where the user's own account has overlap.
- **Search Console MCP** - first-party ground truth for the user's own domain.

## 6. Review & Software Marketplace Platforms

- **Trustpilot** - UK/Nordic-founded, dominant consumer and B2C-services review platform in Europe; often more relevant than G2 for non-SaaS European categories.
- **G2 / Capterra / TrustRadius** - solid for B2B software categories, US-headquartered but with real European review volume for enterprise software.
- **Kununu / Glassdoor** - employee reviews; useful for the "hiring signal" and culture angle in a competitor dossier, stronger European coverage from Kununu in DACH specifically.

## 7. Trade Bodies, Chambers of Commerce & Funding Agencies

- **Enterprise Europe Network (EEN)** - EU-wide SME support network, useful for identifying sector-specific trade bodies and partnering opportunities per country.
- **National investment/trade promotion agencies** - e.g. Flanders Investment & Trade (FIT) for Belgium, Germany Trade & Invest (GTAI), Business France, Netherlands Foreign Investment Agency (NFIA) - good sources for sector reports and market-entry support, and often publish free market studies by vertical.
- **Sector-specific trade associations** - identify per vertical (e.g. for security/critical-event-management categories: national security-industry associations, plus EU-level bodies like CoESS for private security services).
- **Chambers of Commerce** (national and bilateral, e.g. Belgian-German, Benelux) - useful for local business-culture and partnership-norms context ahead of a market-entry recommendation.

## 8. GDPR / OSINT Compliance Reference

Referenced from the main SKILL.md's compliance layer. Applies whenever research touches named individuals rather than corporate/aggregate facts.

**Legitimate Interest Assessment (LIA) - outline:**
1. **Purpose test** - state the genuine business purpose (market research, competitive intelligence, prospecting). These generally pass the purpose test.
2. **Necessity test** - is processing this specific data actually necessary for that purpose, or would less/aggregated data do?
3. **Balancing test** - weigh the business interest against the individual's rights and reasonable expectations; document it, don't just assert it.
4. **Safeguards** - data minimization, retention limits, and a path for the individual to object.

**2026 regulatory context:** the EDPB published draft Guidelines 03/2026 on web scraping in July 2026 (public consultation ran to 30 October 2026; final version expected later in 2026). Written primarily for AI-training scraping, but the same three-part legitimate-interest reasoning is what national DPAs apply to any scraping-based research more broadly. Key practical takeaways that carry over to market/competitive research:
- Consent is not a workable basis for scraping at scale - legitimate interest is the primary route, and it requires a *documented* LIA, not an assumption that public data is automatically fair game.
- "Publicly accessible" does not mean "usable for any purpose" - purpose limitation still applies.
- Ignoring `robots.txt` doesn't create direct liability by itself but is treated as evidence of bad faith that weakens a legitimate-interest defense in EU regulatory proceedings.
- Distinguish targeted scraping (specific domains/topics, lower risk) from untargeted crawling (higher risk, harder to document a clean purpose for).

**Practical guidance for this skill:** keep research at the corporate/aggregate level wherever the deliverable allows it. Named-individual research (leadership mapping, hiring-signal analysis from job postings with named recruiters, etc.) should stick to professionally-published facts and avoid compiling anything that reads as a personal dossier.
