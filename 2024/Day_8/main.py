from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os





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

            antinodes = {}
            
            for (x1, y1), char1 in grid.items():
                for (x2, y2), char2 in grid.items():
                    if grid.get((x1, y1), "") != grid.get((x2, y2), "") or grid.get((x1, y1), "") == '.' or (x1, y1) == (x2, y2):
                        continue 
                    
                    row_dif, col_dif = x2 - x1, y2 - y1
                    antinode1 = (x1 - row_dif, y1 - col_dif)
                    antinode2 = (x2 + row_dif, y2 + col_dif)
                    
                    # Antinode would be in bounds
                    if grid.get(antinode1, "") != "":
                        antinodes[antinode1] = "#"
                    if grid.get(antinode2, "") != "":
                        antinodes[antinode2] = "#"
            return len(antinodes)
    def part2(self):
        with open(self.input_file) as input:
            result = 0 
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            antinodes = {}
            
            for (x1, y1), char1 in grid.items():
                for (x2, y2), char2 in grid.items():
                    if grid.get((x1, y1), "") != grid.get((x2, y2), "") or grid.get((x1, y1), "") == '.' or (x1, y1) == (x2, y2):
                        continue 
                    
                    
                    antinodes[(x1, y1)] = "#"
                    antinodes[(x2, y2)] = "#"

                    row_dif, col_dif = x2 - x1, y2 - y1
                    antinode1 = (x1 - row_dif, y1 - col_dif)
                    antinode2 = (x2 + row_dif, y2 + col_dif)

                    # Antinode would be in bounds
                    if grid.get(antinode1, "") != "":
                        antinodes[antinode1] = "#"
                    if grid.get(antinode2, "") != "":
                        antinodes[antinode2] = "#"

                    while grid.get(antinode1, "") != "":
                        antinode1 = (antinode1[0] - row_dif, antinode1[1] - col_dif)
                    
                        # Antinode would be in bounds
                        if grid.get(antinode1, "") != "":
                            antinodes[antinode1] = "#"

                    while grid.get(antinode2, "") != "":
                        antinode2 = (antinode2[0] + row_dif, antinode2[1] + col_dif)

                        # Antinode would be in bounds
                        if grid.get(antinode2, "") != "":
                            antinodes[antinode2] = "#"

            return len(antinodes)

puzzle = Day()
puzzle.runner()