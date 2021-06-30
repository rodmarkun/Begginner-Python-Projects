import random # We need to import random as we need the computer to take a random number
"""
The goal of this project is to make a simple application in which the computer
takes a random number from 1 to x (being x a given number by the user) and have
the user guess that same random number. The computer will give the user hints
about the number he has to guess.
"""
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: # While the user's guess is not equal to the random number the computer has chosen
        guess = int(input(f"Guess a number between 1 and {x}: "))
        # Give hints:
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
    # Number guessed:
    print(f"Congratulations! You guessed the number {random_number}!")

guess(int(input("The computer will guess a number from 1 to x. Please enter x: ")))