#!/usr/bin/env python3

from database.db import init_db
from ui.menu import start_menu

def main():

    init_db()
    start_menu()

if __name__ == "__main__":
    main()
