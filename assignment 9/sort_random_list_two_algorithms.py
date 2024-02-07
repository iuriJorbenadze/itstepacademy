
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def generate_and_sort_list():
    # Generate a list of 100 random elements
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Sort the list in ascending order using bubble sort
    sorted_ascending = bubble_sort(random_list.copy())

    # Sort the list in descending order using insertion sort
    sorted_descending = insertion_sort(random_list.copy())
    sorted_descending.reverse()

    return sorted_ascending, sorted_descending

def main():
    ascending, descending = generate_and_sort_list()
    print("Sorted in ascending order (Bubble Sort):", ascending)
    print("Sorted in descending order (Insertion Sort):", descending)

if __name__ == "__main__":
    main()
