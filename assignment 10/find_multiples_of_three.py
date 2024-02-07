
def find_indices(arr, condition):
    # Use linear search and the lambda function to find indices
    return [i for i, x in enumerate(arr) if condition(x)]

def main():
    list_numbers = [1, 3, 4, 6, 9, 11, 12, 15, 18, 20]
    # Lambda function for multiples of three
    is_multiple_of_three = lambda x: x % 3 == 0
    indices = find_indices(list_numbers, is_multiple_of_three)
    print("Indices of multiples of three:", indices)

if __name__ == "__main__":
    main()
