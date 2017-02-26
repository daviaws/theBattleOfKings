class Terrain:

    def __init__( self, label, cost=1, adjacents=None):
        self.label = label
        self.cost = cost
        self.occupant = None
        if adjacents:
            self.adjacents = list(adjacents)
        else:
            self.adjacents = []

    def occupied( self ):
        return self.occupant is not None

    def occupy( self, occupant ):
        self.occupant = occupant

    def unoccupy( self ):
        self.occupant = None
