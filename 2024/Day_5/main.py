from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
from collections import defaultdict


XMAS = "XMAS"


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            result = 0
            rules = defaultdict(list)
            for line in input:
                if line == "\n":
                    break
                vals = line.strip().split("|")
                rules[vals[0]].append(vals[1])
            update = []
            for line in input:
                valid = True
                update = line.strip().split(",")
                for position, page in enumerate(update):
                    valid = all(
                        x not in update[:position]
                        for x in rules[page]
                        if position + 1 >= 0
                    )
                    if not valid:
                        break

                if valid:
                    result += int(update[(len(update) - 1) // 2])

            return result

    def part2(self):
        with open(self.input_file) as input:
            result = 0
            rules = defaultdict(list)
            for line in input:
                if line == "\n":
                    break
                vals = line.strip().split("|")
                rules[vals[0]].append(vals[1])
            update = []
            update_not_valid = []
            for line in input:
                valid = True
                update = line.strip().split(",")
                for position, page in enumerate(update):
                    valid = all(
                        x not in update[:position]
                        for x in rules[page]
                        if position + 1 >= 0
                    )

                    if not valid:
                        update_not_valid.append(update)
                        break

            corrected = []
            for line in update_not_valid:
                valid = False
                corrected = line[:]
                while not is_sorted(line, rules):
                    if not valid:
                        corrected = sort_update(corrected, rules)
                    line = corrected[:]
                result += int(line[(len(line) - 1) // 2])

            return result


def is_sorted(update, rules):
    for position, page in enumerate(update):
        valid = all(
            x not in update[:position] for x in rules[page] if position + 1 >= 0
        )
        if not valid:
            return False
    return True


def sort_update(update: list, rules):
    sorted_update = update[:]
    for position, page in enumerate(update):
        for rule in rules[page]:
            if rule in update[:position]:
                tmp = sorted_update[position]
                sorted_update[position] = sorted_update[update.index(rule)]
                sorted_update[update.index(rule)] = tmp
        update = sorted_update[:]

    return sorted_update


puzzle = Day()
puzzle.runner()
