
def calculator(num1, num2, operator):
    # Define a dictionary with mathematical operations
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Error: Division by zero'
    }

    # Perform the operation
    if operator in operations:
        return operations[operator](num1, num2)
    else:
        return "Error: Invalid operator"


if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter a mathematical operator (+, -, *, /): ")
    result = calculator(num1, num2, operator)
    print("Result:", result)
