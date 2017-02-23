from src import building

class ResourceGenerator(building.Building):
    
    def __init__(self, id, position, modifier, resource, frequency, owner = None):
        super.__init__(self, id, position, modifier, owner=None)
        self.resource = resource
        self.frequency = frequency
        self.turn = 0
        
    def work(self):
        self.turn += 1
        if self.calcGeneration():
            self.owner.addResource(self.resource)
        
    def calcGeneration(self):
        if not self.turn % self.frequency:
            return True
        return False