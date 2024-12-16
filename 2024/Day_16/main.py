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
            x, y, (dxi, dyi) = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] != "#":
                    if (dx, dy) == (dxi, dyi):  # going straight
                        adjacent.append((1, (x + dx, y + dy, (dxi, dyi))))
                    else:  # turning
                        adjacent.append((1001, (x + dx, y + dy, (dx, dy))))
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

            end = None
            start = None
            start_dir = (1, 0)
            for (x, y), char in grid.items():
                if char == "S":
                    start = (x, y, start_dir)
                elif char == "E":
                    end = (x, y)
            p1 = None
            distances = {key: 9999999 for key in grid}
            queue = [(0, start)]
            from_ = defaultdict(set)

            while queue:
                dist, (cx, cy, cd) = queue.pop(0)

                if (cx, cy) == end:
                    if not p1:
                        p1 = dist

                for d, (nx, ny, (ndx, ndy)) in get_adjacent(grid, (cx, cy, cd)):
                    nbr = (nx, ny)
                    nbr_d = (nx, ny, (ndx, ndy))
                    if dist + d < distances[nbr]:
                        distances[nbr] = dist + d
                        queue.append((distances[nbr], nbr_d))
                        from_[nbr] = {(cx, cy, cd)}
                    elif dist + d <= distances[nbr]:
                        from_[nbr].add((cx, cy, cd))

        return distances[end]

    def part2(self):

        def get_adjacent(grid, coord):
            x, y, (dxi, dyi) = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] != "#":
                    if (dx, dy) == (dxi, dyi):  # going straight
                        adjacent.append((1, (x + dx, y + dy, (dxi, dyi))))
                    else:  # turning
                        adjacent.append((1001, (x + dx, y + dy, (dx, dy))))
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

            end = None
            start = None
            start_dir = (1, 0)
            for (x, y), char in grid.items():
                if char == "S":
                    start = (x, y, start_dir)
                elif char == "E":
                    end = (x, y)
            p1 = None
            distances = {
                (*key, dir): 9999999
                for key in grid
                for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            }
            queue = [(0, start)]
            best_paths = defaultdict(set)

            while queue:
                dist, (cx, cy, cd) = queue.pop(0)

                if (cx, cy) == end:
                    if not p1:
                        p1 = dist

                for d, (nx, ny, (ndx, ndy)) in get_adjacent(grid, (cx, cy, cd)):
                    nbr = (nx, ny)
                    nbr_d = (nx, ny, (ndx, ndy))
                    if dist + d < distances[nbr_d]:
                        distances[nbr_d] = dist + d
                        queue.append((distances[nbr_d], nbr_d))
                        best_paths[nbr_d] = {(cx, cy, cd)}
                    elif dist + d <= distances[nbr_d]:
                        best_paths[nbr_d].add((cx, cy, cd))

        min_path_cost = 9999999
        if end:
            smallest = 9999999
            for (x, y, _), dist in distances.items():
                if (x, y) == end:
                    smallest = min(smallest, dist)
            min_path_cost = smallest

        stack = [(*end, (0, -1))]
        gnodes = set(stack)
        # Backtrack from end to start, while only using best possible paths from/to nodoes
        while len(stack) > 0:
            some = stack.pop(-1)
            for other in best_paths[some]:
                if other not in gnodes:
                    gnodes.add(other)
                    stack.append(other)

        gnodes = set(x[:2] for x in gnodes)
        print(len(gnodes))


cache = {}
puzzle = Day()
puzzle.runner()
