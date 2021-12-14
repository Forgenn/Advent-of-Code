from collections import Counter, defaultdict

def part1(steps):
    with open("input.txt") as input:

        inp = input.read().splitlines()
        template = inp[0]
        last_char = template[-1]

        template_count = defaultdict(int)
        for i in range(len(template) - 1):
            pair = template[i:i + 2]
            template_count[pair] += 1

        rules_tmp = [rule.split(" -> ")for rule in inp[2:]]
        rules = {}
        for rule in rules_tmp:
            rules[rule[0]] = rule[1]

        for _ in range(steps):
            new_template = defaultdict(int)
            for pair, value in template_count.items():
                new_char = rules[pair]
                new_template[pair[0] + new_char] += value
                new_template[new_char + pair[1]] += value
            template_count = new_template

        total_element = defaultdict(int)
        for key, value in template_count.items():
            total_element[key[0]] += value
        total_element[last_char] += 1
        return max(total_element.values()) - min(total_element.values())






print("Part 1:", part1(10))
print("Part 2:", part1(40))