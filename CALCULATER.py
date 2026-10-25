# Simple Calculator using Functions in Python

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b, handling division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def get_number(prompt):
    """Safely get a number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculator():
    """Main calculator function."""
    print("=== Simple Calculator ===")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    try:
        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Run the calculator
    calculator()
