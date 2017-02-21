from terrain import Terrain
from src.abstractions.allocable import Allocable
from src.abstractions.walkable import Walkable

class WalkableTerrain(Terrain, Walkable, Allocable):

    def __init__(self, name, speed, modifier):
        Allocable.__init__(self)
        Walkable.__init__(self, speed)
    