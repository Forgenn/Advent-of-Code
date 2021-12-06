def solve(days):
    with open("input.txt") as input:
        lanternfish_school = [int(i) for i in input.readline().split(",")]
        lanternfish_dict = {}
        aux_lanterfish_6 = 0
        aux_lanterfish_8 = 0

        for i in range(9):
            lanternfish_dict[i] = 0

        for fish in lanternfish_school:
            if fish in lanternfish_dict:
                lanternfish_dict[fish] += 1
            else:
                lanternfish_dict[fish] = 1


        for i in range(days):
            for key, value in lanternfish_dict.items():
                if key == 0 and value != 0:
                    aux_lanterfish_8 = value
                    aux_lanterfish_6 = value
                    lanternfish_dict[0] = 0
                elif value != 0:
                    lanternfish_dict[key - 1] += lanternfish_dict[key]
                    lanternfish_dict[key] = 0

            lanternfish_dict[8] += aux_lanterfish_8
            lanternfish_dict[6] += aux_lanterfish_8
            aux_lanterfish_8 = 0
            aux_lanterfish_6 = 0
        return sum(lanternfish_dict.values())



print("Part 1:", solve(80))
print("Part 2:", solve(256))