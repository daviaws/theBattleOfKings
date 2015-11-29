import tropa
import position
import attributes

atr = attributes.Attributes(1,3,2)
pos = position.Position(3,3)

troop = tropa.Tropa(atr, pos, None)

list = troop.calcMove()

print(list)