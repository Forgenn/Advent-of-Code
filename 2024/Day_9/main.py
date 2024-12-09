from copy import deepcopy
import pprint
from helpers.runner import MainHelper
import os


class Day(MainHelper):

    def __init__(self):
        super().__init__(os.path.join(os.path.dirname(__file__), "input.txt"))

    def part1(self):
        return "early stop"
        with open(self.input_file) as input:
            line = input.readline().strip()
            data = []
            for idx in range(len(line)):
                ch = idx // 2 if idx % 2 == 0 else "."
                data.extend([ch] * int(line[idx]))

            compacted_disk = list(data)
            dot_count = compacted_disk.count(".")

            while dot_count:
                pos = compacted_disk.index(".")
                char = compacted_disk.pop()
                compacted_disk[pos] = char

                while compacted_disk[-1] == ".":
                    compacted_disk.pop()
                dot_count = compacted_disk.count(".")
                if dot_count % 1000 == 0:
                    pprint.pprint(dot_count)

            return sum([i * int(char) for i, char in enumerate(compacted_disk)])

    def part2(self):
        def find_chunk(data, chunk_len):
            for i in range(0, len(data)):
                if data[i][1] >= chunk_len and data[i][0] == "GAP":
                    return i, data[i][1] - chunk_len
            return ("", "")

        with open(self.input_file) as input:
            line = input.readline().strip()
            data = []
            files = []
            file_id_count = 0
            for idx in range(len(line)):
                ch = idx // 2 if idx % 2 == 0 else "."
                if idx % 2 == 0:
                    data.append(("FILE_ID", int(line[idx]), file_id_count))
                    file_id_count += 1
                else:
                    if int(line[idx]) != 0:
                        data.append(("GAP", int(line[idx]), "."))

            data_copy = data[:]
            already_moved = set()
            for i in range(len(data_copy) - 1, -1, -1):
                print("".join(int(datain[1]) * str(datain[2]) for datain in data))
                (chunk_type, chunk_value, file_id) = data[i]
                if chunk_type == "FILE_ID" and file_id:
                    (
                        found_chunk_idx,
                        diff,
                    ) = find_chunk(data[:i], chunk_value)
                    if found_chunk_idx == "" and diff == "" or found_chunk_idx >= i:
                        already_moved.add(file_id)
                        continue
                    old_data = data[i]
                    data.insert(found_chunk_idx, data[i])
                    # already_moved.add(file_id)
                    data[i + 1] = ("GAP", chunk_value, ".")
                    if diff == 0:
                        del data[found_chunk_idx + 1]
                    else:
                        data[found_chunk_idx + 1] = ("GAP", diff, ".")

                if chunk_type == "GAP" and chunk_value:
                    continue

            result = 0
            n_current = 0

            for i, (type, file_chunk, file_id) in enumerate(data):
                for j in range(file_chunk):
                    if type == "FILE_ID":
                        result += n_current * int(file_id)
                    n_current += 1
            return result


puzzle = Day()
puzzle.runner()
