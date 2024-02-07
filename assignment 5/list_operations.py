
def main():
    my_llist = [43, '22', 12, 66, 210, ["hi"]]

    # a. Print the index of 210
    index_210 = my_llist.index(210)
    print("Index of 210:", index_210)

    # b. Add "hello" to the last element (which is a list)
    my_llist[-1].append("hello")

    # c. Delete the element at the second index and print the list
    del my_llist[2]
    print("List after deleting the element at index 2:", my_llist)

    # d. Create a new list my_llist_2 and clear my_llist_2
    my_llist_2 = my_llist.copy()
    my_llist_2.clear()
    print("my_llist:", my_llist)
    print("my_llist_2:", my_llist_2)

if __name__ == "__main__":
    main()
