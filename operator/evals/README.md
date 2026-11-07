# Operator evals

Evals for the experimental marketing-operator plugin. Same format as the marketing-agent evals (`prompt.md` plus `graders/`), and the same rule: only the fictional company Acme Access, never client material. None of these have been run yet.

## One plugin per session

The operator carries its own copies of every skill, so it is never tested with marketing-agent installed in the same session: both skill lists would load and the operator would see the 24 absorbed skills next to the families that replace them. Run the `-director` cases with only marketing-agent installed and every other case with only marketing-operator installed. If the Claude app cannot switch a plugin off per session, run them from the Claude Code terminal with one plugin loaded per run.

## compare-campaign, compare-landing and compare-report

Three jobs, each in two cases with the same task: `-director` through `marketing-director`, `-operator` through the operator in the main thread. All use Acme Access and no connectors: a three-week LinkedIn campaign with posts and a nurture pair, a landing page from copy to an Elementor build checklist, and a monthly paid report from given figures.

The `-director` prompts start with "Use the marketing-director agent", which is how the director runs in the Claude app today: as a sub-agent, which cannot start sub-agents of its own. The `-operator` prompts load `operator-routing`, so the main thread becomes the operator and can start threads. Check the first transcript of each to confirm that is what happened before trusting the results.

**Graded:** no em dashes, the `Skills run` line, the skills the job needs, the publish question with nothing claimed as published, and job-specific quality (for the report, the cost per demo request computed from the figures and the ad group beside every search term). The operator cases also check that every thread has a reason matching one of the four spawn rules.

**Measured, not graded:** tokens, wall-clock time and turns per run, the model and effort of every thread (from `decisions.md`), and how many times a person would have had to correct the result. Record them per case and per run.

## route-*

One case per skill that was absorbed into a family skill (24). Each is a plain request that names no skill, the way it would be asked in a chat, and checks two things: the right family skill fired, and the reply works from the right reference inside it. These show whether merging 24 skills into five lost any routing.

| Family | Cases |
|---|---|
| `google-ads-build` | campaign-architect, sea-keyword-research, bid-strategy-advisor, budget-optimizer |
| `google-ads-analyse` | full-account-audit, search-term-auditor, quality-score-doctor, pmax-decoder, geo-performance-analyzer, device-performance-analyzer, ad-schedule-analyzer, auction-insights-monitor, conversion-tracking-auditor, disapproval-diagnoser, landing-page-matcher |
| `google-ads-ads` | rsa-writer, ad-copy-tester |
| `competitive-research` | competitor-analysis, competitive-landscape, content-gap-mapping, competitor-teardown |
| `measurement` | metric-detective, ga4-audit, attribution-readout |

## Not covered yet

Whether Haiku threads follow the Needs input and acceptance rules (the model table marks Haiku as untested), and the copied single skills, which are unchanged from marketing-agent 3.1.2 apart from names and paths and are covered by that plugin's evals.
