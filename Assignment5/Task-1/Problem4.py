# Dictionary of student marks
student_marks = {
    "Ravi": 38,
    "Sneha": 53,
    "Amit": 36,
    "Priya": 41
}

# Ask the user to input a student's name
name = input("Enter the name of the student: ")

# Check and display result
if name in student_marks:
    print(f"{name} scored {student_marks[name]} marks.")
else:
    print(f"Sorry, no records found for '{name}'. Please check the name and try again.")