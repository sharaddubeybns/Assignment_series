# Dictionary with new student data
student_marks = {
    "harsh": 88,
    "Sneha": 93,
    "anil": 76,
    "kiya": 81
}

# Asking the user for input
name = input("Enter the name of the student: ")

# Displaying marks if student is found
if name in student_marks:
    print(f"{name} scored {student_marks[name]} marks.")
else:
    print(f"No record found for {name}.")
