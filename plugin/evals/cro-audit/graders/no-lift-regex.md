---
type: regex
pattern: '(\d+\s*%\s*(more|higher|lift|increase|uplift|improvement|boost|better))|(lift|increase|uplift|improve|boost)[^.\n]{0,40}\d+\s*%'
match: not_contains
target: last_message
---
