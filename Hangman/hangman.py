import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Keep track of all letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Keep track of what the user has guessed

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        # Letters already used
        print("You have", lives, "lives left. You have used these letters: ", " ".join(used_letters))

        # What current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        # Getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 # Subtracts one life if wrong
                print("Letter is not in word.")
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        else:
            print("Please enter a valid character.")

    if lives == 0:
        print("You died, the word was", word)
    else:
        print("You won! Congratulations! The word was", word)

hangman()