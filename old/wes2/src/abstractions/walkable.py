class Walkable:

	def __init__(self, cost):
		self.cost = cost

	def walk_to(self, walker):
		return walker.walk(self.cost)

	def __str__(self):
		return "Cost: {}".format(self.cost)