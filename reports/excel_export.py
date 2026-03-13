import sqlite3
import json
import pandas as pd

DB = "data/journal.db"

def export_excel():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    tables = c.execute("SELECT id,table_name FROM tables").fetchall()

    writer = pd.ExcelWriter("journal_export.xlsx")

    for t in tables:

        rows = c.execute(
            "SELECT data FROM entries WHERE table_id=?",
            (t[0],)
        ).fetchall()

        if not rows:
            continue

        data = [json.loads(r[0]) for r in rows]

        df = pd.DataFrame(data)

        df.to_excel(writer, sheet_name=t[1], index=False)

    writer.close()

    print("Excel report exported")
