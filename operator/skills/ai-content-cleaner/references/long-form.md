# AI Content Cleaner: long-form reference

Read this from `ai-content-cleaner` for pieces over about 300 words, for BALANCED or DETECT mode, and whenever the content type decides what to keep. The brand check, language detection, protected spans, Tier 1, the English word lists and the Unicode pass stay in `SKILL.md`.

---

## Step 0.5 - Content type

Before scanning, determine the content type: blog post, informational article, review, or
customer/case story vs. landing page, pricing page, or CTA-focused copy. This gates Tier 5
(see below). If the type is ambiguous, treat it as ambiguous rather than guessing: Tier 5's
content-type rule tells you what to do in that case.

---

### Tier 3 - Structural tells (language-neutral; check reference file for language-specific variants)

The **BALANCED** column indicates whether BALANCED mode should skip this pattern.
- **Never skip** - clean regardless of mode; no SEO/AEO justification exists
- **Skip if intentional** - preserve if there is a plausible SEO or AEO reason for the structure

A brand Voice Lock overrides this column in either direction (Step 0).

| Pattern | Description | BALANCED mode |
|---|---|---|
| Significance inflation | Inflating importance: "marking a pivotal moment", "underscores its vital role", "reflects broader trends" | Never skip |
| Superficial -ing / participial phrases | Tacked-on participles adding fake depth: "...showcasing how...", "...highlighting the importance of..." | Never skip |
| Promotional language | Tourism-brochure adjectives: "nestled in the heart of", "vibrant community", "rich cultural heritage" | Never skip |
| Vague attribution | "Experts argue", "Industry observers note", "Some critics suggest" with no named source | Never skip |
| Challenges boilerplate | "Despite challenges typical of...", "Despite these challenges, X continues to thrive" | Never skip |
| Negative parallelisms | "It's not just X, it's Y", "Not merely A, but B" | Never skip, but see Step 0: a tight specific antithesis is a device, not this pattern |
| Rule of three | Forced triads: "innovation, inspiration, and industry insights" | Skip if intentional - FAQ lists and feature triads are valid AEO structure |
| Synonym cycling | Excessive variation to avoid repetition: protagonist/main character/central figure/hero | Never skip - hurts both readability and semantic clarity |
| False ranges | "From X to Y" where X and Y aren't on a real scale | Never skip |
| Inline-header lists | Bullet points with **Bolded header:** followed by explanation | Skip if intentional - standard featured snippet and AEO format; preserve unless content is clearly not targeting snippets |
| Title case headings | ## Strategic Negotiations And Global Partnerships (applies primarily to English) | Skip if intentional - heading capitalisation is an editorial/SEO style choice; do not change |
| Overuse of boldface | Mechanically bolded phrases throughout body text | Skip if intentional - keyword bolding and AEO anchor phrases are deliberate; only flag if bolding has no apparent logic |

**BALANCED mode judgment rule for Tier 3:** When a structural pattern could plausibly be an
intentional SEO or AEO choice, preserve it unless the person has explicitly asked to remove it.
When in doubt, flag it in the changes list as "preserved - possible SEO/AEO intent" so the
person can decide.

### Tier 5 - Discourse-level tells (language-neutral, document-level, not phrase-level)

Unlike Tiers 1-4, these patterns live in the shape of the argument, not in individual words or
sentences. Detect them with a single read of the whole piece (Step 0.5) before the
phrase-level scan, not by hunting for quotable instances: they are a document-level signal,
come from discourse-structure research on AI-generated narrative, and survive even a full
phrase-level cleanup untouched. The **Applies to** column gates use by content type
(Step 0.5).

| Pattern | Description | Applies to |
|---|---|---|
| Stated-takeaway inflation | Every section closes with an explicit "this shows/proves/means" line instead of letting some points land unstated | Blog, informational content, reviews (skip for landing/CTA copy) |
| Single-track resolution | Every problem raised gets one clean, fully-resolved answer; nothing acknowledged as a limitation, trade-off, or open question | Blog, case studies, reviews (skip for pricing/landing pages) |
| Structural default to vague attribution | Systematic avoidance of naming a real source, tool, person, or number, in favour of "many businesses," "some experts," "modern brands" | All content types |
| Uniform significance weighting | Every point argued with identical rhetorical weight; no build, no genuine prioritisation of what matters most | Blog, informational content |
| Generic sensory/experiential description | Taste, scent, feel, or look described in terms that could apply to any product in the category, with no idiosyncratic, checkable detail | Review content (coffee, fragrance, watches, EDC) |
| Uniformly positive verdict | No real unevenness in a pros/cons or review judgment; cons present only as token gestures | Personal-brand reviews |

**Content-type applicability rule:** Apply each row only where its "Applies to" column covers
the content type determined in Step 0.5. If content type is ambiguous, apply only the "all
content types" row and note the ambiguity rather than guessing.

**AEO caveat:** A caveat surfaced under "Single-track resolution" should be phrased as a
clear, structured qualifier, for example "works well for X, not for Y", rather than rambling
hedging: this keeps it extractable for AEO rather than diluting the piece. Do not manufacture
a limitation, trade-off, or uneven verdict where none genuinely exists; the aim is to stop
suppressing real nuance, not to invent artificial doubt.

### DETECT mode

1. Brand check (Step 0): identify the brand, load its kit and voice module, read the Voice Lock
2. Identify language; load reference file if applicable
3. Determine content type (Step 0.5) to gate Tier 5
4. Read the whole piece once for Tier 5 discourse-level patterns
5. Scan universal patterns (this file) + language-specific patterns (reference file) for Tiers 1-4
6. Flag every Tier 1-4 instance by tier and type, with a short quote from the text; report Tier 5 findings as a short holistic note rather than per-instance quotes. Mark anything that a loaded Voice Lock protects as "protected, not a finding"
7. Give an overall assessment: how AI-saturated is it?
8. Stop, do not rewrite

### BALANCED mode

1. Brand check (Step 0): identify the brand, load its kit and voice module, read the Voice Lock
2. Identify language; load reference file if applicable
3. Determine content type (Step 0.5) to gate Tier 5
4. Read the text and identify all Tier 1-4 pattern instances (universal + language-specific), after a whole-piece read for Tier 5
5. Set aside every instance the brand kit or Voice Lock protects, and every instance covered by the blanket exemptions in Step 0
6. For remaining Tier 3 instances: classify each as "never skip" or "skip if intentional" per the table
   - For "skip if intentional" patterns: assess whether there is a plausible SEO or AEO
     reason for the structure. If yes, preserve it and note it. If no clear reason exists,
     treat it as CLEAN.
7. Draft a rewrite: apply full CLEAN logic to Tiers 1, 2, 4, 5, and "never skip" Tier 3 patterns;
   preserve protected Tier 3 structures unchanged; phrase any Tier 5 caveat as a clear,
   structured qualifier so it stays extractable for AEO (see Tier 5 AEO caveat)
8. Self-audit: same as CLEAN, including the brand-flattening check
9. Output: final rewrite + changes made + Preserved list, separating brand-protected from SEO/AEO-protected

---

### DETECT mode output
```
DETECTION REPORT
Brand: [brand name + kit loaded, or "none identified"]
Language detected: [language]
Content type: [blog/informational/review/case study/landing/pricing/ambiguous]

Tier 1 (hard removes): [count]
- [pattern type]: "[quoted text]"
...

Tier 2 (AI vocabulary): [count]
- [word]: "[context]"
...

Tier 3 (structural): [count]
- [pattern]: "[quoted text]"
...

Tier 4 (filler/transitions): [count]
- [phrase]: "[context]"
...

Tier 5 (discourse-level): [brief holistic note, e.g. "Every section ends on a stated
takeaway; no acknowledged limitation anywhere; attribution stays vague throughout ("many
businesses") with zero named specifics."]

Protected by brand voice (not findings): [list, with the rule each would otherwise have hit]

Overall: [brief verdict, e.g. "Heavily AI-saturated. Almost every paragraph has Tier 1 or 2
tells. Prioritise removing X and Y."]
```

### BALANCED mode output
1. Final rewrite (in same language as input)
2. Changes made: what was removed or rewritten, including Tier 5 structural changes
3. **Preserved:** two groups
   - Brand-protected: kept per the loaded kit or Voice Lock, naming the rule overridden
   - SEO/AEO-protected: Tier 3 structures kept intact, with brief note on rationale
4. **Unicode:** what the script removed, with counts, or "not run (chat-only text)"

When the user asks for an audit of the cleaning itself, separate what is verifiable (characters
removed, with counts) from what is editorial judgment (the rewrite) and from what is not
established (detector evasion, human authorship, watermark removal).

---

## Full self-check

- Was a brand kit checked for, and loaded if one exists, including its voice module?
- Did every protected span (code, URL, figure, name, quote) come through unchanged?
- If the text is a file or is going to be published, did the Unicode pass run after the rewrite?
- Does the rewrite still pass that brand's own quality checklist?
- Is everything held back for brand reasons listed in the Preserved section?
- Does it read naturally aloud in the target language?
- Would a native speaker say any of these phrases in a real conversation?
- Are sentence lengths varied, and sentence openings too?
- Did the cleanup replace joined sentences with strings of short ones? If so, put the joins back
- Is there a human point of view present?
- Are there any em dashes left?
- Are there any words from the Tier 2 vocabulary list (universal or language-specific) that aren't domain terms?
- Does the conclusion end when the point is made, or does it pad?
- Does the piece admit at least one real limitation or open question, where the content type allows it?
- Is there at least one specific, named, checkable detail rather than a vague plural claim?
- Do all sections land on the same explicit stated takeaway, or are some left for the reader to draw themselves?

---


---

## Reference sources

Pattern library compiled from:
- Wikipedia: Signs of AI Writing (WikiProject AI Cleanup)
- Grammarly (2025), Microsoft 365 Life Hacks (2025), GPTHuman (2025)
- Walter Writes (2025), Textero (2025), Plagiarism Today (2025), Rolling Stone (2025)
- Native-language AI writing pattern research for NL, FR, DE, ES
- Tier 5 informed by Russell et al., "StoryScope: Investigating idiosyncrasies in AI fiction"
  (arXiv:2604.03136, 2026), discourse-level narrative findings adapted from fiction to
  marketing/editorial content; fiction-only findings (plot/temporal structure) excluded as
  not applicable
