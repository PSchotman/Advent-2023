
import re

# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]


# Initial values
time = int(inputfile_lines[0].replace("Time:", "").replace(" ", ""))
current_record_distance = int(inputfile_lines[1].replace("Distance:", "").replace(" ", ""))

print(f"Time: {time}")
print(f"Distance: {current_record_distance}")

races = []
i = -1


i = i + 1
print("====================")
# Go over all possible times
possible_wins = 0
for pressed_time in range(time):
    # print(f"Pressed for {pressed_time}ms")
    timeleft = time - pressed_time
    distance = timeleft * pressed_time
    # print(f"Got distance: {distance}")

    if distance > current_record_distance:
        # print(f"Got a winner! {distance} > {current_record_distance}" )
        possible_wins = possible_wins + 1
    # print("---")
# print("...")
print(f"Possible wins for this race {possible_wins}")
races.append(possible_wins)

print(races)

wincount = 1
for wins in races:
    wincount *= wins

print(f"Should conclude to {wincount}")
# print(times)


# timeleft = time - timepress
# distance = timeleft + timepress
