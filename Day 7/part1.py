
import re
from collections import Counter


# Open file
with open("input-sample.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]


card_score = {
    "A": 14, 
    "K": 13, 
    "Q": 12, 
    "J": 11, 
    "T": 10, 
    "9": 9, 
    "8": 8, 
    "7": 7, 
    "6": 6, 
    "5": 5, 
    "4": 4, 
    "3": 3,
    "2": 2,
}

def is_five_of_a_kind(string):
    counts = Counter(string)
    return sorted(counts.values()) == [5]

def is_four_of_a_kind(string):
    counts = Counter(string)
    return sorted(counts.values()) == [1, 4]

def is_full_house(string):
    counts = Counter(string)
    return sorted(counts.values()) == [2, 3]

def is_three_of_a_kind(string):
    counts = Counter(string)
    return sorted(counts.values()) == [1, 1, 3]

def is_two_pair(string):
    counts = Counter(string)
    return sorted(counts.values()) == [1, 2, 2]

def is_one_pair(string):
    counts = Counter(string)
    return sorted(counts.values()) == [1, 1, 1, 2]

def is_high_card(string):
    counts = Counter(string)
    return sorted(counts.values()) == [1, 1, 1, 1, 1]


# Five of a kind
# Four of a kind
# Full house
# Three of a kind
# Two pair
# One pair
# High card

wintypes = {
    'high_card': [], 
    'one_pair': [], 
    'two_pair': [], 
    'three_of_a_kind': [], 
    'full_house': [], 
    'four_of_a_kind': [], 
    'five_of_a_kind': [], 
}

# print()

for line in inputfile_lines:
    game = line.split(" ")
    cards = str(game[0])
    bid = int(game[1])
    print(f"Processing {game}")
    if is_five_of_a_kind(cards):
        print("is_five_of_a_kind")
        wintypes["five_of_a_kind"].append(game)

    elif is_four_of_a_kind(cards):
        print("is_four_of_a_kind")
        wintypes["four_of_a_kind"].append(game)

    elif is_full_house(cards):
        print("is_full_house")
        wintypes["full_house"].append(game)

    elif is_three_of_a_kind(cards):
        print("is_three_of_a_kind")
        wintypes["three_of_a_kind"].append(game)

    elif is_two_pair(cards):
        print("is_two_pair")
        wintypes["two_pair"].append(game)

    elif is_one_pair(cards):
        print("is_one_pair")
        wintypes["one_pair"].append(game)

    elif is_high_card(cards):
        print("is_high_card")
        wintypes["high_card"].append(game)

# we know all types of hands
# sort them by starting number

# Give points to each card based on letters
ordered_games = []
for win_type in wintypes.keys():
    print("============")
    print(win_type)
    games = []
    for game in wintypes[win_type]:
        print(game)
        i = 0
        points = ""
        for card in game[0]:
            i = i + 1
            number = ""
            if len(str(card_score[card])) < 2:
                points = points + f"0{card_score[card]}"
            else:
                points = points + f"{card_score[card]}"
            # points = points + card_score[card]
        games.append({
            "cards": game[0],
            "points": int(points),
            "bid": game[1],
            "type": win_type,
        })
    games = sorted(games, key=lambda x: x['points'])
    ordered_games = ordered_games + games

print(games)


print("========================")
totalpoints = 0
i = 0
for game in ordered_games:
    i = i + 1
    print(game)
    bid = int(game["bid"])
    # print(f"{bid}*{i}")

    totalpoints = totalpoints + (bid * i)
print(f"And the answer is: {totalpoints}")
