class Controller():
    
    def __init__(self):
        self.system = None
        self.gui = None
        
        self.selection = None
        
    def addSystem(self, system):
        self.system = system
    
    def addGui(self, gui):
        self.gui = gui
        self.gui.add_controller(self)
        
    def start_match(self, board_name):
        board_dict = {}
        troop_list = []
        board, players, map_length = self.system.start_match(board_name)
        
        for key in board:
            board_dict[key] = board[key].getId()
        for player in players:
            troops = player.getTroops()
            for troop in troops:
                troop_list.append((troop.getPosition().key(), troop.getId()))
        
        self.gui.generate_game(board_dict, players, map_length)