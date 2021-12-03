def part1():
    with open("input.txt") as input:
        lines = [str(line.rstrip('\n')) for line in input]

        all_lines = len(lines)
        gamma_bit_list = []
        epsilon = 0
        common_bit = {}

        for line in lines:
            for bit in range(0, len(line)):
                if bit in common_bit:
                    common_bit[bit] += int(line[bit])
                else:
                    common_bit[bit] = int(line[bit])

        for bit in common_bit.values():
            gamma_bit_list.append("1") if bit > all_lines/2 else gamma_bit_list.append("0")

        gamma = int("".join(gamma_bit_list), 2)
        epsilon = int("".join('1' if x == '0' else '0' for x in gamma_bit_list), 2)
        return gamma * epsilon


def most_common(lines, current_bit):

    n_0 = 0
    n_1 = 0
    final_bit = []

    for line in lines:
        if line[current_bit] == "0":
            n_0 += 1
        else:
            n_1 += 1

    return "1" if n_1 >= n_0 else "0"


def least_common(lines, current_bit):

    n_0 = 0
    n_1 = 0
    final_bit = []

    for line in lines:
        if line[current_bit] == "0":
            n_0 += 1
        else:
            n_1 += 1

    return "1" if n_1 < n_0 else "0"


def part2():
    with open("input.txt") as input:
        lines = [str(line.rstrip('\n')) for line in input]
        oxy_lines = lines[:]
        CO2_lines = lines[:]

        oxy_aux_lines = []
        CO2_aux_lines = []
        line_lenght = len(lines[0])
        is_oxy = 1
        is_CO2 = 1
        current_bit = 0
        oxy_rating = []

        while len(oxy_lines) != 1:
            most_common_bit = most_common(oxy_lines, current_bit)
            for line in oxy_lines:
                if line[current_bit] == most_common_bit:
                    oxy_aux_lines.append(line)

            oxy_lines = oxy_aux_lines[:]
            oxy_aux_lines = []
            current_bit += 1

        current_bit = 0

        while len(CO2_lines) != 1:
            least_common_bit = least_common(CO2_lines, current_bit)
            for line in CO2_lines:
                if line[current_bit] == least_common_bit:
                    CO2_aux_lines.append(line)

            CO2_lines = CO2_aux_lines[:]
            CO2_aux_lines = []
            current_bit += 1

        CO2_rating = int(CO2_lines[0], 2)
        oxy_rating = int(oxy_lines[0], 2)

        return CO2_rating * oxy_rating


print("Part 1", part1())
print("Part 2", part2())

