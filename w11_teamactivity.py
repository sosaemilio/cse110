with open("hr_system.txt") as hr_system:
    for line in hr_system:
        # Split the line to make it easier to work with
        line = line.split(" ",)

        #Save values in variables
        name = str(line[0])
        ID = line[1]
        title = line [2]
        
        # They are paid biweekly
        monthly_salary = (float(line[3]) / 12) /  2

        # If engineer it will get +1000 each two week
        if title.lower() == "engineer":
            monthly_salary += 1000

        print(f"{name} (ID: {ID}), {title} - ${round(monthly_salary, 2)}")
