class Board:

    def __init__( self, terrains=None ):
        if terrains:
            self.terrains = terrains
        else:
            self.terrains = {}

    def contain_terrain( self, terrain ):
        return terrain in self.terrains

    def retrieve_terrain_info( self, terrain ):
        if self.contain_terrain( terrain ):
            return self.terrains[terrain]
