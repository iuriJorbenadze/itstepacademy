
import random

# Function to generate a list of 100 random numbers
def generate_random_list():
    return [random.randint(1, 1000) for _ in range(100)]

# Linear search function
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary search function
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Function to sort the list using insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    # Generate and sort the list
    random_list = generate_random_list()
    sorted_list = insertion_sort(random_list.copy())

    # Perform linear and binary searches
    search_element = random.choice(random_list)
    linear_result = linear_search(random_list, search_element)
    binary_result = binary_search(sorted_list, search_element)

    print(f"Element to search: {search_element}")
    print(f"Linear Search Result: {linear_result}")
    print(f"Binary Search Result: {binary_result}")

if __name__ == "__main__":
    main()
