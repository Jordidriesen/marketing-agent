---
max_turns: 25
timeout_seconds: 1200
allowed_tools: [Read, Write, Edit, Glob, Grep, Skill, Agent]
---

Start one thread with the Agent tool, subagent_type marketing-agent:data-puller, model haiku, effort medium, and give it this brief. Do not do the analysis yourself.

Brief for the thread: Acme Access is a fictional Belgian company selling cloud visitor management and access control. No connectors are available; the export below is the complete search terms report for the last 30 days, in EUR. Use the marketing-agent:google-ads-analyse skill (its search-term-auditor reference) to audit wasted spend. Write the findings to research/search-terms.md in the folder you are in: every search term with its ad group, the total spend, the spend on terms with no conversions, and negative keyword suggestions with match types. Use only the figures in the export; if something you need is missing, return a Needs input block instead of guessing. End with a Skills run line.

```
search_term,ad_group,impressions,clicks,cost_eur,conversions
visitor management software,Visitor management,1200,96,182.40,6
free visitor sign in app,Visitor management,840,61,73.20,0
visitor log book template,Visitor management,610,44,31.68,0
qr code check in office,QR check-in,450,38,64.60,3
access control system price,Access control,390,22,52.80,1
door access card reader,Access control,300,17,40.80,0
visitor management jobs,Visitor management,220,9,10.80,0
```

When the thread is done, return its report to me verbatim, followed by the full contents of research/search-terms.md.
