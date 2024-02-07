
def zip_lists(list1, list2):
    # Zip the two lists together
    return list(zip(list1, list2))

def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    zipped_list = zip_lists(list1, list2)
    print("Zipped List:", zipped_list)

if __name__ == "__main__":
    main()
