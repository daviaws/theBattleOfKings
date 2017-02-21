class Walker:

    def __init__(self, max_energy, rested):
        self._max_energy = max_energy
        if rested:
            self._energy = max_energy
        else:
            self._energy = 0

    def get_max_energy(self):
        return self._max_energy

    def get_energy(self):
        return self._energy

    def have_energy(self):
        return self._energy > 0

    def walk(self, speed):
        if not self.have_energy():
            return False
        self._energy -= speed
        return True

    def rest(self):
        self._energy = self._max_energy