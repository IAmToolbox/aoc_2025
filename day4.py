# Day 4 instructions:
# Part 1: Find the amount of reachable paper rolls in the grid. Reachable rolls have 4 or less other rolls in adjacent positions
# Part 2: Repeatedly run part 1's logic to remove all possible rolls until no more reachable rolls are left

def day_4(part):
    input = ""
    with open("inputs/day4.txt") as f:
        input = f.read()
    input_splits = input.splitlines()

    # We will need a grid for this
    max_x = len(input_splits[0]) # Length of a single element, from left to right
    max_y = len(input_splits) # Length of the entire array, top to bottom

    if part == 1:
        reachable = 0
        for i in range(max_y):
            for j in range(max_x):
                if analyze_adjacent(input_splits, i, j, max_x, max_y):
                    reachable += 1
        
        print(f"The amount of reachable paper rolls is most likely {reachable}")
    
    if part == 2:
        removed = 0
        removal_queue = []
        while True:
            reachable = 0
            for i in range(max_y):
                for j in range(max_x):
                    if analyze_adjacent(input_splits, i, j, max_x, max_y):
                        reachable += 1
                        removal_queue.append((i, j)) # Save the position of the analyzed tile for removal
            if reachable == 0:
                break # Breaks out of the loop if there are no more reachable spaces
            
            for position in removal_queue:
                mutable_row = [] # Python strings are immutable so I need to turn them into a list rq
                for character in input_splits[position[1]]:
                    mutable_row.append(character)
                mutable_row[position[0]] = "."
                removed += 1
                input_splits[position[1]] = "".join(mutable_row)
            removal_queue = [] # Resets the queue for the next iteration
        
        print(*input_splits, sep="\n")
        print(f"Removed a total of {removed} rolls. That's a lot of damage.")

def analyze_adjacent(input_splits, x, y, max_x, max_y):
    if input_splits[y][x] == ".": # Empty space. Processing is not necessary
        return False
    
    if input_splits[y][x] == "@":
        adjacent_rolls = 0
        # Check each position
        # Top Left
        if is_valid_position(x - 1, y - 1, max_x, max_y):
            if input_splits[y - 1][x - 1] == "@":
                adjacent_rolls += 1
        # Top Center
        if is_valid_position(x, y - 1, max_x, max_y):
            if input_splits[y - 1][x] == "@":
                adjacent_rolls += 1
        # Top Right
        if is_valid_position(x + 1, y - 1, max_x, max_y):
            if input_splits[y - 1][x + 1] == "@":
                adjacent_rolls += 1
        # Center Right
        if is_valid_position(x + 1, y, max_x, max_y):
            if input_splits[y][x + 1] == "@":
                adjacent_rolls += 1
        # Bottom Right
        if is_valid_position(x + 1, y + 1, max_x, max_y):
            if input_splits[y + 1][x + 1] == "@":
                adjacent_rolls += 1
        # Bottom Center
        if is_valid_position(x, y + 1, max_x, max_y):
            if input_splits[y + 1][x] == "@":
                adjacent_rolls += 1
        # Bottom Left
        if is_valid_position(x - 1, y + 1, max_x, max_y):
            if input_splits[y + 1][x - 1] == "@":
                adjacent_rolls += 1
        # Center Left
        if is_valid_position(x - 1, y, max_x, max_y):
            if input_splits[y][x - 1] == "@":
                adjacent_rolls += 1
        
        if adjacent_rolls >= 4:
            return False
        else:
            return True

                
def is_valid_position(x, y, max_x, max_y): # helper functions go brrrrrrrrrrr
    if x < 0 or y < 0 or x >= max_x or y >= max_y:
        return False
    return True
