from re import T


favorite_letter = str(input("What is your favorite letter? "))
word = "commitment"
for letter in word:
    if letter == favorite_letter:
        letter = "_"
        print(letter.upper(), end="")
    else:
        print(letter, end="")