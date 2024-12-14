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

class Robot:
    def __init__(self, position: tuple, movement: tuple):
        self.position = namedtuple("position", "x y")(*position)
        self.movement = namedtuple("movement", "x y")(*movement)
class Day(MainHelper):
    

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        MAX_X = 101
        MAX_Y = 103
        MAX_LOOPS = 100

        with open(self.input_file) as input:
            rgx = re.findall(r"p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)", input.read())
            robots = [Robot(position=(int(p1), int(p2)), movement=(int(v1), int(v2))) for p1, p2, v1, v2 in rgx]
        for _ in range(MAX_LOOPS):
            for i, robot in enumerate(robots):
                new_position = namedtuple("position", "x y")((robot.position.x + robot.movement.x) % MAX_X, (robot.position.y + robot.movement.y) % MAX_Y)
                robot.position = new_position

        quadrants_count = defaultdict(int)

        for robot in robots:
            x, y = robot.position.x, robot.position.y
            if x == MAX_X //2 or y == MAX_Y // 2:
                continue
            if x < MAX_X // 2 and y < MAX_Y // 2:
                quadrants_count[0] += 1
            elif x < MAX_X // 2 and y >= MAX_Y // 2:
                quadrants_count[1] += 1
            elif x >= MAX_X // 2 and y < MAX_Y // 2:
                quadrants_count[2] += 1
            elif x >= MAX_X // 2 and y >= MAX_Y // 2:
                quadrants_count[3] += 1

        return prod(quadrants_count.values())
    
    def part2(self):
        MAX_X = 101
        MAX_Y = 103
        MAX_LOOPS = 10000

        with open(self.input_file) as input:
            rgx = re.findall(r"p=([+-]?\d+),([+-]?\d+) v=([+-]?\d+),([+-]?\d+)", input.read())
            robots = [Robot(position=(int(p1), int(p2)), movement=(int(v1), int(v2))) for p1, p2, v1, v2 in rgx]
        import numpy as np
        import imageio

        with open(f"loop.txt", 'w') as f:
            for _ in range(MAX_LOOPS):
                for i, robot in enumerate(robots):
                    new_position = namedtuple("position", "x y")((robot.position.x + robot.movement.x) % MAX_X, (robot.position.y + robot.movement.y) % MAX_Y)
                    robot.position = new_position
                            
                grid = [['.' for _ in range(MAX_X)] for _ in range(MAX_Y)]
                for robot in robots:
                    x, y = robot.position.x, robot.position.y
                    grid[y][x] = '#'

                # Convert the grid to a numeric array
                grid_array = np.array([[0 if cell == '.' else 255 for cell in row] for row in grid], dtype=np.uint8)

                imageio.imwrite(f'frames/{_}.png', grid_array, format='png')
                if _ % 500 == 0:
                    print(f'Currently at loop {_}')
            
            
            
        




puzzle = Day()
puzzle.runner()
