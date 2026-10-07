#  Md Tahseenur Rahman, COSC 1100, User Input Validation


# 1. Student Name Validation
name = input("Enter student name: ")
if name.strip() != "":
    print("Name saved successfully!\n")
else:
    print("Error: Name cannot be blank.\n")

# 2. Student ID Validation (Exactly 9 digits)
student_id = input("Enter 9-digit Student ID: ")
if student_id.isnumeric() and len(student_id) == 9:
    print("Student ID saved successfully!\n")
else:
    print("Error: Student ID must be exactly 9 numeric digits.\n")

# 3. Exercise Mark Validation (0 to 100 inclusive)
mark_input = input("Enter exercise mark (0 to 100): ")
if mark_input.isnumeric():
    mark = int(mark_input)
    if 0 <= mark <= 100:
        print("Exercise mark saved successfully!\n")
    else:
        print("Error: Mark must be between 0 and 100.\n")
else:
    print("Error: Mark must be a whole number.\n")

# 4. Attendance Mode Validation
mode = input("Enter attendance mode (Online, In person, Hybrid): ")
if mode in ["Online", "In person", "Hybrid"]:
    print("Attendance mode saved successfully!\n")
else:
    print("Error: Mode must be 'Online', 'In person', or 'Hybrid'.\n")
