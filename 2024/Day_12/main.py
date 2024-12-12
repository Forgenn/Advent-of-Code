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
                if grid.get((x + dx, y + dy), "OUT") == grid[coord]:
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def calculate_perimeter(grid, coord):
            x, y = coord
            adjacent = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid.get((x + dx, y + dy), "OUT") != grid[coord]:
                    adjacent += 1
            return adjacent

        with open(self.input_file) as input:
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            result = {}
            regions = []
            perimeters = []
            slot_regions_visited = defaultdict(list)
            for idy in range(max_y + 1):
                for idx in range(max_x + 1):
                    if (idx, idy) not in slot_regions_visited.get(grid[(idx, idy)], []):
                        visited = set()
                        queue = []
                        visited.add((idx, idy))
                        queue.append((idx, idy))
                        trailhead = (idx, idy)
                        perimeter = 0
                        while queue:
                            current = queue.pop(0)
                            if grid[current] != grid[trailhead]:
                                continue
                            perimeter += calculate_perimeter(grid, current)
                            list_visited = slot_regions_visited.get(grid[current], [])
                            slot_regions_visited[grid[current]].append(current)
                            for neighbor in get_adjacent(grid, current):
                                if neighbor not in visited:
                                    visited.add(neighbor)
                                    queue.append(neighbor)
                        perimeters.append(perimeter)
                        regions.append(visited)
            areas = [len(region) for region in regions]
            return sum(
                [area * perimeter for area, perimeter in zip(areas, perimeters)]
            )  # sum(

            # )

    def part2(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid.get((x + dx, y + dy), "OUT") == grid[coord]:
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def calculate_perimeter(regions: dict):
            corners = []
            for region in regions:
                region_corners = 0
                for x, y in region:
                    #   AA
                    #   A
                    if (x + 1, y) in region and (x, y + 1) in region:
                        region_corners += 1
                    #   A
                    #   AA
                    if (x, y - 1) in region and (x + 1, y) in region:
                        region_corners += 1
                    #    A
                    #   AA
                    if (x - 1, y) in region and (x, y - 1) in region:
                        region_corners += 1
                    #   AA
                    #    A
                    if (x - 1, y) in region and (x, y + 1) in region:
                        region_corners += 1

                corners.append(region_corners)
            return corners

        with open(self.input_file) as input:
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            max_x = max(x for x, y in grid)
            max_y = max(y for x, y in grid)

            result = {}
            regions = []
            perimeters = []
            slot_regions_visited = defaultdict(list)
            for idy in range(max_y + 1):
                for idx in range(max_x + 1):
                    if (idx, idy) not in slot_regions_visited.get(grid[(idx, idy)], []):
                        visited = set()
                        queue = []
                        visited.add((idx, idy))
                        queue.append((idx, idy))
                        trailhead = (idx, idy)
                        while queue:
                            current = queue.pop(0)
                            if grid[current] != grid[trailhead]:
                                continue
                            list_visited = slot_regions_visited.get(grid[current], [])
                            slot_regions_visited[grid[current]].append(current)
                            for neighbor in get_adjacent(grid, current):
                                if neighbor not in visited:
                                    visited.add(neighbor)
                                    queue.append(neighbor)
                        regions.append(visited)
            perimeters = calculate_perimeter(regions)
            areas = [len(region) for region in regions]
            return sum([area * perimeter for area, perimeter in zip(areas, perimeters)])


cache = {}
puzzle = Day()
puzzle.runner()
