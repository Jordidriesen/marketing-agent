---
max_turns: 30
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Use the seo-geo-specialist agent. Write the AI visibility report for Acme Access (a fictional Belgian visitor management company, no brand kit) from the two rounds of checks below. Competitor tracked: Visiguard (fictional). The prompt set is v1: 10 non-branded Dutch (nl-BE) buyer questions, each asked once per engine in each round, same location, logged out, search on. Round 1 was run on 2026-09-14 and round 2 on 2026-10-12. A new Acme blog post, acme.example/blog/visitor-management-warehouse, was published on 2026-09-30.

ROUND 1 (answers checked: 10 per engine)
Acme Access: ChatGPT mentioned 2, cited 1. Perplexity mentioned 4, cited 3. Google AI Overviews mentioned 1, cited 1.
Visiguard: ChatGPT mentioned 5, cited 4. Perplexity mentioned 5, cited 4. Google AI Overviews mentioned 4, cited 4.

ROUND 2 (answers checked: 10 per engine)
Acme Access: ChatGPT mentioned 2, cited 1. Perplexity mentioned 8, cited 7. Google AI Overviews mentioned 1, cited 1.
Visiguard: ChatGPT mentioned 5, cited 4. Perplexity mentioned 4, cited 3. Google AI Overviews mentioned 4, cited 4.
Acme pages cited on Perplexity in round 2: acme.example/blog/visitor-management-warehouse (5 answers), acme.example/products/visitor-management (2 answers).

Search Console and GA4 were not available for this report. Return the agent's reply to me verbatim, including its closing Skills run line. Put the full deliverable in your reply; do not write files.
