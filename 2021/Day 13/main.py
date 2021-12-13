from scipy.sparse import csc_matrix

def part1():
    with open("input.txt") as input:

        sparse = input.read().splitlines()
        dots, fold = set(), []
        is_dots = True
        for item in sparse:
            if item == '':
                is_dots = False
                continue

            if is_dots:
                x, y = item.split(",")
                dots.add((int(x), int(y)))

            else:
                if 'x' in item:
                    fold.append(('x', int(item.split("=")[1])))
                else:
                    fold.append(('y', int(item.split("=")[1])))

        first = True
        for axis, value in fold:
            if axis == "x":
                fold_x(value, dots)
            else:
                fold_y(value, dots)

            if first:
                print("Part 1:", len(dots))
                first = False

        max_y = max(dots, key=lambda x: x[1])[1]
        max_x = max(dots, key=lambda t: t[0])[0]
        dense = []
        for y in range(max_y + 1):
            aux = []
            for x in range(max_x + 1):
                if (x, y) in dots:
                    aux.append("#")
                else:
                    aux.append(".")
            dense.append(aux)
        print("Part 2:")

        for line in dense:
            print(line)


def fold_y(y, dots):
    copy_dots = dots.copy()
    for x_dot, y_dot in copy_dots:
        if y <= y_dot:
            dots.remove((x_dot, y_dot))
            dots.add((x_dot, 2*y - y_dot))


def fold_x(x, dots):
    copy_dots = dots.copy()
    for x_dot, y_dot in copy_dots:
        if x < x_dot:
            dots.remove((x_dot, y_dot))
            dots.add((2*x - x_dot, y_dot))


part1()