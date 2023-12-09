#   0123456789
# 0 467..114..
# 1 ...*......
# 2 ..35..633.
# 3 ......#...
# 4 617*......
# 5 .....+.58.
# 6 ..592.....
# 7 ......755.
# 8 ...$.*....
# 9 .664.598..
# In this schematic, two numbers are not part numbers because they
# are not adjacent to a symbol: 114 (top right) and 58 (middle right).
# Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

import re

with open("input.txt", "r") as f:
    # with open("input.txt", "r") as f:
    schematic = [line.strip() for line in f]

# print(schematic)


number_coordinates = []
# number coordinates
rownumber = -1
for row in schematic:
    rownumber = rownumber + 1
    # split row into parts to find whole numbers
    values = re.split(r"(\d+|\D+)", row)
    # remove empties
    values = [value for value in values if value]
    start = 0
    for value in values:
        if value.isdigit():
            # print("start position: ", row.find(value))
            # print("end   position: ", row.find(value) + len(value))
            # print(value)
            number_coordinates.append(
                {
                    "row": rownumber,
                    "start": start,
                    "len": len(value),
                    "value": value,
                    "counts": False,
                }
            )
        start = start + len(value)

# rondom checken cell
# start -1
# eind + 1
# row -1
# row +1

# limits:
# rows: 0, len(schematic)-1
# columns: len(schematic[row])-1

# { "row", "start", "end", "value" }
symbols = ["-", "+", "*", "&", "/", "@", "%", "=", "$", "#"]
# print(number_coordinates)
for number in number_coordinates:
    # print("looking for", number)
    for y_loc in range(3):
        # print("y_loc_old", y_loc)
        y_loc = number["row"] + y_loc - 1
        # print("y_loc_new", y_loc)
        # Skip non existing row
        if y_loc < 0 or y_loc > len(schematic) - 1:
            continue

        for x_loc in range(len(number["value"]) + 2):
            x_loc = number["start"] + x_loc - 1
            # Skip non-existing col
            if x_loc < 0 or x_loc > len(schematic[number["row"]]) - 1:
                continue

            # print("coordinates", y_loc, x_loc, schematic[y_loc][x_loc])  # coordinates 139 139 .
            if schematic[y_loc][x_loc] in symbols:
                # print("Found symbol at", y_loc + 1, x_loc + 1, schematic[y_loc][x_loc])
                number["counts"] = True
    # print("result for", number)
    # print()

# print(number_coordinates)
totalsum = 0
for number in number_coordinates:
    # print(number)
    if number["counts"] == True:
        totalsum = totalsum + int(number["value"])

print("totalsum", totalsum)
# for row in range(3):
# for char in range(number["end"] - number["start"] + 2):
# print(row, char)

# if(number['row'] < len(schematic)):
# if(number['start'] < 1):
# if(number['end'] < len(schematic)):
