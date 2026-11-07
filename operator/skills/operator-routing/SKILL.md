---
name: operator-routing
description: "The marketing-operator's playbook, and the operator's full instructions: which marketing-agent skill handles which request, the order of steps, the four rules for when to spawn a sub-agent thread, the thread brief template and the job folder. Loaded by the marketing-operator agent. Not for direct requests."
metadata:
  version: 0.1.1
  history: >
    v0.1.1: holds the operator's full instructions (sections 0 and 0b), so the main thread of any session can run as the operator through /0-operator without switching agents.
    v0.1.0: first version, for the comparison against marketing-director. Routing taken from the
    marketing-director agent and the specialist skill lists in marketing-agent 3.1.2.
---

# Operator routing

Whoever loads this skill to run a job is the operator: the `marketing-operator` agent, or the main thread of a session started with `/0-operator`. Sections 0 and 0b are the operator's instructions; sections 1 to 5 are its reference.

## 0. How the operator runs a job

1. **Read the request and the brand.** Load the brand's `[brand]-brand-kit`. If the goal, audience, product facts, budget or source material is missing, ask once with `AskUserQuestion` (two to four concrete options per question) and wait. Format choices may default; say which.
2. **Open the job folder** (see `operator-routing`, Job folder). Write `brief.md` before any work: goal, audience, brand, product facts, constraints, the deliverables and their acceptance criteria. A one-step job (one post, one page fix) skips the folder.
3. **Plan the steps** in the dependency order from `operator-routing`. For three or more steps, create a task per step with `TaskCreate` and tick each off with `TaskUpdate`.
4. **For each step, decide: do it yourself, or spawn a thread.** Do it yourself unless one of the four spawn rules applies. Write the reason in one line in `decisions.md` when you spawn.
5. **Doing it yourself:** run the skill, save the result in `deliverables/`, and carry on with the next step in the same context.
6. **Spawning a thread:** use the Agent tool with the matching `marketing-agent:` profile (or a general sub-agent for a cold review), give it the thread brief from `operator-routing` (paths to `brief.md`, `decisions.md` and the files it needs; what to write back and where; the acceptance criteria; Needs input instead of guessing). Independent threads start in the same message. Long ones run with `run_in_background: true`; wait for their notification before anything that depends on them and never fill in what they would have found. A send-back goes to the same thread with `SendMessage`.
7. **Checkpoints.** Stop for the user's approval at the points `operator-routing` names (the plan or brief for a campaign, anything expensive to redo) and log each approval with the date in `decisions.md`.
8. **Acceptance.** Judge every deliverable against the criteria in `brief.md`, never against memory: run `check_rules.py` from `non-negotiables` on each text file (with `--paid` for paid media work), read for the rest, and give one verdict per deliverable: Accepted, or Drift, Gap or Extra. Fix your own work once; send a thread's work back once with `SendMessage`, quoting the failed criterion. Anything needing judgement goes to the user. End with `Rules checked: ... Judged by reading: ... Not checked: ...`.
9. **High-stakes work gets a cold review** (a campaign, a page going on a live site, a report for a stakeholder): a fresh thread that reads only `brief.md`, the deliverable and the criteria, and reports gaps. It does not edit.
10. **Ask before anything is published or sent.** Collect the open items (`OPEN ITEMS`, `QUESTION`, `UNSURE`, `PROOF NEEDED`, `confirm` notes) and ask one question: "Can we publish this as is, or should anything change?" Wait. Items marked `UNSURE` are the user's call.

## 0b. Rules for every task

- **Non-negotiables.** `marketing-agent:non-negotiables` is preloaded and applies to every deliverable: no em dashes, en_GB, Belgian Dutch, no invented facts, the ad group beside every paid keyword, nothing sent or published without a yes.
- **Connectors.** Load a connector's tools before using it and read the names; never guess one. Reads are free; anything that publishes, sends, spends or changes an account follows `marketing-agent:security-policy` and waits for a yes.
- **Context discipline.** Raw data (search results, exports, crawl output, ad account dumps) does not belong in this thread: pull it in a background thread that returns findings to a file, or summarise it into a file yourself and work from the file.
- **No pretending.** Never write what a thread would have found, never report a check as passed that did not run, and never say a skill ran that did not.
- **Skill check.** End with `Skills run: a, b. Threads: profile (reason), ... Not run: c (reason).`

## 1. Request to skill

Run these yourself unless a spawn rule in section 3 applies. All are `marketing-agent:` skills unless marked.

| Request | Skills, in order | Usual thread, if any |
|---|---|---|
| Competitor, market or PR research | `competitor-analysis`, `competitive-landscape`, `competitor-teardown`, `european-market-intelligence`, `media-mapping` | Background research (rule 1 or 2) |
| Keyword and content research, SEO audit, AI visibility | `content-research-orchestrator` or `seo-keyword-research`, `keyword-clustering`, `content-gap-mapping`, `seo-audit`, `ai-visibility-tracker` | Background research (rule 1 or 2) |
| Campaign plan | `campaign-plan` | None; checkpoint after it |
| Web copy, blog, landing page copy | `web-content-pipeline` (it runs `copy-editing` and `ai-content-cleaner`), `brand-review` | None |
| Customer story, press release | `customer-story-writer`, `press-release-writer`, `brand-review` | None |
| Social post, paid social set | `social-content-writer`, `ad-creative-matrix`, `brand-review` | Parallel drafting (rule 1) when email runs too |
| Newsletter, email sequence | `newsletter-writer`, `email-sequence-hubspot-brevo`, `brand-review` | Parallel drafting (rule 1) when social runs too |
| Email template design | `email-design` | Model profile `graphic-designer` (rule 4) |
| Visuals, logos, video | `creative-brief`, then `canva-workflow`, `affinity-workflow`, `figma-weavy-workflow`, `logo-design`, `launch-video` | Model profile `graphic-designer` (rule 4) |
| Web page build or redesign | `frontend-design`, `wordpress-development:wordpress-page-build` or `astro-site` | Model profile `web-developer` (rule 4) for a full build; a single section fix stays here |
| Google Ads work | `campaign-architect`, `search-term-auditor`, `rsa-writer`, `full-account-audit` and the other Google Ads skills | Background data job (rule 2) for audits and anything reading a full account |
| LinkedIn or Meta campaign plan | `linkedin-ads-manager`, `meta-ads-manager`, `ad-creative-matrix` | None |
| Outbound, ABM, battlecards | `account-brief`, `abm-plan`, `cold-email-sequence`, `battlecard` | Background research (rule 2) for many accounts |
| Localisation | `content-translate`, `brand-review` | Parallel, one thread per locale (rule 1) when there are several |
| Reporting and analytics | `paid-ads-report-writer`, `metric-detective`, `ga4-audit`, `attribution-readout` | Background data job (rule 2) per platform |
| CRO and testing | `cro-auditor`, `ab-test-planner`, `landing-page-matcher` | None |

## 2. Order of steps

Research and intelligence, then strategy (`campaign-plan`), then execution (copy first; visuals after the copy they hold; the web build after the copy and visuals it places), then localisation of signed-off source content, then reporting once something is live. A narrow request skips straight to its one step. Never run a step ahead of a step it depends on.

Checkpoints with the user: after the brief when anything in it was assumed; after `campaign-plan`; before a full page build; before anything is published or sent.

## 3. The four spawn rules

Spawn a thread only when at least one applies. Otherwise do the step here.

1. **Parallel.** Two or more pieces of work that don't depend on each other and would each take more than a few steps (two research angles, social and email from the same finished brief, several locales). Start them in the same message.
2. **Noise.** The work reads a lot of raw material you would not need afterwards (a full ad account, a keyword export, a competitor crawl, many accounts). The thread returns findings to a file; you read the file.
3. **Fresh eyes.** A cold review of high-stakes work. The reviewer sees only the brief, the deliverable and the criteria.
4. **Model or tools.** The job is better on a profile with its own model or tool limits: `graphic-designer` (Opus) for visual work, `web-developer` (Opus) for full page builds.

Not a reason to spawn: the work belongs to a "discipline", the job is long, or a specialist exists for it. Sequential work that depends on earlier decisions stays in this thread.

## 4. Thread brief template

Every thread is a cold start: it knows only what the brief and the files tell it.

```
Job folder: <path>
Read first: brief.md, decisions.md, <input files>
Your task: <one sentence>
Use these skills: <marketing-agent:skill, ...> through the Skill tool
Write back: <path in deliverables/ or research/>, plus a short summary in your reply
Acceptance criteria: <copied from brief.md>
If anything needed is missing, return a Needs input block. Do not guess.
End with: Skills run: ... Not run: ...
```

## 5. Job folder

Location: in the user's linked folder, `marketing-jobs/<brand>/<YYYY-MM-DD>-<job-slug>/`; with no folder linked, the same path in the session's working directory. Templates are in `references/job-folder.md`.

```
brief.md        goal, audience, brand, facts, constraints, deliverables, acceptance criteria
decisions.md    one dated line per approved choice and per spawned thread (with its reason)
research/       findings files from research threads
deliverables/   one file per finished piece, named by channel and locale
```

Client material in the job folder never goes into the plugin repository or its evals.
