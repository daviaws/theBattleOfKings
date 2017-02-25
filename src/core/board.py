from networkx import MultiDiGraph
from core.info import Info

class Board:

    def __init__( self, terrains=None ):
        if terrains:
            self.terrains = terrains
        else:
            self.terrains = {}
        self.graph = MultiDiGraph()
        self.__populate_graph()

    def terrain_cost( self, label ):
        return self.terrains[label].cost

    def __populate_graph( self ):
        for src_label, terrain in self.terrains.items():
            for dst_label in terrain.adjacents:
                weight = self.terrain_cost( dst_label )
                self.graph.add_edge(src_label, dst_label, weight=weight)

    def contain_terrain( self, label ):
        return label in self.terrains

    def retrieve_info( self, label ):
        if self.contain_terrain( label ):
            terrain = self.terrains[label]
            occupant = terrain.occupant
            return Info( terrain, occupant )
        return None
