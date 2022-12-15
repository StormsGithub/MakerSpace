# Python Workshop, Activity 07

# Import the Random module
import random

# Define actions for the Computer to choose from
actions = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# Run indefinitely
while True:
    # Get user input
    user_choice = input("Rock, Paper, or Scissors?")
    
    # Use the Random module to choose an item in actions
    computer_choice = random.choice(actions)
    
    # If player and computer chose the same thing:
    if user_choice == computer_choice:
        print("It's a tie!")
    
    # Else, if the user chose Rock
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("Rock smashes scissors, you won!")
        player_score = player_score + 1
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Paper covers rock, you lost!")
        computer_score = computer_score + 1
    
    # Else, if the user chose Paper
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("Paper covers rock, you won!")
        player_score = player_score + 1
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("Scissors cuts paper, you lost!")
        computer_score = computer_score + 1
    
    # Else, if the user chose Scissors
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("Scissors cuts paper, you won!")
        player_score = player_score + 1
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("Rock smashes scissors, you lost!")
        computer_score = computer_score + 1
    
    # If none of the above, user likely entered an incorrect option
    else:
        print("Incorrect input! Please try again.")

        # Print the scoreboard
    print("--------------")
    print("Current Score:")
    print("Player | Computer")
    print(player_score, "-", computer_score)
    print("--------------")
