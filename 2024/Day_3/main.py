from copy import deepcopy
from helpers.runner import MainHelper
import os

import re


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            sum = 0
            for line in input:
                for match in re.findall(r'mul\(\d+,\d+\)', line):
                    operands: str = match[4:-1]
                    operands = operands.split(',')
                    sum += int(operands[0]) * int(operands[1])
                    print(match)
            return sum
        
    def part2(self):
        with open(self.input_file) as input:
            sum = 0
            enabled = True
            pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
            for line in input:
                for match in re.findall(pattern, line):
                    op = match.split('(')[0]
                    match op:
                        case "do":
                            enabled = True
                        case "don't":
                            enabled = False
                        case "mul":
                            if enabled:
                                operands: str = match[4:-1]
                                operands = operands.split(',')
                                sum += int(operands[0]) * int(operands[1])
            return sum
puzzle = Day()
puzzle.runner()
