# 1. Opens and reads a text file named sample.txt
try:
    with open("C:\\Users\\91789\\Desktop\\Importent Folder\\Assignment4\\Task 1\\sample.txt", "r") as file:
        content = file.read()
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

# Explanation:
# open("sample.txt", "r") → Opens the file in read mode.
# with → Ensures the file is automatically closed after reading.
# file.read() → Reads the entire content of the file as a string.
# try/except → Handles the case where the file does not exist (avoids crashing).