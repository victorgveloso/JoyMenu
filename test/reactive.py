import unittest
import unittest.mock as mock

import joymenu.loader as loader
import joymenu.cursor as cursor
from joymenu.reactive import ReactiveBroker


class ReactiveBrokerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.loader = mock.MagicMock(wraps=loader.Loader)
        self.cursor = mock.MagicMock(wraps=cursor.Cursor)
        self.sut = ReactiveBroker(self.cursor, self.loader)

    def test_one_forward(self):
        self.cursor.forward = mock.Mock()
        self.sut.register(self.sut.FORWARD)
        self.cursor.forward.assert_not_called()
        self.sut.react()
        self.cursor.forward.assert_called_once()

    def test_one_backward(self):
        self.cursor.backward = mock.Mock()
        self.sut.register(self.sut.BACKWARD)
        self.cursor.backward.assert_not_called()
        self.sut.react()
        self.cursor.backward.assert_called_once()

    def test_one_select(self):
        self.loader.load = mock.Mock()
        self.sut.register(self.sut.SELECT)
        self.loader.load.assert_not_called()
        self.sut.react()
        self.loader.load.assert_called_once_with(self.cursor.curr_entry)

    def test_three_register_one_react(self):
        self.cursor.forward = mock.Mock()
        for _ in range(3):
            self.sut.register(self.sut.FORWARD)
        self.cursor.forward.assert_not_called()
        self.sut.react()
        self.cursor.forward.assert_called_once()

    def test_one_register_three_react(self):
        self.cursor.forward = mock.MagicMock()
        self.sut.register(self.sut.FORWARD)
        self.cursor.forward.assert_not_called()
        for _ in range(3):
            self.sut.react()
        self.cursor.forward.assert_called_once()

    def test_forward_backward(self):
        self.cursor.backward = mock.Mock()
        self.cursor.forward = mock.Mock()
        self.sut.register(self.sut.BACKWARD)
        self.sut.register(self.sut.FORWARD)
        self.cursor.backward.assert_not_called()
        self.cursor.forward.assert_not_called()
        self.sut.react()
        self.cursor.backward.assert_called_once()
        self.cursor.forward.assert_called_once()

    def test_all_three_times(self):
        import random
        self.cursor.backward = mock.Mock()
        self.cursor.forward = mock.Mock()
        self.loader.load = mock.Mock()

        all_operations = [self.sut.BACKWARD, self.sut.FORWARD, self.sut.SELECT]

        for _ in range(3):
            random.shuffle(all_operations)
            for operation in all_operations:
                self.sut.register(operation)
        self.cursor.backward.assert_not_called()
        self.cursor.forward.assert_not_called()
        self.loader.load.assert_not_called()

        self.sut.react()
        self.cursor.backward.assert_called_once()
        self.cursor.forward.assert_called_once()
        self.loader.load.assert_called_once_with(self.cursor.curr_entry)
