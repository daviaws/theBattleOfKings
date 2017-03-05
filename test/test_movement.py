import unittest

from core.terrain import Terrain
from core.movement import Movement

class TestMovement( unittest.TestCase ):

    def setUp( self ):
        self.cost = 3
        self.terrain = Terrain('my_test')
        self.movement = Movement( self.cost, self.terrain )

    def test_movement_invalid_constrution( self ):
        with self.assertRaises( TypeError ):
            Movement( None, None )

        with self.assertRaises( TypeError ):
            Movement( None, Terrain( "terrain_01" ) )

        with self.assertRaises( TypeError ):
            Movement( 0, None )

    def test_movement_cost_equals( self ):
        self.assertEqual( self.movement.cost, self.cost )

    def test_movement_terrain_equal( self ):
        self.assertIs( self.movement.terrain, self.terrain )

if __name__ == '__main__':
    unittest.main()
