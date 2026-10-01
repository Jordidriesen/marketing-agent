# Cultural Adaptation Profiles

Locale profiles for cultural adaptation, loaded during the Cultural
Profile step of `content-translate`. Covers address form (formality),
example brands and companies to substitute in, currency and pricing
conventions, statistics sources to prefer, legal references to swap, CTA
tone, and idiom notes, applied during the translation pass itself rather
than as a separate second-pass skill.

**Brand-specific terminology overrides** (a client's confirmed preferred
term for a given concept, "always translate X as Y") belong in that
client's `[brand]-brand-kit` skill, not here. This file covers market-level
knowledge that applies regardless of which brand is being translated; a
brand kit's locked terminology always wins when the two conflict. See an
existing `[brand]-brand-kit`'s Locked Terminology section for a working
example, if you have one.

## DACH (Germany, Austria, German-speaking Switzerland)

**Locales:** `de-DE`, `de-AT`, `de-CH`.

- **Formality:** B2B and tech: `Sie` (formal). Lifestyle, gaming,
  D2C: `du` (informal). Pick one and use it consistently for the
  entire post. SaaS for SMB defaults to `du`; enterprise SaaS defaults
  to `Sie`.
- **Brand examples to swap to:** MediaMarkt, Saturn, Otto,
  Zalando (retail), Lidl, Aldi (grocery), Deutsche Bank, ING (finance),
  SAP, Siemens (B2B tech). For Austria: Spar, Hofer, BAWAG. For Swiss:
  Migros, Coop, UBS.
- **Currency:** EUR for DE and AT, CHF for CH. Format: `1.234,56 EUR`
  (DE/AT) or `CHF 1'234.56` (CH).
- **Statistics sources to prefer:** Statista (Germany scope), Bitkom,
  Bundesnetzagentur, Destatis (Statistisches Bundesamt), HWWI,
  ifo Institut, Bertelsmann Stiftung. Avoid US-only Pew or Nielsen
  unless explicitly framed as US comparison.
- **Legal references to swap:** CCPA to DSGVO (GDPR in DACH-speak),
  FTC to Bundeskartellamt, FCC to Bundesnetzagentur. Accessibility law is
  jurisdiction-specific: DE BGG, AT BGStG, CH BehiG. Keep ADA when the claim
  is specifically about US compliance.
- **CTA tone:** Informational, never imperative. Prefer "Jetzt
  entdecken", "Mehr erfahren", "Kostenlos testen". Avoid "Buy now",
  "Sign up today" style. Trust signals (data protection, GDPR
  compliance) outperform urgency.
- **Idiom notes:** Compound nouns are normal; don't break them.
  "Game-changer" becomes "Wendepunkt" or a specific concrete claim.
  "Best practices" stays in English.

## Francophone (France, Quebec, Belgium-FR, Switzerland-FR)

**Locales:** `fr-FR`, `fr-CA`, `fr-BE`, `fr-CH`.

- **Formality:** Default `vous` for almost all professional content.
  `tu` only for B2C lifestyle aimed at under-30 audiences. France
  business culture is markedly more formal than US.
- **Brand examples to swap to:** Carrefour, Auchan, Leclerc, FNAC
  (retail/electronics), Orange, SFR (telecom), BNP Paribas, Société
  Générale (finance), Dassault, Capgemini (B2B tech). Quebec: Hydro-Québec,
  Desjardins, Couche-Tard.
- **Currency:** EUR for `fr-FR` and `fr-BE`, CHF for `fr-CH`, CAD for
  `fr-CA`. Format: `1 234,56 EUR` (NBSP as thousands separator). Quebec
  writes CAD as `1 234,56 $` with the symbol after.
- **Statistics sources to prefer:** INSEE, Médiamétrie, IFOP, BVA,
  ARCOM (formerly CSA), Statistique Canada (for fr-CA), Eurostat (for
  fr-FR European context).
- **Legal references to swap:** CCPA / GDPR to RGPD, FTC to DGCCRF,
  ADA to loi du 11 février 2005. Quebec adds Loi 25 (privacy) and
  Loi 96 (French language).
- **CTA tone:** Polite, restrained, value-focused. "Découvrez",
  "En savoir plus", "Essayer gratuitement". Avoid "Achetez maintenant"
  unless e-commerce flash-sale context. Quebec accepts slightly more
  direct CTAs than France.
- **Idiom notes:** "Workflow" stays English in tech contexts. "Brand"
  often translated as "marque". Be careful with Quebec vs. France
  vocabulary differences (e.g., "courriel" vs. "email", "fin de
  semaine" vs. "weekend").

## Benelux (Netherlands, Flemish Belgium)

**Locales:** `nl-NL`, `nl-BE` (Flanders). French-speaking Belgium is
covered under Francophone above (`fr-BE`), not here.

- **Formality:** Dutch business culture defaults informal even in B2B,
  `je`/`jij` is standard. Reserve `u` for very traditional sectors (legal,
  government, some banking) or a noticeably senior audience. Flemish
  Belgium runs a little more formal on first contact than the Netherlands
  but still trends informal compared to French Wallonia; for `nl-BE`, when
  in doubt, open with `u` and drop to `je` if the brand voice calls for
  warmth.
- **Brand examples to swap to:** Bol.com, Coolblue, Albert Heijn, Jumbo
  (retail), ING, ABN AMRO, Rabobank (finance), Exact, AFAS (B2B software).
  For Flanders: Colruyt, Delhaize (retail), KBC, Belfius (finance),
  Proximus, Telenet (telecom).
- **Currency:** EUR for both. Format: `1.234,56 EUR` (period thousands,
  comma decimal).
- **Statistics sources to prefer:** CBS (Centraal Bureau voor de
  Statistiek) for the Netherlands, Statbel for Belgium, Eurostat for
  EU-wide framing. Avoid US-only Pew or Nielsen unless explicitly framed
  as a US comparison.
- **Legal references to swap:** CCPA/GDPR to AVG (the Dutch-language term
  is shared across NL and BE). FTC to the ACM (Autoriteit Consument &
  Markt) for Dutch consumer-protection matters, or the
  Gegevensbeschermingsautoriteit (GBA) for Belgian-specific data
  protection. Advertising self-regulation in the Netherlands runs through
  the Reclame Code Commissie (RCC).
- **CTA tone:** Direct and practical, avoid hard-sell urgency. Prefer
  "Ontdek", "Probeer gratis", "Meer weten". Concrete, provable claims land
  better here than aspirational language; overpromising reads as
  untrustworthy faster in this market than in most other EU markets.
- **Idiom notes:** English loanwords are common and accepted in tech and
  business contexts ("workflow", "deadline", "meeting" stay untranslated);
  don't force a Dutch equivalent where the loanword is the actual working
  term. Compound nouns follow German-style rules (write as one word, not
  space-separated). "Best practices" stays in English.

## Hispanic (Spain vs. LATAM)

Hispanic markets split sharply. Do not conflate `es-ES` with `es-MX` or
generic `es`. If a user writes `es`, ask which market or require explicit
neutral Spanish mode.

### Spain (`es-ES`)

- **Formality:** `tú` for B2C and most digital content. `usted` only
  for highly formal B2B (banking, legal). "Vosotros" exists; LATAM
  doesn't use it.
- **Brand examples:** El Corte Inglés, Mercadona, Carrefour España
  (retail), Telefónica/Movistar, Vodafone España (telecom),
  Santander, BBVA (finance), Inditex/Zara, Iberdrola (B2B).
- **Currency:** EUR. Format: `1.234,56 EUR`.
- **Sources:** INE (Instituto Nacional de Estadística), CIS,
  IAB Spain, Comscore España, Eurostat.
- **Legal:** RGPD (GDPR), AEPD (data protection authority),
  CNMC (competition), Ley General de Publicidad.
- **CTAs:** Direct but warm. "Descubre", "Empieza ahora",
  "Pruébalo gratis".

### LATAM (Mexico `es-MX`, Argentina `es-AR`, Colombia `es-CO`)

- **Formality:** `tú` general default. Argentina uses `vos` (voseo).
  Colombia mixes `tú` and `usted` depending on region. Mexico is
  consistently `tú`.
- **Brand examples (MX):** Walmart México, Liverpool, Coppel,
  Telcel, BBVA México, Bimbo. (AR): Mercado Libre, Banco Galicia.
  (CO): Éxito, Bancolombia, Rappi.
- **Currency:** Local. MXN (`$1,234.56 MXN`), ARS (`$1.234,56`),
  COP (`$1.234 COP`). Use whole-peso COP examples unless a source explicitly
  uses centavos. Always specify the currency code; bare `$`
  is ambiguous.
- **Sources:** INEGI (MX), DANE (CO), INDEC (AR), Comscore LATAM,
  IAB LATAM.
- **Legal:** LFPDPPP (MX), Ley 1581 (CO), Ley 25.326 (AR). PROFECO
  (MX consumer protection).
- **CTAs:** Warm, direct, relationship-building. "Descubre cómo",
  "Únete gratis", "Empieza hoy".

## Japanese (Japan, `ja-JP`)

- **Formality registers:** Three to know. `desu/masu` (polite, default
  for most published content). `de aru` (declarative, used in
  serious essays, white papers). Casual forms (`da`, plain verbs)
  for blog posts aimed at consumer audiences. Pick one register and
  stay in it.
- **Honorifics:** Use `-san` when referring to people. Companies
  take `sama` in formal contact contexts but not in editorial body.
- **Brand examples:** Aeon, Ito-Yokado, Don Quijote (retail),
  Rakuten, Mercari (e-commerce), NTT Docomo, SoftBank (telecom),
  MUFG, SMBC (finance), Sony, Toyota, Hitachi (B2B), LINE,
  PayPay (payments).
- **Currency:** Yen, no decimals. Prefer `1,234円` in body copy or
  `JPY 1,234` in finance-style contexts.
- **Sources:** Statistics Bureau of Japan (Soumusho), METI, Nikkei
  research, Dentsu reports, Macromill, Recruit Works Institute,
  Mitsubishi Research.
- **Legal:** APPI (Act on Protection of Personal Information),
  JFTC (Japan Fair Trade Commission), METI guidelines.
- **CTAs:** Soft, indirect, group-oriented. Avoid imperative tone.
  Prefer phrases that emphasize benefit, ease, or community
  ("everyone is using it" angles). Hard urgency converts poorly.
- **Idiom notes:** English loanwords (katakana) are common in tech
  copy but should be reserved for established terms. Avoid
  inventing new katakana words. Numbered lists work well; rhetorical
  questions are less common than in EN.

## Custom-Locale Template

When the target locale lacks a profile here, build one inline. Required
fields:

```yaml
locale: <code>           # e.g. pl-PL, sv-SE, tr-TR
formality:
  default: <formal|informal|mixed>
  notes: <when to switch>
brand_examples:
  retail: [..., ...]
  finance: [..., ...]
  telecom: [..., ...]
  b2b_tech: [..., ...]
currency:
  code: <ISO 4217>
  format: <example: 1 234,56 PLN>
sources_preferred:
  - <local statistics body>
  - <local industry research>
legal_references:
  privacy: <local equivalent of GDPR/CCPA>
  competition: <regulator>
  advertising: <regulator>
cta_tone:
  style: <imperative|informational|polite|warm>
  avoid: [...]
idiom_notes: <quirks the translator must respect>
```

Quick research pass to fill the template:

1. Search `[country] official statistics agency` for the sources block.
2. Search `[country] data protection authority` for the legal block.
3. Pull the top 3 retailers and top 3 banks from a recent business
   press article.
4. Read 2-3 native blog posts in the target market to calibrate
   `formality.default` and `cta_tone.style`.

Save custom locale profiles outside this shared reference, for example in
a project-local locale-profile file or in the task output. Do not append
runtime profiles to this file, add a proper profile section above instead
once a market becomes a repeat target.

## Profile Selection Logic

1. Exact locale match (`de-CH`, `fr-CA`, `es-MX`, `nl-BE`).
2. Language-only fallback only for unambiguous editorial markets (`de`,
   `fr`, `nl`, `ja`). Treat `es`, `pt`, `zh`, and any language spanning
   materially different legal, currency, or script markets as ambiguous
   unless the user requests explicit neutral mode.
3. Regional grouping: DACH for any `de-*`, LATAM for any `es-*` other than
   `es-ES`, Benelux for any `nl-*`.
4. Custom-locale template if no match.
