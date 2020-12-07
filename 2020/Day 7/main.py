def part1():
    f = open("input.txt", "r").read()
    input = f.replace(' bags', '').replace(' bag', '').replace('.', '').splitlines()

    table = [x.split(' contain ') for x in input]
    found = ['shiny gold']
    iterations = 0
    while iterations < len(found):
        for element in table:
            if element[1].find(found[iterations]) != -1 and element[0] not in found:
                found.append(element[0])
        iterations += 1
    print(len(found) - 1)

# Da fuck is this, almost got filtered, I'm dumb
def part2():
    f = open("input.txt", "r").read()
    input = f.replace(' bags', '').replace(' bag', '').replace('.', '').splitlines()

    table = [x.split(' contain ') for x in input]
    found = [('shiny gold', 1)]
    iterations = 0
    total = 0
    while len(found) > 0:
        line = 0
        for element in table:
            if iterations == 0:
                element[1] = [x.lstrip() for x in element[1].split(',')]

            for color in element[1]:
                if len(found) != 0:
                    if element[0] == found[0][0] and color != 'no other':
                        for x in element[1]:
                            n_bags = int(x[0]) * int(found[0][1])
                            total += n_bags
                            found.append((x[2:], n_bags))
                        found.pop(0)
                    elif color == 'no other' and element[0] == found[0][0]:
                        found.pop(0)

            line += 1
        iterations += 1
    print(total)

part1()
part2()


