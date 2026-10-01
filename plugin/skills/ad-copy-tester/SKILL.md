---
name: ad-copy-tester
description: Analyzes responsive search ad asset performance and says which headlines and descriptions to keep, cut, or replace. Use when the user shares asset performance data or asks why an ad is underperforming.
---

# ad-copy-tester

You read the asset report and turn it into a swap list.

## Inputs you need
- RSA asset performance data (asset text plus performance rating where available).
- The keywords or themes the ad group targets.

## Workflow
1. Group assets by performance rating and by angle: price, speed, trust, outcome, objection.
2. Find the coverage gaps. An ad group with five headlines all making the same argument cannot be optimized by any algorithm. Name the missing angles.
3. Identify what to cut: consistently low-rated assets, and near-duplicates competing with each other.
4. Write replacements for what you cut, matching character limits and filling the missing angles. Pull `content-references/references/behavioral-psychology.md` when choosing what a replacement angle should actually argue: it's the same persuasion grounding `rsa-writer` uses, so a fresh asset written here should feel like it belongs in the same set, not a different voice bolted on.
5. Check relevance: do the top headlines reflect the ad group's keyword theme?
6. Run any new replacement assets through `ai-content-cleaner` (CLEAN mode) before delivering, same as `rsa-writer`. A replacement that reads as generic AI copy just becomes next month's cut.

## Output format
- Keep / cut / replace table with the reason per asset.
- New replacement assets with character counts.
- One line on angle coverage before and after.

## Rules
- Never cut an asset on low impressions alone. "Learn" ratings usually mean not enough data, not bad copy.
- Never write replacements that repeat an angle already covered.
- Respect character limits exactly, and count them.
