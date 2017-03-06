import unittest

from core.terrain import Terrain
from core.movement import Movement

class TestMovement( unittest.TestCase ):

    def setUp( self ):
        self.cost = 3
        self.terrain = Terrain('my_test')
        self.movement = Movement( self.cost, self.terrain )

    def test_movement_cost( self ):
        self.assertEqual( self.movement.cost, self.cost )

    def test_movement_terrain( self ):
        self.assertIs( self.movement.terrain, self.terrain )

if __name__ == '__main__':
    unittest.main()
