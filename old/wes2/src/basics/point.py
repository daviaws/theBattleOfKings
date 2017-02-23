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

    def __str__(self):
        return '({},{})'.format(self._x, self._y)

    def __repr__(self):
        return self.__str__()

    def calculate_distance(self, point):
        reference = self._x + self._y
        comparison = point._x + point._y
        distance = abs(reference - comparison)
        return distance

    def calculate_points(self, distance):
        points = []
        originx = self._x
        originy = self._y
        for newx in range(originx - distance, originx + distance + 1):
            movex = abs(originx - newx)
            for newy in range(originy - distance + movex, originy + distance - movex + 1):
                p = Point(newx, newy)
                if p not in points:
                    points.append(p)
        return points


    def calculate_points_positive_only(self, distance):
        points = []
        originx = self._x
        originy = self._y
        for newx in range(originx - distance, originx + distance + 1):
            movex = abs(originx - newx)
            for newy in range(originy - distance + movex, originy + distance - movex + 1):
                p = Point(newx, newy)
                if not p.have_negative_cood():
                    if p not in points:
                        points.append(p)
        return points

    def have_negative_cood(self):
        if self._x < 0 or self._y < 0:
            return True
        return False