
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

if __name__ == "__main__":
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operator = input("Enter the mathematical operator (+, -, *, /): ")

        result = calculate(first_number, second_number, operator)
        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
