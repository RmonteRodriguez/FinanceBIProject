import csv
import sqlite3
from pathlib import Path

TABLES = ["advisors", "clients", "accounts", "transactions"]
SEEDS_DIR = Path("advisor_analytics/seeds")

with sqlite3.connect("source.db") as conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute(f"SELECT * FROM {table};")
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        out_path = SEEDS_DIR / f"{table}.csv"
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(columns)
            writer.writerows(rows)

        print(f"{table}: wrote {len(rows)} rows to {out_path}")
