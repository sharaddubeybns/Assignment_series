# Ask for user input
user_input = input("Enter something to append to the file: ")

# Append the input to output.txt
try:
    with open("C:\\Users\\91789\\Desktop\\Importent Folder\\Assignment4\\Task 1\\output.txt", "a") as file:
        file.write(user_input + "\n")
    print("Input appended to output.txt.")
except Exception as e:
    print(f"Error appending to file: {e}")

# Read and display the final content of the file
try:
    with open("output.txt", "r") as file:
        content = file.read()
    print("\nFinal content of output.txt:")
    print(content)
except FileNotFoundError:
    print("File not found. Cannot read from output.txt.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


