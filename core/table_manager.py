import sqlite3
from rich.prompt import Prompt
from rich.console import Console

console = Console()
DB = "data/journal.db"

def create_table():

    name = Prompt.ask("Table name")
    desc = Prompt.ask("Description")

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO tables(table_name,description) VALUES (?,?)",
        (name,desc)
    )

    table_id = c.lastrowid

    console.print("Add fields (type 'done' to finish)")

    while True:

        field = Prompt.ask("Field name")

        if field == "done":
            break

        c.execute(
            "INSERT INTO fields(table_id,field_name) VALUES (?,?)",
            (table_id,field)
        )

    conn.commit()
    conn.close()

    console.print("[green]Table created[/green]")
