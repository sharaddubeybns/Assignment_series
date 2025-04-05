# 1.Check if a Number is Even or Odd

def check_even_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Please enter a valid integer.")

check_even_odd()
