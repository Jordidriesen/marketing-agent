# CRO checklist

Loaded by `cro-auditor` once the audit starts. Work through the six areas in order. Each item is a
question about the page; a "no" or "unclear" becomes a finding only when you can name the element it
applies to. Judge against the page's one conversion goal and its traffic source.

## 1. Clarity (does a stranger understand in five seconds)

Show only the first screen (desktop and mobile) to yourself and answer in one line each:

- **What is this?** Is the product or offer named plainly, with the category a buyer would use?
- **Who is it for?** Is the audience or situation identifiable, without the reader guessing?
- **What happens next?** Does the primary action say what the visitor gets and what happens after
  they click (the demo, the quote, the download), not just "Submit" or "Learn more"?
- **Subhead test.** Does the line under the headline add the specific outcome, mechanism or proof, or
  does it restate the headline in other words?
- **Jargon.** Are terms used that the traffic source's audience would not use themselves?
- **One job.** Does the page have one primary action, with any secondary path visibly smaller?

## 2. Friction (what makes the next step harder than it needs to be)

- **Distance to the action.** How many screens or scrolls before the primary action first appears?
  Is it repeated at the points where intent peaks?
- **Competing exits.** Navigation, footer links, social icons or a second equal-weight button that
  take the visitor away from the goal.
- **Steps and fields.** Number of steps and fields compared with what is needed to qualify and
  follow up. Each field should earn its place.
- **Required-but-unexplained.** Fields, accounts or phone numbers requested without a reason given.
- **Load and stability signals.** Layout that jumps, content that appears late, heavy media above the
  fold. Report only what you saw or were told; never assume speed from the design.
- **Dead ends.** Error states, empty states and confirmation screens that leave the visitor stuck or
  without a next step.

## 3. Credibility (does the page earn the right to ask)

- **Proof fits the stage.** Proof placed where the reader's doubt peaks (next to the claim, next to
  the form), not collected in one block far from the action. See the scepticism stages in
  `content-references/references/behavioral-psychology.md`.
- **Proof is real and specific.** Named customers, quotes with a name and role, figures with a source.
  Vague superlatives ("trusted by leading companies") are a finding. Absent proof is a finding of
  its own: flag it, do not assume it exists elsewhere.
- **Headings do not over-claim.** "Trusted by" or "Customers like you" above nothing real is a
  finding; neutral headings ("Where it runs", "References") stay neutral until proof fills them.
- **Risk reversal.** Is the cost of trying it stated honestly (what it costs, how long it takes, how
  to stop)? Only reassurances the business can keep.
- **Trust basics.** Contact details, company identity, privacy line near the form, in the market's
  language.
- **Consistency.** Do the claims on the page match the ad or email that brought the visitor here?

## 4. Message match (does the page keep the promise that earned the click)

- Does the first screen repeat the promise of the ad, email or search result in the visitor's words?
- If the visitor came from a specific query or offer, is that specific thing visible without scrolling?
- Does the offer, price signal or deadline match what the source said?
- For paid search, run the deeper chain check with `landing-page-matcher` and note that you did.

## 5. Form and CTA microcopy

- **Button label.** States the outcome or action in the visitor's terms, not "Submit".
- **Field labels.** Visible labels (not only placeholders), plain words, an example where the format
  matters, optional fields marked as optional.
- **Reassurance line.** One short line near the button: what happens next, how soon, what is not
  done with the data. No claim the business cannot keep.
- **Error states.** Say what is wrong and how to fix it, next to the field, without losing what the
  visitor typed.
- **Confirmation.** Says what happens next, gives the next useful step, and fires the tracking event
  the goal depends on (flag when this cannot be checked).
- **Consent and privacy.** Present, honest and not blocking, per the market's rules. Legal wording
  stays with the business; flag only that it is missing or hard to read.

## 6. Mobile scannability

Judge the mobile view separately; most paid and social traffic arrives on it.

- Headline, one line of support and the primary action visible without scrolling?
- Tap targets and spacing usable with a thumb; forms use the right input types?
- Sections scannable: short paragraphs, clear subheads, proof not hidden inside carousels or tabs?
- Sticky or repeated primary action available on a long page?
- If the mobile view was not seen, say so: it goes on the Could not verify list, and mobile findings
  stay out of the top ranks.

## Ranking guide

Rank high when the finding sits between the visitor and the goal on the first screen or at the
action (unclear offer, buried or missing action, a form asking for far more than the goal needs,
promise broken after the click). Rank medium for proof placement, microcopy and secondary exits.
Rank low for polish. Evidence from analytics or recordings can move a finding up or down one step;
name the source when it does.
