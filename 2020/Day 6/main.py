def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    answers = set()
    result = 0

    for line in lines:
        if line == "":
            result += len(answers)
            answers = set()
            continue

        for char in line:
            answers.add(char)

    result += len(answers)

    print("Silver:", result)

def part2():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    answers = {}
    group_count = 0

    result = 0

    for line in lines:
        if line == "":
            for i in answers:
                if answers[i] == group_count:
                    result += 1

            answers = {}
            group_count = 0
            continue

        for char in line:
            if char in answers:
                answers[char] += 1
            else:
                answers[char] = 1

        group_count += 1

    for i in answers:
        if answers[i] == group_count:
            result += 1

    print("Gold:", result)

part2()
