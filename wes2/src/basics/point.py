class Point:
	"""
	A basic type that specifies a point in a bidimensional space
	Must be initialized with int arguments x and y
	"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, compare):
        return self._x == compare._x and self._y == compare._y