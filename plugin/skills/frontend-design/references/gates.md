# Gates

How findings bind in `frontend-design`. Used by build, redesign and review. Adapted from
Nutlope's [Hallmark](https://github.com/Nutlope/hallmark) (MIT): the tiers, the waiver rule and
the gates for the fake send, the stock close, the accented word, the echo, the thin section, the
crowded head, the photo wall and the layout robustness rules. Everything else points to where
this skill already holds the rule.

The brand kit outranks Reflex and Finish gates. A rule the kit decides (for example uppercase
labels) is recorded as "kit" and is not a finding. The kit never overrides the Floor.

## Tiers

- **Floor.** Never ships, never waived. Correctness, access, honesty.
- **Reflex.** A default that generated pages fall into. Fix it, or waive it with a real reason.
- **Finish.** Craft detail. Answer it (fixed, or one line on why not). Never blocks.

## Waivers

Record each in the handover, one line:
`Waived: <gate> | <evidence the guard holds> | <reason specific to this page>`
A Floor gate cannot be waived. A reason under about 24 characters, or reused word for word, is
rejected. Waiving the same Reflex gate on three builds for one client means it is a house style:
move it into that client's brand kit `design.md`.

## Floor

- Contrast 4.5:1 body, 3:1 large text, icons, field edges and focus rings
  (`interface-checklist.md`).
- Visible `:focus-visible` on every interactive element, appearing instantly.
- Every animation has a `prefers-reduced-motion` fallback; content is visible with scripting off.
- No invented metric, testimonial, logo wall, customer or case-study count (`taste.md` section 7).
- The fake send: a form or control that prints success ("Sent", "Thanks", "You're on the list")
  with no request behind it. Until the endpoint exists the form validates, posts nowhere, and
  says so plainly.
- No horizontal scroll at any width from 320 to 1920. `overflow-x: clip` on `html` and `body`;
  no `100vw` widths.
- Image-bearing grid tracks use `minmax(0, 1fr)`; display heads carry
  `overflow-wrap: break-word; min-width: 0`.
- The hero's headline, one sentence and primary action are visible at 1280 x 800 without
  scrolling.
- At 1920 x 1080 the container is capped and centred (1360 to 1520px): gutters grow, grids and
  measure do not.
- Text painted under another element (a sticky bar, a card or an image covers a line of it).
- A button label or primary nav link wrapping at any width.
- No card inside a card, no emoji as an icon, no hand-drawn browser bar or OS window, no
  purple-to-blue gradient (`taste.md` section 3).
- On new builds, no colour or `font-family` literal outside the token block.
- A dropdown, tooltip or popover clipped by its container's `overflow`.

## Reflex

- The eyebrow, and tracked-capital or small-caps labels (`taste.md` section 5 rations eyebrows;
  this makes the test explicit: delete the line, and if only a name for what follows is lost, it
  was an eyebrow).
- Middle-dot meta strings, arrows glued to link text, decorative status dots (`taste.md`
  section 8).
- The accented word: one word in a headline set apart by colour, weight or highlight.
- One italic word inside an otherwise roman heading.
- Gradient text; glow and wash backgrounds; bounce easing.
- The template page: hero, three equal cards, call to action, footer (`taste.md` sections 3
  and 5).
- The stock close: the page ends on an email sign-up when the visitor's job is not subscribing.
  End on the job: the booking, the enquiry, the quote request, the next date.
- The echo: one fact (price, date, figure) printed in four or more sections.
- The thin section: below the hero, a section with no mass (no visual, no set of three, no list
  or table, no statement at section size); section heads that render under about 40px at 1440
  beside a large hero; more than 160px of dead space inside the hero.
- The crowded head: a heading nearer the content above it than the content it heads.
- The same hover lift or scale on every card; an image scaling on hover.
- The photo wall: photographs cover more than about a third of the page below the hero.
- Control height outside 44 to 52px on a marketing page (app UI may sit at 32 to 40px).
- Decorative glass, glow or blur; a coloured side stripe on a card; a hairline border plus a wide
  shadow on the same card (`taste.md` section 8). Nested cards are already a Floor gate.
- The icon tile above every feature heading; the hero metric opening (`taste.md` section 8).
- A pulsing status dot or a blinking cursor on static text (`taste.md` section 8, `motion.md`).
- Cards touching the ends of a horizontal scroller with no inset.

## Finish

- `::selection`, `caret-color` and `scrollbar-color` unthemed on a page with a committed palette.
- `hyphens: auto` on justified text; `lang`, `<title>` and meta description present.
- One filled primary button recipe per page; no two filled buttons side by side.
- A paragraph or heading leaving one word on its last line (`text-wrap: balance` or `pretty`).
- A grid or wrapping row leaving one item alone on its last row.
- Everything else in `interface-checklist.md` that is not Floor or Reflex above.

## Not adopted from Hallmark

Theme dealing and the build log (they push variety; brand work needs consistency), the 80 words
per screen and 450 words per page caps (wrong for B2B pages), macrostructure and photo libraries,
and the CSS stamp (waivers go in the handover instead).
