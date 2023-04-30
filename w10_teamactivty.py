""""
W10 -  Team Activity

"""

names = []
balances = []
total = 0

print("Enter the names and balances of bank accounts (type: quit when done)")

quit = False
index = 0

while quit == False:
    name = str(input("What is the name of this account? "))
    if name.lower() == "quit":
        quit = True
    else:
        names.append(name)
        balance = float(input("What is the balance? "))
        total += balance
        balances.append(balance)

print("\nAccount Information: ")
for i in range(len(names)):
    print(f"{names[i]} - ${round(balances[i], 2)}")

print(f"\nTotal: ${round(total, 2)}")
average = total / len(balances)
print(f"Average: ${round(average, 2)}")