import duckdb

TABLES = ["advisors", "clients", "accounts", "transactions"]

with duckdb.connect("dev.duckdb") as conn:
    for table in TABLES:
        count = conn.execute(f"SELECT COUNT(*) FROM {table};").fetchone()[0]
        print(f"{table}: {count} rows")
