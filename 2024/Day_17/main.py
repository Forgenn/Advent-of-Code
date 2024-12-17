from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os
import re
from collections import defaultdict


class Opcodes:
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        with open(self.input_file) as input:
            lines = input.read()
            rgx = re.findall(r"Register (?P<register>[A-Z]): (?P<value>\d+)", lines)
            registers = {key: int(value) for key, value in rgx}
            print()
            program = [int(num) for num in lines.split()[-1].split(",")]
            print(registers, program)

        def get_operand(operand):
            return registers[chr(operand + 61)] if operand in [4, 5, 6] else operand

        i_pointer = 0
        output = ""

        TEST_PROGRAM = [0, 1, 5, 4, 3, 0]
        TEST_REGISTERS = {"A": 2024, "B": 0, "C": 0}

        # program = TEST_PROGRAM
        # registers = TEST_REGISTERS

        while i_pointer < len(program):
            opcode = program[i_pointer]
            operand = program[i_pointer + 1]

            match opcode:
                # COmbo division
                case Opcodes.ADV:
                    numerator = registers["A"]
                    # combo
                    operand = get_operand(operand)

                    denominator = 2**operand
                    registers["A"] = numerator // denominator
                # Literal bitwise XOR
                case Opcodes.BXL:
                    registers["B"] = registers["B"] ^ operand
                # Modulo 8
                case Opcodes.BST:
                    # combo
                    operand = get_operand(operand)

                    registers["B"] = operand % 8
                # COnditional Jump
                case Opcodes.JNZ:
                    if registers["A"] == 0:
                        i_pointer += 2
                        continue
                    i_pointer = int(operand)
                    i_pointer -= 2
                # BItwise BC
                case Opcodes.BXC:
                    registers["B"] = registers["B"] ^ registers["C"]
                # OUtput
                case Opcodes.OUT:
                    # combo
                    operand = get_operand(operand)

                    output += str(operand % 8) + ","
                # DIvision stored in b
                case Opcodes.BDV:
                    numerator = registers["A"]
                    # combo
                    operand = get_operand(operand)

                    denominator = 2**operand
                    registers["B"] = numerator // denominator
                case Opcodes.CDV:
                    numerator = registers["A"]
                    # combo
                    operand = get_operand(operand)

                    denominator = 2**operand
                    registers["C"] = numerator // denominator

            i_pointer += 2
        return output[:-1]

    def part2(self):
        with open(self.input_file) as input:
            lines = input.read()
            rgx = re.findall(r"Register (?P<register>[A-Z]): (?P<value>\d+)", lines)
            registers = {key: int(value) for key, value in rgx}
            print()
            program = [int(num) for num in lines.split()[-1].split(",")]
            print(registers, program)

        def get_operand(operand):
            return registers[chr(operand + 61)] if operand in [4, 5, 6] else operand

        def run(registers, program):
            i_pointer = 0
            output = ""

            TEST_PROGRAM = [0, 1, 5, 4, 3, 0]
            TEST_REGISTERS = {"A": 2024, "B": 0, "C": 0}

            # program = TEST_PROGRAM
            # registers = TEST_REGISTERS

            while i_pointer < len(program):
                opcode = program[i_pointer]
                operand = program[i_pointer + 1]

                match opcode:
                    # COmbo division
                    case Opcodes.ADV:
                        numerator = registers["A"]
                        # combo
                        operand = get_operand(operand)

                        denominator = 2**operand
                        registers["A"] = numerator // denominator
                    # Literal bitwise XOR
                    case Opcodes.BXL:
                        registers["B"] = registers["B"] ^ operand
                    # Modulo 8
                    case Opcodes.BST:
                        # combo
                        operand = get_operand(operand)

                        registers["B"] = operand % 8
                    # COnditional Jump
                    case Opcodes.JNZ:
                        if registers["A"] == 0:
                            i_pointer += 2
                            continue
                        i_pointer = int(operand)
                        i_pointer -= 2
                    # BItwise BC
                    case Opcodes.BXC:
                        registers["B"] = registers["B"] ^ registers["C"]
                    # OUtput
                    case Opcodes.OUT:
                        # combo
                        operand = get_operand(operand)

                        output += str(operand % 8) + ","
                    # DIvision stored in b
                    case Opcodes.BDV:
                        numerator = registers["A"]
                        # combo
                        operand = get_operand(operand)

                        denominator = 2**operand
                        registers["B"] = numerator // denominator
                    case Opcodes.CDV:
                        numerator = registers["A"]
                        # combo
                        operand = get_operand(operand)

                        denominator = 2**operand
                        registers["C"] = numerator // denominator

                i_pointer += 2
            return output[:-1]

        loop = 1
        candidates = defaultdict(list)

        candidates = {0: [x for x in range(8)]}

        for exponent in range(1, len(program)):
            candidates[exponent] = []
            for candidate in candidates[exponent - 1]:
                for idx in range(8):
                    val = (8 * candidate) + idx
                    registers["A"] = val
                    registers["B"] = 0
                    registers["C"] = 0
                    output = run(registers, program)
                    output = [int(x) for x in output.split(",")]
                    if output == program[len(program) - len(output) :]:
                        candidates[exponent].append(val)
                    if output == program:
                        return val


puzzle = Day()
puzzle.runner()
