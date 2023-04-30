import math

# Calculates the area of a square
square_length = float(input('What is the length of a side of the square in Centimeter? '))
area_square = square_length ** 2

print(f'The area of a square is: {area_square} cms and {area_square/100} meters')

# Calculates the area of the rectangule 
rectangule_lenght = float(input('What is the length of rectangle in Centimeter? '))
rectangule_width = float(input('What is the width of the rectangle in Centimeter? '))
rectangule_area = rectangule_width * rectangule_lenght

print(f'The area of the rectangle is: {rectangule_area} cms and {rectangule_area/100} meters ')

# Calculates the area of a Circle in 
circle_radius = float(input('What is the radius of the circle in Centimeter? '))
circle_area = math.pi * (circle_radius ** 2)

print(f'The area of the circle is: {circle_area} cms and {circle_area/100} meters')


# Stretch Challenges 1 is completed and number 3 as well.
# Stretch Challenges 3

value = float(input('What is your unique value in centimer? '))

# Calculations of the unique value
area_square = value ** 2
circle_area = (value ** 2) * math.pi
volume_cube = value ** 3
volume_sphere = (4/3) * math.pi * (value**3)

# Print value of the unique value
print(f'Are of Square is: {area_square} cm and {area_square / 1000} mts')
print(f'Area of a Circle is: {circle_area} cm and {circle_area / 1000} mts')
print(f'Volume of a Cube is: {volume_cube} cm and {volume_cube / 1000} mts')
print(f'Area of a Sphere is: {volume_sphere} cm and {volume_sphere / 1000} mts')