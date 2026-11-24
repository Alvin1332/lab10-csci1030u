# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # Read tokens from left to right
    # Store numbers in a  stack
    # When an operator appears use the last 2 numbers in the stack
    # Calculate result and put it back in the stack
    
    stack = []

    #Go through each token
    for token in tokens:

        #if you find an operator
        if token in ["+", "-", "*", "/"]:

            #remove first and second last 
            b = stack.pop()
            a = stack.pop()

        # do correct opperation
            if token == "+":
                result = a + b
            if token == "-":
                result = a - b
            if token == "*":
                result = a * b
            if token == "/":
                result = int(a / b)

         #Store the result in the stack
            stack.append(result)

        else:
            #convert string into int
            stack.append(int(token))

    return stack.pop()

    pass


def decode_string(s):
    # Outline:
    # Go through each character in a string
    # Keep track of the number of repeitions 
    # When [ appears , save current text and number in a count 
    # When ] appears, repeat the text inside the brackets
    # Combine it with the previous text 
    # Return the decoded string 

    stack = [] #stores previous text and repeat numbers
    current = "" #stores the text we are currently building
    number = 0  #stores how many times to repeat

    #Go through each character in the string
    for char in s:

        #if char is a digit
        if char.isdigit():
            number = number * 10 + int(char) #build the number

             # If we find an opening bracket.
        elif char == "[":

            # Save the current text and repeat number in the stack.
            stack.append((current, number))

            # Reset current text and number for inside the brackets.
            current = ""
            number = 0

        # If we find a closing bracket.
        elif char == "]":

            # Remove the last saved text and repeat number.
            previous, repeat = stack.pop()

            # Repeat the letters and combine with previous text.
            current = previous + current * repeat

        else:
            # If it's a letter, add it to the current text.
            current += char

    # Return the final decoded string.
    return current

    pass


def daily_temperatures(temps):
    # Outline:
    #   GO through each day of temps
    # Store indices of days waiting for warmer temps
    # when a warmer temp is found calculate days waited
    # store number of days in result list
    # return 0 for days that never get warmer 

    result = [0]* len(temps) # Initialize result list with zeros

    stack = [] #store indices of days waiting for warmer temps

    for i in range (len(temps)):
        #while the stack is not empty and the current temp is warmer than the last stored temp
        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()

            result[previous_day] = i - previous_day #days waited

        stack.append(i) #store the current day index

    return result
        
    
    pass


def num_islands(grid):   
    # Outline:
    # Go through every cell in the grid.
    # When land is found, count a new island.
    # Use a stack to check all connected land.
    # Mark visited land so it isn't counted twice.

    # Keep track of how many islands we find.
    islands = 0

    # Store land positions we've already checked.
    visited = set()

    # Go through every row.
    for r in range(len(grid)):

        # Go through every column in the row.
        for c in range(len(grid[0])):

            # If we find land that hasn't been visited.
            if grid[r][c] == "1" and (r, c) not in visited:

                # Count a new island.
                islands += 1

                # Start checking connected land from this position.
                stack = [(r, c)]
                visited.add((r, c))

                # Keep checking while there are positions in the stack.
                while stack:

                    # Remove the last position to check.
                    row, col = stack.pop()

                    # Check up, down, left, and right.
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                        # Calculate the neighbouring position.
                        nr = row + dr
                        nc = col + dc

                        # Make sure the position is inside the grid.
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):

                            # Check if it's land we haven't visited.
                            if grid[nr][nc] == "1" and (nr, nc) not in visited:

                                # Mark the land as visited.
                                visited.add((nr, nc))

                                # Add it to the stack to check its neighbours.
                                stack.append((nr, nc))

    # Return the number of islands found.
    return islands
     
    
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
