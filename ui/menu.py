from rich.console import Console
from rich.prompt import Prompt

from core.table_manager import create_table
from core.entry_manager import add_entry
from core.viewer import view_table
from reports.excel_export import export_excel
from reports.html_dashboard import generate_dashboard

console = Console()

def start_menu():

    while True:

        console.print("""

[bold cyan]

CN JOURNAL FORGE

Built-in Trackers
1 VAPT Projects
2 Red Team Projects
3 Git Tracker
4 Study Journal
5 Time Table
6 Personal Secure Vault

Custom
7 Create Custom Table

Actions
8 Add Entry
9 View Table

Reports
10 Export Excel
11 HTML Dashboard

0 Exit

[/bold cyan]

""")

        c = Prompt.ask("Select")

        if c == "7":
            create_table()

        elif c == "8":
            add_entry()

        elif c == "9":
            view_table()

        elif c == "10":
            export_excel()

        elif c == "11":
            generate_dashboard()

        elif c == "0":
            break
