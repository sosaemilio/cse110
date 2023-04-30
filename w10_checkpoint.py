# Universal Variables
quit = False
shopping_list = []

# First Message
print("Please enter the items of the shopping list (type: quit to finish): ")

# Start appeding new items in the shopping list until it quits
while quit == False:
    item = str(input("Item: "))

    if item.lower() == "quit":
        quit = True
    else:
        shopping_list.append(item)

# Print the Shopping list after the last operation is completed
print("\nThe shopping list is: ")
for item in shopping_list:
    print(item)

# Print the indexes
print("\nThe shopping list with indexes is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

# Change a product
index = int(input("\nWhich item would you like to change? "))
new_item = str(input("What is the new item? "))

shopping_list[index] = new_item

# Print the indexes again
print("\n The shopping list with indexes is: ")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")