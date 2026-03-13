import sqlite3
import json
from rich.table import Table
from rich.console import Console

console = Console()
DB = "data/journal.db"

def view_table():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    tables = c.execute(
        "SELECT id,table_name FROM tables"
    ).fetchall()

    for t in tables:
        console.print(f"{t[0]} - {t[1]}")

    tid = int(input("Table ID: "))

    rows = c.execute(
        "SELECT data FROM entries WHERE table_id=?",
        (tid,)
    ).fetchall()

    if not rows:
        console.print("No entries")
        return

    data_list = [json.loads(r[0]) for r in rows]

    table = Table()

    for col in data_list[0].keys():
        table.add_column(col)

    for row in data_list:
        table.add_row(*[str(v) for v in row.values()])

    console.print(table)
