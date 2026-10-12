# Workflow 2: Competitive Landscape & Company Profiling

Read this when the request is a competitive landscape & company profiling task. Part of `european-market-intelligence`; the tool stack, compliance layer and output formats stay in the main skill.

**Objective:** Merge landscape mapping and deep single-competitor dossiers - discover the field, then go deep on the ones that matter.

1. **Discover.** Exa for semantic discovery of comparable companies and category terms per target market's own language (not just English - "gestion du personnel," "Personalverwaltung," "personeelsbeheer" surface different competitor sets than "workforce management"). OpenSEO SERP data per country/language. Firecrawl on G2/Capterra/Product Hunt category pages.
2. **Verify corporate facts against registries, not marketing copy.** Legal name, seat, legal form, filing status via BRIS (European e-Justice Portal) for a cross-border existence check, then the relevant national register for real depth - see references for the country table. BRIS is a verification layer, not a research database; budget time for national-register lookups per country in scope.
3. **Funding and ownership - free-first.** Start with Exa for funding/press signals (a real substitute for a chunk of what a paid database like Dealroom provides), then pull financials and NACEBEL/NACE codes from free national sources: Bizzy or Databakkes/Busibee for Belgium, Pappers.fr for France, Northdata or Handelsregister for Germany, KVK for the Netherlands, Companies House for the UK (genuinely excellent and fully free). Firecrawl handles the ones with scrape-friendly pages; use Claude for Chrome for anything gated behind a search form or session, most commonly Bizzy. Check BORIS for beneficial ownership where the member state has gone live - coverage is partial as of 2026 (roughly half of EU/EEA countries), so treat gaps as "unknown," not "no ownership." Dealroom/Orbis stay noted as optional paid upgrades, not a dependency.
4. **Categorize** direct/indirect/potential and build a positioning matrix, same as a standard competitive landscape.
5. **Profile deeply** for the 3–7 competitors that matter: product (Firecrawl on product/doc pages), customers (case studies, G2/Capterra/Trustrader-style reviews), hiring signals (job postings as roadmap tells), marketing (Workflow 4), sales motion.

**Deliverable:** Landscape report with positioning matrix, plus full dossiers (SWOT + battlecard, see format below) for priority competitors.
