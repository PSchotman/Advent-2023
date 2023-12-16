
import re
from collections import Counter


# Open file
with open("input.txt", encoding="utf-8") as f:
    inputfile_lines = [line.strip() for line in f]

sequences = []

for line in inputfile_lines:
    numbers = line.split(" ")
    sequence = []
    for number in numbers:
        sequence.append(int(number))
    sequences.append(sequence)

print("Initial seed:")
# print(sequences)
for sequence in sequences:
    print(sequence)
print("-------------")


# def process_sequence(sequence):
#     result = []
#     result.append(sequence)
    
#     while len(sequence) > 1:
#         sequence = [abs(sequence[i+1] - sequence[i]) for i in range(len(sequence)-1)]
#         result.append(sequence)
        
#     return result
    
def process_sequence(sequence):
    result = []
    result.append(sequence)
    
    while len(sequence) > 1:
        sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        result.append(sequence)
        
    return result

total_sum = 0
for sequence in sequences:
    # print(f"GOT: {results}")
    results = process_sequence(sequence)
    # print(f"Sequence: {sequence}")
    results.reverse()
    sequence_sum = 0
    for result in results:
        print(f"Mapping:  {result}")
        # if all(for n in n in result if result[n] == 0):
        #     continue
        # print(f"+{add_number}")
        add_number = result[-1]
        sequence_sum += add_number
    print("=====")
    print(f"Sequence {sequence}")
    print(f"Next number: {sequence_sum}")
    print("=====")
    total_sum += sequence_sum
print(f"SUM: {total_sum}")
            
    # print(f"GOT: {sequence}")