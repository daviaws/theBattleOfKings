import unittest

from src.basics.point import Point

class TestPoint(unittest.TestCase):

    def test_import(self):
        assert Point

    def test_point_is_equal(self):
        p1 = Point(1, 1)
        p2 = Point(1, 1)
        self.assertEqual(p1, p2)

    def test_point_is_not_equal(self):
        p1 = Point(1, 1)
        p2 = Point(1, 2)
        self.assertNotEqual(p1, p2)

if __name__ == '__main__':
    unittest.main()