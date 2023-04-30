"""
Emilio Sosa
CSEPC-110
Week 7 Milestone

"""

print(f"Welcome to the word guessing game! \n")

# Variables
secret_word = "secret"
number = 0
words = ""

# Conditions while the secret word is not guessed

while words != secret_word:
    words = input("Please type the secret word: ")
    # Number of tries
    number += 1
    #If words tried equal to the secret word the condition will be met
    if words.lower() == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {number} tries to guess the secret word.")
    else:
        print("Your guess was not correct.")