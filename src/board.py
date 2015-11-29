import position
import terrain

class Board():
    
    def __init__(self):
        self.terrains = {}
    
    def genBoard(self, x, y):
        for i in range(0,x+1):
            for j in range(0,y+1):
                new_pos = position.Position(i, j)
                plain = terrain.Terrain('Plain', None, True)
                self.terrains[new_pos] = plain