import math

def calculate_seat(line):
    range_row = (0, 127)
    range_col = (0, 7)

    positon = 0

    for char in line:
        if char == 'F':
            row_pos = range_row[0]
            range_row = (range_row[0], int((range_row[1] - range_row[0])/2) + range_row[0])

        if char == 'B':
            row_pos = range_row[1]
            range_row = ((math.ceil((range_row[1] - range_row[0])/2.0)) + range_row[0], range_row[1])

        if char == 'L':
            col_pos = range_col[0]
            range_col = (range_col[0], int((range_col[1] - range_col[0])/2) + range_col[0])

        if char == 'R':
            col_pos = range_col[1]
            range_col = ((math.ceil((range_col[1] - range_col[0]) / 2.0)) + range_col[0], range_col[1])

        positon += 1

    seat_id = row_pos * 8 + col_pos

    return seat_id


def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    silver = 0

    for line in lines:
        seat_id = calculate_seat(line)
        if seat_id > silver:
            silver = seat_id

    print("Silver:", int(silver))

def part2():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    seats = []
    for line in lines:
        seats.append(calculate_seat(line))

    i = 0
    seats = sorted(seats)
    for seat in seats:
        if i != len(seats) - 1:
            if seats[i + 1] != seat + 1:
                print("Gold:", int(seat + 1))
        i += 1
part2()


