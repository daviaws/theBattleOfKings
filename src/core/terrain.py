class Terrain:

	def __init__( self, label, cost=1, occupant=None):
		self.label = label
		self.cost = cost
		self.occupant = occupant

	def info( self ):
		return self.cost

	def occupied( self ):
		return self.occupant is not None

	def occupy( self, occupant ):
		self.occupant = occupant

	def unoccupy( self ):
		self.occupant = None
