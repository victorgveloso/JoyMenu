import joymenu.menuentries as menuentries


class Cursor:
    def __init__(self, entries: menuentries.MenuEntries, pos=0):
        self._entries = entries
        if pos < len(entries):
            self._pos = pos
        else:
            raise IndexError(f"Pos ({pos}) is bigger than or equal to entries size ({len(entries)})")

    def __repr__(self):
        return f"Cursor(pos:{self._pos},{self._entries})"

    def forward(self):
        self._pos = min((self._pos + 1), len(self._entries) - 1)

    def backward(self):
        self._pos = max((self._pos - 1), 0)

    @property
    def curr_entry(self):
        return self._entries.values[self._pos]

    @property
    def pos(self):
        return self._pos
