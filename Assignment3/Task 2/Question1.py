# 1. Asks the user for a number as input.

import math
number = float(input("Enter a number: "))
sqrt_value = math.sqrt(number) if number >= 0 else "Undefined (cannot take square root of a negative number)"
log_value = math.log(number) if number > 0 else "Undefined (logarithm of non-positive numbers is not defined)"
sine_value = math.sin(number)
print(f"Square root: {sqrt_value}")
print(f"Natural logarithm: {log_value}")
print(f"Sine (radians): {sine_value}")
