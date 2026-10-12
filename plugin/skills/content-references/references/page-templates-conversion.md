# Page Templates: Conversion and Site Pages

Load this at Step 4 of `web-content-pipeline` for landing, product, solution, feature, homepage, pricing and about pages. Articles, pillar pages, comparison pages and glossaries use `page-templates-article.md` instead.

## Landing, product, solution and feature pages (Transactional)

**Above the fold:**
- Headline: single most important message, specific over generic.
  Formulas: "{Achieve outcome} without {pain point}," "The {category} for
  {audience}," "Never {unpleasant event} again," or a direct question
  naming the main pain point. A precise number beats a vague superlative
  ("Cut onboarding to 11 days" beats "Faster onboarding"). Lead with
  whichever number or comparison should anchor the visitor's judgment for
  the rest of the page.
- Subheadline: expands the headline, adds specificity, 1–2 sentences max
- Primary CTA; states what they get: "Start Free Trial," not "Sign Up"

**Core sections** (map onto Step 2's chosen framework, StoryBrand's
Problem/Guide/Plan/Success or PAS's Problem/Agitate/Solution):

| Section | Purpose |
|---|---|
| Social proof | Build credibility: logos, stats, testimonials. Lorem Ipsum placeholders until real cases are approved (see Step 4) |
| Problem/pain | Show you understand the visitor's situation (StoryBrand's Problem / PAS's Problem+Agitate) |
| Solution/benefits | Connect to outcomes, 3–5 key benefits (StoryBrand's Plan / PAS's Solution) |
| How it works | Reduce perceived complexity, 3–4 steps |
| Objection handling | FAQ with the question count from the page-type guide, taken from the objections this traffic source arrives with (replace a system? another console? we already have X?), comparisons, guarantees |
| Final CTA | Recap value, repeat CTA, risk reversal |

**CTA copy:** avoid "Submit," "Sign Up," "Learn More," "Click Here,"
"Get Started." Use the formula [Action verb] + [what they get] +
[qualifier if needed], "Start My Free Trial," "Get the Complete
Checklist," "See Pricing for My Team."

**Reduce reactance** near any CTA implying commitment: "no credit card
required," "cancel anytime," "no obligation" next to the button removes
the felt pressure that causes hesitation.

**Frame availability/scarcity toward the desired reading, only when
true**: "12 spots left this month" reads as genuine and socially
confirming; "availability limited" reads as vague hedging. Never fabricate
scarcity.


## Implementation brief (paid landing pages)

Hidden HTML comment at the top of the page: URL, traffic source or ad
group, negative keywords for paid traffic, the framework chosen in Step 2 and why, the ONE conversion
goal, form fields, meta title and description, and schema (Organization, BreadcrumbList,
SoftwareApplication or Product, FAQPage). Every primary CTA on the page opens the same action; a
secondary path (a one-pager, say) is visibly smaller and lower contrast, there to catch someone who is
not ready.


## Page-type specifics

- **Homepage**: serve multiple audiences without going generic; lead with
  the broadest value proposition; provide clear paths for different
  visitor intents
- **Landing page**: single message, single CTA; match the headline to the
  ad/traffic source; complete the argument on one page
- **Product page**: feature → benefit → outcome; show use cases; clear
  path to try or buy
- **Solution page**: same as product page, usually broader and more
  strategic in framing; often the page that needs the fullest StoryBrand
  arc since the visitor is earlier in the decision
- **Pricing page**: help visitors choose the right plan, address "which
  is right for me" anxiety, make the recommended plan obvious. Consider a
  premium tier above the one you actually want to sell: a higher anchor
  makes the middle tier look sensible by contrast (extremeness aversion).
  Lead with the reference price you want anchoring the comparison.
- **Feature page**: connect feature → benefit → outcome; show use cases
  and examples; clear path to try or buy
- **About page**: tell the story of why the company exists, connect
  mission to customer benefit, still include a CTA. Natural home for one
  honest, specific limitation or early mistake ("we spent a year building
  the wrong thing before we found this"): a real admitted flaw from an
  otherwise competent narrative increases trust and likeability (the
  pratfall effect). One instance, genuinely true, not a hedge on every claim.


## Behavioral-science layer (all page types)

Apply the relevant rows from
`content-references/references/behavioral-psychology.md`. Blog/
Informational pages lean on precision numbers, concreteness, and fluency;
Transactional pages get the fuller treatment: anchoring, framing,
reactance reduction, extremeness aversion, and the pratfall effect where
the template above calls for it.

## Visual & layout cues (for briefing designers)

This step produces copy, not layouts, but flag these when handing a draft
to design:
- Isolate the primary CTA visually (contrast, whitespace, size): the
  isolated element is disproportionately noticed (von Restorff effect)
- Keep the same colour/shape/iconography system across every page rather
  than a fresh look each time: recognition compounds from consistently
  reused distinctive assets (Ehrenberg-Bass)
- Never sacrifice contrast or type legibility for aesthetics on any page
  with a conversion goal
- Pair any process or comparison claim with a real diagram or screenshot,
  not decorative stock (picture superiority)

Full detail: `content-references/references/behavioral-psychology.md`.

## Keyword and internal linking (light weight on these pages)

Keyword in the title or H1, the first 100 words and the meta description is usually enough, since the page's job is conversion, not ranking breadth. One or two links to a relevant blog post or case study are enough. The full rules, for articles, are in `seo-aeo-core.md` and `internal-linking-drafting.md`.
