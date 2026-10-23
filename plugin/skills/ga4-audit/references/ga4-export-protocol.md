# GA4 export protocol

Loaded by `ga4-audit` when no live connector is available. Ask for the items below, in this order of
value. Screenshots are fine; a CSV or a pasted table is better. Menu labels in GA4 move, so look for
the equivalent when a name has changed. Pick the last 30 days for volumes unless a question needs
longer, and state the date range with every export.

## Must have

1. **Events and their counts**: all event names with event count, last 30 days (Reports, Engagement,
   Events; or an exploration with Event name as rows and Event count as the value).
2. **Key events list**: every event marked as a key event, with its counting method (Admin, Events,
   or Key events).
3. **Source, medium and campaign**: sessions by Session source / medium and Session campaign, last
   30 to 90 days (Reports, Acquisition, Traffic acquisition, with the secondary dimension added), including
   the Unassigned and Direct rows.
4. **The funnel** in the user's words, or the checkout and form steps as page paths.

## Strongly useful

5. **Property settings**: property name, time zone, currency, and the data retention setting (Admin,
   Property settings and Data settings).
6. **Data streams**: the web stream and any enhanced measurement toggles.
7. **Data filters**: internal traffic and developer traffic, with their state (testing or active).
8. **Define internal traffic** rules and **unwanted referrals** list (Admin, Data streams, Configure tag
   settings).
9. **Cross-domain** configuration: the listed domains (same place as 8).
10. **Consent**: the consent banner or CMP in use, whether consent mode signals are passed, and any
    consent status the property shows in Admin.
11. **Custom definitions**: custom dimensions and metrics, and what feeds them.
12. **Attribution settings**: reporting attribution model and key event lookback windows (Admin,
    Attribution settings).
13. **Product links**: Google Ads, Search Console, BigQuery (Admin, Product links).

## When it is a pasted description only

Record what was described, label it "reported by the user, not seen", and keep every finding that
rests on it on the Could not verify list.

## What never to ask for

Login details, API keys or exports containing personal data (emails, names, phone numbers, user IDs).
If an export holds them, ask for a version without those columns, and say that finding PII in it is
itself a finding.
