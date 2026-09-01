# AI Content Humanizing Reference

Detect and remove AI writing patterns so text reads as if a real person
wrote it — not just "clean," but voiced, specific, and alive. Applicable
to any content type: blog posts, landing pages, email copy, social posts,
customer stories, personal blog reviews.

**Always clean and respond in the same language as the input text.**

Part of the `content-references` shared library. Also directly invocable
as the standalone `ai-content-cleaner` skill for one-off cleaning requests
that aren't part of a larger generation pipeline.

---

## Step 0 — Language detection

Identify the language of the input text before anything else.

- **English** → this file only
- **Dutch/Nederlands** → also load `ai-humanizing-patterns-nl.md`
- **French/Français** → also load `ai-humanizing-patterns-fr.md`
- **German/Deutsch** → also load `ai-humanizing-patterns-de.md`
- **Spanish/Español** → also load `ai-humanizing-patterns-es.md`
- **Other language** → apply universal patterns from this file; flag that
  language-specific vocabulary isn't covered

Load the relevant file **before** scanning. It extends, not replaces, the
universal patterns below — language-specific Tier 2 vocabulary, Tier 3
structural tells, Tier 4 filler, and rewriting cues for that language.

---

## Three modes

**DETECT mode** — Audit only. Flag patterns with severity and line
references, no rewrite. Use for an audit, a score, or when the person
wants to know *what's* wrong before fixing it.

**CLEAN mode** — Full rewrite. Detect all patterns, then rewrite to remove
them. Default mode unless the person explicitly asks for detection-only or
balanced cleaning.

**BALANCED mode** — Full rewrite with SEO/AEO preservation. Same as CLEAN
for Tiers 1, 2, and 4. For Tier 3: skip structural patterns that are
likely intentional SEO or AEO choices (see the Tier 3 table's protected
column). **Use this mode whenever the content came through the SEO/AEO
reference or another AEO-structured pipeline** — otherwise an aggressive
CLEAN pass strips exactly the structure that pipeline built in.

If unsure which mode fits, default to CLEAN.

---

## Universal pattern index (all languages)

### Tier 1 — Hard removes (always cut or rewrite)

| Pattern | Examples | Fix |
|---|---|---|
| Em dash overuse | used in place of comma, colon, or parenthesis | Replace with comma, colon, or restructured sentence |
| Chatbot artifacts | "Great question!", "I hope this helps!", "Let me know if...", "Of course!", "Certainly!" | Delete entirely |
| Copula avoidance | serves as, stands as, marks, represents, boasts, features, offers | Replace with is/are/has |
| Collaborative scaffolding | "Here is a...", "Would you like me to...", "Let me expand on..." | Delete entirely |
| Knowledge-cutoff disclaimers | "as of my last update", "while specific details are limited" | Delete or replace with real attribution |
| Sycophantic openers | "You're absolutely right", "That's an excellent point" | Delete entirely |
| Emojis as structural decoration | 🚀 bullet points, ✅ headers | Remove entirely |

### Tier 3 — Structural tells (language-neutral)

BALANCED mode column: **Never skip** = clean regardless of mode, no
SEO/AEO justification exists. **Skip if intentional** = preserve if a
plausible SEO/AEO reason exists for the structure.

| Pattern | Description | BALANCED mode |
|---|---|---|
| Significance inflation | "marking a pivotal moment", "underscores its vital role", "reflects broader trends" | Never skip |
| Superficial -ing / participial phrases | "...showcasing how...", "...highlighting the importance of..." | Never skip |
| Promotional language | "nestled in the heart of", "vibrant community", "rich cultural heritage" | Never skip |
| Vague attribution | "Experts argue", "Industry observers note", "Some critics suggest" with no named source | Never skip |
| Challenges boilerplate | "Despite challenges typical of...", "Despite these challenges, X continues to thrive" | Never skip |
| Negative parallelisms | "It's not just X, it's Y", "Not merely A, but B" | Never skip |
| Rule of three | Forced triads: "innovation, inspiration, and industry insights" | Skip if intentional — FAQ lists and feature triads are valid AEO structure |
| Synonym cycling | protagonist/main character/central figure/hero | Never skip — hurts readability and semantic clarity |
| False ranges | "From X to Y" where X and Y aren't on a real scale | Never skip |
| Inline-header lists | Bullet points with **bolded header:** then explanation | Skip if intentional — standard AEO/featured-snippet format |
| Title case headings | Heading capitalisation (English) | Skip if intentional — editorial/SEO style choice |
| Overuse of boldface | Mechanically bolded phrases throughout body | Skip if intentional — keyword bolding and AEO anchor phrases are deliberate; flag only if there's no apparent logic |

**BALANCED mode judgment rule:** when a structural pattern could plausibly
be intentional SEO/AEO, preserve it unless explicitly asked to remove it.
When in doubt, flag it in the changes list as "preserved — possible
SEO/AEO intent" so the person can decide.

### English-only patterns

**Tier 2 — AI vocabulary:**
delve, leverage, optimise/optimize, utilise/utilize, facilitate, foster,
bolster, underscore, unveil, navigate (figurative), streamline, enhance,
endeavour, ascertain, elucidate, showcase, highlight (as verb), garner,
cultivate; robust, comprehensive, pivotal, crucial, vital, transformative,
cutting-edge, groundbreaking, innovative, seamless, intricate, nuanced,
multifaceted, holistic, vibrant, profound, breathtaking, stunning,
renowned, rich (figurative); landscape (abstract), tapestry (abstract),
testament, interplay, intricacies, myriad of, plethora of; shed light on,
pave the way for, paramount, pertaining to, prior to, subsequent to, in
light of, with respect to, in terms of, the fact that

**Tier 4 — Filler and transitions:**
"Furthermore", "Moreover", "Notwithstanding", "That being said", "It is
worth noting that", "In the realm of", "In today's [anything]", "To put it
simply", "In essence", "This begs the question"; opening phrases like "In
today's fast-paced world...", "Imagine a world where...", "Let's delve
into..."; closing phrases like "In conclusion", "At the end of the day",
"Exciting times lie ahead", "The future looks bright", "By [doing X], you
can [achieve Y]" closers; empty intensifiers: absolutely, actually,
basically, certainly, clearly, definitely, essentially, extremely,
fundamentally, incredibly, interestingly, naturally, obviously, quite,
really, significantly, simply, surely, truly, ultimately, undoubtedly, very

---

## Rewriting: what "humanized" actually means

Removing patterns is half the job. Clean-but-voiceless text is still
obviously AI. Human writing has a person behind it.

**Signs of soulless writing (even after pattern removal):**
- Every sentence the same length and rhythm
- No opinions, only neutral reporting
- No first-person when appropriate
- No acknowledgment of uncertainty or mixed feelings
- Reads like a press release or Wikipedia stub

**How to add voice:**
- **Have opinions.** React to facts, don't just report them.
- **Vary rhythm.** Short punchy sentences. Then longer ones that take
  their time getting where they're going.
- **Use first person when it fits.** Signals a real person thinking.
- **Be specific about feelings.** Not "this is concerning" but something
  concrete and particular.
- **Let some mess in.** Tangents and asides are human; perfect structure
  feels algorithmic.
- **Conclusions end when the point is made.** Don't inflate endings with
  uplift.
- **Consider one honest, small admitted flaw or limitation**, once
  competence is already established, rather than hedging throughout. See
  `behavioral-psychology.md` on the pratfall effect — this is a
  persuasion principle as much as a voice one.

---

## Process

**DETECT mode:** identify language → load reference file if applicable →
scan universal + language-specific patterns → flag every instance by tier
and type with a short quote → give an overall saturation assessment → stop,
no rewrite.

**CLEAN mode:** identify language → load reference file → identify all
pattern instances → draft a rewrite removing all flagged patterns → self-
audit ("what makes this still obviously AI-generated?") → revise → output
final rewrite + brief change list.

**BALANCED mode:** same as CLEAN, but for Tier 3 classify each instance as
"never skip" or "skip if intentional" per the table; for "skip if
intentional," assess whether a plausible SEO/AEO reason exists — preserve
and note it if so, otherwise treat as CLEAN. Output: final rewrite + a
Cleaned/Preserved breakdown, with preserved structures' SEO/AEO rationale
called out.

---

## Self-check before finalizing

- Does it read naturally aloud in the target language?
- Would a native speaker say any of these phrases in real conversation?
- Are sentence lengths varied?
- Is there a human point of view present?
- Any em dashes left?
- Any Tier 2 vocabulary (universal or language-specific) left?
- Does the conclusion end when the point is made, or does it pad?

---

## Reference sources

Pattern library compiled from: Wikipedia's Signs of AI Writing
(WikiProject AI Cleanup); Grammarly, Microsoft 365 Life Hacks, GPTHuman
(2025); Walter Writes, Textero, Plagiarism Today, Rolling Stone (2025);
native-language AI writing pattern research for NL, FR, DE, ES.
