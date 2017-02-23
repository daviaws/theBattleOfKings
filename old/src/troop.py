from src import position

class Troop():

    def __init__(self, id, attributes, terrain, player, acted=True):
        self.id = id
        self.attributes = attributes
        self.position = None
        self.terrain = None
        self.player = player
        self.acted = acted
        
        self.move(terrain)
    
    def getId(self):
        return self.id
    
    def getPosition(self):
        return self.position
    
    def calcMove(self):
        movesList = []
        
        minX = self.position.x - self.attributes.speed
        maxX = self.position.x + self.attributes.speed + 1
        minY = self.position.y - self.attributes.speed
        maxY = self.position.y + self.attributes.speed + 1
        
        for x2 in range(minX, maxX):
            for y2 in range(minY, maxY):
                new_pos = position.Position(x2,y2)
                if self.validMove(new_pos):
                    movesList.append(new_pos)
        
        return movesList  
    
    def validMove(self, position2):
        if (abs(self.position.x - position2.x) + abs(self.position.y - position2.y) <= self.attributes.speed):
            return True
        return False
    
    def move(self, terrain):
        if self.position:
            self.terrain.deallocate()
        self.terrain = terrain
        self.position = self.terrain.getPosition()
        self.terrain.allocate(self)