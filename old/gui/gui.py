import tkinter
from tkinter import *

import json

from symbol import compound_stmt
 
IMAGE_DATA_PATH = './data/images.data' 


class GUI:
    def __init__(self, toplevel):       
        
        self.controller = None
        
        self.resources = {}
        
        self.board = Frame(toplevel)
        self.board.pack(side=LEFT) 
        self.positions = []
        
        self.load_resources()
    
    def load_resources(self):
        file = open(IMAGE_DATA_PATH)
        file = file.readlines()
        for line in file:
            data = json.loads(line)
            for key in data:
                data[key] = PhotoImage(file=data[key])
            self.resources.update(data)
    
    def add_controller(self, controller):
        self.controller = controller
    
    def generate_game(self, terrains, troops, map_length):
        for l in range(0,map_length[1]):
            self.positions.append([])
            for c in range(0,map_length[0]):
                pos = (c,l)
                position = Home((c,l), terrains[(c,l)], self.resources, self.board)
                self.positions[l].append(position)
    
    def start_match(self):
        self.controller.start_match('board1')
        
 
class Home():
    def __init__(self, position, terrain_id, resources, toplevel=None):
            self.resources = resources
            self.terrain_id = terrain_id
            self.position = position
            self.troopId = None
            self.canvas = Canvas(toplevel,width=50,height=50)
            self.canvas.grid(row=self.position[1],column=position[0])
            self.canvas.bind("<Button-1>", self.on_click)
            self.canvas.create_image(27, 25, image=self.resources[terrain_id])
            self.hasTroop = False
    
    def on_click(self, event):
        if self.hasTroop:
            self.hasTroop = False
            self.canvas.delete(self.troopId)
        else:
            self.hasTroop = True
            self.troopId = self.canvas.create_image(30, 25, image=self.resources['ElvenKing'])
