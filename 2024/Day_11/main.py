from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import functools

cache = {}


@functools.cache
def calculate_step(pebble):
    pebble = str(pebble)
    if pebble in cache:
        return cache[int(pebble)]
    old_pebble = pebble

    if pebble == "0":
        pebble = "1"
    elif len(pebble) % 2 == 0:
        old_pebble = pebble
        mid_index = len(old_pebble) // 2
        pebble = (old_pebble[:mid_index], str(int(old_pebble[mid_index:])))
    else:
        pebble = str(int(pebble) * 2024)
    cache[int(old_pebble)] = pebble
    return pebble


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            pebbles = input.readline().strip().split()
            for _ in range(26):
                i = 0
                while i < len(pebbles):
                    if pebbles[i] == "0":
                        pebbles[i] = "1"
                    elif len(pebbles[i]) % 2 == 0:
                        old_pebble = pebbles[i]
                        mid_index = len(old_pebble) // 2
                        pebbles[i] = old_pebble[:mid_index]
                        pebbles.insert(i + 1, str(int(old_pebble[mid_index:])))
                        i += 1
                    else:
                        pebbles[i] = str(int(pebbles[i]) * 2024)
                    i += 1
                print("{:.2f}%".format(((_ + 1) / 75) * 100), end="\r")
            return len(pebbles)

    def part2(self):
        with open(self.input_file) as input:
            pebbles = input.readline().strip().split()

        @functools.cache
        def calculate_step(pebble):

            old_pebble = str(pebble)

            if pebble == "0":
                pebble = ["1"]
            elif len(str(pebble)) % 2 == 0:
                mid_index = len(str(pebble)) // 2
                pebble = [old_pebble[:mid_index], str(int(old_pebble[mid_index:]))]
            else:
                pebble = [int(pebble) * 2024]
            return pebble

        @functools.cache
        def calculate_blink(pebbles, blinks):
            if blinks == 0:
                return 1
            values = calculate_step(pebbles)
            print("{:.2f}%".format(((blinks + 1) / 75) * 100), end="\r")
            return sum(calculate_blink(x, blinks - 1) for x in values)

        return sum(calculate_blink(pebble, 26) for pebble in pebbles)


cache = {}
puzzle = Day()
puzzle.runner()
