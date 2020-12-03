import re

def part1():
    f = open("bigboy.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    result = 0
    for line in lines:
        line = re.split(r"[- :]", line)
        min, max, letter, nj , message = line
        letter_count = message.count(letter)
        if int(max) >= letter_count >= int(min):
            result = result + 1

    print("Silver:" ,result)

def part2():
    f = open("bigboy.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    result = 0
    for line in lines:
        line = re.split(r"[- :]", line)
        first, second, letter, nj , message = line

        if (message[int(first) - 1] == letter and not message[int(second) - 1] == letter) or (message[int(second) - 1] == letter and not message[int(first) - 1] == letter ):
            result = result + 1

    print("Gold:" ,result)

part2()
