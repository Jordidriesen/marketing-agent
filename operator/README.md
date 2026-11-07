# Marketing Operator (experimental)

A self-contained, single-operator alternative to the marketing-agent plugin and its `marketing-director`, built to be compared against it before anything switches. It does not need marketing-agent, and it changes nothing in it.

| | marketing-agent (director) | marketing-operator |
|---|---|---|
| Who does the work | A specialist sub-agent for every step | The operator itself, in the main thread |
| Hand-offs | Summaries in each brief | Files in a job folder (`brief.md`, `decisions.md`, `research/`, `deliverables/`) |
| When sub-agents run | Always, one per discipline | Only under four rules: parallel, noise, fresh eyes, model or tools |
| Thread models | Fixed per agent | Chosen per thread from a model table, logged |
| Skills | 69 | 49: five family skills hold 24 former skills as references |

## What is in it

- `agents/marketing-operator.md`: the operator as an agent (for the Claude Code terminal).
- `agents/*.md`: thread profiles the operator spawns (`graphic-designer`, `web-developer`, `competitive-intel-analyst` and the rest), copied from marketing-agent 3.1.2 with their skill names pointing at this plugin.
- `skills/operator-routing/`: the operator's full instructions (sections 0 and 0b), the request-to-skill table, the four spawn rules, the model table (3b), the thread brief template and the job folder.
- `skills/0-operator/`: the shortcut that turns the main thread into the operator.
- Five family skills:

| Family skill | Holds, as references |
|---|---|
| `google-ads-build` | campaign-architect, sea-keyword-research, bid-strategy-advisor, budget-optimizer |
| `google-ads-analyse` | full-account-audit, search-term-auditor, quality-score-doctor, pmax-decoder, geo-performance-analyzer, device-performance-analyzer, ad-schedule-analyzer, auction-insights-monitor, conversion-tracking-auditor, disapproval-diagnoser, landing-page-matcher |
| `google-ads-ads` | rsa-writer, ad-copy-tester |
| `competitive-research` | competitor-analysis, competitive-landscape, content-gap-mapping, competitor-teardown |
| `measurement` | metric-detective, ga4-audit, attribution-readout |

  The three Google Ads families each carry the former `google-ads-tool-map` as a shared reference.
- 44 single skills copied unchanged from marketing-agent 3.1.2, apart from skill names and paths. `non-negotiables`, `security-policy`, `content-references` and `mcp-efficiency` are hidden from the menu (`user-invocable: false`).
- `evals/`: the comparison cases and one routing case per absorbed skill. See `evals/README.md`.

The skills were generated once from marketing-agent 3.1.2. They are this plugin's own copies now: a later change in marketing-agent does not reach them, and a change here does not reach marketing-agent. WordPress builds still call `wordpress-development:` skills when that plugin is installed.

## How to run it

1. Install marketing-operator **instead of** marketing-agent for the session you test in, not next to it. With both installed, the operator would see the 24 absorbed skills beside the families that replace them.
2. Run `/0-operator <your request>`. The shortcut loads `operator-routing` into the main thread, and the main thread becomes the operator. No agent switch is needed.

Why the main thread: a sub-agent cannot start sub-agents, so an operator started as a sub-agent could not start its parallel, background or review threads. In the Claude app a plugin's default main agent setting does not appear to apply, so the shortcut works through the main thread instead. In the Claude Code terminal you can also set `"agent": "marketing-operator:marketing-operator"` in the project's `.claude/settings.json`. Not tested.

## Removing it

Delete `operator/` and its entry in `.claude-plugin/marketplace.json`, and uninstall the plugin. Nothing in marketing-agent depends on it, so nothing is left behind. If the operator wins the comparison, moving its structure into marketing-agent 4.0.0 is a separate plan.
