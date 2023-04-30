
age = int(input('How old are you? '))
age += 1
print(f'Your age is {age}.')


eggs = int(input('\nHow many egg cartons do you have? '))
eggs *= 12
print(f'You have {eggs}.')

cookies = int(input(f'\nHow many cookies do you have? '))
people = int(input('How many people are there? '))

cookies_per_person = cookies / people 
print(f'Each person may have {cookies_per_person} cookies ')