loan_size = int(input(f"How large is the loan? "))
credit_history = int(input(f"How good is your credit history? "))
income = int(input(f"How high is your income? "))
down_payment = int(input(f"How large is your down payment? "))

approved = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        approved = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            approved = True
        else:
            approved = False
    else:
        approved = False
elif loan_size <= 5:
    if credit_history < 4:
        approved = False
    else: 
        if income >= 7 or down_payment >= 7:
            approved = True
        elif income <= 7 and down_payment <= 7:
            approved = False
        else:
            approved = False
else:
    print(f"You didn't choose a right number...")

if approved:
    print("YES")
else:
    print("NO")