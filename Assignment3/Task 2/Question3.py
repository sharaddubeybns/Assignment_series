#3.Displays the calculated results.

number = input("Please enter a number: ")
try:
    number = float(number) 
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
    
