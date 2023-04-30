height = int(input(f"Type the height of the pyramid: "))
blocks = "#"


if height <= 0:
    print(f"The value you type is lower than 0")
else:
    count = 0
    while (count < height):
        count = count + 1
        print (blocks)
        blocks = "#" + blocks


