import re

def part1():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    fields = set()
    result = 0
    #Doesnt count the last line because there is no newline after it, just ignores it
    for line in lines:
        if line == "":
            if 'byr' in fields and 'iyr' in fields and 'eyr' in fields and 'hgt' in fields and 'hcl' in fields and 'ecl' in fields and 'pid' in fields:
                print("Correct passport: ", sorted(fields))
                result += 1
            fields = set()
            continue
        line = re.split(r"[ :]", line)

        for element in line:
            fields.add(element)

    print(result)

def part2():
    f = open("input.txt", "r")
    lines = [line.rstrip('\n') for line in f]

    fields = {}
    result = 0
    #Doesnt count the last line because there is no newline after it, just ignores it, so sum 1

    for line in lines:
        if line == "":

            byr = fields.get("byr")
            iyr = fields.get("iyr")
            eyr = fields.get("eyr")
            hgt = fields.get("hgt")
            hcl = fields.get("hcl")
            ecl = fields.get("ecl")
            pid = fields.get("pid")

            ecl_matches = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

            height = False
            color = False
            pida = False

            if hgt:
                resulthgt = re.split(r'(\d+)', hgt)
                if (resulthgt[2] == 'cm' and 150 <= int(resulthgt[1]) <= 193) or (resulthgt[2] == 'in' and 59 <= int(resulthgt[1]) <= 76):
                    height = True

            if hcl:
                match = re.search(r'^#(\d|\w){6}$', hcl)
                if match:
                    color = True

            if pid:
                match = re.search(r'^\d{9}$', pid)
                if match:
                    pida = True

            if byr and iyr and eyr:
                if (1920 <= int(byr) <= 2002) and (2010 <= int(iyr) <= 2020) and (2020 <= int(eyr) <= 2030) and height and color and ecl in ecl_matches and pida:
                    result += 1
            fields = {}
            continue

        line = re.split(r"[ ]", line)

        for element in line:
            element = re.split(r"[:]", element)

            fields[element[0]] = element[1]

    print(result)
part2()