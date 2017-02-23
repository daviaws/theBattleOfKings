import unittest

from src.abstractions.position import Position, InvalidX, InvalidY

class TestPosition(unittest.TestCase):

    def test_import(self):
        assert Position

    def test_create_position_with_lesser_than_1x_arg(self):
        try:
            Position(0,1)
        except Exception as e:
            self.assertIsInstance(e, InvalidX)

    def test_create_position_with_lesser_than_1y_arg(self):
        try:
            Position(1,0)
        except Exception as e:
            self.assertIsInstance(e, InvalidY)

    def test_valid_position(self):
        p = Position(1, 1)
        self.assertIsInstance(p, Position)

    def test_area_calculation(self):
        position_to_calculate = Position(2, 2)
        area_expected = [Position(1, 1), Position(1, 2), Position(2, 1), Position(2, 2)]
        area_calculated = position_to_calculate.calculate_area()
        self.assertEqual(area_expected, area_calculated)

if __name__ == '__main__':
    unittest.main()