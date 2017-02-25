class Terrain:

    def __init__( self, label, cost=1, occupant=None, adjacents=None):
        self.label = label
        self.cost = cost
        self.occupant = occupant
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
