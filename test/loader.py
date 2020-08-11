import unittest

import joymenu.menuentries as entries
import joymenu.loader as loader
import os


class LoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.entry = entries.Entry('', '', '', './script-mock.sh')
        self.sut = loader.Loader()
        self.code = 113
        with open(self.entry.script, 'w') as file:
            file.write(f'''uname -r
exit {self.code}''')

    def tearDown(self) -> None:
        os.remove(self.entry.script)

    def test_load(self):
        status_code = self.sut.load(self.entry)
        self.assertEqual(status_code, self.code)
