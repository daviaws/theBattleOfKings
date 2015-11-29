from src import terrain
from src import building
from src import position
import os

class Loader():
    
    RESOURCE_PATH = './resources/'
    BOARDS_PATH = RESOURCE_PATH + 'boards/'
    
    FOREST = 1
    ELVENCASTLE = 5
    
    def show_boards(self):
        list = os.listdir(self.BOARDS_PATH)
        list.remove('readme')
        return  list
    
    def load_board(self, board_name):
        board_path = self.BOARDS_PATH + board_name
        file = open(board_path)
         
        readed = file.readlines()
        
        table = {}
        castles_list = []
        
        l = 0
        
        for line in readed:
            c = 0
            element_list = line.split()
            for element in element_list:
                home = self.decode_element(c, l, element)
                table[home.getPosition().key()] = home
                if home.id == 'ElvenCastle':
                    castles_list.append(home.getPosition().key())
                c += 1
            l += 1
         
        return table, castles_list, (c,l)
        
    def decode_element(self, c, l, element):        
        element = int(element)
        if element == self.FOREST:
            pos = position.Position(c, l)
            element = terrain.Terrain('Forest', pos, None, True)
            return element
        elif element == self.ELVENCASTLE:
            pos = position.Position(c, l)
            element = building.Building('ElvenCastle', pos, None, True)
            return element