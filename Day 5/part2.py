
import re

# Open file
with open("input.txt", encoding="utf-8") as f:
# with open("input.txt", encoding="utf-8") as f:
    mapsfile = [line.strip() for line in f]

# Initiate maps object
maps = []
# Process file
i = 0
for line in mapsfile:
    i = i + 1
    # Requested seeds
    if line.find("seeds:") >= 0:
        # Extract numbers
        initial_seed_numbers = line.split(":")[1].split(" ")
        # Clean empties
        initial_seed_numbers = [int(seed) for seed in initial_seed_numbers if seed]
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
        if res[2] == 1:
            destinationRange = res[0]
            sourceRange = res[1]
        else:
            destinationRange = range(res[0], res[0]+res[2] - 1)
            sourceRange = range(res[1], res[1]+res[2] - 1)

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

# Set initial seed ranges
requested_seed_ranges = []
i = 0
for number in initial_seed_numbers[0::2]:
    # requested_seed_ranges.append([initial_seed_numbers[i], initial_seed_numbers[i+1]])
    requested_seed_ranges.append(range(initial_seed_numbers[i], initial_seed_numbers[i]+initial_seed_numbers[i+1]-1))
    i = i + 2


# 79 93
# 98 101
# if search lowest  in mapping > write down
#     lowest? > save
#     update search mapping 
# or
# if search highest in mapping > write down
#     lowest? > save
# search_mapping = 
# if 
# lowest 79

# 79 93
# 50 99
#=79-93 > index 79-93 > destinationrange index 79-93 > only solve matches

# 81 95


def loopsearchrange(status, maps_dict, search_range, final_outcome):
    current_lowest = None
    
    source = maps_dict[status]
    print(f"==========")
    print(f"Processing:")
    print(f"{source['from']}:{source['to']}")
    print(f"Search:  {search_range}")

    # Update status
    status = source["to"]


    # ============================ #
    # Get matches from search:source
    # ============================ #

    mapping_index = -1
    # Map new search ranges for the next mapping
    new_search_ranges = []
    # Keep track of what we already mapped
    mapped_ranges = []
    for mapping in source["sourceRanges"]:
        mapping_index = mapping_index + 1
        
        print(f"Mapping: {mapping}")
        
        # only first number matches, turn range into int
        if isinstance(mapping, int):
            # mapping = search_range
            match_number_start = mapping
            match_number_ends = mapping
            # mapping 

        # search int     mapping range
        if isinstance(mapping, range) and isinstance(search_range, int):
            # Match start number
            match_number_start = max(search_range, mapping[0])
            # Match end number
            match_number_ends = min(search_range, mapping[-1])


        # search range   mapping int
        elif isinstance(search_range, range) and isinstance(mapping, int):
            # Match start number
            match_number_start = max(search_range[0], mapping)
            # Match end number
            match_number_ends = min(search_range[-1], mapping)
        # search int mapping int
        elif isinstance(search_range, int) and isinstance(mapping, int):
            # Match start number
            match_number_start = max(search_range, mapping)
            # Match end number
            match_number_ends = min(search_range, mapping)
        # search range mapping range
        else:
            # Match start number
            match_number_start = max(search_range[0], mapping[0])
            # Match end number
            match_number_ends = min(search_range[-1], mapping[-1])
            
        
        # Nothing can be found, move on
        if match_number_start > match_number_ends:
            continue
        
        if isinstance(mapping, int):
            # # Match index start
            # match_index_start = 0
            # # Match index end
            # match_index_ends  = 0
            if isinstance(source["destinationRanges"][mapping_index], range):
                overlap = source["destinationRanges"][mapping_index][match_index_start]
            else:
                overlap = source["destinationRanges"][mapping_index]
        else:
            # Match index start
            match_index_start = mapping.index(match_number_start)
            # Match index end
            # if match_number_ends == mapping[0]:
                # match_index_ends = mapping[0]
            # else:    
            match_index_ends = mapping.index(match_number_ends)

            # Find out which numbers should be mapped to new numbers
            overlap = range(
                source["destinationRanges"][mapping_index][match_index_start], 
                source["destinationRanges"][mapping_index][match_index_ends] + 1
            )
        
        
        # Add overlap to passed on range(s)
        if overlap:
            print(f"Overlap found:({match_number_start}, {match_number_ends + 1})")
            print("SourceRange", source["sourceRanges"][mapping_index])
            print("TargetRange", source["destinationRanges"][mapping_index])
            print(f"Added range to next search from overlap: {overlap}")
            if isinstance(mapping, int):
                mapped_ranges.append(match_number_start)
            else:
                mapped_ranges.append(range(match_number_start, match_number_ends + 1))
            new_search_ranges.append(overlap)
        
            

    # Remove mapped_ranges from search_range, add result to new_search_ranges
    remaining = search_range

    mapped_ranges = sorted(mapped_ranges, key=lambda r: r.start)
    # Go over all currently mapped ranges
    for mapped_range in mapped_ranges:
        if remaining is None:
            continue
        # Remove mapped range from search_range
        print("Already mapped:", mapped_range)

        
        
        # Chunk was already taken off, missing start
        # if mapped_range[0] < remaining[0]:
        #     remaining = range(mapped_range[0], remaining[-1])

        # calc: remaining = max(mapped) + 1, max(remaining)

        # Mapped range starts after the remaining, need to add to next search
        if mapped_range[0] > remaining[0]:
            gap = range(remaining[0], mapped_range[0] - 1)
            # new_search_ranges.append(gap)

        # If both ends don't meet:
        if mapped_range[-1] != remaining[-1]:
            # Remaining = max(mapped) + 1, max(remaining) - 1
            remaining = range(mapped_range[-1] + 1, remaining[-1] + 1)
        
        
        print(f"Search:  {search_range}")
        
        # Both ends meet, clear the remainder
        if mapped_range[-1] == remaining[-1]:
            remaining = None
        print("Remaining:", remaining)
        

    # Add all leftovers
    if remaining is not None:
        new_search_ranges.append(remaining)
    # We're at location, stop here
    # if status == "location":
    new_search_ranges = sorted(new_search_ranges, key=lambda r: r[0])
    print(f"Current search ranges: {new_search_ranges}")
        # return new_search_ranges[0][0]
    
    
    outcome = 0
    result = 999999999999999


    # Move on to next mapping
    for search_range in new_search_ranges:
        
        if status == "location":
            final_outcome.append(search_range)
        else:
            result = loopsearchrange(status, maps_dict, search_range, final_outcome)
            print("RESULT: ", result)
            # return new_search_ranges[0][0]
        # # Continue on
        # if result < outcome:
        #     outcome = result
    return final_outcome
        # print(result)
    # return result
        #     if check_number is None:
        #         return None
        #     if check_number < lowest_number:
        #         return check_number
    



        
        

    print("==================")

    # 79 93
    # 50 75

    #=79-75,76-93
    #=return loopsearchrange('70-75'), return loopsearchrange('76-93')



print(f"Initial seed ranges: {requested_seed_ranges}")
print("===")
# print("...")
# print(maps.index[50]
# requested_seeds = [79]

lowest_location = 9999999999
maps_dict = {map['from']: map for map in maps}
results = []


# ========================= #
# GO OVER INItiAL SEED RANGES
# ========================= #
status = ""
# Get seed ranges
lowest_location = []
rangenumber = 0
for search_range in requested_seed_ranges:
    print("...")
    print(f"Processing seed range: {search_range}")
    status = "seed"
    result = loopsearchrange(maps_dict=maps_dict, status=status, search_range=search_range, final_outcome=[])
    print("SEED OUTCOME RESULT:", result)
    lowest_location = lowest_location + result

# sorted(result)

print(f"=====================")
print(f"=====================")
print(f"FINAL OUTCOME RESULT BEFORE SORT: {lowest_location}")

# smt = lambda r: r.start
# print(smt)
lowest_location = sorted(lowest_location, key=lambda r: r[0])  # sort by the first element of each list
print(f"FINAL OUTCOME RESULT AFTER SORT: {lowest_location}")
print("AND THE FINAL ANSWER IS:", lowest_location[0][0])
# lowest_location = [list(r) for r in lowest_location]  # convert ranges to lists
