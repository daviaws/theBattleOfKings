import unittest

from core.terrain import Terrain

DEFAULT_COST = 1

class TestTerrain( unittest.TestCase ):

    def setUp( self ):
        self.label = "g1"
        self.cost = 2
        self.occupant = 1
        self.terrain = Terrain( self.label, self.cost, self.occupant)
        self.terrain1 = Terrain( self.label )

    def test_label( self ):
        self.assertIsNotNone( self.terrain.label )

    def test_label_equal( self ):
        self.assertEqual( self.terrain.label, self.label )

    def test_cost( self ):
        self.assertEqual( self.terrain.cost, self.cost )

    def test_default_cost( self ):
        self.assertEqual( self.terrain1.cost, DEFAULT_COST )

    def test_info( self ):
        self.assertIsNotNone( self.terrain.info() )

    def test_info_equals( self ):
        self.assertEqual( self.terrain.info(), self.cost )

    def test_occupied( self ):
        self.assertTrue( self.terrain.occupied() )

    def test_unoccupied( self ):
        self.assertFalse( self.terrain1.occupied() )

    def test_occupy( self ):
        self.assertEqual( self.terrain.occupant, self.occupant )

    def test_occupy_many( self ):
        for occupant in range(2):
            self.terrain.occupy( occupant )
            self.assertEqual( self.terrain.occupant, occupant )            

    def test_unoccupy( self ):
        self.terrain.unoccupy()
        self.assertIsNone( self.terrain.occupant )

if __name__ == '__main__':
    unittest.main()
    