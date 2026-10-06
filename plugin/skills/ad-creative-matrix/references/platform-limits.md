# Platform limits for ad copy

Working figures for `ad-creative-matrix`. **These are third-party summaries of platform specs
and platform specs change.** Treat them as a starting point. When a limit matters to a decision,
check the platform's own current specification page and use that. If it differs, use the current
spec and say so.

LinkedIn's help centre could not be fetched when this file was written (it disallows automated
access), so the LinkedIn figures come from a third-party guide and are not confirmed against
LinkedIn's own page.

Last checked: October 2026.

## LinkedIn single image ads

| Field | Recommended | Maximum | Note |
|---|---|---|---|
| Introductory text | up to about 150 characters | 600 | Longer text is cut behind an expand control on the feed |
| Headline | up to about 70 characters | 200 | Mobile cuts off aggressively beyond the recommendation |
| Description | about 70 characters | 300 | Shown only on some placements, such as the LinkedIn Audience Network |

Source: ZenABM, "LinkedIn single image ad specs".

## Meta feed ads

| Field | Visible without expansion | Note |
|---|---|---|
| Primary text | about 125 characters | More text is allowed but is cut behind an expand control |
| Headline | about 40 characters | |
| Description | about 25 to 30 characters | Varies by placement |

Source: AdsUploader, "Ad specifications". Meta's allowed maximums are higher than the visible
lengths. Write for the visible length, with the hook inside it.

## Video and short-form (YouTube, TikTok, Reels)

No character limit applies to the hook. The constraint is time: the first 3 seconds carry the
spoken line, the on-screen text and the first shot. Write the hook for sound-off viewing as well,
so the on-screen text line is never optional.

## Locale expansion

Copy translated into German or French often runs about 30 percent longer than English. When
the set will be localised, draft hooks about 20 percent under the limit, or plan to re-write the
hook for each locale instead of translating it (see `content-translate`).

## Naming convention for ads

Tag every assembled ad so results map back to the parts.

`[platform]-[campaign]-H[hook id]-B[body id]-C[cta id]`

Example pattern: `li-launch-H07-B2-C1`

Keep the hook, body and CTA IDs stable between the sheet, the ad names and any later analysis in
`ad-copy-tester` or `paid-ads-report-writer`, so a result can be traced to one hook, one body and
one CTA.
