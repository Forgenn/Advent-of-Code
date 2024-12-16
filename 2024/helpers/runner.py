import os
import pprint


class MainHelper:
    def __init__(self, input_data):
        self.input_file = input_data

    def part1(self):
        return NotImplementedError("Not implemented")

    def part2(self):
        return NotImplementedError("Not implemented")

    def runner(self):
        print("Part 1:", end=" ")
        pprint.pprint(self.part1())
        print("Part 2:", end=" ")
        pprint.pprint(self.part2())
