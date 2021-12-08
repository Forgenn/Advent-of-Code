from collections import Counter

def part1():
    with open("input.txt") as input:
        digits = [line.rstrip(" \n").split("|") for line in input]
        output = []
        for line in digits:
            output.append(line[1].split(" "))
        counter = 0
        for line in output:
            for out in line:
                if len(out) == 2 or len(out) == 4 or len(out) == 3 or len(out) == 7:
                    counter += 1
        return counter

def decode_line(line):
    decoded_display = {}

    for display in line:
        display_sort = "".join(sorted(display))
        if len(display) == 2:
            coded_1 = display
            decoded_display[display_sort] = 1
        elif len(display) == 3:
            coded_7 = display
            decoded_display[display_sort] = 7
        elif len(display) == 4:
            coded_4 = display
            decoded_display[display_sort] = 4
        elif len(display) == 7:
            coded_8 = display
            decoded_display[display_sort] = 8



    for display in line:
        if len(display) == 5:
            dict_4 = Counter(coded_4)
            dict_display = Counter(display)
            display_sort = "".join(sorted(display))
            if coded_1[0] in display and coded_1[1] in display:
                decoded_display[display_sort] = 3
            elif len(dict_4 & dict_display) == 2:
                decoded_display[display_sort] = 2
            elif len(dict_4 & dict_display) == 3:
                decoded_display[display_sort] = 5
                coded_5 = display_sort

    for display in line:
        if len(display) == 6:
            dict_4 = Counter(coded_4)
            dict_5 = Counter(coded_5)
            dict_display = Counter(display)
            display_sort = "".join(sorted(display))

            if len(dict_4 & dict_display) == 4:
                decoded_display[display_sort] = 9
            elif len(dict_5 & dict_display) == 5:
                decoded_display[display_sort] = 6

    for display in line:
        if "".join(sorted(display)) not in decoded_display.keys() and "".join(sorted(display)) != '':
            decoded_display["".join(sorted(display))] = 0

    return decoded_display



def part2():
    with open("input.txt") as input:
        digits = [line.rstrip(" \n").split("|") for line in input]
        coded = [line[0].split(" ") for line in digits]
        output = [line[1].split(" ") for line in digits]
        counter_in = ''
        counter_final = 0

        for i in range(len(digits)):
            decoded_display = decode_line(coded[i])
            for out in output[i]:
                if "".join(sorted(out)) in decoded_display.keys():
                    counter_in += str(decoded_display["".join(sorted(out))])
            counter_final += int(counter_in)
            counter_in = ''

        return counter_final
print("Part 1:", part1())
print("Part 2:", part2())
