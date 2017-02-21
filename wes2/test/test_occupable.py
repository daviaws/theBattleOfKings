import unittest
from src.abstractions.allocable import Allocable

class TestOccupable(unittest.TestCase):

    def test_import(self):
        assert Allocable

    def test_allocate_unocuppied(self):
        to_allocate = 1
        a = Allocable()
        self.assertIsNone(a.allocate(to_allocate))

    def test_allocate_ocuppied(self):
        occupant = 1
        to_allocate = 2
        a = Allocable()
        a.allocate(occupant)
        self.assertEqual(occupant, a.allocate(to_allocate))

    def test_deallocate_unocuppied(self):
        a = Allocable()
        self.assertIsNone(a.deallocate())

    def test_deallocate_ocuppied(self):
        occupant = 1
        a = Allocable()
        a.allocate(occupant)
        self.assertEqual(occupant, a.deallocate())

if __name__ == '__main__':
    unittest.main()