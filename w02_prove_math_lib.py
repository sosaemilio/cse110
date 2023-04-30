'''
Author: Emilio E. Sosa
File name: w02_prove_math_lib.py

Assigment: CSPC 110 W02 - Prove Activity
Instructor: Brother Travis Christiansen

NOTES:

I included a sentence at the end of the "print" and also, included an if/else statement in case the body part start with a vowel or a consonant. 
'''

print(f'Please enter the following: \n')


# Save all the data
adjective = str(input(f'Adjective: '))
animal = str(input(f'Animal: '))
first_verb = str(input(f'Verb: '))
first_exclamation = str(input(f'Exclamation: '))
second_verb = str(input(f'Verb: '))
third_verb = str(input(f'Verb: '))
second_exclamation = str(input(f'Exclamation: '))
emotion = str(input(f'Emotion: '))
body_part = str(input(f'Body Part: '))

# Determinates the "a" or "an" before the body_part string
if body_part[0] == 'a' or body_part[0] == 'e' or body_part[0] == 'i' or body_part[0] == 'o' or body_part[0] == 'u':
    body_part = 'an ' + body_part
else:
    body_part = 'a ' + body_part


# Print First Statement
print('\nYour story is: \n')

# Print the story. I decided to separated them so I will look better
print(f'The other day, I was really in trouble. It all started when I saw a very')
print(f'{adjective.lower()} {animal.lower()} {first_verb.lower()} down the hallway. "{first_exclamation.capitalize()}!" I yelled. But all') 
print(f'I could think to do was to {second_verb.lower()} over and over. Miraculously,') 
print(f'that caused it to stop, but not before it tried to {third_verb.lower()}')

#Included an aditional setence and the body_part variable.
print(f'right in front of my family. They yelled "{second_exclamation.capitalize()}!", because they were so {emotion}')
print(f'I was going to break {body_part.lower()}.')