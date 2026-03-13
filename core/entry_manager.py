import sqlite3
import json
from rich.prompt import Prompt
from rich.console import Console

console = Console()

DB = "data/journal.db"

def add_entry():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    tables = c.execute(
        "SELECT id,table_name FROM tables"
    ).fetchall()

    for t in tables:
        console.print(f"{t[0]} - {t[1]}")

    tid = Prompt.ask("Select table ID")

    fields = c.execute(
        "SELECT field_name FROM fields WHERE table_id=?",
        (tid,)
    ).fetchall()

    data = {}

    for f in fields:

        value = Prompt.ask(f[0])
        data[f[0]] = value

    c.execute(
        "INSERT INTO entries(table_id,data) VALUES (?,?)",
        (tid,json.dumps(data))
    )

    conn.commit()
    conn.close()

    console.print("[green]Entry added[/green]")
