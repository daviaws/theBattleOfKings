class Board:
    """
    A board to be used in board-games
    It must be initialized with a limit-point that will calculate the area
    The limit-point must have a method calculate_area() that returns a list of the points type
    """

    def __init__(self):
        self.area = []

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return self.area

    def set_area(self, area):
        """
        Uses the calculate_area() from the limit-point to initialize the area attribute
        """
        self.area = area

    def get_position(self, position):
        """
        Receives a position argument that will be asserted
        The assertion is made comparing the given position with the elements in area attribute
        Return the position in area if asserted
        Return None if don't assert
        """
        for square in self.area:
            if position == square:
                return square
        return None
