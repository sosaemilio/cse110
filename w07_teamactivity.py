import random
play_again = "yes"

while play_again.lower() == "yes":
    random_number = random.randint(1, 100)
    user_numer = int(input(f"What is your guess? "))
    attempts = 1

    while user_numer != random_number:
        if user_numer > random_number:
            print("Too high!")
        else:
            print("Too low!")
        user_numer = int(input(f"What is your guess? "))
        attempts += 1

    if user_numer == random_number:
        print("You got it!")
        print(f"It took you {attempts} attempts.")
        play_again = str(input("Would you like to play again? "))