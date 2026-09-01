---
name: press-release-writer
description: "Draft a press release — headline, dateline, lead paragraph, body, quotes, boilerplate, and media contact — following standard PR conventions and AP-style formatting. Use for \"write a press release,\" \"PR announcement,\" \"launch announcement,\" \"funding announcement,\" or \"partnership announcement.\" For finding outlets to pitch it to, see media-mapping."
---

# Press Release Writer

Drafts a press release ready for distribution or direct pitching.

## Step 1 — Identify the Brand

Same pattern as `web-content-pipeline`: determine the brand/client, check for a matching `[brand]-brand-kit` skill, load it if found. Press releases sit at the formal end of most brands' tone spectrum — apply the brand kit's most formal/factual register even if its default voice is more casual, since PR conventions expect a newsworthy, factual tone.

## Step 2 — Gather Requirements

| Field | Input |
|---|---|
| Brand/client | Determines which brand kit applies |
| Announcement type | Product launch, funding, partnership, milestone, executive hire, event |
| The news | What happened, in one sentence |
| Why it matters | To customers, the market, or the industry |
| Quote source(s) | Who is quoted, and their title — draft placeholder quotes for the user to approve, never fabricate one and present it as final |
| Data/proof points | Numbers, dates, figures to include |
| Boilerplate | Standard company description, if one exists |
| Media contact | Name, email, phone |

## Step 3 — Write to Structure

- **Headline** — factual, newsworthy, under ~80 characters
- **Subheadline** — optional, adds context
- **Dateline** — city, state/region, date
- **Lead paragraph** — who, what, when, where, why in 2-3 sentences
- **Body paragraphs** — supporting details, context, one or two quotes
- **Boilerplate** — standardized company description (reuse if the brand has one)
- **Media contact** — name, email, phone

Newsworthy, not promotional: state facts, avoid superlatives without evidence (mirrors `brand-review`'s unsubstantiated-claims flag), and never invent a quote or statistic — mark any placeholder clearly as `[PLACEHOLDER — confirm with source]`.

## Step 4 — Copy Edit

Run `copy-editing` (Seven Sweeps), focused on Clarity and Prove It — press releases lean on evidence, not persuasion technique. Skip the Heightened Emotion sweep; press releases stay factual.

## Output

- Full press release, ready to distribute
- 2-3 headline options
- List of any placeholder quotes/figures still needing confirmation
- Suggested distribution angle (which media type this fits)

Ask: "Would you like help identifying outlets to pitch this to?" (Hand off to `media-mapping`.)

## Related Skills

- `[brand]-brand-kit` — loaded in Step 1
- `media-mapping` — identifies outlets to pitch the release to
- `copy-editing` — Step 4
- `content-creation` — the gateway skill; routes here when the content type is a press release