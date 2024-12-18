from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import re
from collections import defaultdict
from math import inf


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] == ".":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def heuristic(node1, node2):
            return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

        def lowest_cost(nodes_set: set, heuristic_costs: dict):
            min_cost = inf
            best_node = None
            for node in nodes_set:
                if heuristic_costs[node] < min_cost:
                    best_node = node
                    min_cost = heuristic_costs[node]
            return best_node

        def reconstruct_path(cameFrom, current):
            total_path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                total_path.insert(0, current)
            return total_path

        with open(self.input_file) as input:
            falling_bytes = []
            for line in input:
                x, y = line.strip().split(",")
                falling_bytes.append((int(x), int(y)))

            MAX_X = 71
            MAX_Y = 71
            START = (0, 0)
            END = (70, 70)

            N_BYTES = 1024

            grid = defaultdict(str)
            grid.update({(x, y): "." for x in range(MAX_X) for y in range(MAX_Y)})
            grid.update({(x, y): "#" for (x, y) in falling_bytes[:N_BYTES]})

            queue = set()
            queue.add(START)
            from_ = {}

            current_costs = defaultdict(lambda: inf)
            current_costs[START] = 0

            heuristic_costs = defaultdict(lambda: inf)
            heuristic_costs[START] = heuristic(START, END)

            best_path = []
            while queue:
                current = lowest_cost(queue, heuristic_costs)

                if current == END:
                    best_path = reconstruct_path(from_, current)
                    break

                queue.remove(current)

                for nbr in get_adjacent(grid, current):
                    # Cost always +1, as we want shortest
                    tentative_cost = current_costs[current] + 1
                    if tentative_cost < current_costs[nbr]:
                        from_[nbr] = current
                        current_costs[nbr] = tentative_cost
                        heuristic_costs[nbr] = tentative_cost + heuristic(nbr, END)
                        if nbr not in queue:
                            queue.add(nbr)

            print()
            grid.update({(x, y): "O" for (x, y) in best_path})
            for y in range(MAX_Y):
                for x in range(MAX_X):
                    print(grid[(x, y)], end=" ")
                print()

            print(len(best_path) - 1)
            return 0

    def part2(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] == ".":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def heuristic(node1, node2):
            return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

        def lowest_cost(nodes_set: set, heuristic_costs: dict):
            min_cost = inf
            best_node = None
            for node in nodes_set:
                if heuristic_costs[node] < min_cost:
                    best_node = node
                    min_cost = heuristic_costs[node]
            return best_node

        def reconstruct_path(cameFrom, current):
            total_path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                total_path.insert(0, current)
            return total_path

        with open(self.input_file) as input:
            falling_bytes = []
            for line in input:
                x, y = line.strip().split(",")
                falling_bytes.append((int(x), int(y)))

        MAX_X = 71
        MAX_Y = 71
        START = (0, 0)
        END = (70, 70)

        # MAX_X = 7
        # MAX_Y = 7
        # START = (0, 0)
        # END = (6, 6)

        N_BYTES = 1024

        for N_BYTES, corrupted_block in enumerate(falling_bytes):
            grid = defaultdict(str)
            grid.update({(x, y): "." for x in range(MAX_X) for y in range(MAX_Y)})
            # grid.update({(x, y): "#" for (x, y) in falling_bytes})

            queue = set()
            queue.add(START)
            from_ = {}

            current_costs = defaultdict(lambda: inf)
            current_costs[START] = 0

            heuristic_costs = defaultdict(lambda: inf)
            heuristic_costs[START] = heuristic(START, END)

            best_path = []

            grid.update({(x, y): "#" for (x, y) in falling_bytes[:N_BYTES]})
            while queue:
                current = lowest_cost(queue, heuristic_costs)

                if current == END:
                    best_path = reconstruct_path(from_, current)
                    break

                queue.remove(current)

                for nbr in get_adjacent(grid, current):
                    # Cost always +1, as we want shortest
                    tentative_cost = current_costs[current] + 1
                    if tentative_cost < current_costs[nbr]:
                        from_[nbr] = current
                        current_costs[nbr] = tentative_cost
                        heuristic_costs[nbr] = tentative_cost + heuristic(nbr, END)
                        if nbr not in queue:
                            queue.add(nbr)

            print()
            grid.update({(x, y): "O" for (x, y) in best_path})
            for y in range(MAX_Y):
                for x in range(MAX_X):
                    print(grid[(x, y)], end=" ")
                print()

            if not len(best_path):
                return falling_bytes[N_BYTES - 1]
        return "END"


puzzle = Day()
puzzle.runner()
