import duckdb

with duckdb.connect("dev.duckdb") as conn:
    rows = conn.execute("SELECT * FROM main.stg_advisors LIMIT 5;").fetchall()
    for row in rows:
        print(row)

    count = conn.execute("SELECT COUNT(*) FROM main.stg_advisors;").fetchone()[0]
    print(f"\nrow count: {count}")
