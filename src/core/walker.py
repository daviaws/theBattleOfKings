class Walker:
    
    def __init__( self, energy, terrain ):
        self.terrain = terrain
        self.max_energy = energy
        self.energy = energy
        terrain.occupy( self )

    def has_energy( self, energy ):
        return energy <= self.energy

    def waste_energy( self, energy ):
        self.energy -= energy

    def rest( self ):
        self.energy = self.max_energy

    def occupy( self, terrain ):
        terrain.occupy( self )
        self.terrain = terrain

    def move( self, movement ):
        cost = movement.cost
        terrain = movement.terrain
        if self.has_energy( cost ):
            if not terrain.occupied():
                self.occupy( terrain )
                self.waste_energy( cost )
                return True
        return False
