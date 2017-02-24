from core.info import Info

class Board:

    def __init__( self, terrains=None ):
        if terrains:
            self.terrains = terrains
        else:
            self.terrains = {}

    def contain_terrain( self, terrain ):
        return terrain in self.terrains

    def retrieve_info( self, terrain ):
        if self.contain_terrain( terrain ):
            terrain = self.terrains[terrain]
            return Info( terrain, terrain.occupant )
