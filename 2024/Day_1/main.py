def part1():
    with open("input.txt") as input:
        col1 = []
        col2 = []
        for line in input:
            linepar = line.split()
            col1.append(int(linepar[0]))
            col2.append(int(linepar[1]))
        col1.sort()
        col2.sort()

        distance = 0
        for i in range(0, len(col1)):
            distance += abs(col2[i] - col1[i])
        return distance 

print("Part 1:", part1())

def part2():
    with open("input.txt") as input:
        col1 = []
        col2 = []
        for line in input:
            linepar = line.split()
            col1.append(int(linepar[0]))
            col2.append(int(linepar[1]))
        
        similarity = 0
        for num in col1:
            similarity += col2.count(num) * num
        return similarity 

print("Part 1:", part1())
print("Part 2:", part2())