from terrain import Terrain
from src.abstractions.allocable import Allocable

class WalkableTerrain(Terrain, Allocable):

    def __init__(self, name, modifier):
        Allocable.__init__(self)
        self.modifier = modifier

    def walk(self, walker):
        #allocate
        #success
        ##apply modifiers
        #fail
        ##return occuper
        pass

    def exit(self):
        #deply modifiers
        #deallocate
        ##return occuper
        pass