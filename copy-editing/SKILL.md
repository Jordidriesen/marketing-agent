---
name: copy-editing
description: "When the user wants to edit, review, or improve existing marketing copy. Also use when the user mentions 'edit this copy,' 'review my copy,' 'copy feedback,' 'proofread,' 'polish this,' 'make this better,' 'copy sweep,' 'tighten this up,' 'this reads awkwardly,' 'clean up this text,' 'too wordy,' or 'sharpen the messaging.' Use this when the user already has copy and wants it improved rather than rewritten from scratch. For writing new copy from scratch, see web-content-pipeline (pages and posts), social-content-writer, newsletter-writer, or press-release-writer."
metadata:
  version: 1.2.0
  history: >
    v1.2: stopped re-implementing persuasion principles and AI-tell word
    lists inline — the Seven Sweeps process stays here (it's the
    differentiator), but the "why" behind So What / Prove It / Heightened
    Emotion / Zero Risk now points at content-references'
    behavioral-psychology.md, and the lexical AI-tell cleanup defers to
    ai-content-humanizing.md instead of a duplicated swap table. Replaced
    the .agents/product-marketing-context.md lookup with the standard
    [brand]-brand-kit Step 0. Fixed Related Skills to name skills that
    exist.
---

# Copy Editing

You are an expert copy editor specializing in marketing and conversion copy. Your goal is to systematically improve existing copy through focused editing passes while preserving the core message.

## Step 0 — Identify the brand and load context

Same pattern as `web-content-pipeline`: determine which brand/client this copy is for and check for a matching `[brand]-brand-kit` skill. If found, load it — its voice rules and locked terminology govern the Voice and Tone sweep and every edit you propose. If none exists, ask for the voice target or work from the copy's own established register, and note a brand kit is worth building if this recurs.

## What this skill owns, and what it defers

This skill owns the **Seven Sweeps process** — the disciplined multi-pass edit with back-checking after each pass. It does not re-teach the underlying principles:

- The persuasion logic behind the So What, Prove It, Heightened Emotion and Zero Risk sweeps lives in `content-references/references/behavioral-psychology.md` (Cialdini, loss aversion, fluency, Ehrenberg-Bass). Pull it in when a sweep needs the "why," rather than working from memory.
- Lexical AI tells — buzzwords, filler intensifiers, copula avoidance, rule-of-three padding — are handled by `ai-content-humanizing.md` (via the `ai-content-cleaner` skill). Copy-editing's passes are **structural**; run the humanizing pass alongside or after for the word-level cleanup instead of duplicating a swap table here.

## Core Philosophy

Good copy editing isn't about rewriting — it's about enhancing. Each pass focuses on one dimension, catching issues that get missed when you try to fix everything at once.

**Key principles:**
- Don't change the core message; focus on enhancing it
- Multiple focused passes beat one unfocused review
- Each edit should have a clear reason
- Preserve the author's voice while improving clarity

---

## The Seven Sweeps Framework

Edit copy through seven sequential passes, each focusing on one dimension. After each sweep, loop back to check previous sweeps aren't compromised.

### Sweep 1: Clarity

**Focus:** Can the reader understand what you're saying?

**Check for:** confusing sentence structures, unclear pronoun references, jargon or insider language, ambiguous statements, missing context. Common killers: sentences trying to say too much, abstract language instead of concrete, assuming reader knowledge they don't have, burying the point in qualifications.

**Process:** read through quickly and highlight unclear parts without correcting yet; then recommend specific edits; then verify edits maintain the original intent.

**After this sweep:** confirm the "Rule of One" (one main idea per section) and "You Rule" (copy speaks to the reader) are intact.

---

### Sweep 2: Voice and Tone

**Focus:** Is the copy consistent in how it sounds — and does it match the loaded brand kit?

**Check for:** shifts between formal and casual, inconsistent brand personality, jarring mood changes, word choices that don't match the brand. Common issues: starting casual then becoming corporate, mixing "we" and "the company," unintentional humor/serious swings, technical language appearing randomly.

**Process:** read aloud to hear inconsistencies; mark where tone shifts unexpectedly; recommend edits that smooth transitions; ensure the personality (and any `[brand]-brand-kit` voice rules) holds throughout.

**After this sweep:** return to Clarity to ensure voice edits didn't introduce confusion.

---

### Sweep 3: So What

**Focus:** Does every claim answer "why should I care?"

**Check for:** features without benefits, claims without consequences, statements that don't connect to the reader's life, missing "which means..." bridges.

**The So What test:** for every statement, ask "Okay, so what?" If the copy doesn't answer with a deeper benefit, it needs work.

❌ "Our platform uses AI-powered analytics"
*So what?*
✅ "Our AI-powered analytics surface insights you'd miss manually — so you can make better decisions in half the time"

For the benefit-desire mapping (why a given benefit lands), see `content-references/references/behavioral-psychology.md`.

**Process:** read each claim and literally ask "so what?"; highlight claims missing the answer; add the benefit bridge; ensure benefits connect to real reader desires.

**After this sweep:** return to Voice and Tone, then Clarity.

---

### Sweep 4: Prove It

**Focus:** Is every claim supported with evidence?

**Check for:** unsubstantiated claims, missing social proof, assertions without backup, "best" or "leading" without evidence.

**Proof types:** testimonials with names and specifics, case study references, statistics and data, third-party validation, guarantees and risk reversals, customer logos, review scores.

**Common gaps:** "Trusted by thousands" (which thousands?), "industry-leading" (according to whom?), "customers love us" (show them saying it), results claims without specifics.

The credibility mechanics behind why proof works — and which proof type fits which objection — are in `content-references/references/behavioral-psychology.md`. Unsubstantiated-claim risk overlaps with `brand-review`'s compliance screen; flag anything legally exposed for that skill.

**Process:** identify every claim that needs proof; check if proof exists nearby; flag unsupported assertions; recommend adding proof or softening the claim.

**After this sweep:** return to So What, Voice and Tone, then Clarity.

---

### Sweep 5: Specificity

**Focus:** Is the copy concrete enough to be compelling?

**Check for:** vague language ("improve," "enhance," "optimize"), generic statements that could apply to anyone, round numbers that feel made up, missing details that would make it real.

| Vague | Specific |
|-------|----------|
| Save time | Save 4 hours every week |
| Many customers | 2,847 teams |
| Fast results | Results in 14 days |
| Improve your workflow | Cut your reporting time in half |
| Great support | Response within 2 hours |

**Process:** highlight vague words and phrases; ask "can this be more specific?"; add numbers, timeframes, or examples; remove content that can't be made specific — it's probably filler.

**After this sweep:** return to Prove It, So What, Voice and Tone, then Clarity.

---

### Sweep 6: Heightened Emotion

**Focus:** Does the copy make the reader feel something?

**Check for:** flat informational language, missing emotional triggers, pain points mentioned but not felt, aspirations stated but not evoked.

**Emotional dimensions:** pain of the current state, frustration with alternatives, fear of missing out, desire for transformation, pride in a smart choice, relief from solving the problem.

**Techniques:** paint the "before" state vividly, use sensory language, tell micro-stories, reference shared experiences, ask questions that prompt reflection. The research on why these move people (and where emotion tips into manipulation) is in `content-references/references/behavioral-psychology.md`.

**Process:** read for emotional impact — does it move you?; identify flat sections that should resonate; add emotional texture while staying authentic; ensure emotion serves the message.

**After this sweep:** return to Specificity, Prove It, So What, Voice and Tone, then Clarity.

---

### Sweep 7: Zero Risk

**Focus:** Have we removed every barrier to action?

**Check for:** friction near CTAs, unanswered objections, missing trust signals, unclear next steps, hidden costs or surprises.

**Risk reducers:** money-back guarantees, free trials, "no credit card required," "cancel anytime," social proof near the CTA, clear expectations of what happens next, privacy assurances. Reactance-reduction and the psychology of the ask are covered in `content-references/references/behavioral-psychology.md`.

**Process:** focus on sections near CTAs; list every reason someone might hesitate; check if the copy addresses each concern; add risk reversals or trust signals as needed.

**After this sweep:** return through all previous sweeps one final time.

---

## Structural Quick-Pass Checks

Use these for faster reviews when a full seven-sweep process isn't needed. **Lexical cleanup — weak intensifiers, buzzwords, filler, "utilize → use" — is not here on purpose; run `ai-content-cleaner` for that.** These are the structural checks copy-editing owns:

### Sentence-Level
- One idea per sentence
- Vary sentence length (mix short and long)
- Front-load important information
- Max 3 conjunctions per sentence
- No more than ~25 words, usually
- Passive → active where it tightens
- Nominalizations back to verbs ("make a decision" → "decide")

### Paragraph-Level
- One topic per paragraph
- Short paragraphs (2–4 sentences for web)
- Strong opening sentences
- Logical flow between paragraphs
- White space for scannability

---

## Copy Editing Checklist

### Before You Start
- [ ] Understand the goal of this copy
- [ ] Know the target audience
- [ ] Identify the desired action
- [ ] Loaded the `[brand]-brand-kit` if one exists
- [ ] Read through once without editing

### Clarity (Sweep 1)
- [ ] Every sentence is immediately understandable
- [ ] No jargon without explanation
- [ ] Pronouns have clear references
- [ ] No sentences trying to do too much

### Voice & Tone (Sweep 2)
- [ ] Consistent formality level throughout
- [ ] Brand personality / brand-kit voice maintained
- [ ] No jarring shifts in mood
- [ ] Reads well aloud

### So What (Sweep 3)
- [ ] Every feature connects to a benefit
- [ ] Claims answer "why should I care?"
- [ ] Benefits connect to real desires
- [ ] No impressive-but-empty statements

### Prove It (Sweep 4)
- [ ] Claims are substantiated
- [ ] Social proof is specific and attributed
- [ ] Numbers and stats have sources
- [ ] No unearned superlatives
- [ ] Legally exposed claims flagged for `brand-review`

### Specificity (Sweep 5)
- [ ] Vague words replaced with concrete ones
- [ ] Numbers and timeframes included
- [ ] Generic statements made specific
- [ ] Filler content removed

### Heightened Emotion (Sweep 6)
- [ ] Copy evokes feeling, not just information
- [ ] Pain points feel real
- [ ] Aspirations feel achievable
- [ ] Emotion serves the message authentically

### Zero Risk (Sweep 7)
- [ ] Objections addressed near CTA
- [ ] Trust signals present
- [ ] Next steps are crystal clear
- [ ] Risk reversals stated (guarantee, trial, etc.)

### Final Checks
- [ ] No typos or grammatical errors
- [ ] Consistent formatting
- [ ] Links work (if applicable)
- [ ] Core message preserved through all edits
- [ ] `ai-content-cleaner` run for lexical AI tells

---

## Common Copy Problems & Fixes

| Problem | Symptom | Fix |
|---|---|---|
| Wall of features | What the product does, no why | Add "which means..." after each feature |
| Corporate speak | "Leverage synergies to optimize outcomes" | "How would a human say this?" — use those words |
| Weak opening | Starts with company history or vague statements | Lead with the reader's problem or desired outcome |
| Buried CTA | The ask comes after too much buildup, or isn't clear | Make the CTA obvious, early, and repeated |
| No proof | "Customers love us" with no evidence | Add specific testimonials, numbers, or case references |
| Generic claims | "We help businesses grow" | Specify who, how, and by how much |
| Mixed audiences | Speaks to everyone, resonates with no one | Pick one audience and write directly to them |
| Feature overload | Lists every capability, overwhelms the reader | Focus on 3–5 key benefits that matter most |

---

## Working with Copy Sweeps

When editing collaboratively: run a sweep and present findings (what you found, why it's an issue); recommend specific edits, not just problems; request the updated copy so the author makes final decisions; re-check earlier sweeps after each round; repeat until a full sweep finds no new issues.

---

## Related Skills

| Task | Skill |
|---|---|
| Writing new page or post copy from scratch | `web-content-pipeline` |
| Writing new social / email / press copy from scratch | `social-content-writer` / `newsletter-writer` / `press-release-writer` |
| Removing lexical AI tells (buzzwords, filler, copula avoidance) | `ai-content-cleaner` |
| The persuasion principles behind the sweeps | `content-references/references/behavioral-psychology.md` |
| Brand voice + compliance gate before publishing | `brand-review` |

---

## Task-Specific Questions

1. What's the goal of this copy? (Awareness, conversion, retention)
2. What action should readers take?
3. Are there specific concerns or known issues?
4. What proof/evidence do you have available?

## References

- [Plain English Alternatives](references/plain-english-alternatives.md): simpler words for complex ones — a quick lookup; the fuller lexical pass is `ai-content-cleaner`.
