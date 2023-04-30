"""
W10 - Prove
Emilio Sosa

Complted all requirements for requirements.


"""

from os import remove


exit = False
cart = list()
prices = list()
quantities = list()
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
        # Add product in the cart and save it
        item = str(input("What item would you like to add? "))

        # Creativity Part. I decided to incliudedn the qty of the products
        quantity = int(input("How many would you like to add? "))
        quantities.append(quantity)
        if quantity > 1:
            item = item + "s"

        cart.append(item)
        # Price of the product
        product_price = float(input(f"What is the price of '{item}'? "))

        # Get the total prices of the products
        product_price = product_price * quantity
        prices.append(product_price)
       
        #Confirmation
        print(f"'{item}' has been added to your cart.")
    elif choice == 2:
        # Feature to View the cart
        print("Your cart contains: ")
        
        #Use a loop to provide the items in the cart
        print("Name\t\tQuantity\tPrice")
        for i in range(len(cart)):
            print(f"{i + 1}. {cart[i]}\t{quantities[i]}\t\t${round(prices[i], 2)}")
    elif choice == 3:
        # REMOVE ITEM
        # Get the number of the prodoct to delete and go one number down so it matches the index.
        remove_product = int(input("Which item would you like to remove? "))
        remove_product = remove_product - 1

        # Use pop function to rmeove
        cart.pop(remove_product)
        prices.pop(remove_product)
        quantities.pop(remove_product)

        #Confirmation
        print("Item removed sucesfully")
    elif choice == 4:
        # Calculate total
        total = 0
        for price in prices:
            total += price
        print(f"The total price of the items in the shopping cart is ${round(total, 2)}")
    elif choice == 5:
        #Exit
        exit = True
        