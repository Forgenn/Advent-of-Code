import numpy
import numpy as np


def part1():
    with open("input.txt") as input:
        lava_tubes = [str(i).rstrip() for i in input.readlines()]

        return sum(is_low(lava_tubes))



def is_low(lava_tubes):

    low_point = []
    for row in range(len(lava_tubes)):
        neighbors = set()
        for column, value in enumerate(lava_tubes[row]):
            if row != 0:
                neighbors.add(lava_tubes[row - 1][column])

            if row != len(lava_tubes) - 1:
                neighbors.add(lava_tubes[row + 1][column])

            if column != 0:
                neighbors.add(lava_tubes[row][column - 1])

            if column != len(lava_tubes[row]) - 1:
                neighbors.add(lava_tubes[row][column + 1])

            if all(int(value) < int(i) for i in neighbors):
                height = int(min(neighbors)) - int(value)
                low_point.append(1 + int(value))
            neighbors.clear()
    return low_point

def basins(lava_tubes):
    low_point = []
    all_basins = []
    for row in range(len(lava_tubes)):
        neighbors = []
        for column, value in enumerate(lava_tubes[row]):
            if row != 0:
                neighbors.append((row - 1, column))

            if row != len(lava_tubes) - 1:
                neighbors.append((row + 1, column))

            if column != 0:
                neighbors.append((row, column - 1))

            if column != len(lava_tubes[row]) - 1:
                neighbors.append((row, column + 1))

            if all(int(value) < int(lava_tubes[row][column]) for row, column in neighbors):
                visited = []
                print("new basin")
                basin = dfs(lava_tubes, visited, neighbors, (row, column))
                all_basins.append(basin)
            neighbors.clear()
    return all_basins


def get_neighbors(lava_tubes, row, column):
    neighbors = []
    if row != 0:
        neighbors.append((row - 1, column))

    if row != len(lava_tubes) - 1:
        neighbors.append((row + 1, column))

    if column != 0:
        neighbors.append((row, column - 1))

    if column != len(lava_tubes[row]) - 1:
        neighbors.append((row, column + 1))

    return neighbors

def dfs(lava_tubes, visited, neighbors, node):

    for row, column in neighbors:
        if lava_tubes[row][column] != '9' and (row, column) not in visited:
            visited.append((row, column))
            new_neighbors = get_neighbors(lava_tubes, row, column)
            dfs(lava_tubes, visited, new_neighbors, (row, column))

    return visited
def part2():
    with open("input.txt") as input:
        lava_tubes = [str(i).rstrip() for i in input.readlines()]

        biggest_basins = sorted(basins(lava_tubes), key=len)[-3:]
        result = 1
        for basin in biggest_basins:
            result *= len(basin)

        return result

print("Part 1:", part1())
print("Part 2:", part2())