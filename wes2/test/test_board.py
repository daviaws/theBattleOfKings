import unittest

from src.game.board import Board
from src.abstractions.position import Position

class TestBoard(unittest.TestCase):

    def setUp(self):
        position_limit = Position(2, 2)
        self.board = Board(position_limit)

    def test_import(self):
        assert Board

    def test_get_inexistent_position(self):
        p = Position(1, 3)
        self.assertIsNone(self.board.get_position(p))

    def test_get_position(self):
        p = Position(1, 1)
        self.assertEqual(p, self.board.get_position(p))

if __name__ == '__main__':
    unittest.main()