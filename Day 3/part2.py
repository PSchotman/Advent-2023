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

# number coordinates
number_coordinates = []
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


# gear coordinates
gears = []
rownumber = -1
for row in schematic:
    rownumber = rownumber + 1
    colnumber = -1
    for char in row:
        colnumber = colnumber + 1
        if char == "*":
            # print("start position: ", row.find(value))
            # print("end   position: ", row.find(value) + len(value))
            # print(value)
            gears.append(
                {
                    "row": rownumber,
                    "col": colnumber,
                    "connected_numbers": [],
                }
            )


# for number in number_coordinates:
#     print(number)

for gear in gears:
    # print("=====")
    # print("Processing GEAR: ", gear)
    # print("=====")
    check_rows = [gear["row"] - 1, gear["row"], gear["row"] + 1]
    check_cols = [gear["col"] - 1, gear["col"], gear["col"] + 1]
    for number in number_coordinates:
        # print("Processing NUMBER:", number)
        number_cols = range(number["start"], number["start"] + number["len"])
        # print("Checking rows: ", check_rows)
        # print("Checking cols: ", check_cols)
        # print("number_cols", number_cols)
        if number["row"] in check_rows and any(
            item in check_cols for item in number_cols
        ):
            gear["connected_numbers"].append(number["value"])
            # print("FOUND MATCH", number["value"])
        # print()

totalsum = 0
# print()
# print("Gears:")
for gear in gears:
    # print(gear)
    if len(gear["connected_numbers"]) > 1:
        result = 1
        for number in gear["connected_numbers"]:
            result = result * int(number)
        totalsum = totalsum + result

print("Total:", totalsum)
