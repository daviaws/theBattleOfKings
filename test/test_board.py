import unittest

from core.board import Board
from core.terrain import Terrain
from core.info import Info

class TestBoard( unittest.TestCase ):

    def setUp( self ):
        terrain0 = Terrain("my_terrain_0", 1)
        terrain1 = Terrain("my_terrain_1")
        self.terrains = { terrain0.label: terrain0, terrain1.label: terrain1 }
        self.board = Board(self.terrains)

    def test_create_board( self ):
        self.assertEqual( self.board.terrains, self.terrains )

    def test_contain_terrains( self ):
        for label in self.terrains:   
            self.assertTrue( self.board.contain_terrain( label ) )

    def test_contain_equal_terrains( self ):
        for label in self.terrains:   
            self.assertEqual( self.board.terrains[label], self.terrains[label] )

    def test_retrieve_retrieve_info( self ):
        for label in self.terrains:
            info = self.board.retrieve_info( label )
            self.assertIsNotNone( info )

    def test_retrieve_inexistent_retrieve_info( self ):
        label = "my_inexistent_terrain"
        self.assertIsNone( self.board.retrieve_info(label) )

    def test_retrieve_info_equals_instance( self ):
        instance_of = Info
        for label in self.terrains:
            info = self.board.retrieve_info( label )
            self.assertIsInstance( info , instance_of )

    def test_retrieve_infos_terrain( self ):
        for label in self.terrains:
            info = self.board.retrieve_info( label )
            self.assertEqual( info.terrain , self.terrains[label] )

    def test_retrieve_infos_occupant( self ):
        for label in self.terrains:
            info = self.board.retrieve_info( label )
            self.assertEqual( info.occupant , self.terrains[label].occupant )

if __name__ == '__main__':
    unittest.main()
