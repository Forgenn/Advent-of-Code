def part1():
    with open("input.txt") as input:
        previous = 999999999
        result = 0
        for line in input:
            if int(line) > previous:
                result += 1
            previous = int(line)
        return result

print("Part 1:", part1())

def part2():
    with open("input.txt") as input:
        previous = 999999999
        result = 0
        lines = [int(line.rstrip('\n')) for line in input]

        for i in range(0, len(lines) - 2):
            sliding_sum = lines[i] + lines[i+1] + lines[i+2]

            if sliding_sum > previous:
                result += 1
            previous = sliding_sum


        return result

print("Part 2:", part2())