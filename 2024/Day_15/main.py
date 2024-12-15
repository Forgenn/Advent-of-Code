from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import functools
from collections import defaultdict, namedtuple
from itertools import combinations, batched
import re
from math import prod
import imageio

import ipdb; 
class Day(MainHelper):
    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        grid = defaultdict(str)
        global robot_pos
        robot_pos = ()
        movements = []
        is_movements = False
        with open(self.input_file) as input:
            for y, line in enumerate(input):
                if line == "\n":
                    is_movements = True
                for x, char in enumerate(line):
                    if char == "@":
                        robot_pos = (x, y)
                    if char == "\n" or char == ".":
                        continue
                    if not is_movements:
                        grid[(x, y)] = char
                    elif char != "\n":
                        movements.append(char)

        def boxes_in_line(orig_position, direction):
            global robot_pos
            x, y = orig_position
            dx, dy = direction
            should_move = True
            o_movements = []
            # Next O cell
            while grid[(x, y)] == "O":
                initial_x, initial_y = x, y
                x += dx
                y += dy
                #Should not stop
                if grid[(x, y)] != "#":
                    o_movements.append(((initial_x, initial_y),(x, y))) 
                else:
                    should_move = False
                    break
                # Cell next to this O
                if grid[(x, y)] == "":
                    should_move = True
                    break
            for movement in o_movements:
                grid[(movement[1][0], movement[1][1])] = "O"

            return should_move
        
        def move(direction):
            global robot_pos
            x, y = robot_pos
            dx, dy = direction

            if grid[(x + dx, y + dy)] == "O":
                should_move = boxes_in_line((robot_pos[0] + dx, robot_pos[1] + dy), direction)
                if should_move:
                    grid[(x, y)] = "."
                    robot_pos = (robot_pos[0] + dx, robot_pos[1] + dy)
                    grid[(robot_pos[0], robot_pos[1])] = "@"
            elif grid[(x + dx, y + dy)] == "#":
                robot_pos =  robot_pos
            else:
                grid[(x, y)] = "."
                grid[(x + dx, y + dy)] = "@"
                robot_pos = (x + dx, y + dy)
        
        max_x = max(x for x, _ in grid)
        max_y = max(y for _, y in grid)
        
        for movement in movements:
            
            if movement == "<":
                move((-1, 0))
            if movement == ">":
                move((1, 0))
            if movement == "^":
                move((0, -1))
            if movement == "v":
                move((0, 1))


            #print("Moved: ", movement)
            #for y in range(max_y + 1):
            #    for x in range(max_x + 1):
            #        print(grid.get((x, y), "."), end="")
            #    print()
        
        result = 0
        for (x, y), val in grid.items():
            if val == "O":
                result += (100 * abs(y)) + abs(x)
                

        return result
            
    def part2(self):
        grid = defaultdict(str)
        global robot_pos
        robot_pos = ()
        movements = []
        is_movements = False
        with open(self.input_file) as input:
            for y, line in enumerate(input):
                if line == "\n":
                    is_movements = True
                x = 0
                for char in line:
                    if char == "@":
                        robot_pos = (x, y)
                    if char == "\n":
                        continue
                    if not is_movements:
                        if char == "#":
                            grid[(x, y)] = "#"
                            grid[(x+1, y)] = "#"
                            x += 2
                        if char == "O":
                            grid[(x, y)] = "["
                            grid[(x+1, y)] = "]"
                            x += 2
                        if char == ".":
                            grid[(x, y)] = "."
                            grid[(x+1, y)] = "."
                            x += 2
                        if char == "@":
                            grid[(x, y)] = "@"
                            grid[(x+1, y)] = "."
                            x += 2
                    elif char != "\n":
                        movements.append(char)

            max_x = max(x for x, _ in grid)
            max_y = max(y for _, y in grid)

            for y in range(max_y + 1):
                for x in range(max_x + 1):
                    print(grid.get((x, y), "."), end="")
                print()
        def boxes_in_line(orig_position, direction):
            global robot_pos
            x, y = orig_position
            dx, dy = direction
            should_move = True
            o_movements = []
            # Next O cell
            if direction == (1, 0) or direction == (-1, 0):
                while grid[(x, y)] == "[" or grid[(x, y)] == "]":
                    initial_x_1, initial_y_1, initial_x_2, initial_y_2 = x, y, x + dx, y + dy
                    x1, y1, x2, y2 = x + dx, y + dy, x + dx + dx, y + dy + dy
                    #Should not stop
                    if grid[(x2, y2)] != "#":
                        o_movements.append((((initial_x_1, initial_y_1), (initial_x_2, initial_y_2)),
                                            ((x1, y1), (x2 , y2)),
                                            (grid[(initial_x_1, initial_y_1)], grid[(initial_x_2, initial_y_2)])
                                            ))
                    else:
                        should_move = False
                        break
                    # Cell next to this O
                    if grid[(x, y)] == "":
                        should_move = True
                        break
                    x += dx + dx
                    y += dy + dy
                    
            if should_move:
                for movement in o_movements:
                    grid[movement[1][0]] = movement[2][0]
                    grid[movement[1][1]] = movement[2][1]

            if direction == (0, -1) or direction == (0, 1):
                queue = [(x, y)]
                visited = {(x, y): grid[(x, y)]}
                while queue:
                    current = queue.pop(0)
                    neighbors = []
                    if grid[current] == "[":
                        neighbors.append((current[0] + 1, current[1]))
                    if grid[current] == "]":
                        neighbors.append((current[0] - 1, current[1]))
                    neighbors.append((current[0] + dx, current[1] + dy))

                    for neighbor in neighbors:
                        if neighbor not in visited and grid[neighbor] in "[]":
                            visited[neighbor] = grid[neighbor]
                            queue.append(neighbor)
                
                moves = []
                for box in visited:
                    space_next = box[0] + dx, box[1] + dy
                    moves.append((box, space_next, grid[box]))

                should_move = True
                for box, next_space, char in moves:
                    if grid[next_space] == "#":
                        should_move = False
                        break

                if should_move:
                    for move in moves:
                        if not any(move[0] == m[1] for m in moves):
                            grid[move[0]] = "."
                        grid[move[1]] = move[2]

            return should_move
        
        def move(direction):
            global robot_pos
            x, y = robot_pos
            dx, dy = direction

            if grid[(x + dx, y + dy)] == "[" or grid[(x + dx, y + dy)] == "]":
                should_move = boxes_in_line((robot_pos[0] + dx, robot_pos[1] + dy), direction)
                if should_move:
                    grid[(x, y)] = "."
                    robot_pos = (robot_pos[0] + dx, robot_pos[1] + dy)
                    grid[(robot_pos[0], robot_pos[1])] = "@"
            elif grid[(x + dx, y + dy)] == "#":
                robot_pos =  robot_pos
            else:
                grid[(x, y)] = "."
                grid[(x + dx, y + dy)] = "@"
                robot_pos = (x + dx, y + dy)
        
        for movement in movements:
            
            if movement == "<":
                move((-1, 0))
            if movement == ">":
                move((1, 0))
            if movement == "^":
                move((0, -1))
            if movement == "v":
                move((0, 1))


        print("Moved: ", movement)
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                print(grid.get((x, y), "."), end="")
            print()
        
        result = 0
        for (x, y), val in grid.items():
            if val == "[":
                result += (100 * abs(y)) + abs(x)
                

        return result
        




puzzle = Day()
puzzle.runner()
