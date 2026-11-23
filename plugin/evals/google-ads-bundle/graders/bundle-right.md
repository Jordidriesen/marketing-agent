---
type: llm
---
PASS only if the reply shows all of these:
1. Upload files in Google Ads Editor format were written: at least campaigns, ad groups, keywords, negatives and RSAs (file names starting google-ads-).
2. Every keyword has a match type (Broad, Phrase or Exact) in its own column, not as brackets or quotes in the keyword text.
3. Negatives cover job seekers and free or template intent, each with a negative match type, and none of them blocks one of the five keywords.
4. The campaign is imported as Scratchpad or Paused, not Enabled.
5. The validator's final output says the bundle is valid.
6. No volume, CPC or performance figure is invented.
FAIL if any point does not hold, and name which.
