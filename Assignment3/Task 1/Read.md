#1 
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120

# 2
# Deep Dive: Recursive Version
# Each call waits for the next:
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 = 120

#  Iterative Version
Example for n = 5:
result = 1
→ 1 * 2 = 2
→ 2 * 3 = 6
→ 6 * 4 = 24
→ 24 * 5 = 120


#3
# Example when n = 5:

# result = 1
# i = 2 → result = 1 * 2 = 2  
# i = 3 → result = 2 * 3 = 6  
# i = 4 → result = 6 * 4 = 24  
# i = 5 → result = 24 * 5 = 120  

# Optional Enhancements:
# Add input() to get user input.

# Add error handling for non-integer values.

# Calculate factorials for a list of numbers.