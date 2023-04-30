'''
Author: Emilio E. Sosa
File name: w03_prove_milestone.py

Assigment: CSPC 110 W03 - Milestone
Instructor: Brother Travis Christiansen

'''

#Save the data
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of a adult's meal? "))
#Included for the Week 04
drink_price = float(input("What is the price of a drink? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

# Included for the week 04
drink_qty = int(input("How many drinks did will you purhcase? "))
tax_rate = float(input("What is the sales tax rate? "))
tip_rate = float(input("Percentaje of the tip (type 0 if you don't want to): "))

#Determinates, rounds and prints the subtotal
sales_subtotal = round((children * child_meal_price) + (adults * adult_meal_price) + (drink_price * drink_qty), 2)

print(f"\nSubtotal: ${sales_subtotal}")

#Included in the week 04 - Tip
tip = (sales_subtotal * tip_rate) / 100

print(f"Tip ({tip_rate}%): ${tip}")

#Calculates the sales tax
sales_tax = round(((sales_subtotal + tip)* tax_rate) / 100, 2)

print(f"Sales Tax: ${sales_tax}")

#Total
total = sales_tax + sales_subtotal + tip
print(f"Total: ${round(total,2)}")

#Payment
payment_amount = float(input("\nWhat is the payment amount: "))

#Conditional in case the user an amount lower than the total
if payment_amount < total:
    debt = round(total - payment_amount,2)
    print(f"You owe: ${debt}")
    print(f"Don't forget to do your payment")
else:
    change = round(payment_amount - total, 2)
    print(f'Change: ${change}')
    print(f"Thanks for your payment, please come back!")