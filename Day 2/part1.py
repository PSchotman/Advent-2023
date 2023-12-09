# read line
# break on ':'
# <number> <color>
# Determine which games would have been possible if the bag had been loaded
# with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
# of the IDs of those games?
import re

games = {}
with open("input.txt") as fp:
    lines = fp.readlines()
for line in lines:
    # print(line) # Game 1: 8 green, 4 red, 4 blue; 1 green, 6 red, 4 blue; 7 red, 4 green, 1 blue; 2 blue, 8 red, 8 green

    line = line.split(":")
    # print(line) # ['Game 1', ' 8 green, 4 red, 4 blue; 1 green, 6 red, 4 blue; 7 red, 4 green, 1 blue; 2 blue, 8 red, 8 green\n']

    id = line[0].split("Game ")
    print(f"ID: {id[1]}")  # ID: 1
    games[id[1]] = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    throws = line[1].split(";")
    for throw in throws:
        # print(throw)  # 8 green, 4 red, 4 blue
        colors = throw.split(",")
        for color in colors:
            value = int(re.findall(r"\d+", color)[0])

            if "red" in color:
                if games[id[1]]["red"] < value:
                    games[id[1]]["red"] = value
            if "green" in color:
                if games[id[1]]["green"] < value:
                    games[id[1]]["green"] = value
            if "blue" in color:
                if games[id[1]]["blue"] < value:
                    games[id[1]]["blue"] = value

# print(games) # {'1': {'red': 8, 'green': 8, 'blue': 4},

# limits = {"red": 1, "green": 1, "blue": 1}
limits = {"red": 12, "green": 13, "blue": 14}


good_games = []
for id, game in games.items():
    bad_game = False
    if game["red"] > limits["red"]:
        bad_game = True
    if game["green"] > limits["green"]:
        bad_game = True
    if game["blue"] > limits["blue"]:
        bad_game = True
    if not bad_game:
        good_games.append(int(id))

print(good_games)
totalsum = 0

for gamenumber in good_games:
    totalsum += gamenumber

print(totalsum)
