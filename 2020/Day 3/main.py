

def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    treeCount = 0
    right = 3
    down = 1

    init = 0
    for line in lines:

        if init == 0:
            init = 1
            continue

        if line[right % len(line)] == '#':
            treeCount = treeCount + 1
        right = right + 3
    print("Silver:", treeCount)

def calculateTrees(right, down):
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    treeCount = 0
    right2 = right

    init = 0
    for i in range(0, len(lines), down):

        if init == 0:
            init = 1
            continue

        if lines[i][right % len(lines[i])] == '#':
            treeCount = treeCount + 1

        right += right2

    print("Slope ", right2, down, treeCount)
    return treeCount

def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1
    for slope in slopes:
        result = calculateTrees(slope[0], slope[1]) * result

    print(result)

part2()