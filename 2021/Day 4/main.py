def part1():
    with open("input.txt") as input:

        bingo_numbers = input.readline().split(",")
        bingo_numbers[-1] = bingo_numbers[-1].rstrip("\n")
        bingo_cards =[]
        aux_line = []
        current_bingo_numbers = []
        found_winner = 0
        winner_card = None

        new_card = 0
        for line in input:
            line = line.rstrip("\n").split()
            if line:
                aux_line.append(line)
                if new_card == 4:
                    bingo_cards.append(aux_line)
                    aux_line = []
                    new_card = -1
                new_card += 1

        for bingo_number in bingo_numbers:
            if not found_winner:
                current_bingo_numbers.append(bingo_number)
            if not found_winner:
                for bingo_card in bingo_cards:
                    if not found_winner:
                        bingo_card_columns = list(map(list, zip(*bingo_card)))
                        for bingo_line in range(len(bingo_card)):
                            if set(bingo_card[bingo_line]).issubset(current_bingo_numbers) and not found_winner:
                                winner_card = (bingo_card, bingo_line, current_bingo_numbers[-1], 1)
                                found_winner = 1
                                break
                            if set(bingo_card_columns[bingo_line]).issubset(current_bingo_numbers) and not found_winner:
                                winner_card = (bingo_card, bingo_line, current_bingo_numbers[-1], 0)
                                found_winner = 1
                                break

        card, index, bingo_number_winner, is_row = winner_card

        if is_row:
            del card[index]

            flatten_card = set([j for sub in card for j in sub])

            non_marked = flatten_card - set(current_bingo_numbers)

            non_bingo_sum = sum([int(x) for x in non_marked])

        return non_bingo_sum * int(bingo_number_winner)

def part2():
    with open("input.txt") as input:

        bingo_numbers = input.readline().split(",")
        bingo_numbers[-1] = bingo_numbers[-1].rstrip("\n")
        bingo_cards =[]
        aux_line = []
        current_bingo_numbers = []
        found_winner = 0
        winner_card = None

        new_card = 0
        for line in input:
            line = line.rstrip("\n").split()
            if line:
                aux_line.append(line)
                if new_card == 4:
                    bingo_cards.append(aux_line)
                    aux_line = []
                    new_card = -1
                new_card += 1


        for bingo_number in bingo_numbers:
            if len(bingo_cards) == 1 and found_winner:
                break
            current_bingo_numbers.append(bingo_number)
            for bingo_card in bingo_cards:
                bingo_card_columns = list(map(list, zip(*bingo_card)))
                for bingo_line in range(len(bingo_card)):
                    if set(bingo_card[bingo_line]).issubset(current_bingo_numbers) and not found_winner:
                        winner_card = (bingo_card, bingo_line, current_bingo_numbers[-1], 1)
                        found_winner = 1
                        break
                    if set(bingo_card_columns[bingo_line]).issubset(current_bingo_numbers) and not found_winner:
                        winner_card = (bingo_card, bingo_line, current_bingo_numbers[-1], 0)
                        found_winner = 1
                        break
                if found_winner and len(bingo_cards) == 1:
                    break
                elif found_winner:
                    bingo_cards.remove(bingo_card)
                    found_winner = 0
                    continue
        print(bingo_cards)


        card, index, bingo_number_winner, is_row = winner_card

        if is_row:
            del card[index]
            flatten_card = set([j for sub in card for j in sub])
            non_marked = flatten_card - set(current_bingo_numbers)
            non_bingo_sum = sum([int(x) for x in non_marked])

        else:
            col_card = list(map(list, zip(*card)))
            del col_card[index]
            flatten_card = set([j for sub in col_card for j in sub])
            non_marked = flatten_card - set(current_bingo_numbers)
            non_bingo_sum = sum([int(x) for x in non_marked])

        print(non_bingo_sum, bingo_number_winner)
        return non_bingo_sum * int(bingo_number_winner)


print("part 1", part1())
print("part 2", part2())