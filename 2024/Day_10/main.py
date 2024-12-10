from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid.get((x + dx, y + dy), "OUT") == grid[coord] + 1:
                    adjacent.append((x + dx, y + dy))
            return adjacent

        with open(self.input_file) as input:
            data = input.readlines()
            grid = {
                (x, y): int(char) if char != "." else -2
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            result = {}

            for idy in range(max_y + 1):
                for idx in range(max_x + 1):
                    if grid[(idx, idy)] == 0:
                        visited = set()
                        queue = []
                        visited.add((idx, idy))
                        queue.append((idx, idy))
                        trailhead = (idx, idy)
                        while queue:
                            current = queue.pop(0)
                            if grid[current] == 9:
                                result[trailhead] = result.get(trailhead, 0) + 1
                            for neighbor in get_adjacent(grid, current):
                                if neighbor not in visited:
                                    visited.add(neighbor)
                                    queue.append(neighbor)

            return sum([x for x in result.values()])

    def part2(self):
        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid.get((x + dx, y + dy), "OUT") == grid[coord] + 1:
                    adjacent.append((x + dx, y + dy))
            return adjacent

        with open(self.input_file) as input:
            data = input.readlines()
            grid = {
                (x, y): int(char) if char != "." else -2
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            result = {}

            for idy in range(max_y + 1):
                for idx in range(max_x + 1):
                    if grid[(idx, idy)] == 0:
                        visited = set()
                        queue = []
                        visited.add((idx, idy))
                        queue.append((idx, idy))
                        trailhead = (idx, idy)
                        while queue:
                            current = queue.pop(0)
                            if current not in visited:
                                visited.add(current)

                            if grid[current] == 9:
                                result[(trailhead, current)] = (
                                    result.get((trailhead, current), 0) + 1
                                )
                            for neighbor in get_adjacent(grid, current):
                                if neighbor not in visited:
                                    queue.append(neighbor)

            print(result)
            return sum([x for x in result.values()])


puzzle = Day()
puzzle.runner()
