
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


# Had to look all this up :(
@functools.cache
def calculate_valid_solutions(record: str, groups: tuple[int, ...]) -> int:
    # If there are no more spots to check,
    # our only chance at success is if there are no `groups` left
    if not record:
        return len(groups) == 0

    # If there are no more groups the only possibility of success
    # is that there are no `#` remaining
    if not groups:
        return "#" not in record

    first_char, remaining_record = record[0], record[1:]

    # Ignore dots and continue recursion
    if first_char == ".":
        return calculate_valid_solutions(remaining_record, groups)

    # If first character is a `#`, we're at the start of a group!
    # Make sure there are enough characters here to fill the first group
    if first_char == "#":
        current_group = groups[0]
        # Check if we have enough characters to match,
        # if they are only `#` and not `.` 
        # and if we are either at the end of the record 
        # or the next character is not also a `#` (would be too big)
        if (
            len(record) >= current_group
            and all(char != "." for char in record[:current_group])
            and (len(record) == current_group or record[current_group] != "#")
        ):
            return calculate_valid_solutions(record[current_group + 1 :], groups[1:])

        return 0

    # If first character is a `?`, we consider both possibilities: 
    # it could be either `#` or `.`
    if first_char == "?":
        return (
            calculate_valid_solutions(f"#{remaining_record}", groups)
            + calculate_valid_solutions(f".{remaining_record}", groups)
        )

def solve_line(line: str, with_multiplier=False) -> int:
    record, raw_shape = line.split()
    shape = tuple(map(int, raw_shape.split(",")))

    if with_multiplier:
        record = "?".join([record] * 5)
        shape *= 5

    return calculate_valid_solutions(record, shape)

totalscore = sum(solve_line(line, with_multiplier=True) for line in inputfile_lines)
print(totalscore)
raise










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


# ?#?#?#?#?#?#?#? 1,3,1,6 == 1 option
# .#.###.#.######
# 8x"?"


# ?###???????? == 10 options
# 9x"?"


# ?###??????????###??????????###??????????###??????????###???????? == 506250 options
# 49x"?"
# 506250

