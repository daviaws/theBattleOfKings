class Walker:
    """A movable unit.

    It has energy, max energy and always is in a terrain.
    It can move, rest, and waste energy.  

    Parameters
    ----------
    energy : int
        This will set the max energy and the actual energy of walker.

    terrain : Terrain instance
        Terrain that will be occupied by walker.
    """

    def __init__( self, energy, terrain ):
        self.max_energy = energy
        self.energy = energy
        terrain.occupy( self )
        self.terrain = terrain

    def has_energy( self, energy ):
        """Return a boolean representing if the walker energy is at least the energy argument.

        Parameters
        ----------
        energy : int
            Used in the comparison.

        Returns
        -------
        has : bool
            True if has energy.
            False otherwise.
        """
        return energy <= self.energy

    def waste_energy( self, energy ):
        """Deduct the amount of energy of argument from the walker energy.
        Can result in a negative walker energy.

        Parameters
        ----------
        energy : int
            The amount to be deducted.
        """
        self.energy -= energy

    def rest( self ):
        """Recover the walker energy to its max energy"""
        self.energy = self.max_energy

    def __occupy( self, terrain ):
        """Occupy the argument terrain.
        Desocuppy the actual terrain.

        Parameters
        ----------
        terrain : Terrain instance.
            The terrain to be occupied.
        """
        terrain.occupy( self )
        self.terrain.unoccupy()
        self.terrain = terrain

    def move( self, movement ):
        """Check the movement cost and movement destine.
        And execute the movement if possible that results
        in walker occupying the movement destine
        and wasting the movement cost from it energy.

        Parameters
        ----------
        movement : Movement instance
            Movement has a terrain : Terrain.
            Movement has a cost : int.

        Returns
        -------
        success : bool
            True if the walker has energy to afford from the movement cost
            AND the movement destine is unoccupied.
            False otherwise.
        """
        cost = movement.cost
        terrain = movement.terrain
        if self.has_energy( cost ):
            if not terrain.occupied():
                self.__occupy( terrain )
                self.waste_energy( cost )
                return True
        return False

    def is_at_terrain( self, terrain ):
        """Check if walker are at terrain.

        Parameters
        ----------
        terrain : core.terrain.Terrain

        Returns bool
        """
        return terrain != None and\
               terrain == self.terrain and\
               terrain.is_occupied_by( self )
