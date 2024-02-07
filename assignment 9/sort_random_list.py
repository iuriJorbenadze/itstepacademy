
import random

def generate_and_sort_list():
    # Generate a list of 100 random elements
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # Sort the list in ascending order using sort()
    random_list.sort()

    # Sort the list in descending order using sorted()
    sorted_descending = sorted(random_list, reverse=True)

    return random_list, sorted_descending

def main():
    ascending, descending = generate_and_sort_list()
    print("Sorted in ascending order:", ascending)
    print("Sorted in descending order:", descending)

if __name__ == "__main__":
    main()
