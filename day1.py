# Day 1 instructions:
# Part 1: Find the combination to a safe. The code is the amount of times the dial points to 0 in the sequence.
# The dial starts pointing at 50
# Part 2: The code is actually the amount of total times the dial passes 0 on every rotation.
# The dial still starts pointing at 50

def day_1(part):
    if part == 1:
        pointer = 50
        code_count = 0
        input_text = ""
        with open("inputs/day1.txt") as f:
            input_text = f.read()
        input_split = input_text.split("\n")
        for step in input_split:
            steps = int(step[1:])
            if step[0] == "R":
                pointer += steps
            elif step[0] == "L":
                pointer -= steps
            
            while pointer >= 100:
                pointer -= 100
            
            while pointer <= -1:
                pointer += 100
            
            if pointer == 0:
                code_count += 1
        
        print(f"The code is: {code_count}")
    
    if part == 2:
        pointer = 50
        code_count = 0
        input_text = ""
        with open("inputs/day1.txt") as f:
            input_text = f.read()
        input_split = input_text.split("\n") # I should put these in their own function tbh. Food for thought for future days
        for step in input_split:
            steps = int(step[1:])
            if step[0] == "R":
                for i in range(steps):
                    pointer += 1
                    if pointer >= 100:
                        pointer -= 100
                    if pointer == 0:
                        code_count += 1
            elif step[0] == "L":
                for i in range(steps):
                    pointer -= 1
                    if pointer <= -1:
                        pointer += 100
                    if pointer == 0:
                        code_count += 1
        
        print(f"The real code is: {code_count}")


