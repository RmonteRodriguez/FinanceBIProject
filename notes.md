There are two david wilson both having differnt advisor id so they are two different people, they also have two differnt start dates and client counts

amount sign in raw data doesn't match txn_type direction; corrected using CASE + ABS in net_flow query

Metrics we are using Net Flow, Client Count, Account Count

## 1 Session summary

- Verified 3 metrics per advisor: client_count, account_count, net_flow
- All three cross-checked against known totals/values before trusting them
- Found and fixed: amount sign doesn't match txn_type (had to derive direction manually)
- Found and resolved: two advisors both named "David Wilson" (ids 8, 13) — different people, not a data error, but never group/join on advisor_name
- Gotcha: combining verified metrics into one bigger query silently reintroduced the amount-sign bug — Claude Code doesn't remember earlier validated logic unless you explicitly carry it forward
