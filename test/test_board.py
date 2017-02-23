import unittest
from core.board import Board

class TestBoard( unittest.TestCase ):

    def setUp( self ):
        self.terrains = { "my_terrain_0": (1,1), "my_terrain_1": (2,2) }
        self.board = Board(self.terrains)

    def test_create_board( self ):
        self.assertEqual( self.board.terrains, self.terrains )

    def test_board_contain_terrains( self ):
        for terrain in self.terrains:   
            self.assertTrue( self.board.contain_terrain( terrain ) )

    def test_board_contain_equal_terrains( self ):
        for terrain in self.terrains:   
            self.assertEqual( self.board.retrieve_terrain_info( terrain ), self.terrains[terrain] )

    def test_retrieve_terrain_info( self ):
        for terrain in self.terrains:
            info = self.board.retrieve_terrain_info( terrain )
            self.assertIsNotNone( info )

    def test_retrieve_inexistent_terrain_info( self ):
        terrain = "my_inexistent_terrain"
        self.assertIsNone( self.board.retrieve_terrain_info(terrain) )

    def test_retrieve_terrain_info_equals_instance( self ):
        instance_of = tuple
        for terrain in self.terrains:
            info = self.board.retrieve_terrain_info( terrain )
            self.assertIsInstance( info , instance_of )

if __name__ == '__main__':
    unittest.main()
