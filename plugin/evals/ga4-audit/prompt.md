---
max_turns: 30
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Use the performance-reporter agent. Audit the GA4 setup of Acme Access (a fictional Belgian visitor management company) from the exports below. The funnel is: visit the product page, start the demo form, submit the demo form, and become a sales-qualified lead (the last step happens in the CRM, not on the site). The data must support bidding in Google Ads on demo requests and a monthly channel report. There is no brand kit. No GA4 connector is installed.

EVENTS (last 30 days, event name: count)
page_view: 48,210
session_start: 31,880
scroll: 20,114
click: 9,870
form_start: 1,402
generate_lead: 0
thank_you_view: 311

KEY EVENTS (counting method)
thank_you_view: once per event
scroll: once per event

SOURCE / MEDIUM / CAMPAIGN (sessions, last 30 days)
google / cpc / brand-2026: 4,100
Google / CPC / Brand-2026: 1,260
linkedin / paid-social / q4-abm: 2,300
linkedin / Paid_Social / Q4_ABM: 840
newsletter / email / oct: 1,100
e-mail / newsletter / october: 620
(direct) / (none): 9,400
(not set): 3,950

SETTINGS (reported by the user, not seen)
Internal traffic filter exists, state: testing. Data retention: 2 months. Consent banner present, consent mode not configured.

Return the agent's reply to me verbatim, including its closing Skills run line. Put the full deliverable in your reply; do not write files.
