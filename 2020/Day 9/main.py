def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    offset = 25 # Change for examples
    found = False
    for line in range(offset, len(lines)):
        found = True
        for num_1 in range(line - offset, line + 1):
            for num_2 in range(num_1 + 1, line + 1):
                if int(lines[num_1]) + int(lines[num_2]) == int(lines[line]):
                    found = False
        if found:
            print("Silver:", lines[line])
            return lines[line]

def part2():
    f = open("input.txt", "r")
    lines = [int(line.rstrip('\n')) for line in f]
    target = int(part1())

    sum_set = []
    for i in range(0, len(lines)):
        sum_set.append(lines[i])
        for j in range(i + 1, len(lines)):
            result = 0
            sum_set.append(lines[j])
            for num in sum_set:
                result += num
            if result == target:
                sum_set.sort()
                print("Gold:", sum_set[0] + sum_set[-1])
                return
            elif result > target:
                break
        sum_set = []


part2()