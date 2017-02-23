from src.basics.point import Point
from src.abstractions.allocable import Allocable

class InvalidX(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr("'{}' is lesser than 1".format(self.value))

class InvalidY(Exception):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr("'{}' is lesser than 1".format(self.value))

class Position(Point, Allocable):
    """
    A extension of point
    Must be initialized with int arguments x and y bigger than 0
    """
    def __init__(self, x, y):
        self.valid(x, y)
        Point.__init__(self, x, y)
        Allocable.__init__(self)

    def __str__(self):
        return '({}, {})'.format(Point.__str__(self), Allocable.__str__(self))

    def valid(self, x, y):
        """
        Test if arguments x and y are bigger than 0
        If x < 0 raise InvalidX exception
        If y < 0 raise InvalidX exception
        """
        if x < 1:
            raise InvalidX(x)
        if y < 1:
            raise InvalidY(y)

    def calculate_area(self):
        """
        Calculate the area of position referente to origin (1, 1)
        Return a list of positions beginning from Position(1, 1) to it limits (values x and y)
        The minor list of positions to be returned is [Position(1,1)]
        """
        area = []
        for x in range(1, self._x+1):
            for y in range(1, self._y+1):
                position = Position(x, y)
                area.append(position)
        return area
