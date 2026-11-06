---
name: email-design
description: "Designs marketing email templates and email visuals: modular layout, header and hero, bulletproof buttons, dark mode, Outlook-safe HTML, accessibility, for Brevo, HubSpot or Canva. Use for \"email template\", \"newsletter design\", \"design this email\", \"email layout\". Copy: newsletter-writer or email-sequence-hubspot-brevo."
metadata:
  version: 1.0.0
  history: >
    v1.0.0: new skill. Fills the gap between the email copy skills (newsletter-writer,
    email-sequence-hubspot-brevo) and the visual skills: none of them owned the look of an email.
argument-hint: "<the email or template, the platform (Brevo, HubSpot, Canva or HTML), the brand>"
---

# Email Design

You design the email the copy goes into: a reusable template, or the visuals for one send. An email is
read in a narrow column, in clients that strip CSS, often with images off and frequently in dark mode.
Design for that reader first and the inbox preview second.

**Required skill calls.** Call `brand-review` through the Skill tool on anything with copy in it before it
is called finished, and never imitate it inline. End the reply with one line: `Skills run: ...`.

## Step 0: Brand, copy and platform

1. Load the `[brand]-brand-kit` skill (`references/design.md`): palette with hex, fonts and web-safe
   fallbacks, logo files, button style.
2. Take the copy verbatim from the approved `newsletter-writer` or `email-sequence-hubspot-brevo`
   piece. Missing copy goes back to `email-marketer`; you don't write it.
3. Settle the platform, because it decides what you deliver:

| Platform | You deliver |
|---|---|
| Brevo (drag-and-drop editor) | A block-by-block build spec in Brevo's terms, plus image assets |
| Brevo or HubSpot (custom HTML template) | Tested HTML with the platform's merge tags and unsubscribe link in place |
| HubSpot (drag-and-drop email or a template module) | A module-by-module build spec, plus image assets |
| Canva (`email` design type) | The design through `canva-workflow`; note that Canva output is mostly images, so live text and links are rebuilt in the sending tool |
| Visuals only (hero, banner, product shots) | Image assets at the sizes below, routed through `canva-workflow`, `affinity-workflow` or `figma-weavy-workflow` |

Connectors: load the Brevo or HubSpot tools before using them and read the names; never guess one.
Creating or changing a template is a draft; sending, scheduling or activating anything waits for a yes
(`security-policy`). If the connector isn't connected (HubSpot's connection may still be unfinished),
hand back the spec or the HTML for manual entry.

## Layout rules

- **Width:** 600px content column (up to 640px), single column on mobile below about 480px. Two columns
  only where the content is genuinely paired, and they stack on mobile.
- **Modules, top to bottom:** preheader text (hidden, 40 to 100 characters, completes the subject line),
  header with logo (linked, under 60px high), hero (one message, one action), body modules, a single
  primary button per message, footer (sender address, reason for receiving, unsubscribe, preferences).
  The footer content is a legal requirement in the EU: never remove it to save space.
- **Type:** body 16px minimum (14px only in the footer), line-height about 1.5, headings 22 to 28px.
  Brand fonts as web fonts only where the client supports them (Apple Mail, iOS); every font stack ends in
  a web-safe fallback with similar width.
- **Buttons:** bulletproof (an HTML or VML button with live text, not an image), at least 44px high, the
  label in the copy's words. A text link after the button for clients that break it.
- **Images:** every image has `alt` text that carries the message when images are off; no essential text
  inside an image (a headline baked into the hero image disappears with images off and fails screen
  readers). Export at 2x for retina, compressed: a hero under about 200 KB, the whole email under about
  1 MB. Width and height set on every `<img>`.
- **Colour and contrast:** 4.5:1 for body text, 3:1 for large text and buttons, on the background it
  actually sits on. Never carry meaning by colour alone.
- **Dark mode:** expect clients to invert colours. Use transparent PNG logos with a light outline or a
  dark-mode variant, avoid pure black and pure white backgrounds, and add `prefers-color-scheme`
  overrides where the client honours them. Check that the logo and buttons survive inversion.
- **Text-to-image balance:** mostly live text. An email that is one big image is the clearest way to land
  in spam and to be unreadable with images off.
- **Accessibility:** `lang` on the `<html>` element, tables marked `role="presentation"`, logical reading
  order when stacked, meaningful link text (never "click here").
- **Localisation:** German and French copy runs about 30% longer; leave room in buttons and headings.

## HTML build (custom templates)

Table-based layout with inline styles for the core, a `<style>` block only for media queries and dark mode
overrides, VML for buttons and background images in Outlook for Windows, conditional comments for Outlook
widths. Merge tags and the unsubscribe link in the platform's own syntax (look them up in the platform's
documentation or the connector; don't guess). No JavaScript, no forms, no external CSS, no web fonts
loaded from a source the user hasn't approved.

Test before handing over: render at 600px and 375px, images off, dark mode. If an email testing tool is
available in the session use it; otherwise say `Not verified` for the clients you could not check
(Outlook for Windows, Gmail app, Apple Mail).

## Output

1. The design read in two lines: what the email is for and the one action.
2. The module plan: each module in order with its copy source, image (size and alt text) and button.
3. Per platform: the build spec in the platform's own terms, or the HTML, or the Canva design link.
4. The asset list: file name, pixel size at 1x and 2x, weight, alt text.
5. The check result: contrast, images off, dark mode, mobile, footer present, plus anything `Not verified`.

## Related Skills

Copy comes from `newsletter-writer` (one send) or `email-sequence-hubspot-brevo` (a flow, which also
holds the automation build). Visual assets come from `canva-workflow`, `affinity-workflow` or
`figma-weavy-workflow`, briefed by `creative-brief`. A landing page the email links to is built by the
`web-developer` agent; check that its message matches the email.

Conciseness note: any chat framing around this deliverable stays short, a sentence or two. It never
applies to the deliverable itself, which is produced at the full length and detail the structure above
requires.
