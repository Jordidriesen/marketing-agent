# Workflow 3: Pricing & Product Intelligence

Read this when the request is a pricing & product intelligence task. Part of `european-market-intelligence`; the tool stack, compliance layer and output formats stay in the main skill.

**Objective:** Reverse-engineer pricing strategy and feature parity - same as the source skills, with a European pricing-display note.

1. Extract published pricing via Firecrawl. **Flag VAT treatment explicitly** - B2B European pricing pages often show ex-VAT prices that aren't directly comparable across countries with different VAT rates (17–27% across the EU) without normalizing.
2. Cross-reference multi-country pricing pages (many European vendors price per-country or per-currency) rather than assuming one EU-wide price point.
3. Build the feature comparison matrix (binary + quality rating + maturity) as in the source workflow.
4. Uncover non-published pricing via reviews, job postings mentioning quota/ACV, and - for anything touching public buyers - actual awarded contract values from TED (see Workflow 6). TED award notices are one of the only places European B2B pricing becomes a matter of public record.

**Deliverable:** Pricing intelligence report normalized to a common currency and VAT basis, with a feature-gap matrix.
