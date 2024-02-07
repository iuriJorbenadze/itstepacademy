
mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9, 12, 34, 49]

def sum_specific_elements(lst):
    # Adding the 3rd, 9th, and 14th elements of the list
    # Indices in Python are 0-based, so we subtract 1 from each position
    return lst[2] + lst[8] + lst[13]

def main():
    result = sum_specific_elements(mylist)
    print("Sum of 3rd, 9th, and 14th elements:", result)

if __name__ == "__main__":
    main()
