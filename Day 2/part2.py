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


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
# Adding up these five powers produces the sum 2286.
# For each game, find the minimum set of cubes that must have been present.
# What is the sum of the power of these sets?

powers = []
for id, game in games.items():
    # needed = {"red": 0, "green": 0, "blue": 0}
    # if game["red"] > needed["red"]:
    #     needed["red"] = game["red"]
    # if game["green"] > needed["green"]:
    #     needed["green"] = game["green"]
    # if game["blue"] > needed["blue"]:
    #     needed["blue"] = game["blue"]
    powers.append(game["red"] * game["green"] * game["blue"])


# print(needed)  # {'red': 20, 'green': 13, 'blue': 15}
# power = needed["red"] * needed["green"] * needed["blue"]
print(sum(powers))
