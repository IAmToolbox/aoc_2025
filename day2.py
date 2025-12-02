# Day 2 instructions:
# Part 1: Check each given number range for any invalid IDs, which are numbers that have the same sequence of numbers repeated twice
# Part 2: Check each range again. Invalid IDs are numbers that have a sequence of numbers repeated AT LEAST twice
import re

def day_2(part):
    input = ""
    with open("inputs/day2.txt") as f:
        input = f.read()
    input_split = input.split(",")

    if part == 1:
        id_sum = 0
        for id_range in input_split:
            ids = id_range.split("-")
            lower_id = int(ids[0])
            higher_id = int(ids[1])

            for i in range(lower_id, higher_id + 1):
                if len(str(i)) % 2 == 1: # Takes numbers with odd digit amounts out of the equation
                    continue
                half_length = len(str(i)) / 2
                half_length = int(half_length) # Gotta type cast here ugh
                string_i = str(i)
                if string_i[:half_length] == string_i[half_length:]:
                    id_sum += i
        
        print(f"The code SHOULD be: {id_sum}")
    
    if part == 2:
        id_sum = 0
        for id_range in input_split:
            ids = id_range.split("-")
            lower_id = int(ids[0])
            higher_id = int(ids[1])

            for i in range(lower_id, higher_id + 1):
                string_i = str(i)
                # Time to assemble a bit of a complex loop
                # What it should do is check each digit individually, then check on steps of 2, then 3, and so on
                for amount in range(1, len(string_i) + 1):
                    regex = ""
                    for _j in range(amount):
                        regex = regex + "\d" # Will this even work??????????
                    split_i = re.findall(regex, string_i)
                    if len(split_i) == 1:
                        continue
                    print(split_i)
                    if is_all_equal(split_i):
                        id_sum += i
                        break
        
        print(f"Heavy doubts but the code may be: {id_sum}")

def is_all_equal(split_i):
    return len(set(split_i)) <= 1