
# Task 2: Python program to sum positive numbers until 'sum' text is entered

def sum_positive_numbers():
    total_sum = 0
    while True:
        number = input("Enter a number (or 'sum' to finish): ")
        if number.lower() == 'sum':
            break
        try:
            number = float(number)
            if number > 0:
                total_sum += number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"Sum of positive numbers: {total_sum}")

# Example usage
# sum_positive_numbers()  # Uncomment this line to test the function
