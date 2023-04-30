
# Welcome Message

from audioop import cross
import math


print(f"Welcome to the velocity calculator. Please enter the following: \n")

# Store the datda
mass = float(input(f"Mass (in kg): "))
gravity = float(input(f"Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time_in_seconds = int(input(f"Time (in seconds): "))
fluid_density = float(input(f"Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_section = float(input(f"Cross sectional area (in m^2): "))
drag_constant = float(input(f"Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# Formula Hint to calculate "c = (1 / 2) * p * A * C"
c = (1 / 2) * fluid_density * cross_section * drag_constant

# Formula Hint "v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))"
velocity_at_t = math.sqrt((mass * gravity) / c ) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass ) * time_in_seconds))

print(f"\nThe inner value of c is: {round(c,3)}")
print(f"The velocity after {time_in_seconds} seconds is: {round(velocity_at_t, 3)}")

# Stretch Challenge 3

v_terminal = math.sqrt((mass*gravity)/c)

print(f"\nThe terminal velocity is: {round(v_terminal,3)}")