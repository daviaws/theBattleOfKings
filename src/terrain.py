class Terrain():
    
    def __init__(self, id, position, modifier, walkable):
        self.id = id
        self.position = position
        self.modifier = modifier
        self.walkable = walkable
        
        self.troop = None
    
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    
    def allocate(self, troop):
        self.troop = troop
        
    def deallocate(self, troop):
        self.troop = None
        
    def hasTroop(self):
        if self.troop:
            return True
        return False
    
    def getTroop(self):
        return self.troop