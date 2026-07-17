import sqlite3

with sqlite3.connect("source.db") as conn:
    cur = conn.cursor()

    cur.execute("""
        WITH client_counts AS (
            SELECT advisor_id, COUNT(client_id) AS client_count
            FROM clients
            GROUP BY advisor_id
        ),
        account_counts AS (
            SELECT c.advisor_id, COUNT(acc.account_id) AS account_count
            FROM clients c
            JOIN accounts acc ON c.client_id = acc.client_id
            GROUP BY c.advisor_id
        ),
        net_flows AS (
    SELECT
        c.advisor_id,
        SUM(
            CASE
                WHEN t.txn_type IN ('deposit', 'dividend') THEN ABS(CAST(t.amount AS REAL))
                WHEN t.txn_type IN ('withdrawal', 'fee') THEN -ABS(CAST(t.amount AS REAL))
            END
        ) AS net_flow
    FROM clients c
    JOIN accounts acc ON c.client_id = acc.client_id
    JOIN transactions t ON acc.account_id = t.account_id
    GROUP BY c.advisor_id
)
        SELECT
            a.advisor_id,
            a.advisor_name,
            COALESCE(cc.client_count, 0) AS client_count,
            COALESCE(ac.account_count, 0) AS account_count,
            COALESCE(nf.net_flow, 0) AS net_flow
        FROM advisors a
        LEFT JOIN client_counts cc ON a.advisor_id = cc.advisor_id
        LEFT JOIN account_counts ac ON a.advisor_id = ac.advisor_id
        LEFT JOIN net_flows nf ON a.advisor_id = nf.advisor_id
        ORDER BY net_flow DESC;
    """)
    print(f"{'ID':<5}{'Name':<25}{'Client Count':<15}{'Account Count':<15}{'Net Flow':<15}")
    for advisor_id, advisor_name, client_count, account_count, net_flow in cur.fetchall():
        print(f"{advisor_id:<5}{advisor_name:<25}{client_count:<15}{account_count:<15}{net_flow:<15.2f}")