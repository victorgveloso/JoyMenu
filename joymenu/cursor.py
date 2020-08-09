import joymenu.menuentries as menuentries


class Cursor:
    def __init__(self, entries: menuentries.MenuEntries, pos=0):
        self._entries = entries
        if pos < len(entries):
            self._pos = pos
        else:
            raise IndexError(f"Pos ({pos}) is bigger than or equal to entries size ({len(entries)})")

    def forward(self):
        if self._pos + 1 < len(self._entries):
            self._pos += 1
        else:
            raise IndexError("Cursor is already on the last entry")

    def backward(self):
        if self._pos >= 1:
            self._pos -= 1
        else:
            raise IndexError("Cursor is already on the first entry")

    @property
    def curr_entry(self):
        return self._entries.values[self._pos]

    @property
    def pos(self):
        return self._pos
