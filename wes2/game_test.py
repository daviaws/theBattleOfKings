# from memory_profiler import profile

from time import sleep
from random import randint

from src.game.board import Board
from src.concrete.walkableTerrain import WalkableTerrain
from src.concrete.troop import Troop
from src.abstractions.position import Position

#Calculating game area
map_limits = Position(10, 10)
game_area = map_limits.calculate_area()

#Populating area with terrains
terrain_cost = 1
for square in game_area:
    wkb_ter = WalkableTerrain('Grass', terrain_cost)
    square.allocate(wkb_ter)

#Setting the board area
game_board = Board()
game_board.set_area(game_area)

print()
print('Board area unoccupied:')
print(game_board)

#Creating a 3 energy troop
troop_energy = 3
troop1 = Troop('Yoda', troop_energy)
print()
print('Troop created: {}'.format(troop1))

#Getting terrain from board
get_pos = Position(1, 1)
pos = game_board.get_position(get_pos)
print()
print("Initial position taken:")
print(pos)

#Allocating troop
terrain = pos.see()
terrain.allocate(troop1)
print()
print('Terrain allocated: {}'.format(terrain))

# @profile
def troop_movement():
    global game_board
    global troop1
    global pos
    global terrain

    MAX_TURNS = 6
    TIME_TO_ACTION = 2 #Seconds
    turn = 0
    distance = 1
    
    new_pos = pos #Init new pos with initial position
    old_terrain = terrain
    
    while turn <= MAX_TURNS:
        print()
        print('Turn: {}'.format(turn))
        
        #Taking turn
        while troop1.have_energy():
            #Calculating adjacent area
            adj_area = pos.calculate_points(distance)
            print()
            print('Adjacent area: {}'.format(adj_area))

            while new_pos == pos:
                #Moving to adjacent area
                chosing_adjacent_area = randint(0, len(adj_area)-1)
                get_pos = adj_area[chosing_adjacent_area]
                new_pos = game_board.get_position(get_pos)
                if new_pos is None:
                    new_pos = pos
            terrain = new_pos.see()
            success = terrain.walk_to(troop1)
            if success:
                old_terrain.deallocate()
                old_terrain = terrain
            print()
            print("Troop: {}".format(troop1))
            print("Moved to position: {}".format(new_pos))
            sleep(TIME_TO_ACTION)
            pos = new_pos

        troop1.rest()
        turn += 1
        print()
        print("Troop resting. Ending turn.")
        sleep(TIME_TO_ACTION)

troop_movement()