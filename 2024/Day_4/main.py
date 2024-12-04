from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os

XMAS = "XMAS"


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            search = []
            result = 0
            for n, line in enumerate(input):
                search.append([])
                for j, _ in enumerate(line.rstrip()):
                    search[n].append(line[j])

            for y in range(0, len(search)):  # rows
                for x in range(0, len(search[n])):  # columns
                    if search[y][x] == "X":
                        for dy, dx in [
                            (dy, dx)
                            for dy in [-1, 0, 1]
                            for dx in [-1, 0, 1]
                            if (dx != 0 or dy != 0)
                        ]:
                            candidate = ""
                            for i in range(len(XMAS)):
                                try:
                                    if x + dx * i < 0 or y + dy * i < 0:
                                        break
                                    candidate = "".join(
                                        [candidate, search[y + dy * i][x + dx * i]]
                                    )
                                except IndexError:
                                    break
                            if candidate == XMAS:
                                result += 1
            return result

    def part2(self):
        with open(self.input_file) as input:
            data = input.readlines()
            grid = {
                (x, y): char
                for y, line in enumerate(data)
                for x, char in enumerate(line.rstrip())
            }

            result = 0

            for x, y in grid:
                if grid.get((x, y), "") == "A":
                    lmas = "".join(
                        [
                            grid.get((dx + x, dy + y), "")
                            for dx, dy in [(-1, -1), (0, 0), (1, 1)]
                        ]
                    )
                    rmas = "".join(
                        [
                            grid.get((dx + x, dy + y), "")
                            for dx, dy in [(1, -1), (0, 0), (-1, 1)]
                        ]
                    )
                    if (rmas == "MAS" or rmas == "SAM") and (
                        lmas == "MAS" or lmas == "SAM"
                    ):
                        result += 1
            return result


puzzle = Day()
puzzle.runner()
