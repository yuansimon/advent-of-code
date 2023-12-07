from util import *
from inputs.day_7 import input_1, input_2
from enum import Enum


class HandTypes(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


def analyze_hand(hand):
    cards = {}
    for char in hand:
        if char in cards:
            cards[char] += 1
        else:
            cards[char] = 1

    values = list(cards.values())
    if 5 in values:
        assert len(values) == 1
        return HandTypes.FIVE_OF_A_KIND
    if 4 in values:
        assert len(values) == 2
        return HandTypes.FOUR_OF_A_KIND
    if 3 in values:
        if 2 in values:
            assert len(values) == 2
            return HandTypes.FULL_HOUSE
        else:
            assert len(values) == 3
            return HandTypes.THREE_OF_A_KIND
    if 2 in values:
        if len(values) == 3:
            return HandTypes.TWO_PAIR
        assert len(values) == 4
        return HandTypes.ONE_PAIR
    assert len(values) == 5
    return HandTypes.HIGH_CARD


def analyze_hand_with_joker(hand):
    cards = {}
    joker = 0
    for char in hand:
        if char == "J":
            joker += 1
            continue
        if char in cards:
            cards[char] += 1
        else:
            cards[char] = 1

    if joker == 5:
        return HandTypes.FIVE_OF_A_KIND

    values = list(cards.values())
    values.sort(reverse=True)
    values[0] += joker

    if 5 in values:
        assert len(values) == 1
        return HandTypes.FIVE_OF_A_KIND
    if 4 in values:
        assert len(values) == 2
        return HandTypes.FOUR_OF_A_KIND
    if 3 in values:
        if 2 in values:
            assert len(values) == 2
            return HandTypes.FULL_HOUSE
        else:
            assert len(values) == 3
            return HandTypes.THREE_OF_A_KIND
    if 2 in values:
        if len(values) == 3:
            return HandTypes.TWO_PAIR
        assert len(values) == 4
        return HandTypes.ONE_PAIR
    assert len(values) == 5
    return HandTypes.HIGH_CARD


def get_card_rank(card):
    if card == "A":
        return 1
    if card == "K":
        return 2
    if card == "Q":
        return 3
    if card == "J":
        return 4
    if card == "T":
        return 5
    return 15 - int(card)


def get_card_rank_with_joker(card):
    if card == "A":
        return 1
    if card == "K":
        return 2
    if card == "Q":
        return 3
    if card == "T":
        return 4
    if card == "J":
        return 13
    return 14 - int(card)


def solve_1(input, debug=False):
    log = Logger(debug)
    all_hands = []
    for line in parse_lines(input):
        parts = line.split(" ")
        hand = parts[0]
        bid = int(parts[1])
        type = analyze_hand(hand)
        card_ranks = [get_card_rank(card) for card in hand]
        all_hands.append((type.value, card_ranks, hand, bid))
    all_hands.sort()
    if debug:
        for hand in all_hands:
            log.print(f"{hand[2]}: {hand}")

    total_winning = 0
    for index, (type, card_ranks, hand, bid) in enumerate(all_hands):
        total_winning += (len(all_hands) - index) * bid
    return total_winning


def solve_2(input, debug=False):
    log = Logger(debug)
    all_hands = []
    for line in parse_lines(input):
        parts = line.split(" ")
        hand = parts[0]
        bid = int(parts[1])
        type = analyze_hand_with_joker(hand)
        card_ranks = [get_card_rank_with_joker(card) for card in hand]
        all_hands.append((type.value, card_ranks, hand, bid))
    all_hands.sort()
    if debug:
        for hand in all_hands:
            log.print(f"{hand[2]}: {hand}")

    total_winning = 0
    for index, (type, card_ranks, hand, bid) in enumerate(all_hands):
        total_winning += (len(all_hands) - index) * bid
    return total_winning


def main():
    print(solve_1(input_1))
    print(solve_2(input_2))

if __name__ == '__main__':
    main()
