# Marketing Operator (experimental)

A single-operator alternative to the `marketing-director` in the marketing-agent plugin, built to be compared against it before anything switches.

| | marketing-director | marketing-operator |
|---|---|---|
| Who does the work | A specialist sub-agent for every step | The operator itself, in one thread |
| Hand-offs | Summaries in each brief | Files in a job folder (`brief.md`, `decisions.md`, `research/`, `deliverables/`) |
| When sub-agents run | Always, one per discipline | Only under four rules: parallel, noise, fresh eyes, model or tools |
| Connectors in the main thread | No (tool allowlist) | Yes |

## What is in it

- `agents/marketing-operator.md`: the operator (Opus, medium effort). Preloads `marketing-agent:non-negotiables` and `operator-routing`.
- `skills/operator-routing/`: the operator's full instructions (sections 0 and 0b), the request-to-skill table, order of steps, the four spawn rules, the thread brief template, and the job folder with templates in `references/job-folder.md`.
- `skills/0-operator/`: the menu shortcut.

It contains no copies of skills. Every skill it runs and every profile it spawns comes from the `marketing-agent` plugin (and `wordpress-development` for WordPress builds), so that plugin has to be installed.

## How to run it

1. Install both plugins: `marketing-agent` and `marketing-operator`. In the Claude app, upload the plugin zip in the plugin settings if it does not appear through the marketplace.
2. Run `/0-operator <your request>`. The shortcut loads `operator-routing` into the main thread, and the main thread becomes the operator. No agent switch is needed.

Why the main thread: a sub-agent cannot start sub-agents, so an operator started as a sub-agent could not start its parallel, background or review threads. In the Claude app the plugin's default main agent setting does not appear to apply (a session with marketing-agent installed answers as the normal assistant, not as `marketing-director`), so the shortcut works through the main thread instead.

In the Claude Code terminal you can also make the agent itself the main agent with `"agent": "marketing-operator:marketing-operator"` in the project's `.claude/settings.json`. Not tested.

## Comparison

The eval cases `compare-campaign`, `compare-landing` and `compare-report` in `plugin/evals/` run the same three jobs through both setups. See the evals README for how to run them and what is measured. If the operator wins, it moves into the marketing-agent plugin as 4.0.0 and this plugin is retired. If not, uninstall it: nothing in marketing-agent depends on it.
