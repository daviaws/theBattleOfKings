class Terrain():
    
    def __init__(self, id, modifier, walkable):
        self.id = id
        self.modifier = modifier
        self.walkable = walkable
        
        self.troop = None