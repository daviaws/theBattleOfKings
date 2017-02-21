from src.concrete.terrain import Terrain
from src.abstractions.allocable import Allocable
from src.abstractions.walkable import Walkable

class WalkableTerrain(Terrain, Walkable, Allocable):

    def __init__(self, name, cost):
        Terrain.__init__(self, name)
        Allocable.__init__(self)
        Walkable.__init__(self, cost)

    def walk_to(self, walker):
        success = Walkable.walk_to(self, walker)
        if success:
            Allocable.allocate(self, walker)
        return success

    def __str__(self):
        return "({}: {}, {})".format(Terrain.__str__(self), Walkable.__str__(self), Allocable.__str__(self))
