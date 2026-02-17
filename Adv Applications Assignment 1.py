# Program Name: Assignment1.py
# Course: IT3883/Section 01
# Student Name: Torre Walker
# Assignment Number: Lab 1
# Due Date: 01/24/2026
# Purpose: text buffer menu that allows for the user to store input, clear input and display the input
# Resources Used: Python class notes, Python documentation

# an empty input buffer
input_buffer = ""

# This loop keeps the program running until the user chooses to exit
while True:
    print("\n--- Text Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Gather the user's menu choice
    choice = input("Enter your choice (1-4): ")

    # Option 1: Append data to the buffer
    if choice == "1":
        user_text = input("Enter a string to append: ")
        input_buffer += user_text
        print("Text has been added to the buffer.")

    # Option 2: Clear the buffer
    elif choice == "2":
        input_buffer = ""
        print("The input buffer has been cleared.")

    # Option 3: Display the buffer contents
    elif choice == "3":
        if input_buffer == "":
            print("The input buffer is currently empty.")
        else:
            print("Current buffer contents:")
            print(input_buffer)

    # Option 4: Exit the program
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
