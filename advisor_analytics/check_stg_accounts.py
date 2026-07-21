import duckdb

with duckdb.connect("dev.duckdb") as conn:
    rows = conn.execute("SELECT * FROM main.stg_accounts LIMIT 5;").fetchall()
    for row in rows:
        print(row)

    count = conn.execute("SELECT COUNT(*) FROM main.stg_accounts;").fetchone()[0]
    print(f"\nrow count: {count}")
