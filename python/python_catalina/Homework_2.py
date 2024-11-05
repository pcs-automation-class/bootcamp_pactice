# Calculator Program

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

# Display the menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Loop to allow multiple calculations
while True:
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))

        # Ask if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            print("Goodbye!")
            break
    else:
        print("Invalid input. Please select a valid option.")

