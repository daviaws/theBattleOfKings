class Allocable:
	'''
	A class that represents something that have an space to allocate something
	'''
	def __init__(self):
		self.allocated = None

	def allocate(self, to_allocate):
		'''
		Allocate some object in the space
		The argument to_allocate can be any object
		The return is None if it was allocated with success
		The return is the actual allocated if already occupied (dont allocate the new)
		'''
		if self.allocated:
			return self.allocated
		self.allocated = to_allocate
		return None

	def deallocate(self):
		'''
		Remove and returns the actual allocated
		Returns None if it is empty
		'''
		allocated = self.allocated
		self.allocated = None
		return allocated

	def see(self):
		return self.allocated