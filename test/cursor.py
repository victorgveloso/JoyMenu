import unittest

import joymenu.menuentries as menuentries
import joymenu.cursor as cursor


class ParserStub:
    def __init__(self):
        self._entries = menuentries.MenuEntries()
        self._entries.add('a', 'a.png', 'a-selected.png', 'a.sh')
        self._entries.add('b', 'b.png', 'b-selected.png', 'b.sh')
        self._entries.add('c', 'c.png', 'c-selected.png', 'c.sh')
        self._entries.add('d', 'd.png', 'd-selected.png', 'd.sh')

    @property
    def entries(self):
        return self._entries


class CursorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = ParserStub()
        self.sut = cursor.Cursor(self.parser.entries, pos=1)

    def test_forward(self):
        self.assertEqual(self.sut.pos, 1)
        self.sut.forward()
        self.assertEqual(self.sut.pos, 2)

    def test_backward(self):
        self.assertEqual(self.sut.pos, 1)
        self.sut.backward()
        self.assertEqual(self.sut.pos, 0)

    def test_forward_on_last(self):
        for i in range(2):
            self.sut.forward()
        self.assertEqual(self.sut.pos, 3)
        self.sut.forward()
        self.assertEqual(self.sut.pos, 3)

    def test_backward_on_first(self):
        self.sut.backward()
        self.assertEqual(self.sut.pos, 0)
        self.sut.backward()
        self.assertEqual(self.sut.pos, 0)

    def test_pos(self):
        self.assertEqual(self.sut.pos, 1)
        self.assertEqual(cursor.Cursor(self.parser.entries).pos, 0)
        self.assertEqual(cursor.Cursor(self.parser.entries, pos=3).pos, 3)
        self.assertRaises(Exception, lambda: cursor.Cursor(self.parser.entries, pos=5))


if __name__ == '__main__':
    unittest.main()
