import looser

class Player():
    
    def __init__(self):
        self.buildings = []
        self.troops = []
        self.resources = {}
        self.turn = False
        self.loose = False
        
    def removeTroop(self, troop):
        self.troops.remove(troop)
        if issubclass(troop, looser.Looser):
            troop.loose()
    
    def addTroop(self, troop):
        self.troops.append(troop)
    
    def removeBuilding(self, building):
        self.buildings.remove(building)
        if issubclass(building, looser.Looser):
            building.loose()
            
    def addBuilding(self):
    