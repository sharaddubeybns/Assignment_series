#2.Uses the math module to calculate the:

import math
number = float(input("Enter a number: "))
if number >= 0:
    sqrt_value = math.sqrt(number)
else:
    sqrt_value = "Undefined (cannot take square root of a negative number)"
if number > 0:
    log_value = math.log(number)
else:
    log_value = "Undefined (logarithm of non-positive numbers is not defined)"
sine_value = math.sin(number)

print("\nCalculated Results:")
print(f"Square root: {sqrt_value}")
print(f"Natural logarithm (ln): {log_value}")
print(f"Sine (radians): {sine_value}")
