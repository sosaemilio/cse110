"""
Emilio Sosa
CSEPC-110
Week 8 - Final Project

Brother Travis Christiansen

"""

print(f"Welcome to the word guessing game! \n")

# Variables
secret_word = "secret"
number = 0
words = ""
guessed_word = ""


# Conditions while the secret word is not guessed

while words != secret_word:
    print(f"Your hint is: ", end="")
    position = 0
    saved_value = ""
    for letter in secret_word:
        if letter == guessed_word[position:position+1]:
            saved_value += letter.upper()
        elif letter in guessed_word:
            saved_value += letter.lower()
        else:
            saved_value += "_ "
        position += 1
    print(saved_value)

    guessed_word = input("\nWhat is your guess word: ")
    # Number of tries
    number += 1

    #If words tried equal to the secret word the condition will be met
    if guessed_word.lower() == secret_word:
        words = guessed_word.lower()
        print("Congratulations! You guessed it!")
        print(f"It took you {number} tries to guess the secret word.")
    """else:
        print("Your guess was not correct.")"""