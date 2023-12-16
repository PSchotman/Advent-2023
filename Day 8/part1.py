
import re
from collections import Counter


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

stepcounter = 0

step = "AAA"
while step != "ZZZ":
    for instruction in instructions:
        stepcounter = stepcounter + 1
        if(instruction == "L"):
            print(f"Going left on ['{step}']{mappings[step]}")
            step = mappings[step]["left"]
            print(step)
        elif(instruction == "R"):
            print(f"Going right on ['{step}']{mappings[step]}")
            step = mappings[step]["right"]
            print(step)


print(stepcounter)
        