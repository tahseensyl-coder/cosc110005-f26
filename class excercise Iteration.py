"""
# Student Name : Md Tahseenur Rahman
# Course       : COSC 1100-05
# Assignment   : Class Exercise - Iteration
"""

# STEP 1: Initialize counters for each hot dog type
traditional_count = 0
veggie_count = 0
curry_count = 0

# STEP 2: Main loop to display menu repeatedly
while True:
    print("\n--- HOT DOG STAND MENU ---")
    print("1. Traditional Hot Dog")
    print("2. Veggie Dog")
    print("3. Curry Hot Dog")
    print("4. Tally and Exit")
    
    # Read menu selection from user
    choice = input("Select an option (1-4): ")

    # Handle Option 1: Traditional Hot Dog
    if choice == "1":
        quantity = int(input("Enter number of Traditional Hot Dogs sold: "))
        traditional_count += quantity
        print(f"Added {quantity} Traditional Hot Dog(s)!")

    # Handle Option 2: Veggie Dog
    elif choice == "2":
        quantity = int(input("Enter number of Veggie Dogs sold: "))
        veggie_count += quantity
        print(f"Added {quantity} Veggie Dog(s)!")

    # Handle Option 3: Curry Hot Dog
    elif choice == "3":
        quantity = int(input("Enter number of Curry Hot Dogs sold: "))
        curry_count += quantity
        print(f"Added {quantity} Curry Hot Dog(s)!")

    # Handle Option 4: Tally and Exit
    elif choice == "4":
        total_dogs = traditional_count + veggie_count + curry_count

        print("\n================ TALLY REPORT ================")
        
        # Calculate and display percentages if items were sold
        if total_dogs > 0:
            trad_pct = (traditional_count / total_dogs) * 100
            veg_pct = (veggie_count / total_dogs) * 100
            curry_pct = (curry_count / total_dogs) * 100

            print(f"Traditional Hot Dogs : {traditional_count} sold ({trad_pct:.2f}%)")
            print(f"Veggie Dogs          : {veggie_count} sold ({veg_pct:.2f}%)")
            print(f"Curry Hot Dogs       : {curry_count} sold ({curry_pct:.2f}%)")
            print("----------------------------------------------")
            print(f"Total Hot Dogs Sold  : {total_dogs}")
        else:
            print("No hot dogs were sold today!")
            
        print("==============================================")
        print("System closed. Goodbye John!")
        break  # Exit the loop and close system

    # Handle invalid menu choices
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")