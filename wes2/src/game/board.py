class Board:
    """
    A board to be used in board-games
    It must be initialized with a limit-point that will calculate the area
    The limit-point must have a method calculate_area() that returns a list of the points type
    """

    def __init__(self, limit):
        self.area = []
        self.set_area(limit)

    def set_area(self, limit):
        """
        Uses the calculate_area() from the limit-point to initialize the area attribute
        """
        self.area = limit.calculate_area()

    def get_position(self, position):
        """
        Receives a position argument that will be asserted
        The assertion is made comparing the given position with the elements in area attribute
        Return the position in area if asserted
        Return None if don't assert
        """
        for compare_position in self.area:
            if position == compare_position:
                return position
        return None