---
name: astro-site
description: 'Builds and changes marketing sites in Astro: project structure, layouts and components, content collections, images, islands with as little JavaScript as possible, i18n routes, SEO and schema, build and deploy. Use for "Astro site", "build this in Astro", "add a page to the Astro project". Design read and tokens: frontend-design.'
metadata:
  version: 1.0.0
  history: 'v1.0.0: new skill for the web-developer agent. Version-agnostic on purpose: it reads the project''s Astro version and the matching docs before using an API, because Astro renames and moves APIs between major versions.

    '
argument-hint: <the project or repo, the page or feature, the brand>
---

# Astro Site

You build marketing pages and sites in Astro the way Astro is meant to be used: HTML first, content from
collections, JavaScript only where an interaction needs it. The design comes from `frontend-design` and the
brand kit; this skill covers how it is put together in Astro.

**Required skill calls.** Run `frontend-design` for the design read, the tokens and the sweep (Part 5), and
`brand-review` on copy baked into the page, through the Skill tool. End the reply with one line:
`Skills run: ...`.

## Step 0: Read the project before writing anything

1. `package.json`: the Astro major version, integrations (sitemap, MDX, a UI framework such as React or
   Svelte, Tailwind), the adapter if the site renders on a server, and the scripts.
2. `astro.config.*`: `site`, `output` and adapter, `i18n`, integrations, image settings.
3. The structure under `src/`: `pages/`, `layouts/`, `components/`, the content config and collections,
   `styles/`. Note the conventions already used and follow them.
4. Read the official docs (docs.astro.build) for that major version before using any API you are not
   certain of. Astro has renamed and moved APIs between majors (the content collections config, the
   view transitions component, image components), so never write from memory alone. If the docs can't be
   reached, say which API you could not verify.

New project: scaffold with `npm create astro@latest` only on the user's yes, in the folder they name.

## Build rules

- **Pages and layouts.** One base layout owns `<html lang>`, `<head>` (title, meta description, canonical,
  Open Graph, favicon) and the skip link. Pages pass their own title, description and canonical. Routes
  follow the URL plan from `seo-geo-specialist` or the existing site; never change a live URL without a
  redirect and a yes.
- **Content.** Repeated content (blog posts, case studies, products, team, FAQs) lives in content
  collections with a schema, so a missing field fails the build rather than the page. Copy comes verbatim
  from the approved piece.
- **Components.** `.astro` components by default; they ship no JavaScript. A UI framework island only for
  a real interaction (a filter, a calculator, a configurator), with the lightest `client:` directive that
  works (`client:visible` or `client:idle` before `client:load`). When the island needs a library and the
  `pick-ui-library` skill is installed, use it to choose one.
- **Styling.** The token system from `frontend-design` as CSS custom properties in one global file, scoped
  `<style>` in components. Keep the project's existing system (Tailwind or plain CSS) rather than adding a
  second one.
- **Images.** Astro's image components for local images (sizes, formats, lazy loading, width and height
  set); real alt text; the hero image eager and given priority. No invented images that could pass as the
  client's real work.
- **Motion.** Per `frontend-design`'s `motion.md`; `transitions-dev` snippets when installed. Page
  transitions only when the brief asks, with a reduced-motion fallback.
- **i18n.** Astro's i18n routing for multi-language sites (for example `/nl-be/`, `/fr-be/`), `hreflang`
  for every locale version, and a language switcher that links to the same page in the other locale.
  Translated content comes from `localization-specialist`.
- **SEO and schema.** Sitemap integration, `robots.txt`, one `h1` per page, JSON-LD schema from a
  component fed by the page's real data (Organization, BreadcrumbList, Article, FAQPage only when the FAQ
  is visible on the page). Schema never states what the page doesn't.
- **Forms.** A static site posts to a form service or an endpoint the user chooses (Tally.so,
  HubSpot, Brevo, a server endpoint). Never wire a form to a service the user hasn't approved, and never
  fake a successful send.

## Check before handing over

```bash
npx astro check     # types and template errors
npm run build       # must finish with no errors or warnings you have not explained
npm run preview     # look at the built site, not the dev server
```

Then the `frontend-design` Part 5 sweep on the preview, plus: no console errors, every page has a title,
description and canonical, the sitemap lists the new pages, Lighthouse or an equivalent for performance and
accessibility where it can run. Anything that could not be run is `Not verified`.

## Deploy

Deploying, pushing to the main branch or changing DNS is a live change: prepare it, list what will change,
and wait for a yes. When the project is in Git, work on a branch and open a pull request rather than
pushing to the main branch.

## Output

The change list (files added or changed, with one line each), the routes affected, the check results, and
anything the user needs to decide (a URL change, a new dependency, a deploy).

## Related Skills

`frontend-design` for the design and the sweep; `web-content-pipeline` for page copy; `seo-audit` before a
change to URLs, templates or structured data; `localization-specialist` for other locales;
`graphic-designer` (through the director) for images and illustrations.
