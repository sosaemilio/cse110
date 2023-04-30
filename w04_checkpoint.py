#Get the data and store it in a variable
farenheint = int(input("What is the temperature in Fahrenheit? "))

# Conversion to Celcius
celcius = (farenheint - 32) * 5/9

# Print the temperature
print(f"The temperature in Celsius is {round(celcius,1)} degrees.")