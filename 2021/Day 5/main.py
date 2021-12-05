def part1():
    with open("input.txt") as input:
        lines = [str(line.rstrip('\n')) for line in input]
        coord_lines = [line.split(" -> ") for line in lines]
        coords = [coord.split(",") for line in coord_lines for coord in line]
        coord_dict = {}

        for i in range(0, len(coords), 2):
            all_cords = get_points([coords[i], coords[i+1]])
            for points in all_cords:
                if points in coord_dict:
                    coord_dict[points] += 1
                else:
                    coord_dict[points] = 1

        final = 0
        for point in coord_dict.values():
            if point > 1:
                final += 1
        return final


def part2():
    with open("input.txt") as input:
        lines = [str(line.rstrip('\n')) for line in input]
        coord_lines = [line.split(" -> ") for line in lines]
        coords = [coord.split(",") for line in coord_lines for coord in line]
        coord_dict = {}

        for i in range(0, len(coords), 2):
            all_cords = get_points_pt2([coords[i], coords[i+1]])
            for points in all_cords:
                if points in coord_dict:
                    coord_dict[points] += 1
                else:
                    coord_dict[points] = 1

        final = 0
        for point in coord_dict.values():
            if point > 1:
                final += 1
        return final


def get_points_pt2(line):
    x1, y1 = int(line[0][0]), int(line[0][1])
    x2, y2 = int(line[1][0]), int(line[1][1])

    if x1 == x2 or y1 == y2:
        xs = range(x1, x2 + 1) or [x1] if x1 < x2 else range(x2, x1 + 1) or [x1]
        ys = range(y1, y2 + 1) or [x2] if y1 < y2 else range(y2, y1 + 1) or [x2]
        return [(x, y) for x in xs for y in ys]
    else:
        diff = abs(x1 - x2)
        pos_cords = []
        for i in range (diff+1):
            x = x1
            y = y1
            x += i if x1 < x2 else -i
            y += i if y1 < y2 else -i
            pos_cords.append((x, y))
        return pos_cords



def get_points(line):
    x1, y1 = int(line[0][0]), int(line[0][1])
    x2, y2 = int(line[1][0]), int(line[1][1])

    if x1 == x2 or y1 == y2:
        xs = range(x1, x2 + 1) or [x1] if x1 < x2 else range(x2, x1 + 1) or [x1]
        ys = range(y1, y2 + 1) or [x2] if y1 < y2 else range(y2, y1 + 1) or [x2]
        return [(x, y) for x in xs for y in ys]
    else:
        return []

print("part 1", part1())
print("part 2", part2())