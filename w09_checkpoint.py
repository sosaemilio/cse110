end = False
names = list()

# Loop to get the name
while(end == False):
    name = str(input("Type the name of a friend: "))
    if name == "end":
        end = True
    else:
        names.append(name)

## Print the list of names
print("\nYour friends are: ")
for name in names:
    
    print(name)
