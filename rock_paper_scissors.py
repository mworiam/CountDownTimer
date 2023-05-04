import random

# Define the valid options
options = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter your choice (rock/paper/scissors): ")

# Make sure the user enters a valid choice
while user_choice not in options:
    user_choice = input("Invalid choice. Enter rock, paper, or scissors: ")

# Generate a random computer choice
computer_choice = random.choice(options)

# Print the choices
print(f"You chose {user_choice}")
print(f"The computer chose {computer_choice}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins!")
    else:
        print("You win!")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("Computer wins!")
    else:
        print("You win!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins!")
    else:
        print("You win!")
