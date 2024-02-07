
from functools import reduce

def main():
    numbers_list = [-5, 3, -1, 9, -6, 7, 0, -4, 8]
    # Lambda function to filter and accumulate only positive numbers
    positive_sum = reduce(lambda acc, num: acc + [num] if num > 0 else acc, numbers_list, [])
    print("Positive numbers:", positive_sum)

if __name__ == "__main__":
    main()
