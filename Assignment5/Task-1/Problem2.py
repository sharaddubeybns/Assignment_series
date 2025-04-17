# Dictionary of student marks
student_marks = {
    "Sharad": 55,
    "Shubham": 40,
    "Shreesh": 58,
    "Simran": 29
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Check if the name exists in the dictionary
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"{student_name} not found in the record.")