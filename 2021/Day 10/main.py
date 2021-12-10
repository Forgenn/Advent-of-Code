
def part1():
    with open("input.txt") as input:
        lines = [str(i).rstrip() for i in input.readlines()]

        results = []
        for line in lines:
            results.append(find_error(line))

        return sum(results)

chars = {"[" : "]", "{" : "}", "<" : ">", "(" : ")",}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_error(line):
    stack = []
    total_points = 0
    for i, char in enumerate(line):
        if char in chars:
            stack.append(char)
        elif char == chars[stack[-1]]:
            stack.pop()
        else:
            total_points += points[char]
            break

    return total_points


points = {")": 1, "]": 2, "}": 3, ">": 4}

def part2():
    import statistics
    with open("input.txt") as input:
        lines = [str(i).rstrip() for i in input.readlines()]

        results = []
        for line in lines:
            if find_error(line) == 0:
                line_remainder = [points[chars[char]] for char in solve_line(line)]
                results.append(calculate_points(line_remainder))

        return statistics.median(sorted(results))

def solve_line(line):
    stack = []
    total_points = 0
    for i, char in enumerate(line):
        if char in chars:
            stack.append(char)
        elif char == chars[stack[-1]]:
            stack.pop()

    return reversed(stack)


def calculate_points(points):
    total_points = 0
    for point in points:
        total_points *= 5
        total_points += point

    return total_points

print("Part 1:", part1())
print("Part 2:", part2())
