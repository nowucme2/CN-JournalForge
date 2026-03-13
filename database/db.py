import sqlite3
import os

DB = "data/journal.db"

def init_db():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS tables(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_name TEXT UNIQUE,
        description TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS fields(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER,
        field_name TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS entries(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        table_id INTEGER,
        data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    create_default_tables(conn)

    conn.close()


def create_default_tables(conn):

    c = conn.cursor()

    defaults = {

        "vapt_projects": [
            "project_name",
            "activity_name",
            "po_number",
            "quarter",
            "start_date",
            "end_date",
            "current_status",
            "remarks"
        ],

        "redteam_projects": [
            "project_name",
            "activity_name",
            "po_number",
            "quarter",
            "start_date",
            "end_date",
            "current_status",
            "remarks"
        ],

        "git_tracker": [
            "project_name",
            "project_type",
            "repository",
            "start_date",
            "last_update",
            "status",
            "notes"
        ],

        "study_journal": [
            "topic",
            "platform",
            "hours_spent",
            "progress_percent",
            "labs_completed",
            "labs_pending",
            "notes"
        ],

        "timetable": [
            "date",
            "start_time",
            "end_time",
            "activity_type",
            "task",
            "notes"
        ],

        "personal_secure": [
            "category",
            "title",
            "value",
            "expiry_date",
            "notes"
        ]
    }

    for table, fields in defaults.items():

        row = c.execute(
            "SELECT id FROM tables WHERE table_name=?",
            (table,)
        ).fetchone()

        if not row:

            c.execute(
                "INSERT INTO tables (table_name,description) VALUES (?,?)",
                (table,"built-in tracker")
            )

            table_id = c.lastrowid

            for f in fields:

                c.execute(
                    "INSERT INTO fields (table_id,field_name) VALUES (?,?)",
                    (table_id,f)
                )

    conn.commit()
