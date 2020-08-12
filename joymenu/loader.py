import time

import joymenu.menuentries as menuentries


class Loader:
    def __init__(self, game):
        self.game = game

    def load(self, entry: menuentries.Entry):
        import subprocess
        with open(entry.script, 'r') as script_file:
            script = script_file.read()
        self.game.toggle_mode()
        returned_code = subprocess.call(script, shell=True)
        self.game.toggle_mode()
        from joymenu.controllers import InputHandler
        time.sleep(1)
        InputHandler.init_available_joysticks()
        return returned_code
