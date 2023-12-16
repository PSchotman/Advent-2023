
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
    
def process_sequence(sequence, reverse = False):
    result = []
    result.append(sequence)

    
    while len(sequence) > 1:
        if all(value == 0 for value in sequence):
            break
        if(reverse):
            sequence = [sequence[i+1] + sequence[i] for i in range(len(sequence)-1)]
        else:
            sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        result.append(sequence)
        
    return result

def reverse_sequence(sequence):
    sequence = sequence[::-1]  # Reverse the sequence
    result = [sequence[0]]  # Start with the last number in the original sequence

    for i in range(1, len(sequence)):
        # Add the current number to the next number
        num = result[-1] + sequence[i]
        result.append(num)

    return result[::-1]  # Reverse the sequence back to the original order


total_sum = 0
reverse_total_sum = 0
for sequence in sequences:
    # print(f"GOT: {results}")
    results = process_sequence(sequence)

    reversed_sequence = list(sequence)
    reversed_sequence.reverse()
    reversed_results = process_sequence(reversed_sequence)
    reversed_results.reverse()

    # print(f"Sequence: {sequence}")
    results.reverse()
    sequence_sum = 0
    reverse_sequence_sum = 0
    for i, result in enumerate(results):
        print(f"Mapping:  {result}")
        # if all(for n in n in result if result[n] == 0):
        #     continue
        # print(f"+{add_number}")
        add_number = result[-1]
        sequence_sum += add_number

        reverse_add_number = reversed_results[i][-1]
        reverse_sequence_sum += reverse_add_number
    print("=====")
    print(f"Sequence {reversed_sequence}")
    print(f"Previous number: {reverse_sequence_sum}")
    print(f"Sequence {sequence}")
    print(f"Next number: {sequence_sum}")
    print("=====")
    total_sum += sequence_sum
    reverse_total_sum += reverse_sequence_sum
print(f"SUM: {total_sum}")
print(f"REVERSE SUM: {reverse_total_sum}")
            
    # print(f"GOT: {sequence}")