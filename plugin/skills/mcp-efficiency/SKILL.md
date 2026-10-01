---
name: mcp-efficiency
description: "Shared reference for calling any MCP connector in this stack (Google Ads, LinkedIn Ads, LinkedIn Ad Library, OpenSEO, Search Console, Bing Webmaster Tools, Firecrawl, Exa, HubSpot, Brevo, Typefully, WP Umbrella, Adobe for creativity, Canva, Figma, G2, vidIQ, Notion, Google Drive, Tally.so, Make, Zapier) cheaply and safely: filtering, batching, resolving the account once, and respecting credit, billing and write gates. Not triggered directly: loaded by other skills that make live connector calls."
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
   result has to sit through. The same goes for loading tools: when a
   connector's tools are deferred, load every tool the task will need in
   one tool search, not one search per tool.
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

9. **Resolve the account with the connector's own identity call.** Rule 3
   says resolve once; this is the call to use. Tool names below were checked
   against the live connectors on 1 Oct 2026. For any connector not listed,
   or whose tools aren't loaded yet, load its tools first and read the names;
   never guess a method name.

   | Connector | Resolve with | Then carry |
   |---|---|---|
   | Google Ads | `list_accounts` | customer ID |
   | OpenSEO | `list_projects` (and `get_project_context` for the brand's saved context) | `projectId` |
   | WP Umbrella | `list_projects` with `search` set to the domain | `projectId` (internal; don't show it in replies) |
   | Typefully | `list_social_sets` | social set ID |
   | Brevo | `accounts_get_account`, then `senders_get_senders` before any draft | account, sender |
   | Figma | `whoami` | user and plan |
   | Adobe for creativity | `adobe_mandatory_init`, once per conversation, before any other Adobe tool | session ID from its result |
   | LinkedIn Ads, LinkedIn Ad Library, Search Console, Bing Webmaster Tools, G2, vidIQ, Tally.so, Canva, Notion, Google Drive | Load the tools, then use the connector's own list or "me" call | the resolved ID |

10. **Respect cost and side effects before the call, not after.**
    - **OpenSEO credits.** Research tools spend credits; first-party tools
      (Search Console, GA4, `inspect_urls`, `get_search_opportunities`) and
      housekeeping (`create_project`, `save_keywords`, `save_report`) don't.
      Ask before any planned batch over 2,000 credits. Local tools scale fast:
      `get_local_rank_grid` costs one SERP per grid point (3x3 is 9, 5x5 is
      25), and `get_business_reviews` is billed per 10 reviews. Run
      `estimate_rank_tracker_cost` before adding keywords to a scheduled
      tracker; trackers stay on a manual schedule unless the user asks.
    - **WP Umbrella.** Reading is free; acting is not. Updates, database
      optimisation (cannot be undone), backups, hourly backup settings
      (billed per site), security add-ons (may start billing) and
      `generate_report` (emails the recipients) all need explicit approval,
      site by site, per `security-policy`. Follow any process ID with
      `wait_for_process` rather than polling other tools. Never say a backup
      was taken before an update: WP Umbrella doesn't take one.
    - **Adobe for creativity.** Image and PDF edits are fine once asked for.
      Share links, collaborator invites, Adobe Stock licensing and Express
      exports need approval. Canva stays the default for template-based
      design work; reach for Adobe when the job is an image edit, a PDF task,
      font sourcing, or the user asks for Adobe Express.
    - **Brevo, Typefully, Tally.so, Make, Zapier, HubSpot.** Drafts only.
      Sending, scheduling, publishing a form, or running an automation waits
      for the user's go-ahead on that specific item.

## Why this exists

Every skill in this library that talks to a live connector (Google Ads,
LinkedIn Ads, OpenSEO, Firecrawl, HubSpot, Brevo, WP Umbrella, Adobe, and
the rest of the stack in `CONNECTORS.md`) was written separately,
and each one re-derives its own batching and filtering discipline in its
own words if it derives it at all — `content-research-orchestrator` has
strong discipline here, several of the Google Ads audit skills have none.
Rather than repeating the same ten rules inside every skill that calls
a connector, they live here once and get pulled in by reference, the same
reasoning that keeps `security-policy` a single shared hub instead of
being copy-pasted into every research skill.
