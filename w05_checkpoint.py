"""
CSEPC-110  W05 - Checkpoint

DEVELOPED by Emilio Sosa
"""
## Inputs from the user
first_integer = int(input(f"What is the first number? "))
second_integer = int(input(f"What is the second number? "))


## Conditions
if first_integer > second_integer:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_integer == second_integer:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if first_integer < second_integer:
    print("The second number is greater")
else:
    print("The second number is not greater")


## Favorite animal part
my_favorite_animal = "dog"

animal = str(input("\nWhat is your favorite animal? "))

if animal.lower() == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")