#1. Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")
