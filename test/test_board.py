import unittest

from core.board import Board
from core.terrain import Terrain
from core.walker import Walker
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

    def test_create_graph( self ):
        terrains = {}
        nodes = []
        edges = []
        for i in range( 0, 100 ):
            nodes.append(i)
            if i == 0:
                adjacents = [i+1]
                edges.append( ( i, i+1 ) )
            elif i == 99:
                adjacents = [i-1]
                edges.append( ( i, i-1 ) )
            else:
                edges.append( ( i, i-1 ) )
                edges.append( ( i, i+1 ) )
                adjacents = [i-1, i+1]
            terrains[i] = Terrain( i, cost=i, adjacents=adjacents )
        board = Board( terrains )
        self.assertEqual( board.graph.nodes(), nodes )
        self.assertEqual( sorted( board.graph.edges() ), sorted( edges ) )
        for edge in edges:
            weight = board.graph.get_edge_data( edge[0], edge[1] )[0]['weight']
            self.assertEqual( terrains[edge[1]].cost, weight )

    def create_movement_board( self ):
        self.terrain1 = Terrain( 1, adjacents=[2,6] )
        self.terrain2 = Terrain( 2, adjacents=[2,3,4,5] )
        self.terrain3 = Terrain( 3 )
        self.terrain4 = Terrain( 4 )
        self.terrain5 = Terrain( 5 )
        self.terrain6 = Terrain( 6, adjacents=[7] )
        self.terrain7 = Terrain( 7, adjacents=[5] )
        self.terrains = {
                            self.terrain1.label : self.terrain1,
                            self.terrain2.label : self.terrain2,
                            self.terrain3.label : self.terrain3,
                            self.terrain4.label : self.terrain4,
                            self.terrain5.label : self.terrain5,
                            self.terrain6.label : self.terrain6,
                            self.terrain7.label : self.terrain7,
                        }
        self.board = Board( self.terrains )

    def test_calcule_of_movements( self ):
        self.create_movement_board()
        test_movements = {6: 1, 2: 1, 3: 2, 7: 2, 5: 2, 4: 2, 1: 0}
        walker = Walker( 3, self.terrain1 )
        info = self.board.retrieve_info( self.terrain1.label )
        possible_movements = info.movements
        self.assertEqual( possible_movements, test_movements )

if __name__ == '__main__':
    unittest.main()
