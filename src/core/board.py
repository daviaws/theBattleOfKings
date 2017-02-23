class Board:

	def __init__( self ):
		self.terrain = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

	def contain_terrain( self, terrain ):
		return True

	def retrieve_terrain_info( self, terrain ):
		return object()