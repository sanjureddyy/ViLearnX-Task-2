# Simple Calculator

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to run the calculator
def main():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display operation options to the user
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt the user to choose an operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the selected operation and display the result
    if operation == '+':
        print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
    elif operation == '-':
        print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
    elif operation == '*':
        print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
    elif operation == '/':
        print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
    else:
        print("Invalid operation! Please choose one of the specified options.")

# Run the calculator program
if __name__ == "__main__":
    main()
