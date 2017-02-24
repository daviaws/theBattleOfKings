import unittest

from core.terrain import Terrain
from core.moviment import Moviment

class TestMoviment( unittest.TestCase ):

    def setUp( self ):
        self.cost = 3
        self.terrain = Terrain('my_test')
        self.moviment = Moviment( self.cost, self.terrain )

    def test_moviment_cost( self ):
        self.assertIsNotNone( self.moviment.cost )

    def test_moviment_cost_equals( self ):
        self.assertEqual( self.moviment.cost, self.cost )

    def test_moviment_terrain_not_none( self ):
        self.assertIsNotNone( self.moviment.terrain )

    def test_moviment_terrain( self ):
        self.assertIsInstance( self.moviment.terrain, Terrain )

    def test_moviment_terrain_equal( self ):
        self.assertIs( self.moviment.terrain, self.terrain )

if __name__ == '__main__':
    unittest.main()
