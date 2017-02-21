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

    def test_distance(self):
        reference = Point(1, 1)
        p = Point(2, 2)
        self.assertEqual(reference.calculate_distance(p), 2)
        p = Point(0, 0)
        self.assertEqual(reference.calculate_distance(p), 2)
        p = Point(-1, -1)
        self.assertEqual(reference.calculate_distance(p), 4)
        p = Point(0, 1)
        self.assertEqual(reference.calculate_distance(p), 1)
        p = Point(10, 1)
        self.assertEqual(reference.calculate_distance(p), 9)
        p = Point(10, 3)
        self.assertEqual(reference.calculate_distance(p), 11)

    def test_calcule_points00(self):
        points_comparison = [Point(-2, 0), Point(-1, 0), Point(0, 0), Point(2, 0), Point(1, 0),
                            Point(-1, 1), Point(0, 1), Point(1, 1), Point(-1, -1), Point(0, -1),
                            Point(1, -1), Point(0, -2), Point(0, 2)]
        reference = Point(0, 0)
        distance = 2
        calculated = reference.calculate_points(distance)
        for point in points_comparison:
            self.assertIn(point, calculated)
        for point in calculated:
            self.assertIn(point, points_comparison)

    def test_calcule_points11(self):
        points_comparison = [Point(-1, 1), Point(0, 1), Point(1, 1), Point(3, 1), Point(2, 1),
                            Point(0, 2), Point(1, 2), Point(2, 2), Point(0, 0), Point(1, 0),
                            Point(2, 0), Point(1, -1), Point(1, 3)]
        reference = Point(1, 1)
        distance = 2
        calculated = reference.calculate_points(distance)
        for point in points_comparison:
            self.assertIn(point, calculated)
        for point in calculated:
            self.assertIn(point, points_comparison)

    def test_calcule_points11_only_positive(self):
        points_comparison = [Point(0, 1), Point(1, 1), Point(3, 1), Point(2, 1),
                            Point(0, 2), Point(1, 2), Point(2, 2), Point(0, 0), Point(1, 0),
                            Point(2, 0), Point(1, 3)]
        reference = Point(1, 1)
        distance = 2
        calculated = reference.calculate_points_positive_only(distance)
        for point in points_comparison:
            self.assertIn(point, calculated)
        for point in calculated:
            self.assertIn(point, points_comparison)

if __name__ == '__main__':
    unittest.main()