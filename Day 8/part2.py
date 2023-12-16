
import re
from collections import Counter
import math
from functools import reduce



# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

mappings = {}
instructions = inputfile_lines[0]
for line in inputfile_lines:
    if "=" in line:
        key = line.split("=")[0].strip(" ")
        left_right = line.split("=")[1]
        left = left_right.split(",")[0].strip("( ")
        right = left_right.split(",")[1].strip(" )")
        mappings[key] = {
            "left": left,   
            "right": right,
        }



# foreach mappingpkey ending in a,
keys_ending_with_a = [key for key in mappings if key.endswith('A')]
# games = {key for key in mappings if key.endswith('A')}
games = []
games_step_counter = []
for game in keys_ending_with_a:
    games.append(game)
    games_step_counter.append(0)
print(games)


stepcounter = 0
found = False
while found != True:
    for instruction in instructions:
        stepcounter = stepcounter + 1
        for i, game_step in enumerate(games):
            if(instruction == "L"):
                # print(f"Going left on ['{game_step}']:['{mappings[game_step]['left']}':'{mappings[game_step]['right']}']")
                games[i] = mappings[game_step]["left"]
            elif(instruction == "R"):
                # print(f"Going right on ['{game_step}']:['{mappings[game_step]['left']}':'{mappings[game_step]['right']}']")
                games[i] = mappings[game_step]["right"]
    
    for i, game_step in enumerate(games):
        if game_step.endswith('Z') and games_step_counter[i] == 0:
            print(f"Updates position [{i}] with counter {stepcounter}")
            games_step_counter[i] = stepcounter
            
            if all(n > 0 for n in games_step_counter):
                found = True
                break


lcd = lambda a, b: abs(a*b) // math.gcd(a, b)
lcm = reduce(lcd, games_step_counter)



    
print(stepcounter)
print(lcm)   