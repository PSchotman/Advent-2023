
import re

# Open file
with open("input-sample.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]


times     = [int(i) for i in inputfile_lines[0].split() if i.isdigit()]
distances = [int(i) for i in inputfile_lines[1].split() if i.isdigit()]

races = []
i = -1
for time in times:
    i = i + 1
    current_record_distance = distances[i]
    print("====================")
    print(f"Checking race: {time}")
    print(f"Record distance: {current_record_distance}")

    # Go over all possible times
    possible_wins = 0
    for pressed_time in range(time):
        print(f"Pressed for {pressed_time}ms")
        timeleft = time - pressed_time
        distance = timeleft * pressed_time
        print(f"Got distance: {distance}")

        if distance > current_record_distance:
            print(f"Got a winner! {distance} > {current_record_distance}" )
            possible_wins = possible_wins + 1
        print("---")
    print("...")
    print(f"Possible wins for this race {possible_wins}")
    races.append(possible_wins)

print(races)
wincount = 1  # Don't use 0 here, otherwise, you'll get zero 
             # because anything times zero will be zero.
for wins in races:
    wincount *= wins

print(f"Should conclude to {wincount}")
# print(times)


# timeleft = time - timepress
# distance = timeleft + timepress
