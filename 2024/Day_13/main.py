from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import functools
from collections import defaultdict
from itertools import combinations, batched
import re

class Machine:
    def __init__(self, button_a: tuple, button_b: tuple, prize: tuple):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize
class Day(MainHelper):
    

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):

        with open(self.input_file) as input:
            rgx = re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", input.read())
            machines = [Machine(button_a=(int(x1), int(y1)), button_b=(int(x2), int(y2)), prize=(int(xf), int(yf))) for x1, y1, x2, y2, xf, yf in rgx]
        
        result = 0
        for machine in machines:
            button_a_presses = 0
            button_b_presses = 0

            button_a_presses = ((machine.button_b[1] * machine.prize[0]) - (machine.button_b[0] * machine.prize[1])) / \
                               ((machine.button_a[0] * machine.button_b[1]) - (machine.button_a[1] * machine.button_b[0]))
            button_b_presses = ((machine.button_a[0] * machine.prize[1]) - (machine.button_a[1] * machine.prize[0])) / \
                               ((machine.button_a[0] * machine.button_b[1]) - (machine.button_a[1] * machine.button_b[0]))
            if button_b_presses.is_integer() and button_a_presses.is_integer():
                result += (3 * int(button_a_presses)) + int(button_b_presses)
        return result
    
    def part2(self):

        with open(self.input_file) as input:
            rgx = re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", input.read())
            machines = [Machine(button_a=(int(x1), int(y1)), button_b=(int(x2), int(y2)), prize=(int(int(xf) + 10000000000000), int(int(yf) + 10000000000000))) for x1, y1, x2, y2, xf, yf in rgx]
        
        result = 0
        for machine in machines:
            button_a_presses = 0
            button_b_presses = 0

            button_a_presses = ((machine.button_b[1] * machine.prize[0]) - (machine.button_b[0] * machine.prize[1])) / \
                               ((machine.button_a[0] * machine.button_b[1]) - (machine.button_a[1] * machine.button_b[0]))
            button_b_presses = ((machine.button_a[0] * machine.prize[1]) - (machine.button_a[1] * machine.prize[0])) / \
                               ((machine.button_a[0] * machine.button_b[1]) - (machine.button_a[1] * machine.button_b[0]))
            if button_b_presses % 1 == 0 and button_a_presses % 1 == 0:
                result += 3 * int(button_a_presses) + int(button_b_presses)
        return result




cache = {}
puzzle = Day()
puzzle.runner()
