import unittest
from src.abstractions.walker import Walker

class TestWalker(unittest.TestCase):

    def test_import(self):
        assert Walker

    def test_walk_1_cost(self):
        wkr = Walker(3, True)
        success = wkr.walk(1)
        self.assertEqual(success, True)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, 2)

    def test_create_rested(self):
        wkr = Walker(3, True)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, 3)

    def test_create_not_rested(self):
        wkr = Walker(3, False)
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, 0)

    def test_rest(self):
        wkr = Walker(3, False)
        wkr.rest()
        result_energy = wkr.get_energy()
        self.assertEqual(result_energy, 3)

if __name__ == '__main__':
    unittest.main()