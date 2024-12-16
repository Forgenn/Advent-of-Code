from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import functools
from collections import defaultdict
from itertools import combinations


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] == "." or grid[(x + dx, y + dy)] == "S":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        with open(self.input_file) as input:
            data = input.readlines()
            grid = defaultdict(str)
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            distances = {key: 9999999 for key in grid}
            directions = {key: None for key in grid}

            end = None
            start = None
            for (x, y), char in grid.items():
                if char == "E":
                    start = (x, y)
                elif char == "S":
                    end = (x, y)

            distances[start] = 0
            visited = set()
            queue = [(start, 0)]
            directions[start] = (0, -1)

            while queue:
                u = queue.pop(0)

                for nbr in get_adjacent(grid, u[0]):
                    if nbr in visited:
                        continue
                    cur_direction = directions[u[0]]
                    # New step
                    new_dist = u[1] + 1

                    # changing directions
                    if (
                        nbr[0] - cur_direction[0] != u[0][0]
                        and cur_direction in ((0, -1), (0, 1))
                        or nbr[1] - cur_direction[1] != u[0][1]
                        and cur_direction in ((1, 0), (-1, 0))
                    ):
                        new_dist = u[1] + 1000 + 1

                    directions[nbr] = (nbr[0] - u[0][0], nbr[1] - u[0][1])

                    if new_dist < distances[nbr]:
                        distances[nbr] = new_dist
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append((nbr, new_dist))
                            queue.sort(key=lambda x: x[1])
                if queue:
                    grid[queue[0][0]] = "!"
                # Remove the current node from the queue
            return distances[end]

    def part2(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] != "#":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        with open(self.input_file) as input:
            data = input.readlines()
            grid = defaultdict(str)
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            distances = {key: 9999999 for key in grid}
            directions = {key: None for key in grid}

            end = None
            start = None
            for (x, y), char in grid.items():
                if char == "S":
                    start = (x, y)
                elif char == "E":
                    end = (x, y)

            distances[start] = 0
            visited = set()
            queue = [(start, 0)]
            directions[start] = (0, -1)

            while queue:
                u = queue.pop(0)

                for nbr in get_adjacent(grid, u[0]):
                    if nbr in visited:
                        continue
                    cur_direction = directions[u[0]]
                    # New step
                    new_dist = u[1] + 1

                    # changing directions
                    if (
                        nbr[0] - cur_direction[0] != u[0][0]
                        and cur_direction in ((0, -1), (0, 1))
                        or nbr[1] - cur_direction[1] != u[0][1]
                        and cur_direction in ((1, 0), (-1, 0))
                    ):
                        new_dist = u[1] + 1000 + 1

                    directions[nbr] = (nbr[0] - u[0][0], nbr[1] - u[0][1])

                    if new_dist < distances[nbr]:
                        distances[nbr] = new_dist
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append((nbr, new_dist))
                            queue.sort(key=lambda x: x[1])
                if queue:
                    grid[queue[0][0]] = "!"
                # Remove the current node from the queue
            return distances[end]


cache = {}
puzzle = Day()
puzzle.runner()
