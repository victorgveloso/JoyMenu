import joymenu.menuentries as menuentries


class Loader:
    def load(self, entry: menuentries.Entry):
        import subprocess
        with open(entry.script, 'r') as script_file:
            script = script_file.read()
        return subprocess.call(script, shell=True)
