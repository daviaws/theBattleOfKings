from src import troop
from src import position
from src import attributes
from control import system
from gui import gui
from control import controller

# atr = attributes.Attributes(1,3,2)
# pos = position.Position(3,3)
# 
# troop = troop.Troop(atr, pos, None)
# 
# list = troop.calcMove()

syst = system.System()
root= gui.Tk()
g = gui.GUI(root)

controller = controller.Controller()
controller.addSystem(syst)
controller.addGui(g)

g.start_match()


root.mainloop()