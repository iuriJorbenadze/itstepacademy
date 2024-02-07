
def main():
    list_numbers = [1, 2, 3, 4, 5, 6, 7]
    # Lambda function to filter odd elements
    filter_odd = lambda numbers: [num for num in numbers if num % 2 != 0]
    odd_numbers = filter_odd(list_numbers)
    print("Odd elements:", odd_numbers)

if __name__ == "__main__":
    main()
