
def sum_of_digits(n):
    # Base case: when the number becomes 0
    if n == 0:
        return 0
    # Recursive case: add the last digit and call the function with the remaining number
    return n % 10 + sum_of_digits(n // 10)

def main():
    number = int(input("Enter a number: "))
    total = sum_of_digits(number)
    print(f"Sum of the digits of {number} is:", total)

if __name__ == "__main__":
    main()
