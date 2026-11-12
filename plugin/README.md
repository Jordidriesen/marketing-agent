# Marketing Agent (plugin)

A marketing team for Claude, built by [Jordi Driesen](https://github.com/Jordidriesen) for Cowork and Claude Code. One command, `/team`, turns the main thread into a director that writes the brief, does the work with the plugin's skills, starts threads only where they pay off, reviews the result and asks before anything is published. For a single, clearly scoped task you just ask: the right skill triggers on its own.

**One install, skills and profiles together.** The plugin ships its 50 skills, the `team` command and six thread profiles, so they can't drift apart. Only client brand kits live outside it: each brand gets a private `[brand]-brand-kit` skill that every content, review and design skill loads automatically (see [`templates/brand-kit`](../templates/brand-kit)).

## Installation

```
claude plugin marketplace add Jordidriesen/marketing-agent
/plugin install marketing-agent@marketing-agent
```

Update later with `claude plugin marketplace update marketing-agent`.

## When to use `/team`

Use `/marketing-agent:team` followed by your request when:

- the job has several steps or deliverables that must hang together (a campaign with a page, ads and a nurture sequence);
- the result goes live or to a client (you get the job folder, acceptance criteria, a cold review at the right tier and the publish question);
- it needs heavy data work (a full account audit, a competitor crawl), which runs in a background thread;
- pieces can run in parallel (several locales, social and email from one brief);
- you are not sure which skill owns it.

For one post, a copy edit, a set of RSA headlines, a quick metric question or one translation, just ask. It is cheaper and faster, and the skill's own rules still apply.

## Thread profiles

The director does the work itself and starts a thread only under four rules: parallel work, a noisy data job, a cold review, or a job that needs a profile's own model or tools. These are the profiles it starts. None of them triggers on its own; each description says it is a thread profile for the director.

| Profile | Thread type | Model / effort | Max turns |
|---|---|---|---|
| [`data-puller`](agents/data-puller.md) | Bulk pulls (ad account, keyword or Search Console export, crawl, many accounts), findings to a file | haiku / low | 80 |
| [`researcher`](agents/researcher.md) | Research that needs judgement: competitors, market, keywords, accounts | sonnet / medium | 80 |
| [`drafter`](agents/drafter.md) | Parallel drafting from a finished brief: social, email, locales, a second page | sonnet / medium | 60 |
| [`graphic-designer`](agents/graphic-designer.md) | Fixed-format visuals: social, ads, email templates, print, decks, logos, short video | opus / medium | 60 |
| [`web-developer`](agents/web-developer.md) | Full web builds in WordPress and Astro, redesigns, Figma to code, performance and accessibility | opus / medium | 100 |
| [`cold-reviewer`](agents/cold-reviewer.md) | Reviews deliverables cold against `brief.md`; Read, Glob and Grep only | by tier (`light` sonnet / medium, `full-sonnet` sonnet / high, `full-opus` opus / high) | none |

The director passes `model` and `effort` on every thread from the model table in `director-playbook` and logs both in the job's `decisions.md`. What each discipline needs to know (connector order, hard limits, hand-offs) is in `director-playbook/references/discipline-notes.md`; the director reads the section before a step and pastes it into each thread brief.

Every profile preloads `marketing-agent:non-negotiables`. The profiles use `disallowedTools`, so they keep their connector (MCP) tools; none of them has a shell, so the director runs the mechanical rule checks.

Order for a full job: intelligence and research first, strategy second, execution third (independent pieces in parallel threads), localisation once source content is signed off, reporting last, with a cold review at the job's tier before the publish question.

## Example workflows

### Planning a campaign

```
/marketing-agent:team
Goal: 150 qualified leads for the new product line
Audience: Facility managers at mid-sized companies in Belgium and Germany
Timeline: 8 weeks
Budget: EUR 20,000
```

The director writes the brief, runs competitor and SEO research (in background threads when they are large), writes the plan and stops for your approval, then produces the pieces; localisation follows once each piece is signed off.

### Researching a competitor

Ask directly ("analyse competitor X, domain x.example"): `competitive-research` fires, with its `competitor-analysis` reference for organic footprint, content and positioning and its `competitor-teardown` reference for paid ad angles. Use `/team` when the research feeds a campaign.

### Reporting on paid media

```
/marketing-agent:team
Monthly paid report for [brand]: Google Ads and LinkedIn Ads, September 2026 compared with August
```

`paid-ads-report-writer` pulls live data where the connectors are connected (a `data-puller` thread per platform), works from exports for the rest, normalises conversion definitions across platforms, and writes the executive summary plus a section per platform. A client report gets a `full-opus` review.

## Brand kits

Every content, review, design and localisation skill identifies the brand and loads its `[brand]-brand-kit` skill when one exists. A modular kit is a short router plus three modules: `context.md` (who the brand is, audiences, channels, data sources), `voice.md` (tone of voice and Voice Lock) and `design.md` (colour, type, layout tokens). Start from [`templates/brand-kit`](../templates/brand-kit).

## Connectors

See [CONNECTORS.md](CONNECTORS.md) for which connector each discipline uses, what happens when one isn't connected, and the data-source rule for brands with and without an OpenSEO project.
