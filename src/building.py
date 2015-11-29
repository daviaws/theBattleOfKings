import terrain

class Building(terrain.Terrain):
    
        def __init__(self, id, position, modifier, owner=None):
            super(id, position, modifier, True)
            self.owner = owner
            
        def hasOwner(self):
            if self.owner:
                return True
            return False
        
        def isOwner(self, player):
            if self.owner is player:
                return True
            return False
        
        def conquered(self, player):
            if self.hasOwner():
                if self.isOwner(player):
                    return
                self.owner.removeBuilding(self)
            self.owner = player
            self.owner.addBuilding(self)
