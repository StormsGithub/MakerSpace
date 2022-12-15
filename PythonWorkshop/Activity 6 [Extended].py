# Python Workshop, Activity 06 (Extended)

import random

# Create a flag to determine if we stay in the loop
repeat = True

# Get user input
numSides = int(input("How many sides to the dice?"))

# A loop that executes so long as the repeat flag is 'True'
while repeat == True:
    # Randomly generate a number between 1 and what the user inputs
    dice = random.randint(1, numSides)
    # Print the result
    print("You rolled a:", dice)
    # Get user input
    answer = input("Would you like to roll again? y/n")
    
    if answer == "n":
        break
