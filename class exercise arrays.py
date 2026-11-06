# Name: Md Tahseenur Rahman
# Course: COSC 1100 - Intro to Programming
# class Excercise - Midterm Grade Calculator

# Helper function to get valid input
def get_valid_mark(prompt, max_mark):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= max_mark:
                return val
            print(f"Must be between 0 and {max_mark}.")
        except ValueError:
            print("Enter a valid number.")

# Get Pre-Class marks
pc_marks = []
for i in range(1, 4):
    pc_marks.append(get_valid_mark(f"Pre-Class {i} mark (out of 10): ", 10))

# Get Class Exercise marks
ce_marks = []
for i in range(1, 4):
    ce_marks.append(get_valid_mark(f"Class Exercise {i} mark (out of 10): ", 10))

# Get Test mark
test_mark = get_valid_mark("Test 1 mark (out of 50): ", 50)

# Calculations
pc_pct = (sum(pc_marks) / (len(pc_marks) * 10)) * 100
ce_pct = (sum(ce_marks) / (len(ce_marks) * 10)) * 100
test_pct = (test_mark / 50) * 100

final_grade = (pc_pct * 0.15) + (ce_pct * 0.25) + (test_pct * 0.60)

# Display results
print(f"\nPre-Class: {pc_pct:.2f}%")
print(f"Class Exercises: {ce_pct:.2f}%")
print(f"Test 1: {test_pct:.2f}%")
print(f"Final Midterm Grade: {final_grade:.2f}%")