# Script formats

## Pace and reading floors

| Unit | Working figure |
|---|---|
| Spoken English | about 150 words per minute (2.5 per second); slower for a technical B2B voice-over, about 130 |
| Spoken Dutch, French, German | plan on the English figure, then recheck: the translation usually has more words |
| On-screen short label (1 to 3 words) | about 0.8 s fully settled |
| On-screen sentence | about 0.3 s per word, minimum about 1.2 s |
| Captions on a talking head | the speech sets the pace; keep lines to about 42 characters |

These are working figures, not measured reading speeds. When vidIQ is connected, its length check
outranks them for spoken copy. Check on-screen text against the real frames.

## Spoken script (face on camera)

```markdown
# [Working title]
Length target: [N] min ([N] words at [wpm]). Format: [long-form / Short]. Pillar: [if any]

## Hook (0:00 to 0:05)
[The first line said. It states the payoff or the tension. Works with the sound off as a caption.]
[B-ROLL: what is on screen, if not the face]

## Promise (0:05 to 0:30)
[Why stay: what the viewer gets by the end, said plainly.]

## Section 1: [name] (0:30 to 2:00)
[Spoken lines.]
[B-ROLL: ...] [ON SCREEN: exact text] [CUT TO: ...]
Re-hook into section 2: [the line that opens the next question]

## Section 2 ...

## Payoff
[The answer, the verdict, the result. Delivered, not teased again.]

## CTA
[One ask only. The brand's own wording.]

## Open items
[NEEDS SOURCE] ... / [JORDI'S TAKE NEEDED] ...
```

Rules: write it as said, with contractions. One idea per sentence. No line that only makes sense when read.
Directions in square brackets so word counts can exclude them. Personal opinions, wear-time notes, results
and anecdotes come from the user's notes; where they are missing, leave a marked gap.

## Two-column A/V script (voice-over and built video)

```markdown
# [Title]: A/V script
Length: [N] s. Format: [W]x[H]. Language: [locale]. Voice: [VO / on-screen only / presenter]

| # | Time | Visual | Audio |
|---|---|---|---|
| 1 | 0:00 to 0:03 | Close-up of the product's dashboard, cursor enters | VO: "[line]" / ON SCREEN: "[text]" |
| 2 | 0:03 to 0:07 | ... | MUSIC: track fades in, under VO |

Total: [sum] s. Target: [N] s.
Source per visual: [scene number: file, page or screen it comes from]
```

Rules: one row per beat. The visual column names the shot and the real material it uses; never "generic
footage of people working". The audio column holds the exact words. A row whose words do not fit its time
gets fewer words or more time, never a faster read.

## Locale versions

Translate the script with `content-translate`, then recount every row. Where a locale no longer fits, cut
words in that locale (with the translator's choice of what to drop) or lengthen the scene in every locale
together; never shorten a reading floor.
