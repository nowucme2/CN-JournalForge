import sqlite3
import json
from rich.console import Console
from rich.table import Table

console = Console()
DB = "data/journal.db"


def view_specific_table(table_name):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    row = c.execute(
        "SELECT id FROM tables WHERE table_name=?",
        (table_name,)
    ).fetchone()

    if not row:
        console.print("[red]Table not found[/red]")
        return

    table_id = row[0]

    rows = c.execute(
        "SELECT data FROM entries WHERE table_id=?",
        (table_id,)
    ).fetchall()

    if not rows:
        console.print("[yellow]No entries yet[/yellow]")
        return

    data_list = [json.loads(r[0]) for r in rows]

    table = Table(title=table_name)

    for col in data_list[0].keys():
        table.add_column(col)

    for row in data_list:
        table.add_row(*[str(v) for v in row.values()])

    console.print(table)

    conn.close()
