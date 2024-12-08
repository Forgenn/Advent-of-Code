from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
from collections import defaultdict

DIRS = [
    #"UP"
    (0, -1),
    #"RIGHT"
    (1, 0),
    #"DOWN"
    (0, 1),
    #"LEFT"
    (-1, 0)
]



class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
       with open(self.input_file) as input:
            result = 0 
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }
            guard_coords = ()
            guard_direction_index = 0
            for y, line in enumerate(data):
                for x, char in enumerate(line.rstrip()):
                    if char == '^':
                        guard_coords = (x, y)
                        guard_direction_index = 0
                    grid[(x,y)] = char

            while True:
                old_guard_coords = guard_coords
                next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                  guard_coords[1] + DIRS[guard_direction_index][1])
                next_position = grid.get(next_position_index, "")
               # Broke out 
                if next_position == "":
                    break

                if next_position != "#":
                    if next_position != "X":
                        result += 1
                    
                
                if next_position == "#":
                    guard_direction_index = (guard_direction_index + 1) % 4
                    next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                guard_coords[1] + DIRS[guard_direction_index][1])
                    result += 1

                guard_coords = next_position_index
                grid[old_guard_coords] = "X"
                grid[next_position_index] = "^"

            ''' max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            grid_2d = [[grid.get((x, y), ' ') for x in range(max_x + 1)] for y in range(max_y + 1)]

            pprint.pprint(grid_2d)
            print("")'''

            return  sum(1 for char in grid.values() if char == 'X') + 1
    
    def part2(self):
        def visited_grid():
           with open(self.input_file) as input:
            result = 0 
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }
            guard_coords = ()
            guard_direction_index = 0
            for y, line in enumerate(data):
                for x, char in enumerate(line.rstrip()):
                    if char == '^':
                        guard_coords = (x, y)
                        guard_direction_index = 0
                    grid[(x,y)] = char

            while True:
                old_guard_coords = guard_coords
                next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                  guard_coords[1] + DIRS[guard_direction_index][1])
                next_position = grid.get(next_position_index, "")
               # Broke out 
                if next_position == "":
                    grid[old_guard_coords] = "X"
                    break

                if next_position != "#":
                    if next_position != "X":
                        result += 1
                    
                
                if next_position == "#":
                    guard_direction_index = (guard_direction_index + 1) % 4
                    next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                guard_coords[1] + DIRS[guard_direction_index][1])
                    result += 1

                guard_coords = next_position_index
                grid[old_guard_coords] = "X"
                grid[next_position_index] = "^"
            return grid
        
        with open(self.input_file) as input:
            result = 0 
            data = input.readlines()
            orig_grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }
            orig_guard_coords = ()
            orig_guard_direction_index = 0
            for y, line in enumerate(data):
                for x, char in enumerate(line.rstrip()):
                    if char == '^':
                        orig_guard_coords = (x, y)
                        orig_guard_direction_index = 0
                    orig_grid[(x,y)] = char
                    
            max_x = max(x for x, y in orig_grid)
            max_y = max(y for x, y in orig_grid)
            
            visited_grid = visited_grid()
            loops = 0
            for y in range(max_y + 1):
                for x in range(max_x + 1):
                    if visited_grid[(x, y)] != "X":
                        continue
                    grid = orig_grid.copy()
                    grid[x, y] = "#"
                    n_visited = 0
                    guard_coords = orig_guard_coords
                    visited_obstacles = {}
                    times_visited = {}
                    guard_direction_index = orig_guard_direction_index
                    while True:
                        old_guard_coords = guard_coords
                        next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                        guard_coords[1] + DIRS[guard_direction_index][1])
                        next_position = grid.get(next_position_index, "")
                    # Broke out 
                        if next_position == "":
                            grid[old_guard_coords] = "X"
                            break
                            
                        # Possibly the worst thing ive ever done
                        #   For maps liek #.#. 
                        #                 ##..
                        #                 .#..
                        #   We should check changing direction doesnt direct the guard to another #, we have 4 possiblities
                        # so copy paste 4. WHile and for loops dont work WHAT!
                        if next_position == "#":
                            guard_direction_index = (guard_direction_index + 1) % 4
                            next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                        guard_coords[1] + DIRS[guard_direction_index][1])
                            next_position = grid.get(next_position_index, "")
                            if next_position_index not in visited_obstacles:
                                visited_obstacles[next_position_index] = [DIRS[guard_direction_index]]
                            elif DIRS[guard_direction_index] not in visited_obstacles[next_position_index]:
                                visited_obstacles[next_position_index].append(DIRS[guard_direction_index])
                            else:
                                loops += 1
                                break
                        if next_position == "#":
                            guard_direction_index = (guard_direction_index + 1) % 4
                            next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                        guard_coords[1] + DIRS[guard_direction_index][1])
                            next_position = grid.get(next_position_index, "")
                            if next_position_index not in visited_obstacles:
                                visited_obstacles[next_position_index] = [DIRS[guard_direction_index]]
                            elif DIRS[guard_direction_index] not in visited_obstacles[next_position_index]:
                                visited_obstacles[next_position_index].append(DIRS[guard_direction_index])
                            else:
                                loops += 1
                                break
                        if next_position == "#":
                            guard_direction_index = (guard_direction_index + 1) % 4
                            next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                        guard_coords[1] + DIRS[guard_direction_index][1])
                            next_position = grid.get(next_position_index, "")
                            if next_position_index not in visited_obstacles:
                                visited_obstacles[next_position_index] = [DIRS[guard_direction_index]]
                            elif DIRS[guard_direction_index] not in visited_obstacles[next_position_index]:
                                visited_obstacles[next_position_index].append(DIRS[guard_direction_index])
                            else:
                                loops += 1
                                break
                        if next_position == "#":
                            guard_direction_index = (guard_direction_index + 1) % 4
                            next_position_index = (guard_coords[0] + DIRS[guard_direction_index][0], 
                                        guard_coords[1] + DIRS[guard_direction_index][1])
                            next_position = grid.get(next_position_index, "")
                            if next_position_index not in visited_obstacles:
                                visited_obstacles[next_position_index] = [DIRS[guard_direction_index]]
                            elif DIRS[guard_direction_index] not in visited_obstacles[next_position_index]:
                                visited_obstacles[next_position_index].append(DIRS[guard_direction_index])
                            else:
                                loops += 1
                                break

                            

                        guard_coords = next_position_index
                        grid[old_guard_coords] = "X"
            return loops




puzzle = Day()
puzzle.runner()
