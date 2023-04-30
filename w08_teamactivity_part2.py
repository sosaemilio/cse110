try_again = True

while(try_again):
    number = int(input("Enter a number: "))
    phrase = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

    for i, letter in enumerate(phrase):
        if i % number == False:
            print(letter.upper(), end="")
        else:
            print(letter, end="")

    # Condition to exit the loop
    try_again = input("\nTry again? (y/n) ")
    if try_again == "y":
        try_again = True
    elif try_again == "n":
        try_again = False
    else:
        print("Invalid input.")