# Python Workshop, Activity 06

# Import the "random" module
import random

# Get user input
numSides = int(input("How many sides to the dice?"))
# Randomly generate a number between 1 and what the user inputs
dice = random.randint(1, numSides)

# Print the result
print("You rolled a:", dice)
