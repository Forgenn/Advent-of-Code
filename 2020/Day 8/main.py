def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]
    i = 0
    accumulator = 0
    visited = []
    while i < len(lines):
        instruction = (lines[i].split(' '))
        if i not in visited:
            visited.append(i)
        else:
            print("Silver:", accumulator)
            break

        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
            i += 1

        if instruction[0] == 'jmp':
            i += int(instruction[1])

        if instruction[0] == 'nop':
            i += 1

def part2():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    visited = []
    changed = 0
    while changed < len(lines):
        line_copy = lines[:]
        loop = False
        accumulator = 0
        i = 0

        changed_jmp = (lines[changed].split(' '))

        if changed_jmp[0] == 'nop':
            changed_jmp[0] = 'jmp'
        elif changed_jmp[0] == 'jmp':
            changed_jmp[0] = 'nop'

        line_copy[changed] = changed_jmp[0] + ' ' + changed_jmp[1]

        while i < len(lines):
            instruction = (line_copy[i].split(' '))

            if i not in visited:
                visited.append(i)
            else:
                loop = True
                break

            if instruction[0] == 'acc':
                accumulator += int(instruction[1])
                i += 1

            if instruction[0] == 'jmp':
                i += int(instruction[1])

            if instruction[0] == 'nop':
                i += 1

        if not loop:
            print("Gold:", accumulator)
            return

        changed += 1
        visited = []

part2()