---
max_turns: 30
timeout_seconds: 1200
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Use the content-writer agent. Run a CRO audit of this page. The goal is newsletter signups. Traffic comes from a LinkedIn post that links straight to the page. There is no analytics export and no brand kit. The company is Acme Access, a fictional Belgian company selling cloud visitor management and access control. Give me the findings and what to test first.

Page, top to bottom:

HEADER: logo, menu (Home, Products, Pricing, Blog, About, Careers, Contact, Login)

HERO
Headline: Visitor management insights, once a month
Subhead: A short newsletter for facility managers about running safer, simpler sites.
Button: Learn more

SECTION "What you get"
- One practical idea per issue
- Short case notes from Belgian warehouses and offices
- Early access to new product notes

SECTION "Sign up"
Form fields: First name, Last name, Company, Phone number, Job title, Work email
Button: Submit

SECTION "FAQ"
How often do you send it? Once a month.
Can I unsubscribe? Yes, every issue has an unsubscribe link.

SECTION "What readers say"
"Short, useful and I always learn one thing." (Sofie Declercq, facility manager)

FOOTER: company address, privacy policy, social icons

Return the agent's reply to me verbatim, including its closing Skills run line. Put the full deliverable in your reply; do not write files.
