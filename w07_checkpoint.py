number = 0

while number <= 0:
    number = int(input("Please type a positive number: "))
    if number <= 0:
        print("Sorry, that is a negative number. Please try again. ")
    else:
        print("The number is:", number)

candy = "no"
while candy != "yes":
    candy = input("May I have a piece of candy? ")
