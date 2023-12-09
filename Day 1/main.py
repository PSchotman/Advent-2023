import re
from word2number import w2n


def extract_numbers(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    number_word_mapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    numberslist = []

    for line in lines:
        line = line.replace("\n", "")

        print(line)
        for word, number in number_word_mapping.items():
            line = line.replace(word, number)
        print(line)

        numbers = []  # Start with an empty list
        for char in line:  # Iterate over each character in the string
            if char.isdigit():  # Check if the character is a digit
                numbers.append(char)  # If it is, add it to the list

        # Print the first and last numbers
        if numbers:
            print(numbers[0] + numbers[-1])
            # print()
            numberslist.append(f"{numbers[0]}{numbers[-1]}")

        print()

    return numberslist


numberslist = extract_numbers("input.txt")
total = 0
for number in numberslist:
    total += int(number)

print(total)
