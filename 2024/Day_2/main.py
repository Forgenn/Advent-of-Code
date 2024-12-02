from copy import deepcopy
from helpers.runner import MainHelper
import os

INCREASING = 1
DECREASING = -1


class Day2(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            result = 0
            for line in input:
                report = line.split()
                last_level = int(report[0])
                direction = 0
                safe = 1
                for level in report[1:]:
                    # Not safe
                    print(last_level, level)
                    print(abs(last_level - int(level)))
                    if not (1 <= abs(last_level - int(level)) <= 3):
                        safe = 0
                        break
                    new_direction = (
                        INCREASING if last_level < int(level) else DECREASING
                    )
                    if direction != 0 and new_direction is not direction:
                        safe = 0
                        break
                    last_level = int(level)
                    direction = new_direction
                if safe:
                    result += 1
            return result

    def part2(self):
        with open(self.input_file) as input:
            result = 0
            for line in input:
                report = line.split()
                for i in range(0, len(report) + 1):
                    direction = 0
                    safe = 1
                    report_in = deepcopy(report)
                    if i != len(report):
                        del report_in[i]
                    last_level = int(report_in[0])

                    for level in report_in[1:]:
                        # Not safe
                        if not (1 <= abs(last_level - int(level)) <= 3):
                            safe = 0
                            break
                        new_direction = (
                            INCREASING if last_level < int(level) else DECREASING
                        )
                        if direction != 0 and new_direction is not direction:
                            safe = 0
                            break
                        last_level = int(level)
                        direction = new_direction
                    if safe:
                        result += 1
                        break
            return result


puzzle = Day2()
puzzle.runner()
