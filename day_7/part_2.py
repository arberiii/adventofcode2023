from collections import defaultdict
from functools import cmp_to_key


def part_2(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    hands = []
    for line in lines:
        hands.append(line.split(" "))
    cmp_items_py3 = cmp_to_key(letter_cmp)

    hands.sort(key=cmp_items_py3)


    total = 0
    for i in range(len(hands)):
        total += int(hands[i][1]) * (i+1)

    return total

def letter_cmp(a, b):
    if a is None:
        return -1
    if b is None:
        return 1
    hand_a = a[0]
    hand_b = b[0]
    if get_power(hand_a) > get_power(hand_b):
        return 1
    elif get_power(hand_a) < get_power(hand_b):
        return -1

    for i in range(5):
        if get_card_power(hand_a[i]) > get_card_power(hand_b[i]):
            return 1
        elif get_card_power(hand_a[i]) < get_card_power(hand_b[i]):
            return -1
    return 0


def get_card_power(card):
    if card == 'J':
        return 0
    if card == '2':
        return 1
    if card == '3':
        return 2
    if card == '4':
        return 3
    if card == '5':
        return 4
    if card == '6':
        return 5
    if card == '7':
        return 6
    if card == '8':
        return 7
    if card == '9':
        return 8
    if card == 'T':
        return 9
    if card == 'J':
        return 10
    if card == 'Q':
        return 11
    if card == 'K':
        return 12
    if card == 'A':
        return 13

def get_power(hand):
    counts = defaultdict(int)
    for char in hand:
        counts[char] += 1

    if 'J' in counts:
        m = 0
        k = None
        for key in counts:
            if key == 'J':
                continue
            if k is None or m < counts[key]:
                m = counts[key]
                k = key

        if m == 0:
            return 7

        counts[k] += counts['J']
        counts['J'] = 0

    if 5 in counts.values():
        return 7
    elif 4 in counts.values():
        return 6
    elif 3 in counts.values():
        if 2 in counts.values():
            return 5
        return 4
    elif 2 in counts.values():
        how_many = 0
        for key in counts:
            if counts[key] == 2:
                how_many += 1
        if how_many == 2:
            return 3
        return 2
    return 1

print(part_2("data.txt"))
