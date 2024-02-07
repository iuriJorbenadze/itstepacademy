
def check_even_odd(number):
    return 'even' if number % 2 == 0 else 'odd'

try:
    num = int(input("Enter a number: "))
    print(check_even_odd(num))
except ValueError:
    print("Please enter a valid integer.")
