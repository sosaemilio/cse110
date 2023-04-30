"""
W06 - Team Activity

"""

age_first_rider = int(input(f"What is the age of the first rider? "))
height_frist_rider =  float(input(f"What is the height of the first rider? "))
is_there_a_second_rider = str(input(f"Is there a second rider (yes/no)? "))

# 2 Strech Challenge - Golden Passport
if age_first_rider > 12 and age_first_rider < 17:
    golden_passport = str(input(f"Do you have a golden passport? "))
    if golden_passport.lower() == "yes":
        age_first_rider = 19


## Age Conditions - 
if is_there_a_second_rider.lower() == "yes":
    age_second_rider = int(input(f"\nWhat is the age of the second rider? "))
    height_second_rider = float(input(f"What is the height of the second rider? "))

    # 2 Strech Challenge - Golden Passport
    if age_second_rider > 12 and age_second_rider < 17:
        golden_passport = str(input(f"Do you have a golden passport? "))
        if golden_passport.lower() == "yes":
            age_second_rider = 19
    #First rider must be taller than 46 and older than 36
    if height_frist_rider >= 36 and age_first_rider >= 18:
        # Second river must be taller than 36 inches
        if height_second_rider >= 36:
            print(f"Welcome to the ride. Please be safe and have fun!")
        else:
            print(f"Sorry, you may not ride")
    # If first rider is older than 12 but younger than 18        
    elif age_first_rider >= 12 and age_first_rider <=18:
        if (age_first_rider > 16 or age_second_rider > 16) and (age_first_rider > 14 or age_second_rider > 14):
            print(f"Welcome to the ride. Please be safe and have fun!")   
        ## 1 Stretch Challenge 
        elif age_second_rider >= 12 and height_second_rider >= 46 and height_frist_rider >=46:
            print(f"Welcome to the ride. Please be safe and have fun!")
        else:
            print(f"Sorry, you may not ride")
    else:
        print("Sorry, you may not ride.")
elif is_there_a_second_rider.lower() == "no":
    #Single River
    if height_frist_rider < 36 or age_first_rider < 18:
        print("Sorry, you may not ride")
    else:
        print(f"Welcome to the ride. Please be safe and have fun!")
else:
    print(f"You wrote an incorrect value")