"""
File: w02_team_activity_id_badge.py
Author: Emilio Sosa

Purpose: W02 Team Activity
"""
#Intro Message
print("Please enter the following information: \n")

#Store the values in the ID Badge
first_name = input("First name: ")
last_name = input("Last Name: ")
email_address = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID Number: ")
hair_color = input("What is your hair color: ")
eyes_color = input("What is your eye color: ")
starting_month = input("What month did you started?: ")
advanced_training = input("Did the employee complete the training? YES/NO: ")

#ID Badge print
print(f"\n The ID Card is: ")
print(f"----------------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number} \n")

print(f"{email_address.lower()}")
print(f"{phone_number} \n")

print(f"{"Hair: " + hair_color.capitalize():<20} Eyes: {eyes_color.capitalize()}")
print(f"{"Month: " + starting_month.capitalize():<20} Training: {advanced_training.capitalize()}")
print("----------------------------------------")