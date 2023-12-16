
import itertools
import re
from collections import Counter
import sys
sys.setrecursionlimit(140*140)
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# directions[4][7] = up, down
# directions[4][7] = (1, 0), (-1, 0)
instructions = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, 1),  (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0),  (0, -1)],
    "F": [(1, 0),  (0, 1)],
    ".": [(0, 0)],
    "S": [(1, 0),  (0, 1), (-1, 0), (0, -1)],
}
field = []
def flood_fill(x ,y, old, new):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return
    
    
    # secondly, check if the current position equals the old value
    if field[y][x] == new:
        return
    
    if field[y][x] == "." or field[y][x] == "#":
        # thirdly, set the current position to the new value
        field[y][x] = new
        # fourthly, attempt to fill the neighboring positions
        flood_fill(x+1, y, old, new)
        flood_fill(x-1, y, old, new)
        flood_fill(x, y+1, old, new)
        flood_fill(x, y-1, old, new)

# .....  .....     ..F7.  ..45.
# .S-7.  .012.     .FJ|.  .236.
# .|.|.  .1.3.     SJ.L7  01.78
# .L-J.  .234.     |F--J  14567
# .....  .....     LJ...  23...

def print_map(map):
    # Get the maximum y and x coordinates
    max_y = max(coord[0] for coord in map.keys())
    max_x = max(coord[1] for coord in map.keys())

    # Create a 2D list with the same size as the map
    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with the values from the map
    for coord, value in map.items():
        grid[coord[0]][coord[1]] = value

    # Print the grid line by line
    for line in grid:
        print("".join(line))

# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

map = {}
start_position = []
# for y, line in enumerate(inputfile_lines):
#     for x, instruction in enumerate(line):
#         if instruction in instructions:
#             map[y, x] = instruction
#         else:
#             map[y, x] = "."
# Add border around the map


for y in range(len(inputfile_lines) + 2):
    for x in range(len(inputfile_lines[0]) + 2):
        if 0 < y < len(inputfile_lines) + 1 and 0 < x < len(inputfile_lines[0]) + 1:
            instruction = inputfile_lines[y - 1][x - 1]
            if instruction == "S":
                start_position.append(y)
                start_position.append(x)
            if instruction in instructions:
                map[y, x] = instruction
            else:
                map[y, x] = "."
        else:
            map[y, x] = "."  # Use '#' or any other character for the border

# Now map includes the original map with a border around it

# "|": [(-1, 0), (1, 0)],
# "-": [(0, 1), (0, -1)],
# "L": [(-1, 1)],
# "J": [(-1, -1)],
# "7": [(1, -1)],
# "F": [(1, 1)],
# ".": [(0, 0)],
# "S": [(1, 1), (-1, -1)],

# Start at S
# TODO: Follow the thread in all directions untill you're back to start
# keep track of last done instruction, look if it can come back as well
# if it can, keep going

# If we're not back to start or if we're at ".", kill all positions we have had (except start)

# start_instructions = map[start_s[0], start_s[1]]
# for start_instruction in start_instructions:
#     current_position = (start_s[0], start_s[1])
#     visited = {}
#     looped = False
#     while looped == False:
#         next_position = (current_position[0]+start_instruction[0], current_position[1]+start_instruction[1])
#         if next_position == (start_s[0], start_s[1]):
#             looped = True
        
        # visited[y, x] = true

        # search_set = (-instruction_set[-0], -instruction_set[1])

revised_map = dict(map)
changed_cell = True
s_loop = {}
# Clean the entire map
while changed_cell != False:
    # Assume no change will be made
    changed_cell = False

    # Go over every position in map
    for y, x in revised_map:

        # What are we parsing?
        instruction_string = revised_map[y, x]

        # If instruction is a "S", continue
        if instruction_string == "S":
            continue
        
        # If instruction is a ".", continue
        if instruction_string == ".":
            continue
        # Get all instructions for position
        instruction_sets = instructions[instruction_string]
        
        # Assume all pieces connect back
        all_pieces_connect = True

        # Get instructions to be converted into positions we need to check
        for instruction_set in instruction_sets:
            search_set = (-instruction_set[-0], -instruction_set[1])
            
            # Get next instruction string
            next_instruction_string = revised_map[y + instruction_set[0], x + instruction_set[1]]
            # Get next instruction sets
            next_instruction_sets = instructions[next_instruction_string]
            
            # Something doesn't connect back. So flag our current position to be cleared
            if search_set not in next_instruction_sets:
                all_pieces_connect = False

        # Not all next pieces connect back, a change has to be made
        if all_pieces_connect == False:
            changed_cell = True
            revised_map[y, x] = "."

map = dict(revised_map)
print_map(map)

# Fitbit
steps = 0
# Go to start
start_instructions = instructions["S"]
# Go away from start
for start_instruction in start_instructions:
    steps = 0
    # Current position
    current_position = start_position
    # Keep track of the places we've visited
    visited = {}
    def clear_map_from_visited():
        for dy, dx in visited:
            revised_map[dy, dx] = "."

    # Keep track of the instruction being executed
    current_instruction = start_instruction
    # Know how we should be able to get back
    # get_back_instruction = (-start_instruction[0], -start_instruction[1])

    # Are we back to start?
    back_to_start = False
    while back_to_start == False:
        steps = steps + 1
        get_back_instruction = (-current_instruction[0], -current_instruction[1])

        # print(f"From {current_position}")
        # print(f"We apply {current_instruction}")
        # Get next position
        next_position = (current_position[0] + current_instruction[0], current_position[1] + current_instruction[1])
        
        # Get the next position string
        next_position_string = map[next_position]
        # print(f"And end up {next_position}: {next_position_string}")

        # Get the instructions mapped for the next step
        next_position_instructions = instructions[next_position_string]

        if next_position_string == "S":
            # We made a succesfull circle! Yay!
            back_to_start = True
            s_loop = visited
            s_loop[start_position[0], start_position[1]] = True
            break
        
        # Reached the end. Remove all visited spots
        if next_position_string == ".":
            clear_map_from_visited()
            break

        # Already been here
        if next_position in visited:
            clear_map_from_visited()
            break

        # Are here
        visited[next_position] = True
        
        # Can't get back, so quit here
        if get_back_instruction not in next_position_instructions:
            continue
        
        # Go over positions for next instruction
        for next_position_instruction in next_position_instructions:
            # We don't need to move back
            if get_back_instruction == next_position_instruction:
                continue
            
            current_position = next_position
            current_instruction = next_position_instruction
            get_back_instruction = (-next_position_instruction[0], -next_position_instruction[1])
            break
            # current_position_string = next_position_string
            # current_instruction = map[current_instruction]
        

        # if visited[0,0] == True:
        #     break

    if back_to_start == True:
        break

print("===")
for y, x in map:
    if (y, x) not in s_loop:
        map[y, x] = "."
# print_map(map)
print(f"Halfway point: {int(steps/2)}")
# print(s_loop)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
new_map = []
current_y = 0
line = ""
for y, x in map:
    if current_y != y:
        current_y = y
        line_under = ""
        for char in line:
            if char == "S" or char == "|" or char == "7" or char == "F":
                line_under += "|"
            else:
                line_under += "#"
        new_map.append(list(line))
        new_map.append(list(line_under))
        line = ""
    char = map[y, x]
    line += char
    
    if char == "S" or char == "-" or char == "L" or char == "F":
        line += "-"
    else:
        line += "#"

new_map.append(list(line))

for line in new_map:
    print(line)

# matrix = flood_recursive(new_map)
field = new_map
flood_fill(0, 0, ".", "@")
for line in field:
    print("".join(line))

mapstring = "".join(list(itertools.chain.from_iterable(new_map)))

print(f"Total trapped: {mapstring.count('.')}")
