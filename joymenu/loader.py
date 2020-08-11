import joymenu.menuentries as menuentries


class Loader:
    def __init__(self, game):
        self.game = game

    def load(self, entry: menuentries.Entry):
        import subprocess
        with open(entry.script, 'r') as script_file:
            script = script_file.read()
        self.game.toggle_mode()
        return subprocess.call(script, shell=True)
