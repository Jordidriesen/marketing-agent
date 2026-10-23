---
type: llm
weight: 3
---
The export has two planted problems that matter most for the stated decisions (Google Ads bidding on demo requests, and a channel report): (1) the demo-submit step has no working event: generate_lead has a count of 0 and the only key events are thank_you_view and scroll, so the form submit is not measured as the goal and scroll is wrongly a key event; (2) the UTM values use several conventions (google / Google, cpc / CPC, paid-social / Paid_Social, email / e-mail), splitting channels, plus 3,950 sessions in (not set).
PASS if the key-event problem (the missing generate_lead and the wrong key events, which may be several findings) is ranked first among the findings, and the UTM and (not set) problem appears within the first five findings. FAIL otherwise.
