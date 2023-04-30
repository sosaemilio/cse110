"""
Emilio Sosa
W13 - PROVE
Brother Travis Christiansen

BYUI CS CSC110

"""


temperature = float(input("Enter the temperature: "))

# Core requiremnts 2 - Write a function to convert from Celsius to Fahrenheit. The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
def celcius_to_farhenheit(temperature_celsius):
    temperature_farehnheit = (temperature_celsius * 9/5) + 32
    return temperature_farehnheit

# Core requirements 3 - Allow the user to enter the temperature in Celsius of Fahrenheit. If they provide it in Celsius, first convert it to Fahrenheit before using the formula above.
temperature_type = input("Enter 'C' for Celsius or'F' for Fahrenheit: ")
if temperature_type.lower() == "c":
    temperature = celcius_to_farhenheit(temperature)

# Core requirements 1 - Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def wind_chill(temperature_farehnheit, wind_speed):
    # Wind_chil = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
    wind_chill = 35.74 + (0.6215 * temperature_farehnheit) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temperature_farehnheit * (wind_speed ** 0.16))
    
    #Core requirement 5 - Display the wind chill value to 2 decimals of precision.
    print(f"At temperature {temperature_farehnheit}F, and wind speed {wind_speed} mph, the windchill is: {round(wind_chill, 2)}F")
    

# Core requiments 4 -Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and calculate and display the wind chill for each of these wind speeds.
wind_speed = 5
while wind_speed <= 60:
    wind_chill(temperature, wind_speed)
    wind_speed += 5
