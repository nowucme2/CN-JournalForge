import sqlite3
import json
from rich.prompt import Prompt
from rich.console import Console

console = Console()

DB = "data/journal.db"


def add_entry_to_table(table_name):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    table = c.execute(
        "SELECT id FROM tables WHERE table_name=?",
        (table_name,)
    ).fetchone()

    if not table:
        console.print("[red]Table not found[/red]")
        return

    table_id = table[0]

    fields = c.execute(
        "SELECT field_name FROM fields WHERE table_id=?",
        (table_id,)
    ).fetchall()

    data = {}

    console.print(f"[cyan]Adding entry to {table_name}[/cyan]")

    for f in fields:

        value = Prompt.ask(f[0])
        data[f[0]] = value

    c.execute(
        "INSERT INTO entries(table_id,data) VALUES (?,?)",
        (table_id,json.dumps(data))
    )

    conn.commit()
    conn.close()

    console.print("[green]Entry added successfully[/green]")
