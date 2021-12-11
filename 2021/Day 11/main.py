

def part1(steps):
    with open("input.txt") as input:
        octopuses = []
        for i in input.readlines():
            octopus = []
            for coord in i.rstrip():
                octopus.append(int(coord))
            octopuses.append(octopus)

        total_flashes = 0
        for day in range(steps):
            flashes = simulate_day(octopuses)
            total_flashes += flashes
            if flashes == len(octopuses) * len(octopuses[0]): print("Part 2:", day)
        return total_flashes


def part2(steps):
    with open("input.txt") as input:
        octopuses = []
        for i in input.readlines():
            octopus = []
            for coord in i.rstrip():
                octopus.append(int(coord))
            octopuses.append(octopus)

        for day in range(steps):
            flashes = simulate_day(octopuses)
            if flashes == len(octopuses) * len(octopuses[0]): return day


def get_adjacent(coord, octopuses):
    adjacent = []
    x, y = coord
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if in_bounds((i, j), octopuses) and not (x == i and y == j):
                adjacent.append((i,j))
    return adjacent


def in_bounds(coord, octopuses):
    x, y = coord
    if x != -1 and x < len(octopuses) and y != -1 and y < len(octopuses[0]):
        return True
    return False

def simulate_day(octopuses):
    for x in range(len(octopuses)):
        for y, octopus in enumerate(octopuses[x]):
            octopuses[x][y] = int(octopuses[x][y]) + 1

    flashed = {}
    total_flashed = 0
    for x in range(len(octopuses)):
        for y, octopus in enumerate(octopuses[x]):
            simulate_flashes(octopuses, (x, y), flashed)
    total_flashed += len(flashed)
    flashed = {}
    return total_flashed



def simulate_flashes(octopuses, coord, flashed):
    x, y = coord
    if octopuses[x][y] > 9:
        octopuses[x][y] = 0
        flashed[(x, y)] = 1
        for adjacent in get_adjacent((x,y), octopuses):
            i, j = adjacent
            if (i, j) not in flashed:
                octopuses[i][j] = octopuses[i][j] + 1
            if octopuses[i][j] > 9 and (i, j) not in flashed:
                simulate_flashes(octopuses, (i, j), flashed)



print("Part1:", part1(100))
print("Part2:", part2(10000))