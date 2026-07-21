There are two david wilson both having differnt advisor id so they are two different people, they also have two differnt start dates and client counts

amount sign in raw data doesn't match txn_type direction; corrected using CASE + ABS in net_flow query

Metrics we are using Net Flow, Client Count, Account Count

## 1 Session summary

- Verified 3 metrics per advisor: client_count, account_count, net_flow
- All three cross-checked against known totals/values before trusting them
- Found and fixed: amount sign doesn't match txn_type (had to derive direction manually)
- Found and resolved: two advisors both named "David Wilson" (ids 8, 13) — different people, not a data error, but never group/join on advisor_name
- Gotcha: combining verified metrics into one bigger query silently reintroduced the amount-sign bug — Claude Code doesn't remember earlier validated logic unless you explicitly carry it forward

---

## Session 2 notes

- stg means staging

---

## Session 3 notes

- Upper/Lower works exactly like TOUPPER/TOLOWER()
- Trim removes extra spaces or anything from the value
- All 4 staging models complete + verified: stg_advisors, stg_clients, stg_accounts, stg_transactions
- Found real dbt error: amount was auto-typed as DOUBLE by dbt seed (not TEXT like SQLite version) — had to drop the TRIM/NULLIF text-handling logic since it no longer applied
- Next: mart layer (dim_clients, fact_transactions, mart_advisor_performance), then Streamlit app
