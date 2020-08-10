from typing import List

import yaml


class Entry:
    def __init__(self, title, icon, selected_icon, script):
        self.title = title
        self.icon = icon
        self.selected_icon = selected_icon
        self.script = script

    def __repr__(self):
        return f"[t={self.title},i={self.icon},s={self.script}]"


class MenuEntries:
    def __init__(self):
        self.values: List[Entry] = []

    def __repr__(self):
        return self.values.__repr__()

    def add(self, title, icon, selected_icon, script) -> Entry:
        entry = Entry(title=title, icon=icon, selected_icon=selected_icon, script=script)
        self.values.append(entry)
        return entry

    def __len__(self):
        return len(self.values)


class Parser:
    def __init__(self):
        self._entries = MenuEntries()
        self.load_menu_entries()

    def load_menu_entries(self, path="joymenu.yaml"):
        with open(f'./{path}', 'r') as config:
            for entry in yaml.safe_load(config)['menu-entries']:
                self._entries.add(**entry)

    @property
    def entries(self):
        return self._entries
