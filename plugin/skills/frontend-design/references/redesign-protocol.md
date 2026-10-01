# Redesign protocol

How `frontend-design` handles an existing site or page. Merged and adapted from Leonxlnx's
[taste-skill](https://github.com/Leonxlnx/taste-skill) (section 11) and
[redesign-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/redesign-skill) (MIT),
with their generic swaps replaced by brand-kit precedence and the SEO, analytics and content
rules this library already follows.

---

## 1. Detect the mode first

| Mode | When | Starting point |
|---|---|---|
| **Preserve** | Modernise without changing the brand | The existing site's look, read in step 2 |
| **Overhaul** | New visual language on existing content | Treat visuals as new, keep content, IA and URLs |
| **Greenfield** | No site yet, or the brand itself is changing | `taste.md` from the start |

If it isn't clear, ask once: "Should this redesign keep the existing brand look, or start
visually from scratch?" Misreading the mode is the biggest source of bad redesigns.

---

## 2. Audit before touching anything

Read the site or codebase and document, briefly:

- **Stack:** WordPress (theme, block editor or builder), a framework, or plain HTML and CSS; how
  styles are managed (theme settings, `theme.json`, Tailwind, CSS files). Work with it. Never
  migrate frameworks or styling systems as part of a redesign.
- **Brand tokens in use:** colours, fonts, radii, logo treatment. Compare them with the brand
  kit's `design.md`. Where they differ, report the difference; don't silently pick one.
- **Information architecture:** page tree, main navigation, key conversion paths.
- **WordPress health baseline (WP Umbrella, when the site is in it):** installed plugins and
  theme (`list_plugins`, `list_themes`), outstanding vulnerabilities (`get_vulnerabilities`),
  performance (`get_performance`), PHP errors (`list_issues`) and broken links
  (`list_broken_links`). Read-only. A redesign that adds a plugin to a site already carrying
  outdated or vulnerable ones should say so. Any update or fix through WP Umbrella is a separate,
  approved action, never part of the redesign itself.
- **SEO baseline:** pages that rank or get traffic (Search Console or OpenSEO, per the brand
  kit's data sources), meta titles, structured data, social cards. SEO loss is the biggest
  redesign risk.
- **Analytics dependencies:** button IDs, form field names, section IDs that tracking or
  conversion actions rely on.
- **What to keep:** signature elements, a recognisable hero, the copy voice, accessibility that
  already works.
- **What to retire:** the AI tells in `taste.md` section 8, broken layouts, dead links, stock
  imagery that the brand rules out, performance traps.
- **Settings reading:** the current variance, motion and density (`taste.md` section 2). That is
  the starting point for a preserve redesign, not the defaults.

---

## 3. Never change silently

These need the user's explicit approval:

- URL structure and slugs, anchor IDs.
- Main navigation labels.
- Form field names or order (they break analytics and autofill).
- The logo, wordmark or brand colours.
- Legal, consent and cookie copy.
- Headings and copy, beyond fixing a clear error. Visual modernisation is not a content rewrite;
  copy changes go through `web-content-pipeline` or `copy-editing` and the brand voice.
- Structured content that serves search and AI answers, such as FAQ sections with schema. Restyle
  them; don't remove or restructure them.

---

## 4. Design audit checklist

Work through these and list every finding before fixing.

**Typography**
- Default or off-brand fonts where the brand kit names others (the fix is the brand font, not a
  font of taste).
- Headings without presence: tighten letter-spacing and line-height on display sizes.
- Body text wider than about 65 to 75 characters.
- Only regular and bold in use where a medium or semibold would give quieter hierarchy.
- Numbers that should line up without `font-variant-numeric: tabular-nums`.
- Orphaned last words in headings: `text-wrap: balance` or `pretty`.

**Colour and surfaces**
- More than one accent; warm and cool greys mixed; accents oversaturated against the neutrals.
- Pure black backgrounds or text where an off-black fits the palette.
- Black drop shadows on light backgrounds; shadows implying different light directions.
- One stray section in the opposite theme.

**Layout and alignment**
- No max-width container; content stretching edge to edge on wide screens.
- Equal-height cards forced where content differs; CTAs at random heights across a row of cards.
- Feature lists or prices starting at different heights across comparison columns.
- Shared elements (titles, prices, buttons) not aligned across side-by-side items.
- Optical misalignment: icons beside text, text in buttons, play icons in circles that are
  mathematically centred but look off.
- Identical top and bottom padding where the bottom needs a little more.
- `100vh` heroes that jump on mobile; flexbox percentage maths where a grid is simpler.

**States and interaction**
- Missing hover, active and visible focus states.
- No loading, empty or error states; `window.alert()` for errors.
- Buttons linking to `#`; no indication of the current page in navigation.
- Animations on `top`, `left`, `width` or `height` instead of `transform` and `opacity`.

**Content**
- Placeholder text, lorem ipsum, "John Doe", duplicated avatars, identical blog dates. Flag them;
  the fix is real content from the client, never invented data.
- Exclamation marks in system messages; "Oops!" errors; passive voice.

**Components**
- Every block as a bordered, shadowed card; always one filled plus one ghost button.
- Modals for simple actions that could be inline.
- A four-column footer link farm where a few main links and the legal links would do.

**Code and basics**
- Div soup instead of semantic elements; inline styles mixed with the styling system.
- Missing alt text, arbitrary `z-index: 9999`, commented-out dead code.
- Imports or plugins that aren't actually installed.
- Missing title, meta description or social image.

**What sites usually forget**
- Privacy and legal links in the footer; a consent banner where the law requires one.
- A useful custom 404 page.
- A skip-to-content link.
- Client-side form validation with inline errors.
- A way back from every page (no dead ends).
- A favicon.

---

## 5. Fix in this order

Stop when the brief is satisfied. Each step is lower risk than the next.

1. **Typography:** apply the brand's fonts properly, fix the scale and spacing. Biggest visible
   gain for the least risk.
2. **Spacing and rhythm:** section padding, container width, vertical rhythm, alignment.
3. **Colour cleanup:** one accent, one grey family, brand tokens applied consistently.
4. **States:** hover, active, focus, loading, empty, error.
5. **Motion layer:** only what the settings and the brief justify.
6. **Hero and key sections:** recompose the top of the page using `taste.md`.
7. **Component replacement:** only where an existing block can't be saved.

The decision in between: if IA, content and SEO are sound, stay with steps 1 to 4 (most of the
value for a fraction of the risk). If the problems are structural (broken IA, no system, broken
mobile), propose a full redesign with strict content and URL preservation, and get approval first.

---

## 6. Rules while changing things

- Small, reviewable changes over one big rewrite. Test after each change.
- Check the dependency file (or the WordPress plugin list) before adding any library or plugin.
- For Tailwind projects, check the major version before touching the configuration.
- On a live WordPress site, change a staging copy or drafts first and ask before publishing.
- After a redesign goes live, compare WP Umbrella's `get_performance` and `list_broken_links` with
  the baseline, and run OpenSEO `inspect_urls` on the key URLs to confirm they are still indexed.
- Hand back the audit, the changes made in the order above, and anything left for the user to
  decide.
