
import re
from collections import Counter

# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]


# Expand the universe horizontally
universe = []
galaxies = {}
for y, line in enumerate(inputfile_lines):
    if "#" not in line:
        universe.append(line)
    universe.append(line)

expanded_universe = list(universe)
# Expand it again vertically
# Flip y and x?
added_amount = 0
for x, char in enumerate(universe[0]):
    # make new string
    vertical_line = ""

    # Create new vertical line
    for line in universe:
        vertical_line+= line[x]
        # vertical_line+= [s[x] for s in universe]
    print(f"Processing vertical line [{x}]:{vertical_line}")

    # Check if galaxy in line
    if '#' not in vertical_line:
        newline = ""
        added_amount += 1
        # Add galaxy to the right line
        for y, line in enumerate(universe):
            newline = list(expanded_universe[y])
            newline.insert(x+added_amount, ".")
            s = "".join(newline)
            expanded_universe[y] = s
            print(f"Added {s}")

universe = list(expanded_universe)


# Go over all galaxies
for y, line in enumerate(universe):
    print(f"Updated universe[{y}]: {line}")
    for x, char in enumerate(line):
        if char == '#':
            galaxies[len(galaxies) + 1] = {
                "y": y,
                "x": x,
            }


for galaxy_key in galaxies.keys():
    galaxy = galaxies[galaxy_key]
    galaxies[galaxy_key]["distances"] = []
    print("===")
    print(f"Galaxy location: {galaxy_key}:{galaxy}")
    for galaxy_key_2 in galaxies.keys():
        if galaxy_key == 3 and galaxy_key_2 == 6:
            print("debug")
        galaxy_2 = galaxies[galaxy_key_2]
        print(f"Comparing to: {galaxy_key_2}:{galaxy_2}")
        if galaxy_key >= galaxy_key_2:
            print("Skipped.")
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