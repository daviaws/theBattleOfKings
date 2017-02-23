from src import board
from src import player

from src import troop
from src import attributes

from control import loader

class System():
    
    def __init__(self):
        self.loader = loader.Loader()
        
        self.board = None
        self.players = []
        
        self.not_owned_castles = []
        
    def start_match(self, board_name):
        b, self.not_owned_castles, map_length = self.loader.load_board(board_name)
        self.board = board.Board(b)
        
        player1 = player.Player('Player1')
        castle = self.not_owned_castles.pop() 
        castle = self.board.getHome(castle)
        king = troop.Troop('ElvenKing', attributes.Attributes(3,3,3), castle, player1, False)
        player1.addBuilding(castle)
        player1.addTroop(king)
        
        self.players.append(player1)
        
        return (b, self.players, map_length)
    
    