
import re
from collections import Counter
from itertools import groupby
import itertools
import functools


# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

# ????#?????##??.???
# # Requirements: ['1', '3', '7', '3']
#               ????#?????##??.???
# Valid Option: #.###.#######..###
# Valid Option: #.###..#######.###
# Valid Option: #..###.#######.###
# Valid Option: .#.###.#######.###
#               .#.###.#######.###





# .#.###.#.###### 1,3,1,6
# ####.#...#... 4,1,1

# operational (.)
# damaged (#)
# unknown (?)

# Equipped with this information, 
# it is your job to figure out how many 
# different arrangements of operational 
# and broken springs fit the given 
# criteria in each row.
def generate_possibilities(pattern):
    count = pattern.count('?')
    results = []
    
    for bits in itertools.product("#.", repeat=count):
        temp_pattern = pattern
        for bit in bits:
            temp_pattern = temp_pattern.replace('?', bit, 1)
        results.append(temp_pattern)
    return results




# ['##.#..###', '##..#.###', '#.#.###', '####.#...#...', '#....######..#####.']
def is_valid_combination(row, part_requirements):
    # String should be at least #.#.#
    # Match the string to the requirements
    # pattern = r"\.*#+.+#+.+#+\.+"
    # pattern = r"\.*#+\.+#+\.+#+\.+"
    # pattern = r"\.*#+\.+#+\.+#+\.*"
    pattern = r"\.*(#+\.*?){%s}" % len(part_requirements)
    if re.match(pattern, row):
        # See if part requirements match
        groups = [''.join(g) for k, g in groupby(row)]
        hashes = [element for element in groups if '#' in element]
        # Just for safety
        if len(hashes) != len(part_requirements):
            return False
        i = 0
        valid = True
        # Go over all grouped characters
        for i, hash_count in enumerate(hashes):
            # Find #
            if len(hash_count) != int(part_requirements[i]):
                return False
        print(f"Valid Option: {row}")
        return valid
    return False

# Brute-force all possible combinations
rows = {}
valid_options = []
for y, line in enumerate(inputfile_lines):
    sections_string = line.split(" ")[0]
    part_numbers = line.split(" ")[1].split(",")
    rows[y] = {
        "part_requirements": part_numbers,
        "sections_string": sections_string,        
    }
    options = generate_possibilities(sections_string)
    print("======")
    print(f"Section {sections_string}")
    print(f"Requirements: {part_numbers}")
    for option in options:
        # print(f"Option: {option}")
        if is_valid_combination(option, part_numbers):
            valid_options.append(option)
print(valid_options)
print(len(valid_options))
# ['##.#..###', '##..#.###', '#.#.###']
    # sections_arr = re.split(r"\.|#", sections_string)
    # sections_arr = [section for section in sections_arr if section]  # remove empty strings
    # print(sections_arr)


    
    # is_valid_combination(rows[y]["sections"], rows[y][""])

    # for x, char in enumerate(line.split(" ")[0]):
    #     if char == ".":
    #         rows[y] = {

    #         }
    #     elif char == "#":
    #         pass
    #     elif char == "?":
    #         pass
    #     # rows[x] = {

    #     # }
    #     pass