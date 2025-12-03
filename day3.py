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
            potential_values = np.full(12, float("-inf"))
            joltage_multiplier = 1000000000000 # Initialize this with 12 zeroes to serve as a multiplier
            joltage_bank = 0
            position = 0
            for i in range(len(potential_values)):
                for j in range(position, len(line)):
                    if int(line[j]) > potential_values[i]:
                        position = j
                        potential_values[i] = int(line[j])
                position += 1
            for value in potential_values:
                joltage_bank += value * joltage_multiplier
                joltage_multiplier //= 10
            total_joltage += joltage_bank


        print(f"Is this amount correct? {total_joltage}")