---
name: mcp-efficiency
description: "Shared reference for calling any MCP connector (Google Ads, LinkedIn Ads, OpenSEO, Firecrawl, HubSpot, Brevo, and others) without pulling more into context than the task needs. Not triggered directly — loaded by other skills that make live connector calls."
---

# MCP Efficiency — Shared Reference

One module, reusable across every skill that calls a live MCP connector,
covering how to call it without pulling more into context than the task
needs. This doesn't replace a connector's own tool-map reference (e.g.
`google-ads-tool-map`, `openseo-tool-map`) — those say *which* tool to call
and with *what* parameters; this says how to call *any* of them cheaply.

## Rules

1. **Filter at the source, not after.** If a tool takes `min_cost`,
   `min_impressions`, a date range, a `limit`, or an equivalent narrowing
   parameter, set it before the call. Pulling everything and filtering
   client-side (in your own reasoning) means paying context for rows that
   were discarded anyway.
2. **Batch instead of looping.** If a tool accepts multiple items per call
   (multiple keywords, multiple queries, multiple date ranges, a `requests`
   array), use that. One call for ten items beats ten calls for one item,
   both in tokens and in the number of round trips a person waiting on the
   result has to sit through.
3. **Resolve identity once per task, not once per call.** Account IDs,
   project IDs, customer IDs: resolve at the start of a task and carry the
   resolved value through every subsequent call in that task. Re-resolving
   per call (calling `list_accounts` before every single follow-up call)
   is pure waste.
4. **Reuse what an earlier stage already pulled.** In a multi-stage skill
   or pipeline, check whether the data needed at this stage was already
   fetched at an earlier one before making a fresh call for it.
   `content-research-orchestrator` already does this (Stage 3 reuses
   Stage 1-2's keyword set); the same discipline applies to any
   multi-step Google Ads or SEO workflow.
5. **Don't restate raw tool output in the reply.** A tool call's raw
   response is already in context once. Extract the specific rows,
   numbers, or fields the finding needs — never re-paste a full table or
   JSON blob back into the conversation to "show the work." Present the
   analysis, not the payload.
6. **No blind retries.** An error or an empty result has a specific
   cause — check the skill's own Error Handling table first (wrong
   account/project ID, bad location/language code, a date range the tool
   rejects, a rate limit). Retrying the identical call and hoping is a
   second wasted call, not a fix.
7. **Cap unattended call volume.** A skill or pipeline stage that could
   plausibly fire ten or more connector calls in a row should state a
   limit in its own Workflow (a page cap, a domain cap, a date-range cap)
   rather than running until the task feels done. Where a limit already
   exists (e.g. content-research-orchestrator's 3-domain cap per Stage 4
   approval), keep it; where one doesn't, this is the default: batch
   conservatively, check in before the next large batch.
8. **Delegate large one-off pulls to a subagent.** When a single pull is
   genuinely large — a full account export, a full campaign history, a
   bulk keyword list beyond what one call's batch limit covers — and the
   task only needs the synthesized result (a findings table, a ranked
   list), consider running that pull inside a subagent via the Agent tool
   rather than in the main conversation. The subagent does the fetching
   and returns only the synthesis; the raw pull never enters the main
   context. Use this for genuinely large one-off pulls, not as a default
   for every connector call — the overhead of spinning up a subagent
   isn't worth it for a handful of calls a skill can just make directly.

## Why this exists

Every skill in this library that talks to a live connector (Google Ads,
LinkedIn Ads, OpenSEO, Firecrawl, HubSpot, Brevo) was written separately,
and each one re-derives its own batching and filtering discipline in its
own words if it derives it at all — `content-research-orchestrator` has
strong discipline here, several of the Google Ads audit skills have none.
Rather than repeating the same eight rules inside every skill that calls
a connector, they live here once and get pulled in by reference, the same
reasoning that keeps `security-policy` a single shared hub instead of
being copy-pasted into every research skill.
