# Verification

Measured checks on the rendered page, run with `scripts/verify.mjs` (Playwright). It replaces
"look at a screenshot and say it seems fine" with numbers and evidence, and feeds the sweep in
Part 5 of `SKILL.md`, `gates.md` and the cold review.

This file holds method only. The script holds no design values. Everything it checks against
(viewports, tokens, budgets, selectors, tolerances) comes from a config file filled from the
design system or the brand kit.

## 1. The config comes from the design system

`verify.config.json` is built from the `Verification` section of the brand kit's `design.md`
(template: `templates/brand-kit/references/design.md`), or from the project's own design system.
`scripts/verify.config.example.json` shows the shape with placeholders only.

| Key | Carries | Without it |
|---|---|---|
| `viewports` | The names and sizes the design system tests at | The script refuses to run |
| `budgets` | Performance budgets: LCP, layout shift, page weight | Published Core Web Vitals "good" thresholds apply to LCP and layout shift; weight is `Not verified` |
| `aboveFold` | Selectors for what must be visible without scrolling | `Not verified` |
| `minTargetPx` | Smallest touch target | `Not verified` |
| `tokens`, `colourTolerance` | Colours and font families that exist | `onlyTokens` rule cannot run |
| `rules` | Design rules as measurable assertions (section 3) | Only the objective checks run |
| `tags` | Tag hosts that must or must not fire | Hosts are listed, nothing asserted |
| `blockRequests` | Request patterns to record but not send | Requests are sent |
| `ignoreConsoleErrors` | Known, accepted console messages | None ignored |

If the design system has no `Verification` section, say so. To propose viewports, run
`node verify.mjs --discover-breakpoints <url>`: it lists the widths in the page's own media
queries. Hand those to the design system owner as a proposal; never adopt them silently or fill
the config from memory. A check with no value behind it reports `Not verified`.

## 2. What it checks

| Check | Tier | How |
|---|---|---|
| Horizontal overflow, per viewport | Floor | Document width against viewport width, with the widest offenders named |
| Console errors, failed requests, HTTP status | Floor | Collected during load |
| Broken images, missing `alt`, one `h1`, viewport meta | Floor | DOM |
| Internal links answer | Floor | Status only, no actions (section 5) |
| Automated accessibility scan | Floor | axe, when `@axe-core/playwright` is installed. It covers only part of WCAG; never report it as conformance |
| Visible keyboard focus | Floor | Heuristic: outline or shadow on focus. A custom indicator it cannot see is a false alarm to check by eye |
| Reduced motion | Floor | Animations still running after the preference is set |
| Above the fold | Floor | Configured selectors inside the first viewport |
| LCP, layout shift, weight | Reflex | One lab run against the budget. Lab data, not field data. INP needs interaction and stays `Not verified` |
| Touch targets | Reflex | Against `minTargetPx` |
| Tags | Reflex | Hosts requested, against `tags` |
| Design rules | as set per rule | Section 3 |
| Inventory | Info | Headings, links, form fields, landmarks, JSON-LD to `inventory.json` |

Screenshots (first viewport and full page, per viewport) and `verification.json` go to the output
folder. Write them to `<job folder>/verification/`, not to `deliverables/`: they are evidence, not
deliverables.

## 3. Design rules as assertions

Each entry in `config.rules` has a `name`, a `type`, a `tier` (Floor, Reflex or Info) and the
values its type needs. Selectors, colours and tolerances are written by whoever owns the design
system.

| Type | Passes when | Keys |
|---|---|---|
| `filled` | Every matching element has a background fill or image | `selector` |
| `alignBottom` | Matching elements in each container share a bottom edge | `container`, `selector`, `tolerance` |
| `forbidPair` | No text colour from a list sits on a background colour from another list | `text`, `background`, `tolerance`, optional `selector` |
| `background` | Matching elements use only the allowed backgrounds | `selector`, `allowed`, `tolerance` |
| `onlyTokens` | Computed colours and font families are all in `tokens` | uses `tokens`, `colourTolerance` |

A design rule held in the brand kit in words ("buttons are filled", "sections are white") belongs
in the config as a rule, so it is measured on every build instead of remembered.

## 4. Running it

Setup, once, in a folder you control: `npm install playwright` and, for the accessibility scan,
`npm install @axe-core/playwright`. Use a downloaded Chromium, or point at an installed Chrome with
`--browser-path` or `VERIFY_BROWSER_PATH`.

```
node verify.mjs --config verify.config.json --out <job folder>/verification <url> [<url> ...]
node verify.mjs --config verify.config.json --out ... --baseline before/inventory.json <url>
node verify.mjs --inventory-only [--config verify.config.json] --out <dir> <url>
node verify.mjs --discover-breakpoints <url>
node verify.mjs --self-test
```

- **`--inventory-only`:** needs no design values, so other skills use it (`seo-audit` for rendered
  JSON-LD, `cro-auditor` for form fields, the GA4 audit for tags before consent). It checks status,
  console and request errors, links, images, headings, forms, JSON-LD, tag hosts and the accessibility
  scan. It takes no screenshots and judges nothing visual: no viewports, rules or budgets. The config is
  optional and only supplies `tags`, `blockRequests` and `ignoreConsoleErrors`.
- **Tags before consent:** the script never touches a consent banner, so any host in `tags.forbidden`
  that it sees requested fired before consent. It cannot show what happens after a visitor accepts or
  declines.
- **Redesign:** run once before touching anything and keep `inventory.json`; run again with
  `--baseline`. Any heading, link or form field that disappeared is a Floor failure unless the
  brief says to remove it.
- **Exit code 1** means a Floor check failed. Fix and rerun once, then report what remains.
- **No shell, or no Playwright:** say `Not verified` for every check in section 2 and fall back to
  manual screenshots at the design system's viewports. Do not describe a page you did not render.

## 5. What it will not do

It loads pages and measures. It never clicks, types, submits a form, logs in, accepts a prompt or
uploads a file, and it only requests `http` and `https` URLs.

- Link checks use `HEAD` and skip anything that looks like an action (logout, delete, cart,
  unsubscribe, nonce or action parameters).
- Loading a live page fires its analytics. List the analytics and ad hosts in `blockRequests`:
  they are then recorded as fired and never sent, so tag checks still work and no real event
  reaches an account. Without that, verify on staging.
- A staging site behind a login needs a preview link or the user's own signed-in session. Never
  type a password; hand that step to the user (`security-policy`).
- Anything that needs interaction (an open menu, a modal, a form error state) goes to the
  Playwright MCP if it is installed, under `security-policy`: read-only on a live site, and the
  publish gate asks before any write-capable call. Its page snapshots are large: prefer the script
  for measuring and the MCP for the single state you need to see.

### Chrome DevTools MCP

If the Chrome DevTools MCP is connected, use it for the questions the script cannot answer, and
keep the script for repeatable evidence. It runs in the user's own Chrome through the desktop app,
so it is not available to scheduled or unattended runs.

- **Why a page is slow:** a performance trace and its insights name the cause of a slow LCP,
  render-blocking requests, third parties and cache gaps. The script only measures the number.
- **Which rule styles an element:** read the computed and matched styles to see the cascade, the
  overridden declarations and the resolved tokens. Use it to find page-specific overrides of a
  component (`component-system.md`).
- **States the script does not render:** dark scheme, forced colours and contrast preferences by
  emulation. Which states apply comes from the design system.
- **Throttling:** state the network and CPU settings used next to every number, or call the run
  unthrottled. A throttled and an unthrottled number are never compared.
- **Lighthouse:** its accessibility audit uses the same engine as the script, so it adds nothing
  there. Check that the report's device label matches the emulation requested before quoting
  mobile results; if it does not, report the result as `Not verified` for mobile.
- **Reports are saved on the user's computer**, not in the job folder. Quote the figures and name
  where the report is.
- **Read-only:** loading, tracing, reading styles and emulating display states are allowed.
  Clicks, typing, script evaluation, uploads and dialogs ask first (`security-policy`), as does
  setting extra HTTP headers.

## 6. Reading and reporting

- Map tiers to `gates.md`: Floor never ships, Reflex is fixed or waived, Finish is answered.
- `Not verified` stays `Not verified`. Never turn it into a pass.
- The handover carries the summary line the script prints and the path to `verification.json`.
  Failures are reported with the check name and its detail.
- The cold reviewer gets `verification.md` and the screenshots as inputs and judges them. It does
  not run a browser, so its review stays independent of the build.
- A passing run does not replace the human parts of the sweep (the design read, the AI tells, the
  copy): it removes the arguments about what is measurable.
