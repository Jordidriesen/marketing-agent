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
- `skills/operator-routing/`: request-to-skill table, order of steps, the four spawn rules, the thread brief template, and the job folder with templates in `references/job-folder.md`.
- `skills/0-operator/`: the menu shortcut.

It contains no copies of skills. Every skill it runs and every profile it spawns comes from the `marketing-agent` plugin (and `wordpress-development` for WordPress builds), so that plugin has to be installed.

## How to run it

The operator must be the session's **main agent**. A sub-agent cannot start threads of its own, so the shortcut does not fork.

1. Install both plugins from this marketplace: `marketing-agent` and `marketing-operator`.
2. In the folder you work in, add to `.claude/settings.json`:
   ```json
   { "agent": "marketing-operator:marketing-operator" }
   ```
3. Start a new session there and give it a request, or run `/0-operator`.
4. To go back to the director, remove the line. The marketing-agent plugin makes `marketing-director` the default.

Not tested yet: whether a project setting takes precedence over the plugin's default main agent in every Claude surface. If the session still answers as the director, the switch did not take.

## Comparison

The eval cases `compare-campaign`, `compare-landing` and `compare-report` in `plugin/evals/` run the same three jobs through both setups. See the evals README for how to run them and what is measured. If the operator wins, it moves into the marketing-agent plugin as 4.0.0 and this plugin is retired. If not, uninstall it: nothing in marketing-agent depends on it.
