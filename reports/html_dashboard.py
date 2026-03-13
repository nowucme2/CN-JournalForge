import sqlite3
import webbrowser
from jinja2 import Template

DB = "data/journal.db"

def generate_dashboard():

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    tables = c.execute("SELECT table_name FROM tables").fetchall()

    html = """
    <html>
    <body style="background:#0f172a;color:white;font-family:Arial">

    <h1>🐺 CN Journal Dashboard</h1>

    <h2>Available Trackers</h2>

    <ul>
    {% for t in tables %}
    <li>{{t[0]}}</li>
    {% endfor %}
    </ul>

    </body>
    </html>
    """

    output = Template(html).render(tables=tables)

    open("dashboard.html","w").write(output)

    webbrowser.open("dashboard.html")
