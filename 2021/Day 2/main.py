def part1():
    with open("input.txt") as input:
        depth = 0
        horizontal_pos = 0
        lines = [str(line.rstrip('\n')) for line in input]

        for line in lines:
            if line[0] == "f":
                horizontal_pos += int(line[-1])

            if line[0] == "u":
                depth -= int(line[-1])

            if line[0] == "d":
                depth += int(line[-1])

        return depth * horizontal_pos

def part2():
    with open("input.txt") as input:
        depth = 0
        horizontal_pos = 0
        aim = 0
        lines = [str(line.rstrip('\n')) for line in input]

        for line in lines:
            if line[0] == "f":
                horizontal_pos += int(line[-1])
                depth = depth + aim * int(line[-1])
            if line[0] == "u":
                aim -= int(line[-1])

            if line[0] == "d":
                aim += int(line[-1])

        return depth * horizontal_pos

print("Part 1:", part1())
print("Part 2:", part2())