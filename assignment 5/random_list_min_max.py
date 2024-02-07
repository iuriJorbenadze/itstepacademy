
import random

def create_random_list(size=10, min_val=0, max_val=100):
    # Create a list of random numbers within the specified range
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    random_list = create_random_list()
    print("Random List:", random_list)
    print("Minimum Value:", min(random_list))
    print("Maximum Value:", max(random_list))

if __name__ == "__main__":
    main()
