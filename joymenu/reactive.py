from joymenu import cursor as cursor, loader as loader


class ReactiveBroker:
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'
    SELECT = 'SELECT'

    def __init__(self, cursor_ctrl: cursor.Cursor, loader_ctrl: loader.Loader):
        self.react_to = set()
        self.cursor = cursor_ctrl
        self.loader = loader_ctrl

    def register(self, value):
        self.react_to.add(value)

    def react(self):
        for i in self.react_to:
            if i == self.FORWARD:
                self.cursor.forward()
            elif i == self.BACKWARD:
                self.cursor.backward()
            elif i == self.SELECT:
                self.loader.load(self.cursor.curr_entry)
        self.react_to.clear()
