from core.info import Info

class Board:

    def __init__( self, terrains=None ):
        if terrains:
            self.terrains = terrains
        else:
            self.terrains = {}

    def contain_terrain( self, terrain ):
        return terrain in self.terrains

    def retrieve_info( self, label ):
        if self.contain_terrain( label ):
            terrain = self.terrains[label]
            occupant = terrain.occupant
            return Info( terrain, occupant )
        return None
