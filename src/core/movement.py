class Movement:

    def __init__( self, cost, terrain ):
        self.cost = cost
        self.terrain = terrain

    def get_cost( self ):
        return self.__cost

    def set_cost( self, cost ):
        if not isinstance( cost, int ):
            raise TypeError( "Property cost must be int" )

        self.__cost = cost

    def get_terrain( self ):
        return self.__terrain

    def set_terrain( self, terrain ):
        import core
        if not isinstance( terrain, core.terrain.Terrain ):
            raise TypeError( "Property terrain must be core.terrain.Terrain" )

        self.__terrain = terrain

    cost = property( get_cost, set_cost )
    terrain = property( get_terrain, set_terrain )
