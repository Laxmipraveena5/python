# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Start of the calculator program
while True:
    # Display menu for choices
    print("\nBasic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    # Take user choice
    choice = input("Enter choice (1/2/3/4/0): ")

    # Check if user wants to exit
    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        break

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        try:
            # Take input for two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the calculation based on the choice
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
    else:
        print("Invalid choice! Please select a valid operation (1, 2, 3, 4, or 0).")
