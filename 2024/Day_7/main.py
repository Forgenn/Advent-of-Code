from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
from collections import defaultdict
import itertools
DIRS = [
    #"UP"
    (0, -1),
    #"RIGHT"
    (1, 0),
    #"DOWN"
    (0, 1),
    #"LEFT"
    (-1, 0)
]



class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            calibrations = []
            for line in input:
                calibration = line.split(":")
                test_value = calibration[0]
                equation = calibration[1].lstrip(" ").strip().split(" ")
                calibrations.append((test_value, equation))
            
            result = 0

            for (value, equation) in calibrations:
                operators = ['+', '*']
                permutations = list(itertools.product(operators, repeat=len(equation) - 1))
                permutation_result = 0
                for permutation in permutations:
                    for i in range(len(permutation)):
                        if i == 0:
                            permutation_result = int(equation[0])
                        if permutation[i] == '+':
                            permutation_result += int(equation[i + 1])
                        elif permutation[i] == '*':
                            permutation_result *= int(equation[i + 1])

                    if permutation_result == int(value):
                        print(permutation)
                        result += permutation_result
                        break

            return result
        
    def part2(self):
        with open(self.input_file) as input:
            calibrations = []
            for line in input:
                calibration = line.split(":")
                test_value = calibration[0]
                equation = calibration[1].lstrip(" ").strip().split(" ")
                calibrations.append((test_value, equation))
            
            result = 0

            for (value, equation) in calibrations:
                operators = ['+', '*', '||']
                permutations = list(itertools.product(operators, repeat=len(equation) - 1))
                permutation_result = 0
                for permutation in permutations:
                    for i in range(len(permutation)):
                        if i == 0:
                            permutation_result = int(equation[0])
                        if permutation[i] == '+':
                            permutation_result += int(equation[i + 1])
                        elif permutation[i] == '*':
                            permutation_result *= int(equation[i + 1])
                        elif permutation[i] == '||':
                            permutation_result = int(str(permutation_result) + equation[i + 1])

                    if permutation_result == int(value):
                        print(permutation)
                        result += permutation_result
                        break

            return result

puzzle = Day()
puzzle.runner()
