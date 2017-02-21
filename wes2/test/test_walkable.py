import unittest
from src.abstractions.walkable import Walkable
from src.abstractions.walker import Walker

class TestWalkable(unittest.TestCase):

    def test_import(self):
        assert Walkable
        assert Walker

    def test_walk_1_cost(self):
        wkr = Walker(3, True)
        wkb = Walkable(1)
        wkb.walk_to(wkr)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, 2)

    def test_walk_cost_more_than_energy(self):
        wkr = Walker(3, True)
        wkb = Walkable(4)
        success = wkb.walk_to(wkr)
        self.assertEqual(success, True)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, -1)

    def test_walk_without_energy(self):
        wkr = Walker(3, True)
        wkb = Walkable(4)
        success = wkb.walk_to(wkr)
        self.assertEqual(success, True)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, -1)
        success = wkb.walk_to(wkr)
        self.assertEqual(success, False)

if __name__ == '__main__':
    unittest.main()