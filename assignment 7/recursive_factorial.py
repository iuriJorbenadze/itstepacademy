
def factorial(n):
    # Base case: factorial of 0 or 1
    if n in (0, 1):
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

def main():
    number = int(input("Enter a number: "))
    factorial_result = factorial(number)
    print(f"The factorial of {number} is:", factorial_result)

if __name__ == "__main__":
    main()
