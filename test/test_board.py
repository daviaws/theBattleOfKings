import unittest
from core.board import Board

class TestBoard( unittest.TestCase ):

    def setUp( self ):
        self.terrains = [ "my_terrain_0", "my_terrains_1" ]
        self.board = Board()

    def test_board_contain_terrains( self ):
        for terreain in self.terrains:   
            self.assertTrue( self.board.contain_terrain( terreain ) )

    def test_retrieve_terrain_info( self ):
        for terreain in self.terrains:
            info = self.board.retrieve_terrain_info( terreain )
            self.assertIsNotNone( info )

if __name__ == '__main__':
    unittest.main()

