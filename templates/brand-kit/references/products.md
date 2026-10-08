# Products: [Client Name]

Index of what [Client] sells. Load this when a task names a product, compares products, or needs
to know which product fits which customer. Load the single product file you need from
`references/products/`, not all of them.

Terminology is not set here or in the product files. Product names, feature names and banned
words live in the Locked Terminology table in `voice.md`, once, for the whole brand. Where a
product file needs a locked term, it uses it and does not redefine it.

Delete this file and the `products/` folder if the brand sells a single offer or a service with
no distinct products. `context.md` (Offer and proof) is then enough.

---

## Product index

| Product | Slug | One line: what it is | Primary audience | Status | File |
|---|---|---|---|---|---|
| [Product name as the client writes it] | [slug] | [one sentence] | [buyer role or segment] | [live / beta / retiring / planned] | `products/[slug].md` |

## How the products fit together

[Two to four lines: which products are sold alone, which are bundled, which depend on another,
and which customer problem points to which product. Mark anything not confirmed as unknown.]

## Rules for every product file

- One file per product, named by its slug, copied from `products/_product-template.md`.
- Every fact is confirmed by the client or traced to a source. Anything else is written as
  "unknown". Never fill a gap with a plausible figure, feature or integration.
- Limitations are written down. A product file with an empty limitations section is not finished.
- Proof (customer names, results) only with permission to use it publicly. Say where the
  permission is recorded.
- Put the date of the last review at the top of each file. A file not reviewed in twelve months is
  treated as possibly out of date and flagged when used.
