# Ask for user input
user_input = input("Enter something to write to the file: ")

# Write the input to output.txt
with open("C:\\Users\\91789\\Desktop\\Importent Folder\\Assignment4\\Task 1\\output.txt", "w") as file:
    file.write(user_input)

# Read and display the final content of the file
with open("C:\\Users\\91789\\Desktop\\Importent Folder\\Assignment4\\Task 1\\output.txt", "r") as file:
    content = file.read()

print("\nFinal content of output.txt:")
print(content)
