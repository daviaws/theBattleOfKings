from src.abstractions.walker import Walker

class Troop(Walker):

	def __init__(self, name, max_energy):
		self.name = name
		Walker.__init__(self, max_energy)

	def __str__(self):
		return '({}, {})'.format(self.name, Walker.__str__(self))
