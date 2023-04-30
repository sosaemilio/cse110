"""
W09 - Milestone
Emilio Sosa

Complted all requirements for milestone.
"""

exit = False
cart = list()
print("Welcome to the Shopping Cart Program!")

while (exit == False):
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    choice = int(input("Please enter an action: "))
    if choice == 1:
       item = str(input("What item would you like to add? "))
       cart.append(item)
       print(f"'{item}' has been added to your cart.")
    elif choice == 2:
        print("Your cart contains: ")
        for item in cart:
            print(item)
    elif choice == 5:
        exit = True
        