
from functools import reduce

def multiply_list_elements(numbers_list):
    try:
        # Lambda function to multiply elements
        result = reduce(lambda x, y: x * y, numbers_list)
        return result
    except TypeError:
        return "Error: List must contain only numbers."

def main():
    try:
        numbers_list = [1, 2, 3, 4, 5]
        result = multiply_list_elements(numbers_list)
        print("Result of multiplying elements:", result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
