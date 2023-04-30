"""
W06 - Team Activity

CSEPC-110 - Group 3

GPA Converter 

Instructor Travis Christiansen

"""

## Ask for the percentage grade and save it in variable

percentage_grade = float(input(f"What is your Grade? "))
letter = ""

## Condition to get the grade
if percentage_grade >= 90:
    letter = "A"
elif percentage_grade >= 80:
    letter = "B"
elif percentage_grade >= 70:
    letter = "C"
elif percentage_grade >= 60:
    letter = "D"
elif percentage_grade < 60:
    letter = "F"
else:
    print(f"You wrote an valid number. Please try again. ")
 

## Determinates the Symbol of the Grade
last_number_grade = percentage_grade % 10
sign= ""

if last_number_grade >= 7:
    # When a grade is higher than *7 will show the + except F or A
    if letter == "A" or letter == "F":
        sign = ""
    else:
        sign = "+"
elif last_number_grade < 3:
    # When a grade is less than *3 will show the - except F
    if letter == "F" or percentage_grade == 100:
        sign = ""
    else:
        sign = "-"
else:
    # Otherwise any symbol
    sign = ""

#Print the results and let the user know if the approved or not.
print(f"Your grade is {letter}{sign}")
if percentage_grade >= 70:
    print("\nCongratulations you approved!")
else:
    print("\nYou failed. Please do better next time. ")