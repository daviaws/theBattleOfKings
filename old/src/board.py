from src import position
from src import terrain

class Board():
    
    def __init__(self, table):
        self.table = table
    
    def getHome(self, tuplePosition):
        return self.table[tuplePosition]