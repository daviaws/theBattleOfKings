import unittest

from core.info import Info
from core.terrain import Terrain
from core.walker import Walker

class TestInfo( unittest.TestCase ):

    def setUp( self ):
        self.terrain = Terrain('my_test')
        self.terrain2 = Terrain('my_test2', 3)
        self.occupant = Walker( 3, self.terrain2 )
        self.movement = 1
        self.info = Info(self.terrain, self.terrain.occupant, None)
        self.info2 = Info(self.terrain2, self.terrain2.occupant, self.movement)

    def test_assert_terrain( self ):
        self.assertIs( self.info.terrain, self.terrain )

    def test_assert_occupant_is_none( self):
        self.assertIs( self.info.occupant, self.terrain.occupant )

    def test_assert_occupant( self ):
        self.assertIs( self.info2.occupant, self.terrain2.occupant )

    def test_assert_movement_is_none( self ):
        self.assertIsNone( self.info.movements, None )

    def test_assert_movement_is_none( self ):
        self.assertIsNotNone( self.info2.movements, self.movement )

if __name__ == '__main__':
    unittest.main()
