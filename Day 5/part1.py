
import re

# Open file
with open("input.txt", encoding="utf-8") as f:
    mapsfile = [line.strip() for line in f]

# Initiate maps object
maps = []
# process file
i = 0
for line in mapsfile:
    i = i + 1
    # Requested seeds
    if line.find("seeds:") >= 0:
        # Extract numbers
        requested_seeds = line.split(":")[1].split(" ")
        # Clean empties
        requested_seeds = [int(seed) for seed in requested_seeds if seed]
        continue

    # Maps
    if line.find("map:") >= 0:      
        # status = "Processing map"
        source = line.split("-to-")[0]
        destination = line.split("-to-")[1].split(" map:")[0]
        # Add to maps
        maps.append({
            "from": source,
            "to": destination,
        })
        print(f"Processed: {source} - {destination}")
        continue
    # Extract {destination range start, source range start, range length}
    if bool(re.search(r'\d', line)):    
        res = [int(i) for i in line.split() if i.isdigit()]
        destinationRange = [res[0], res[0]+res[2]-1]
        sourceRange = [res[1], res[1]+res[2]-1]

        # Add to currently processed mapping
        iteration = len(maps) - 1

        # Add source range
        if "sourceRanges" not in maps[iteration]:
            maps[iteration]["sourceRanges"] = []
        
        # for number in tuple(sourceRange):
        maps[iteration]["sourceRanges"].append(sourceRange)
        # else:
        #     maps[iteration]["sourceRanges"] = maps[iteration]["sourceRanges"] + sourceRange

        # Add destination range
        if "destinationRanges" not in maps[iteration]:
            maps[iteration]["destinationRanges"] = []
        # for number in tuple(destinationRange):
        maps[iteration]["destinationRanges"].append(destinationRange)
        # else:
            # maps[iteration]["destinationRanges"] = maps[iteration]["destinationRanges"] + destinationRange
        # print("RES:", res)
        # print("...")

# print("REQUESTED: ", requested_seeds)
print(maps[0])


# print("...")
# print(maps.index[50]
# requested_seeds = [79]
status = ""
maps_dict = {map['from']: map for map in maps}
results = []
for number in requested_seeds:    
    status = "seed"
    print(f"LOOKING FOR {status}: {number}")
    for seedmap in maps:
        source = maps_dict[status]

        rangenumber = -1
        found = False
        for start, ends in source["sourceRanges"]:
            rangenumber = rangenumber + 1
            if found == True:
                continue
            # print(",,,")
            # print("start:", start)
            # print("ends: ", ends)
            if number >= start and number <= ends:
                number = source["destinationRanges"][rangenumber][0] + (number - start)
                print(f"Maps to number: {number}")
                found = True
        # Move on to destination table
        status = source["to"]

    results.append(number)
print(maps)
print("RESULTS:", results)
results.sort()
print("LOWEST: ",  results[0])
