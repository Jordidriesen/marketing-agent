<!-- Shared reference. Source of truth: plugin/skills/google-ads-build/references/google-ads-exports.md. Edit it there and run scripts/sync_shared_refs.py. -->
# Google Ads Editor upload files

**Contents**

- The bundle
- Columns and values
- Limits the validator enforces
- Validating
- Importing

Every Google Ads deliverable that would otherwise be retyped also ships as Google Ads Editor CSV
files, saved next to the readable version in `deliverables/`. The readable version is for review;
the CSV is for import. Both say the same thing.

## The bundle

Write only the files the job produces. Column names are Google Ads Editor's own.

| File | Columns | Made by |
|---|---|---|
| `google-ads-campaigns.csv` | Campaign, Campaign type, Campaign daily budget, Bid strategy type, Campaign status | `google-ads-build` (campaign-architect) |
| `google-ads-ad-groups.csv` | Campaign, Ad group, Max CPC | `google-ads-build` |
| `google-ads-keywords.csv` | Campaign, Ad group, Keyword, Criterion Type | `google-ads-build` (campaign-architect, sea-keyword-research) |
| `google-ads-negatives.csv` | Campaign, Ad group, Keyword, Criterion Type | `google-ads-build`; `google-ads-analyse` (search-term-auditor) |
| `google-ads-rsas.csv` | Campaign, Ad group, Headline 1 to Headline 15, Description 1 to Description 4, Path 1, Path 2, Final URL | `google-ads-ads` (rsa-writer) |
| `google-ads-sitelinks.csv` | Campaign, Sitelink text, Description line 1, Description line 2, Final URL | `google-ads-ads` |
| `google-ads-callouts.csv` | Campaign, Callout text | `google-ads-ads` |

## Columns and values

- **Campaign status:** `Scratchpad` for a new campaign (Editor keeps it as a draft) or `Paused`.
  Never `Enabled`: switching a campaign on is the client's decision, in the account.
- **Criterion Type for keywords:** `Broad`, `Phrase` or `Exact`. The keyword text is plain: no
  brackets, quotes or plus signs.
- **Criterion Type for negatives:** `Negative Broad`, `Negative Phrase` or `Negative Exact` on an
  ad group (Ad group filled in); `Campaign Negative Broad`, `Campaign Negative Phrase` or
  `Campaign Negative Exact` on a campaign (Ad group empty). Google's help names the types
  "Negative" and "Campaign negative"; check the exact spelling against an Editor export of the
  account on the first import, and note any difference in `decisions.md`.
- **Shared negative lists** have no column here: list them in the readable version with their
  match types, to add in the account's shared library by hand.
- Amounts in the account's currency, with a full stop as decimal separator (`2.50`).

## Limits the validator enforces

Headline 30 characters, description 90, path 15, sitelink text 25, sitelink description line 35,
callout 25, keyword 80 characters and 10 words. No exclamation mark in a headline. At least 3
headlines and 2 descriptions per RSA, no repeated headline, a final URL on every ad. No em dash.
Every keyword and ad sits in an ad group the bundle defines. No negative may block one of the
bundle's own keywords (the classic mistake: a broad negative on a word every keyword contains).

## Validating

The plugin's save hook runs the validator every time a `google-ads-*.csv` file is saved in
`deliverables/` and sends its problems back. To run it by hand:

```bash
python3 <google-ads-build skill folder>/scripts/google_ads_bundle.py deliverables/
```

Fix every problem it reports before the publish question; a bundle that was not validated is
listed under Not checked, never as ready.

## Importing

In Google Ads Editor: download the latest account data, then Account > Import > From file, one
file at a time in the table's order (campaigns before ad groups, ad groups before keywords and ads).
Review the proposed changes in Editor. Posting them to the account is the client's step, after the
publish question, never the plugin's.
