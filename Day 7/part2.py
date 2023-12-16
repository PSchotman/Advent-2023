import itertools
import re
from collections import Counter


# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

cards_string = "AKQJT98765432"

card_score = {
    "A": 14, 
    "K": 13, 
    "Q": 12, 
    "J": 1, 
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

wintypes = {
    'high_card': [], 
    'one_pair': [], 
    'two_pair': [], 
    'three_of_a_kind': [], 
    'full_house': [], 
    'four_of_a_kind': [], 
    'five_of_a_kind': [], 
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


def best_win_type(game):
    game = game[0]
    if is_five_of_a_kind(game):
        return "five_of_a_kind", 6
    elif is_four_of_a_kind(game):
        return "four_of_a_kind", 5
    elif is_full_house(game):
        return "full_house", 4
    elif is_three_of_a_kind(game):
        return "three_of_a_kind", 3
    elif is_two_pair(game):
        return "two_pair", 2
    elif is_one_pair(game):
        return "one_pair", 1
    elif is_high_card(game):
        return "high_card", 0
    return "", 0

def calculate_points(game):
    for card in game[0]:
        i = i + 1
        number = ""
        if len(str(card_score[card])) < 2:
            points = points + f"0{card_score[card]}"
        else:
            points = points + f"{card_score[card]}"
        
    return {
        "cards": game[0],
        "points": int(points),
        "bid": game[1],
        "type": win_type,
    }






# foreach ocurrence
# 
# JJJJJ 

# Change ocurrence
# AJJJJ

# Still J, change
# AAJJJ

# Still J, change
# AAAJJ

# Still J, change
# AAAAJ


# AAAAA
# AAAAK
# AAAAQ
# AAAAT

# AAAAA
# AAAAB
# AAAAC
# AAAAD
# AAAAE
# AAAAF
# ...



def get_joker_options(game):
    options = []
    # Count the number of 'J' characters in the string
    count_J = game[0].count('J')    
    # Generate all combinations of symbols of length 'count_J'
    combinations = itertools.product(cards_string, repeat=count_J)
    # Replace 'J's in the string with each combination and add to results
    for combo in combinations:
        temp_str = game[0]
        for char in combo:
            temp_str = temp_str.replace('J', char, 1)
        
        new_game = list(game)
        new_game[0] = temp_str
        options.append(new_game)
        print(f"NEW GAME: {new_game}")
        

        

            
            
        print("===")

    highest_win_type = 0
    for option in options:
        # print("Option:", option)
        win_type_string, value = best_win_type(option)
        if highest_win_type < value:
            highest_win_type = value
    
    keys = list(wintypes.keys())
    wintype = keys[highest_win_type]
    return wintype




def best_joker_possibility(game):
    # if "J" not in list(game[0]):
    #     win_type_string, value = best_win_type(game)
    #     return game, value
    
    j_indexes = [i for i, char in enumerate(game[0]) if char == 'J']
    options = []
    # options.append(game)
    highest_win_type = 0

    for index in j_indexes:
        for card in cards_string:
            # change first ocurrence, skip if J though
            if(card == 'J'):
                continue
            
            new_game = list(game)

            new_game_hand = list(new_game[0])
            new_game_hand[index] = card

            new_game[0] = "".join(new_game_hand)

            if new_game[0] == "KTTTT":
                print("here")
            
            # pass along for further processing if still J
            if 'J' in new_game[0]:
                new_game, extra_options = best_joker_possibility(new_game)
                options = options + extra_options
            print("NEW GAME:", new_game)
            
            options.append(new_game)
            # game[0][index] = card
            # calculate_points
            # best_win_type
    
    # highest_win_type = 0
    for option in options:
        if option[0] == "KTTTT":
            print("here")

        win_type_string, value = best_win_type(option)
        if highest_win_type < value:
            highest_win_type = value
    print("///")
    return game, options
    # return game
    # for game in options:
    #     best_win_type(game)
    

# Five of a kind
# Four of a kind
# Full house
# Three of a kind
# Two pair
# One pair
# High card



# print()

for line in inputfile_lines:
    game = line.split(" ")
    cards = str(game[0])
    bid = int(game[1])

    print(f"Processing {game}")
    
    
    if 'J' in cards:
        wintype = get_joker_options(game)

        
        print("Needed to process J")
    else:
        wintype, value = best_win_type(game)
    wintypes[wintype].append(game)

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


# Go over wintypes if a J is found
# Change J 
# List all possible options
# Get best win type
# Get best score
#  