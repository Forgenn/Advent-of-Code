import sys
from collections import defaultdict
from queue import PriorityQueue

def part1():
    with open("input.txt") as input:
        cave = input.read().splitlines()

        neighbors = defaultdict(None)
        for y in range(len(cave)):
            for x in range(len(cave[0])):
                neighbors[(y, x)] = get_neighbors(cave, (y, x))

        all_paths = dijkstra(neighbors, (0, 0), (len(cave) - 1, len(cave[0]) - 1))
        return all_paths


def part2():
    with open("input.txt") as input:
        cave = [[*map(int, l.strip())] for l in input]

        expanded_cave = extend(cave)


        neighbors = defaultdict(None)
        for y in range(len(expanded_cave)):
            for x in range(len(expanded_cave[0])):
                neighbors[(y, x)] = get_neighbors(expanded_cave, (y, x))

        all_paths = dijkstra(neighbors, (0, 0), (len(expanded_cave) - 1, len(expanded_cave[0]) - 1))
        return all_paths


def extend(cave):
    X, Y = len(cave), len(cave[0])
    return [[(cave[x%X][y%Y] + x//X+y//Y - 1)%9+1
        for y in range(5*Y)] for x in range(5*X)]


def dijkstra(neighbors, start, target):
    distances = {keys: sys.maxsize for keys in neighbors.keys()}
    distances[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))
    all_paths = []
    while not queue.empty():
        (dist, current_vertex) = queue.get()

        for neighbor in neighbors[current_vertex]:
            current_neigh = (neighbor[0], neighbor[1])
            if distances[current_neigh] > dist + neighbor[2]:
                queue.put((dist + neighbor[2], current_neigh))
                distances[current_neigh] = distances[current_vertex] + neighbor[2]
                if current_neigh == target:
                    all_paths.append((dist + neighbor[2], current_neigh))

    return all_paths


def get_neighbors(cave, coord):
    row, column = coord
    neighbors = []
    if row != 0:
        neighbors.append((row - 1, column, int(cave[row - 1][column])))

    if row != len(cave) - 1:
        neighbors.append((row + 1, column, int(cave[row + 1][column])))

    if column != 0:
        neighbors.append((row, column - 1, int(cave[row][column - 1])))

    if column != len(cave[row]) - 1:
        neighbors.append((row, column + 1, int(cave[row][column + 1])))

    # min_neighbor = min(neighbors, key=lambda x: x[2])
    # min_list = [x for x in neighbors if x[2] == min_neighbor[2]]
    # print(min_list)
    return neighbors


print("Part 1:", part1())
print("Part 2:", part2())
