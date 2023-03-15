import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# initialize the number of guesses to 0
guesses = 0

# ask the player to guess the number
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1

    # give a hint if the guess is too high or too low
    if guess > number:
        print("Too high, try again!")
    elif guess < number:
        print("Too low, try again!")
    else:
        print("Congratulations, you guessed the number in", guesses, "guesses!")
        break



