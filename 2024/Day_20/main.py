from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import re
from collections import defaultdict, Counter
from math import inf
from tqdm import tqdm


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        return "Skip part 1"

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] == "." or grid[(x + dx, y + dy)] == "E":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def get_all_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                adjacent.append((x + dx, y + dy))
            return adjacent

        def cheating_get_adjacent(grid, coord, cheating_pos):
            if not cheating_pos:
                cheating_pos = ((), ())
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    grid[(x + dx, y + dy)] == "."
                    or grid[(x + dx, y + dy)] == "E"
                    or grid[(x + dx, y + dy)] == "!"
                ):
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
            data = input.readlines()
            grid = defaultdict(str)
            grid.update(
                {
                    (x, y): char
                    for y, line in enumerate(data)
                    for x, char in enumerate(line.rstrip())
                }
            )

            MAX_Y = len(data)
            MAX_X = max(len(line.rstrip()) for line in data)

            END = None
            START = None
            for (x, y), char in grid.items():
                if char == "S":
                    START = (x, y)
                elif char == "E":
                    END = (x, y)

            cheating_positions = set()

            for y in range(MAX_Y):
                for x in range(MAX_X):
                    if grid[(x, y)] == "#":
                        for nbr in get_all_adjacent(grid, (x, y)):
                            if grid[nbr] == "." or grid[nbr] == "E":
                                if x != MAX_X - 1 and y != MAX_Y - 1:
                                    cheating_positions.add((((x, y))))

            def a_star(grid, cheating=False, cheating_pos=None, default_cost=0):
                def get_adjacent_fn(grid, pos):
                    return (
                        cheating_get_adjacent(grid, pos, cheating_pos)
                        if cheating
                        else get_adjacent(grid, pos)
                    )

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

                    if current_costs[current] >= default_cost - 100 and cheating:
                        queue.remove(current)
                        continue

                    if current == END:
                        best_path = reconstruct_path(from_, current)
                        break

                    queue.remove(current)

                    for nbr in get_adjacent_fn(grid, current):
                        # Cost always +1, as we want shortest
                        tentative_cost = current_costs[current] + 1
                        if tentative_cost < current_costs[nbr]:
                            from_[nbr] = current
                            current_costs[nbr] = tentative_cost
                            heuristic_costs[nbr] = tentative_cost + heuristic(nbr, END)
                            if nbr not in queue:
                                queue.add(nbr)

                return best_path, current_costs[END]

            best_path, default_cost = a_star(deepcopy(grid))
            n_better_costs = 0
            cost_count = Counter()

            for pos in tqdm(cheating_positions, desc="Processing positions"):
                cheating_grid = deepcopy(grid)
                cheating_grid[pos] = "!"
                best_path, cheated_cost = a_star(
                    cheating_grid,
                    cheating=True,
                    cheating_pos=pos,
                    default_cost=default_cost,
                )

                if cheated_cost <= default_cost - 100:
                    cost_count.update({str(default_cost - cheated_cost): 1})
                    n_better_costs += 1

            return n_better_costs

    def part2(self):

        def get_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if grid[(x + dx, y + dy)] == "." or grid[(x + dx, y + dy)] == "E":
                    adjacent.append((x + dx, y + dy))
            return adjacent

        def get_all_adjacent(grid, coord):
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if (0 < new_x < MAX_X - 1) and (0 < new_y < MAX_Y - 1):  # Exclude edges
                    adjacent.append((new_x, new_y))
            return adjacent

        def cheating_get_adjacent(grid, coord, cheating_pos):
            if not cheating_pos:
                cheating_pos = ((), ())
            x, y = coord
            adjacent = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (
                    grid[(x + dx, y + dy)] == "."
                    or grid[(x + dx, y + dy)] == "E"
                    or grid[(x + dx, y + dy)] == "!"
                ):
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
            data = input.readlines()
            grid = defaultdict(str)
            grid.update(
                {
                    (x, y): char
                    for y, line in enumerate(data)
                    for x, char in enumerate(line.rstrip())
                }
            )

            MAX_Y = len(data)
            MAX_X = max(len(line.rstrip()) for line in data)

            END = None
            START = None
            for (x, y), char in grid.items():
                if char == "S":
                    START = (x, y)
                elif char == "E":
                    END = (x, y)

            def a_star(grid, cheating=False, cheating_pos=None, default_cost=0):
                def get_adjacent_fn(grid, pos):
                    return (
                        cheating_get_adjacent(grid, pos, cheating_pos)
                        if cheating
                        else get_adjacent(grid, pos)
                    )

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

                    # if current_costs[current] >= default_cost - 100 and cheating:
                    #    queue.remove(current)
                    #    continue

                    if current == END:
                        best_path = reconstruct_path(from_, current)
                        break

                    queue.remove(current)

                    for nbr in get_adjacent_fn(grid, current):
                        # Cost always +1, as we want shortest
                        tentative_cost = current_costs[current] + 1
                        if tentative_cost < current_costs[nbr]:
                            from_[nbr] = current
                            current_costs[nbr] = tentative_cost
                            heuristic_costs[nbr] = tentative_cost + heuristic(nbr, END)
                            if nbr not in queue:
                                queue.add(nbr)

                return best_path, current_costs[END]

            best_path, default_cost = a_star(deepcopy(grid))
            n_better_costs = 0
            cost_count = Counter()

            def get_all_paths(grid, start_pos, max_depth=20):
                all_paths = []

                def dfs(pos, path, depth):
                    # Stop conditions
                    if depth >= max_depth:
                        return
                    if grid[pos] == "." or grid[pos] == "E":
                        if len(path) > 1:  # Only add non-trivial paths
                            all_paths.append(path)
                        return

                    # Continue DFS
                    for nbr in get_all_adjacent(grid, pos):
                        if nbr not in path:  # Avoid cycles
                            dfs(nbr, path + [nbr], depth + 1)

                dfs(start_pos, [start_pos], 0)
                return all_paths

            cheating_positions = []
            # Usage:
            for y in range(MAX_Y):
                for x in range(MAX_X):
                    if grid[(x, y)] == "#":
                        if x != MAX_X - 1 and y != MAX_Y - 1:
                            paths = get_all_paths(deepcopy(grid), (x, y))
                            if paths:  # Only add if we found valid paths
                                cheating_positions.append(paths)

            for pos in tqdm(cheating_positions, desc="Processing positions"):
                for cheat_paths in pos:
                    cheating_grid = deepcopy(grid)
                    for x, y in cheat_paths:
                        if cheating_grid[(x, y)] != "E":
                            cheating_grid[(x, y)] = "!"

                    best_path, cheated_cost = a_star(
                        cheating_grid,
                        cheating=True,
                        cheating_pos=pos,
                        default_cost=default_cost,
                    )

                    if cheated_cost <= default_cost - 50:
                        cost_count.update({str(default_cost - cheated_cost): 1})
                        n_better_costs += 1
                    # cheating_grid.update({(x, y): "O" for (x, y) in best_path})
                    # print()
                    # for y in range(MAX_Y + 1):
                    #    for x in range(MAX_X + 1):
                    #        print(cheating_grid[(x, y)], end=" ")
                    #    print()

            return n_better_costs


puzzle = Day()
puzzle.runner()
