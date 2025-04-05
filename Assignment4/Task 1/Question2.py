# 2. Prints the content of sample.txt line by line
try:
    with open("C:\\Users\\91789\\Desktop\\Importent Folder\\Assignment4\\Task 1\\sample.txt", "r") as file:
        print("File content (line by line):\n")
        for line in file:
            print(line.strip())  # .strip() removes any extra newline characters
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
