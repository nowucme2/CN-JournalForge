from rich.console import Console
from rich.prompt import Prompt

from core.entry_manager import add_entry_to_table
from core.viewer import view_specific_table
from core.table_manager import create_table
from reports.excel_export import export_excel
from reports.html_dashboard import generate_dashboard

console = Console()


def tracker_menu(table):

    while True:

        console.print(f"""

[bold green]{table.upper()}[/bold green]

1 Add Entry
2 View Entries
0 Back

""")

        c = Prompt.ask("Select")

        if c == "1":
            add_entry_to_table(table)

        elif c == "2":
            view_specific_table(table)

        elif c == "0":
            break


def start_menu():

    while True:

        console.print("""

[bold cyan]

🐺 CN JOURNAL FORGE

Built-in Trackers
1 VAPT Projects
2 Red Team Projects
3 Git Tracker
4 Study Journal
5 Time Table
6 Personal Secure Vault

Custom
7 Create Custom Table

Reports
8 Export Excel
9 HTML Dashboard

0 Exit

[/bold cyan]

""")

        c = Prompt.ask("Select")

        if c == "1":
            tracker_menu("vapt_projects")

        elif c == "2":
            tracker_menu("redteam_projects")

        elif c == "3":
            tracker_menu("git_tracker")

        elif c == "4":
            tracker_menu("study_journal")

        elif c == "5":
            tracker_menu("timetable")

        elif c == "6":
            tracker_menu("personal_secure")

        elif c == "7":
            create_table()

        elif c == "8":
            export_excel()

        elif c == "9":
            generate_dashboard()

        elif c == "0":
            break
