# Day 3 instructions
# Part 1: Turn on EXACTLY 2 batteries for each input line, in order to build the biggest number
# Part 2: Make an absurdly large number by turning on 12 batteries this time
import numpy as np

def day_3(part):
    input = ""
    with open("inputs/day3.txt") as f:
        input = f.read()
    input_splits = input.splitlines()

    if part == 1:
        first_max = float("-inf")
        second_max = float("-inf")
        total_joltage = 0
        first_position = 0
        for line in input_splits:
            for i in range(len(line)): # First loop to find the first value
                if int(line[i]) > first_max and i != len(line) - 1:
                    first_max = int(line[i])
                    first_position = i
            for j in range(first_position + 1, len(line)): # Second loop to find the second value
                if int(line[j]) > second_max:
                    second_max = int(line[j])
            total_joltage += (first_max * 10) + second_max
            first_max = float("-inf")
            second_max = float("-inf")
        
        print(f"The total joltage is: {total_joltage}")
    
    if part == 2:
        total_joltage = 0
        for line in input_splits:
            joltage_bank = strip_and_convert(line)
            print(joltage_bank)
            total_joltage += joltage_bank


        print(f"Is this amount correct? {total_joltage}")

def strip_and_convert(line):
    print(line)
    line_edited = []
    for i in range(len(line)):
        line_edited.append(line[i]) # Turning the entire thing into a list so I can easily mutate it
    for i in range(1, 10):
        while str(i) in line_edited:
            if len(line_edited) == 12:
                return int("".join(line_edited)) # Returns an integer version of the line if the line is 12 digits long already
            line_edited.pop(line_edited.index(str(i)))