# Workflow 1: Market Sizing (TAM/SAM/SOM) - Europe-first

Read this when the request is a market sizing (tam/sam/som) task. Part of `european-market-intelligence`; the tool stack, compliance layer and output formats stay in the main skill.

**Objective:** Calculate TAM/SAM/SOM with European official statistics as the backbone, not press-release market-size claims.

1. **Scope the market in NACE terms.** Every EU statistical dataset is organized by NACE Rev. 2 activity codes, not by marketing category names. Translate "security software for critical infrastructure" into the relevant NACE division(s) first - this is the single biggest accuracy lever in European market sizing.
2. **Top-down via Eurostat Structural Business Statistics (SBS)** - enterprise counts, turnover, value added, and employment by NACE code, country, and size class. This is the closest thing Europe has to a single authoritative top-down source; see references for dataset codes (`sbs_sc_ovw`, `bd_size`). Cross-check with national statistical offices (Statbel, Destatis, INSEE, CBS, INE, ISTAT) for finer geographic or sector cuts Eurostat doesn't carry.
3. **Bottom-up** - unit economics × addressable buyer count, sourced from BRIS/national business registers (enterprise counts by legal form and size class) plus Exa/Firecrawl-built company lists from the free sources in Section 4 of the references file (Bizzy, Databakkes, Pappers.fr, Companies House, Northdata, KVK). Dealroom/Orbis remain listed as an optional paid upgrade if you ever need named-account financial depth beyond what the free registries expose.
4. **Narrow to SAM** - apply country/language/regulatory constraints explicitly. A CE-marked, GDPR-compliant product doesn't have the same SAM as a US-only competitor entering Europe; note standards/certification barriers (CE marking, national security clearances for defence/critical-infrastructure buyers, sector-specific licensing) as SAM reducers, not footnotes.
5. **Project SOM** - competitive intensity from Workflow 2, plus realistic GTM capacity. Compare to comparable companies' actual market-share trajectories in the same NACE code where findable via SBS enterprise-birth/death and high-growth-enterprise data.
6. **Document everything** - dataset code, geography, NACE code(s), currency, VAT treatment, and vintage (Eurostat SBS typically lags 18–24 months; state this explicitly rather than presenting it as current).

**Deliverable:** Report with top-down and bottom-up TAM, SAM with stated constraints, SOM (Year 1/3/5, conservative/base/optimistic), full source and methodology trail.
