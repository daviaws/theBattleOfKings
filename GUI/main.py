import tkinter
from tkinter import *
from symbol import compound_stmt
 
image = None 
troop = None

class Janela:
    def __init__(self, toplevel):       
        global image
        global troop
        image = PhotoImage(file='forest.png')
        troop = PhotoImage(file='king.png')
        self.board = Frame(toplevel)
        self.board.pack(side=LEFT)
         
        self.positions = []
        
    def generate_interface(self, x, y):
        for l in range(0,y):
            for c in range(0,x):
                position = Home(c, l, self.board)
                self.positions.append(position)
 
class Home():
    def __init__(self, x, y, toplevel=None):
            self.x = x
            self.y = y
            self.troopId = None
            self.canvas = Canvas(toplevel,width=50,height=50)
            self.canvas.grid(row=y,column=x)
            self.canvas.bind("<Button-1>", self.on_click)
            self.canvas.create_image(27, 25, image=image)
            self.hasTroop = False
    
    def on_click(self, event):
        if self.hasTroop:
            self.hasTroop = False
            self.canvas.delete(self.troopId)
        else:
            self.hasTroop = True
            self.troopId = self.canvas.create_image(30, 25, image=troop)

 
root=Tk()
j = Janela(root)
j.generate_interface(20, 13)

root.mainloop()
