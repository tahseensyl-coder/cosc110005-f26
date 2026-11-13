# COSC 1100 Class Exercise: Arrays & Functions
# Student: Md Tahseenur Rahman
# This program calculates my midterm grade using functions, lists, and input validation.

# Function to get and validate user input so the program doesn't crash
def get_valid_mark(prompt, max_mark):
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= max_mark:
                return val
            print(f"Error: Mark must be between 0 and {max_mark}. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numbers only.")

# Function to calculate the percentage for any list of marks
def calculate_percentage(marks_list, max_per_item):
    total_earned = sum(marks_list)
    total_possible = len(marks_list) * max_per_item
    return (total_earned / total_possible) * 100

def main():
    print("=== Midterm Grade Calculator ===")
    
    # Get Pre-Class marks
    pc_marks = []
    for i in range(1, 4):
        mark = get_valid_mark(f"Pre-Class {i} mark (out of 10): ", 10)
        pc_marks.append(mark)
        
    # Get Class Exercise marks
    ce_marks = []
    for i in range(1, 4):
        mark = get_valid_mark(f"Class Exercise {i} mark (out of 10): ", 10)
        ce_marks.append(mark)
        
    # Get Test 1 mark
    test_mark = get_valid_mark("Test 1 mark (out of 50): ", 50)
    
    # Calculate category percentages using the function
    pc_pct = calculate_percentage(pc_marks, 10)
    ce_pct = calculate_percentage(ce_marks, 10)
    test_pct = (test_mark / 50) * 100
    
    # Final weighted midterm grade calculation
    final_grade = (pc_pct * 0.15) + (ce_pct * 0.25) + (test_pct * 0.60)
    
    # Print out the final results
    print("\n--------------------------------")
    print(f"Pre-Class Percentage:      {pc_pct:.2f}%")
    print(f"Class Exercises Percentage: {ce_pct:.2f}%")
    print(f"Test 1 Percentage:          {test_pct:.2f}%")
    print("--------------------------------")
    print(f"Final Midterm Grade:        {final_grade:.2f}%")
    print("--------------------------------")

if __name__ == "__main__":
    main()