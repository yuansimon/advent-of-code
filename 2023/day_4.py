from util import *
from inputs.day_4 import input_1, input_2


def parse_line(line, nrs_won_per_card, cards_to_process, log=Logger(True)):
    log.print("parsing line", line)
    card_prefix = line.split(":")[0]
    card_nr = int(card_prefix[len("Card"):])
    assert card_nr not in cards_to_process
    cards_to_process[card_nr] = 1
    all_nrs = line.split(":")[1]
    unparsed_winning_nrs = all_nrs.split("|")[0]
    unparsed_my_nrs = all_nrs.split("|")[1]

    winning_nrs = set([int(nr) for nr in unparsed_winning_nrs.split(" ") if nr != ""])
    my_nrs = set([int(nr) for nr in unparsed_my_nrs.split(" ") if nr != ""])
    nrs_won = len(winning_nrs & my_nrs)
    assert card_nr not in nrs_won_per_card
    nrs_won_per_card[card_nr] = nrs_won
    return nrs_won


def solve_1(input, debug=False):
    log = Logger(debug)
    sum = 0
    cards_to_process = dict()
    nrs_won_per_card = dict()
    for line in parse_lines(input):
        nrs_won = parse_line(line, nrs_won_per_card, cards_to_process, log)
        if nrs_won > 0:
            points = 2 ** (nrs_won - 1)
        else:
            points = 0
        log.print(f"nrs_won: {nrs_won}, points: {points}")
        sum += points
    return sum


def process_cards(cards_to_process, nrs_won_per_card):
    curr_index = 1
    scratch_cards_processed = 0
    while curr_index in cards_to_process:
        cards = cards_to_process[curr_index]
        nrs_won = nrs_won_per_card[curr_index]
        scratch_cards_processed += cards
        for i in range(nrs_won):
            new_copy_nr = curr_index + i + 1
            if new_copy_nr in cards_to_process:
                cards_to_process[new_copy_nr] += cards
            else:
                break
        curr_index += 1

    return scratch_cards_processed


def solve_2(input, debug=False):
    log = Logger(debug)
    nrs_won_per_card = dict()
    cards_to_process = dict()
    for line in parse_lines(input):
        parse_line(line, nrs_won_per_card, cards_to_process, log)

    return process_cards(cards_to_process, nrs_won_per_card)


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))


if __name__ == '__main__':
    main()
