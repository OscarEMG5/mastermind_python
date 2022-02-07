import random
import readchar
import os

MAP_WIDTH = 20
MAP_HEIGHT = 15

POSITION_X = 10
POSITION_Y = 10
my_position = [POSITION_X, POSITION_Y]
tail = []

MAX_OBJECTS = 5
map_objects = []
objects_removed = []
wall = []
#OBSTACLE MAP
obstacle_definition = """\
 ###                
          ##        
          ###       
          ####      
 ###                
###                 
#                   
      ####          
       #            
                    
                    
  ##       ###    # 
   #        ####  # 
                    
        ###         \
"""
OBSTACLE_MAP = [list(row) for row in obstacle_definition.split("\n")]

# GENERATOR OF OBJECTS LOOP
while len(map_objects) < MAX_OBJECTS:
    new_object = ([random.randint(1, 19), random.randint(1, 14)])
    if new_object not in map_objects and my_position != new_object:
        map_objects.append(new_object)

# MAP AND PRINTING LOOP
while True:

    os.system('cls')

    print('+' + '---' * MAP_WIDTH + '+')

    for height in range(MAP_HEIGHT):
        print('|', end='')

        for width in range(MAP_WIDTH):
            priting_cell = [width, height]
            inverse_printing_cell = [height, width]
            char_to_draw = ' '
            object_occupied = None

            for egg in map_objects:

                if egg == priting_cell:
                    char_to_draw = '*'
                    object_occupied = egg

            if priting_cell == my_position:
                char_to_draw = 'c'

                if object_occupied:
                    objects_removed.append(object_occupied)
                    map_objects.remove(object_occupied)
                    while len(map_objects) < MAX_OBJECTS:
                        new_object = ([random.randint(1, 19), random.randint(1, 14)])
                        if new_object not in map_objects and my_position != new_object and new_object not in tail \
                                                                                        and new_object not in wall:
                            map_objects.append(new_object)
                            break

            if OBSTACLE_MAP[height][width] == '#':
                char_to_draw = '#'
                if [width, height] not in wall:
                    wall.append([width, height])

            if my_position in wall:
                char_to_draw = 'X'
                end = 1

            end = 0
            for trail in tail:
                if trail == priting_cell:
                    char_to_draw = 'c'
                if trail == my_position:
                    char_to_draw = 'M'
                    end = 1

            print(' {} '.format(char_to_draw), end='')

        print('|')
    print('+' + '---' * MAP_WIDTH + '+')
    if end == 1:
        input('YOU DIE\n\npress ENTER to exit')
        exit()

    print('TAIL: {} \n SNAKE LENGTH: {} \n EGGS EATEN: {}\n WALL: {}' .format(tail, len(tail), len(objects_removed), wall))

    tail.append(my_position)
    if len(tail) != len(objects_removed):
        tail.pop(0)
        pass

    # movements WASD

    direction = readchar.readchar().decode()
    if direction == 'w':
        POSITION_Y -= 1
        if POSITION_Y < 0:
            POSITION_Y = 14
        else:
            pass
    elif direction == 's':
        POSITION_Y += 1
        if POSITION_Y >= 15:
            POSITION_Y = 0
        else:
            pass
    elif direction == 'a':
        POSITION_X -= 1
        if POSITION_X < 0:
            POSITION_X = 19
        else:
            pass
    elif direction == 'd':
        POSITION_X += 1
        if POSITION_X >= 20:
            POSITION_X = 0
        else:
            pass
    elif direction == 'q':
        exit()

    os.system('cls')
    my_position = [POSITION_X, POSITION_Y]

    # Range and border limits

exit()
