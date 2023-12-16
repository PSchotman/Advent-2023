
import re
from collections import Counter

# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

# Expand the universe horizontally
# Keep track of x, y values per line. So empty == +1000000
# x=0, y=0
# horizontal, # found
# vertical, # found
# x=1, y=0
# horizontal, # found
# vertical, nothing found. x = x + 1000000
universe = []
galaxies = {}
y = -1

# Map the stars
for line in inputfile_lines:
    y += 1
    fake_x = -1
    real_x = -1
    if '#' not in line:
        y += 999999

    for x, char in enumerate(line):
        fake_x += 1
        real_x += 1 
        vertical_line = ""
        for vline in list(inputfile_lines):
            vertical_line += vline[real_x]
        if '#' not in vertical_line:
            fake_x += 999999
        
        if char == '#':
            galaxies[len(galaxies) + 1] = {
                "y": y,
                "x": fake_x,
            }
            print(f"Galaxy location: {len(galaxies)}:{galaxies[len(galaxies)]}")


for galaxy_key in galaxies.keys():
    galaxy = galaxies[galaxy_key]
    galaxies[galaxy_key]["distances"] = []
    print("===")
    print(f"Galaxy location: {galaxy_key}:{galaxy}")
    for galaxy_key_2 in galaxies.keys():
        galaxy_2 = galaxies[galaxy_key_2]
        # print(f"Comparing to: {galaxy_key_2}:{galaxy_2}")
        if galaxy_key >= galaxy_key_2:
            # print("Skipped.")
            continue
        distance = max(galaxy_2["x"], galaxy["x"]) - min(galaxy_2["x"], galaxy["x"])
        distance+= max(galaxy_2["y"], galaxy["y"]) - min(galaxy_2["y"], galaxy["y"])
        # distance += 1
        print(f"Result: {distance}")
        galaxies[galaxy_key]["distances"].append(distance)

total_distance = 0

for galaxy in galaxies.values():
    for distance in galaxy["distances"]:
        total_distance += distance

print(total_distance)