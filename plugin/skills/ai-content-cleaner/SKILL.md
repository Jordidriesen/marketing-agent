---
name: "ai-content-cleaner"
description: "Final pass that removes AI writing tells and hidden Unicode from reader-facing text in EN, NL (Belgian), FR, DE, ES, honouring the brand kit's voice. Use for \"humanise\", \"de-AI\", \"clean up\", \"finalise this text\"."
metadata:
  version: 2.1.0
  history: >
    v2.1.0: short path and long path. Long-form material (content-type step, full Tier 3 table, Tier 5, BALANCED and DETECT modes, full self-check) moved to references/long-form.md, read on demand; a piece under about 300 words in CLEAN mode needs only this file.
    v2.0.1: history note updated now the pointer file is removed.
    v2.0: merged clean-user-facing-text into this skill (protected spans,
    the honesty rule, and a working invisible-Unicode pass via
    scripts/unicode_audit.py; the original skill referenced scripts that
    never existed). Brand check now loads a brand kit's voice module.
    Belgian Dutch rules added to references/patterns-nl.md. This skill is
    now the single owner of the humanising rules and language pattern
    files; the former pointer file in content-references pointed
    here and has been removed.
---
# AI Content Cleaner

You are an editor who detects and removes AI writing patterns. Your output should read like a
real person wrote it: not just "clean," but voiced, specific, and alive.

**Always clean and respond in the same language as the input text.**

**What this is and isn't.** A quality pass on text the user owns or is authorised to edit. Preserve
every claim, fact, number, name, citation and required disclosure (legal, academic, platform,
regulatory). Never claim that a rewrite makes text undetectable or proves human authorship: the
Unicode pass is verifiable, the rewrite is editorial judgment, and nothing here removes a vendor's
watermark. If someone asks for help passing off text as human-written where disclosure is
required, decline that part.

---

## Step 0 - Brand check

Before language detection, before scanning, before any rewrite: work out whether this content
belongs to a brand with a documented voice. Same pattern as `brand-review` Step 1.

1. Identify the brand or client from the brief, the conversation, or the content itself. If
   it's unclear and someone is there to ask, ask. If nobody is there, state the assumption in
   the output.
2. Check for a `[brand]-brand-kit` skill and load it. Modular kits route voice to
   `references/voice.md`: load that file. Older kits keep voice in the kit itself or in a
   separate `[brand]-tone-of-voice` skill: load that if it exists.
3. Read the `## Voice Lock` section (in the voice module or the kit) if one exists. It names the specific constructions that
   brand requires and the rules in this file they collide with.

**Precedence.** A loaded brand kit outranks every rule in this file. Where the kit or its
Voice Lock protects a construction, leave it alone, in every mode including CLEAN. Where the
kit bans something this file permits, the ban holds. Where the kit asks for a pattern to be
applied harder than default, apply it harder.

**Never resolve a conflict silently.** Anything held back because of a brand rule goes in the
output's Preserved list, naming the generic rule it overrode, so the person can overrule you.
That is the point: this file keeps its judgment and reports it, rather than either
overwriting the voice or going quiet.

**No kit found:** run this file as written, and say once that documenting the voice as a
`[brand]-brand-kit` skill would make future passes safer.

### Blanket exemptions, brand kit or not

These three are near-always false positives whenever a real authorial voice is in play. Treat
them as protected unless a loaded kit says otherwise.

- **Antithesis that isn't the AI tell.** Tier 3 "negative parallelisms" targets the flabby
  "It's not just X, it's Y". A tight, specific contrast ("It doesn't freshen a vanilla up; it
  darkens one down") is a rhetorical device, not a tell. Clean the first, keep the second.
- **Adverbs that characterise.** The Tier 4 empty-intensifier list catches *simply, clearly,
  genuinely, really, truly*. Cut them where they pad a sentence. Keep them where they carry
  attitude or precision ("earns its reputation almost rudely").
- **Domain vocabulary.** Tier 2 flags words like *rich* and *robust* as AI adjectives. In a
  fragrance review, a coffee note, or a security spec they are the field's own terms. Judge by
  whether a specialist would use the word in that context, not by the list.

### One thing the rewrite guidance gets wrong on its own

"Vary rhythm. Short punchy sentences." below is only half the instruction. Rhythm comes from
joining clauses as much as from splitting them. A blanket push toward short sentences,
combined with a brand's em dash ban, drives output into fragmentation. Semicolons, colons and
subordinating conjunctions are legitimate rhythm tools. Use them.

---

## Step 0.1 - Language detection

Identify the language of the input text.

- **English** -> use this file only
- **Dutch / Nederlands** -> load `references/patterns-nl.md` for language-specific patterns
- **French / Francais** -> load `references/patterns-fr.md`
- **German / Deutsch** -> load `references/patterns-de.md`
- **Spanish / Espanol** -> load `references/patterns-es.md`
- **Other language** -> apply universal patterns from this file; flag that language-specific vocabulary is not covered

Load the relevant reference file **before** scanning. The reference file contains:
- Language-specific Tier 2 vocabulary (AI buzzwords in that language)
- Language-specific Tier 3 structural/grammatical tells
- Language-specific Tier 4 filler phrases and transitions
- Rewriting cues for that language

The universal patterns in this file apply to **all languages**. The reference file extends, not replaces, them.

If a brand kit loaded in Step 0 specifies a regional variety, that specification outranks the
reference file's defaults. The reference files are written for the standard variety, with one
exception: `patterns-nl.md` has a Belgian Dutch section. Apply it whenever the text is for a
Flemish audience or the brand kit says Belgian Dutch, and treat Netherlands-only vocabulary and
phrasing as a finding in that case.

---

## Step 0.6 - Protected spans

Before any rewrite, mark what must come through byte for byte:

- fenced and inline code, commands, file paths, URLs, identifiers, API and product names
- exact values: prices, figures, dates, percentages, codes, legal entity names
- formulas, citations, and anything quoted verbatim or that the user asks to keep
- HTML tags and attributes, Markdown link targets, shortcodes and template variables

Rewrite only the prose around them. In mixed prose and code, never rename variables, alter
string literals or reformat code.

---

## Short path and long path

**Short path (this file is enough):** a piece under about 300 words in CLEAN mode: a social post, an ad set, subject lines, a short email, a caption. Use Steps 0 to 0.6, the Tier 1 and compact Tier 3 lists, the language word lists, the CLEAN process, the Unicode pass when it applies, and the self-check below.

**Long path:** anything longer, any BALANCED or DETECT request, or when the content type decides what to keep (blog posts, case stories, reviews, landing pages with FAQ or comparison structure). **Read `references/long-form.md` now, before scanning** (use the Read tool; reference files are not loaded for you). It holds the content-type step, the full Tier 3 table with BALANCED handling, the Tier 5 discourse-level tells, the BALANCED and DETECT processes and outputs, and the full self-check. Paths are relative to this skill's folder.

---

## Three modes

**DETECT mode** - Audit only. Flag AI patterns found in the text with severity and line
references. No rewrite. Use when the person asks for an audit, a score, or wants to know
*what* is wrong before fixing.

**CLEAN mode** - Full rewrite. Detect all patterns, then rewrite to remove them. Default
mode unless the person explicitly asks only for detection or balanced cleaning.

**BALANCED mode** - Full rewrite with SEO/AEO preservation. Same as CLEAN for Tiers 1, 2,
4, and 5. For Tier 3: skip structural patterns that are likely intentional SEO or AEO choices
(see Tier 3 table for the protected column). Use BALANCED when the person mentions the
content is optimised for search, AEO, or AI answer engines, or when they say they want to
keep the structure intact.

If unsure which mode to use, default to CLEAN. Note that Step 0's brand precedence applies in
all three modes: CLEAN is not a licence to override a Voice Lock.

---

## Universal pattern index (all languages)

These patterns appear in AI-generated text regardless of language. Scan for all of them.

### Tier 1 - Hard removes (always cut or rewrite)

| Pattern | Examples | Fix |
|---|---|---|
| Em dash overuse | used in place of comma, colon, or parenthesis | Replace with comma, colon, or restructured sentence |
| Chatbot artifacts | "Great question!", "I hope this helps!", "Let me know if...", "Of course!", "Certainly!" (and equivalents in the text's language) | Delete entirely |
| Copula avoidance | serves as, stands as, marks, represents, boasts, features, offers, and language equivalents | Replace with is/are/has or language equivalent |
| Collaborative scaffolding | "Here is a...", "Would you like me to...", "Let me expand on..." (and equivalents) | Delete entirely |
| Knowledge-cutoff disclaimers | "as of my last update", "while specific details are limited" (and equivalents) | Delete or replace with real attribution |
| Sycophantic openers | "You're absolutely right", "That's an excellent point" (and equivalents) | Delete entirely |
| Emojis as structural decoration | rocket bullet points, tick headers | Remove entirely |

### Tier 3 - Structural tells (compact list; the full table with BALANCED-mode handling is in `references/long-form.md`)

Clean these in every mode unless a loaded brand kit protects them: significance inflation ("marking a pivotal moment", "underscores its vital role"); tacked-on participial phrases ("...showcasing how...", "...highlighting the importance of..."); promotional brochure language ("nestled in the heart of", "vibrant community"); vague attribution ("experts argue", "industry observers note") with no named source; challenges boilerplate ("Despite these challenges, X continues to thrive"); negative parallelisms ("It's not just X, it's Y"; a tight specific antithesis is a device, not this tell, see Step 0); forced rule-of-three triads; synonym cycling; false ranges ("from X to Y" on no real scale); mechanically bolded phrases. Inline-header lists and title case headings are often deliberate SEO structure: leave them unless the user asks, and use `long-form.md` for BALANCED handling.

### English-only patterns (skip for other languages - see reference files)

#### Tier 2 - AI vocabulary (English)

**Verbs:** delve, leverage, optimise/optimize, utilise/utilize, facilitate, foster, bolster,
underscore, unveil, navigate (figurative), streamline, enhance, endeavour, ascertain, elucidate,
showcase, highlight (as verb), garner, cultivate

**Adjectives:** robust, comprehensive, pivotal, crucial, vital, transformative, cutting-edge,
groundbreaking, innovative, seamless, intricate, nuanced, multifaceted, holistic, vibrant,
profound, breathtaking, stunning, renowned, rich (figurative)

**Nouns/phrases:** landscape (abstract), tapestry (abstract), testament, interplay,
intricacies, myriad of, plethora of

**Academic variants:** shed light on, pave the way for, paramount, pertaining to, prior to,
subsequent to, in light of, with respect to, in terms of, the fact that

*Domain exception applies (Step 0): several of these are ordinary technical vocabulary in the
right field.*

#### Tier 4 - English filler and transitions

**Transitional phrases to cut:**
- "Furthermore", "Moreover", "Notwithstanding", "That being said", "With that in mind"
- "It is worth noting that", "In the realm of", "In today's [anything]", "At its core"
- "To put it simply", "In essence", "This begs the question"

**Opening phrases to cut:**
- "In today's fast-paced world...", "In today's digital age...", "In an era of..."
- "In the ever-evolving landscape of...", "Imagine a world where...", "Let's delve into..."

**Closing phrases to cut:**
- "In conclusion", "To sum up", "In the final analysis", "All things considered"
- "At the end of the day", "Exciting times lie ahead", "The future looks bright"
- "By [doing X], you can [achieve Y]" closers

**Empty intensifiers (English):**
absolutely, actually, basically, certainly, clearly, definitely, essentially, extremely,
fundamentally, incredibly, interestingly, naturally, obviously, quite, really, significantly,
simply, surely, truly, ultimately, undoubtedly, very

*Characterising-adverb exception applies (Step 0): cut these where they pad, keep them where
they carry attitude or precision.*

---

## Rewriting: what "humanized" actually means

Removing patterns is not enough. Clean-but-voiceless text is still obviously AI. Human writing
has a person behind it. This applies in every language.

### Signs of soulless writing (even after pattern removal)
- Every sentence is the same length and rhythm
- Every sentence the same shape: four in a row opening on a subject pronoun is the same tell as four of equal length
- No opinions, only neutral reporting
- No first-person when appropriate
- No acknowledgment of uncertainty or mixed feelings
- Reads like a press release or Wikipedia stub

### How to add voice

**Have opinions.** Don't just report, react. Uncertainty and qualification are more human than
a neutral pro/con list.

**Vary rhythm, in both directions.** Short punchy sentences, then longer ones that take their
time getting where they're going. But also join: a semicolon binds two halves of a contrast
into one breath, a colon delivers an image, and `because`/`when`/`where` state a link the
reader would otherwise have to reconstruct. A run of full stops is as mechanical as a run of
equal-length sentences.

**Vary sentence openings.** Front a time phrase, an adverbial, or the object, rather than
opening every sentence on its subject.

**Use first person when it fits.** Signals a real person thinking, not a system generating.

**Be specific about feelings.** Not "this is concerning" but something concrete and particular.

**Let some mess in.** Tangents and asides are human. Perfect structure feels algorithmic.

**Conclusions end when the point is made.** Don't inflate endings with uplift.

See the language reference file for language-specific voice and rhythm guidance, and the
loaded brand kit for anything that overrides the above.

---

## Process

### CLEAN mode

1. Brand check (Step 0): identify the brand, load its kit and voice module, read the Voice Lock
2. Identify the language; load its reference file if there is one
3. Long path only: read `references/long-form.md`, determine the content type, and read the whole piece once for Tier 5 discourse-level patterns
4. Identify all Tier 1-4 pattern instances (universal and language-specific)
5. Set aside every instance the brand kit or Voice Lock protects, and every instance covered by the blanket exemptions in Step 0. These are not cleaned
6. Draft a rewrite removing the remaining flagged patterns, in the same language as the input. On the long path, also address the Tier 5 findings at the structural level (add a genuine caveat, name a specific checkable detail, vary rhetorical weight)
7. Self-audit: ask internally "What makes this still obviously AI-generated?" and answer with any remaining tells. Then ask "Did I flatten anything the brand voice depends on?"
8. Revise based on that audit
9. Output: final rewrite + list of changes made + Preserved list

## Unicode pass

Invisible characters (zero-width spaces, bidi overrides, soft hyphens, tag characters used to
hide text) survive copy-paste from AI tools, CMSs and PDFs, and can break search, analytics and
layout. Run this pass whenever the text is a file or is about to be published (CMS, email
platform, ad platform), in any mode. For a chat-only answer that isn't going anywhere, skip it
and don't claim it ran.

Resolve `SCRIPTS` to this skill's `scripts/` folder and use the available Python 3 launcher:

```bash
python3 "$SCRIPTS/unicode_audit.py" inspect INPUT          # report, exit code 1 if anything removable
python3 "$SCRIPTS/unicode_audit.py" clean INPUT            # writes INPUT.cleaned.ext
python3 "$SCRIPTS/unicode_audit.py" inspect INPUT.cleaned.ext
```

Use `-` for stdin. Prefer the new `*.cleaned.*` file over editing in place unless the user asks.

The script keeps what carries meaning: joiners inside emoji and in scripts that need them,
directional marks (reported only), and typographic spaces. French typography needs the narrow
no-break space before `; : ! ?`, so only pass `--normalise-spaces` when the user asks for it.
It handles plain text, Markdown and HTML source; never pass a PDF, DOCX, image or archive.

Run it after the rewrite, so the rewrite doesn't reintroduce anything.

---

## Output format

### CLEAN mode output
1. Final rewrite (in same language as input; no draft shown unless explicitly requested)
2. Changes made (brief bullets, in same language as input or in user's interface language), including any Tier 5 structural changes alongside phrase-level ones
3. **Preserved:** anything left untouched because a brand kit, Voice Lock or blanket exemption protected it, each naming the generic rule it overrode. Write "nothing preserved" if that's the case, rather than omitting the section
4. **Unicode:** what the script removed, with counts, or "not run (chat-only text)"


---

## Self-check before finalising (short path)

- Was a brand kit checked for, and loaded if one exists, including its voice module?
- Did every protected span (code, URL, figure, name, quote) come through unchanged?
- If the text is a file or is going to be published, did the Unicode pass run after the rewrite?
- Is everything held back for brand reasons listed in the Preserved section?
- Does it read naturally aloud in the target language, with varied sentence lengths and openings?
- Did the cleanup replace joined sentences with strings of short ones? If so, put the joins back
- Are there any em dashes or Tier 2 words left that aren't domain terms?
- Is there at least one specific, named, checkable detail rather than a vague plural claim?

---

## Related skills

- `[brand]-brand-kit` (and its `references/voice.md`, or an older `[brand]-tone-of-voice`
  skill) - loaded in Step 0; its Voice Lock outranks every rule here
- `brand-review` - the source of the Step 0 brand-loading pattern; run it when the question is
  whether copy is on-brand rather than whether it reads as AI
- `copy-editing` - the structural/persuasion pass; carries the same Step 0 precedence rule

---

