import time

def part1():
    f = open("expenses.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    for line in lines:
        for line2 in lines:
            if (int(line) + int(line2)) == 2020:
                print(int(line)*int(line2))


def part2():

    f = open("expenses.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    second = time.time()
    for line in lines:
        for line2 in lines:
            num = 2020 - int(line) - int(line2)
            if str(num) in lines:
                print(int(line) * int(line2) * int(num))
                print(time.time() - second)
                return


part2()