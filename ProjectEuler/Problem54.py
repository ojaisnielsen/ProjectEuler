values = {
    "2": 0x1,
    "3": 0x2,
    "4": 0x3,
    "5": 0x4,
    "6": 0x5,
    "7": 0x6,
    "8": 0x7,
    "9": 0x8,
    "T": 0x9,
    "J": 0xA,
    "Q": 0xB,
    "K": 0xC,
    "A": 0xD,
    }

def value(card):
    if card is None:
        return 0
    return values[card[0]]

def high_card(hand):
    return value(hand[-1]), hand[:-1]

def one_pair(hand):
    pair = [None]
    prev = None
    for card in hand:
        if prev is not None and prev[0] == card[0]:
            pair = [prev, card]
        prev = card
    return value(pair[0]), pair

def two_pairs(hand):
    pair_1 = [None]
    pair_2 = [None]
    prev = None
    for card in hand:
        if prev is not None and prev[0] == card[0]:
            if len(pair_1) < 2:
                pair_1 = [prev, card]
            elif pair_1[0][0] != card[0]:
                pair_2 = [prev, card]
        prev = card
    return value(pair_2[0]), pair_1 + pair_2

def three_of_a_kind(hand):
    three = [None]
    prev_1 = None
    prev_2 = None
    for card in hand:
        if prev_1 is not None and prev_2 is not None and prev_1[0] == card[0] and prev_2[0] == card[0]:
            three = [prev_1, prev_2, card]
        prev_2 = prev_1
        prev_1 = card
    return value(three[0]), three

def straight(hand):
    val = 0
    for card in hand:
        if val == 0:
            val = values[card[0]]
        elif value(card[0]) == val + 1:
            val += 1
        else:
            return 0, []
    return val, []

def flush(hand):
    suit = None
    val = 0
    for card in hand:
        if suit == None:
            suit = card[1]
        elif card[1] == suit:
            val = value(card[0])
        else:
            return 0, []
    return val, []

def full_house(hand):
    pair = [None]
    pair_cand = [None]
    three = [None]
    prev_1 = None
    prev_2 = None
    for card in hand:
        if prev_1 is not None and prev_2 is not None and prev_1[0] == card[0] and prev_2[0] == card[0]:
            pair_cand = [None]
            three = [prev_1, prev_2, card]
        elif prev_1 is not None and prev_1[0] == card[0]:
            pair_cand = [prev_1, card]
        else:
            pair = pair_cand
        prev_2 = prev_1
        prev_1 = card
    if len(pair_cand) == 2:
        pair = pair_cand
    return (value(three[0]), pair + three) if len(pair) == 2 else (0, [])

def four_of_a_kind(hand):
    begin = reduce(lambda same_kind, card: same_kind and card[0] == hand[0][0], hand[0:-1], True)
    end = reduce(lambda same_kind, card: same_kind and card[0] == hand[-1][0], hand[1:], True)
    return (value(hand[-1]), [hand[-1]]) if end else (value(hand[0]), [hand[0]]) if begin else (0, [])

def straight_flush(hand):
    val = 0
    suit = None
    for card in hand:
        if val == 0:
            val = values[card[0]]
            suit = card[1]
        elif value(card) == val + 1 and card[1] == suit:
            val += 1
        else:
            return 0, []
    return val, []

def royal_flush(hand):
    suit = None
    vals = ["T", "J", "Q", "K", "A"]
    for i in range(0, len(hand)):
        if suit is None:
            suit = hand[i][1]
        if hand[i][1] != suit or hand[i][0] != vals[i]:
            return 0, []
    return 1, []

ranks = [high_card, one_pair, two_pairs, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush, royal_flush]

def rank(hand):
    r = 0
    coef = 1
    exclude = []
    for sub_rank in ranks:
        sub_r, sub_exclude = sub_rank(hand)
        if sub_r > 0:
            r = coef * sub_r
            exclude = sub_exclude
        coef *= 16
    return r, exclude

win_count_1 = 0
for line in open("p054_poker.txt"):
    row = line.split()
    hand_1 = sorted(row[0:5], key=lambda card: value(card))
    hand_2 = sorted(row[5:10], key=lambda card: value(card))
    rank_1, exclude_1 = rank(hand_1)
    rank_2, exclude_2 = rank(hand_2)
    while rank_1 == rank_2:
        m_1 = None
        while True:
            m_1 = hand_1.pop()
            if m_1 not in exclude_1:
                break
        m_2 = None
        while True:
            m_2 = hand_2.pop()
            if m_2 not in exclude_2:
                break
        rank_1 += value(m_1)
        rank_2 += value(m_2)
    if rank_1 > rank_2:
        win_count_1 += 1

print win_count_1

