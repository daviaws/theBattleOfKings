import unittest

from core.info import Info
from core.terrain import Terrain

class TestInfo( unittest.TestCase ):

    def setUp( self ):
        self.terrain = Terrain('my_test')
        self.info = Info(self.terrain, self.terrain.occupant)

    def test_assert_terrain( self ):
        self.assertIs( self.info.terrain, self.terrain )

    def test_assert_occupant( self ):
        self.assertIs( self.info.occupant, self.terrain.occupant )

if __name__ == '__main__':
    unittest.main()
    