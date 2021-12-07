import statistics
import math

def part1():
    with open("input.txt") as input:
        crab_position = [int(i) for i in input.readline().split(",")]
        median_position = statistics.median(crab_position)

        fuel_cost = sum(list(map(lambda x: abs(x - median_position), crab_position)))
        return int(fuel_cost)


def part2():
    with open("input.txt") as input:
        crab_position = [int(i) for i in input.readline().split(",")]
        median_ceil = math.ceil(statistics.mean(crab_position))
        median_floor = math.floor(statistics.mean(crab_position))


        #Sum of numbers in a series
        fuel_cost_floor = sum(list(map(lambda x, y=0: abs(x - median_floor) * (abs(x - median_floor) + 1) / 2, crab_position)))
        fuel_cost_ceil = sum(list(map(lambda x, y=0: abs(x - median_ceil) * (abs(x - median_ceil) + 1) / 2, crab_position)))

        return int(fuel_cost_floor) if fuel_cost_floor < fuel_cost_ceil else int(fuel_cost_ceil)


print("Part 1:", part1())
print("Part 2:", part2())