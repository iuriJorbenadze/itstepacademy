
def combine_tuples(tuple1, tuple2):
    combined = set(tuple1) | set(tuple2)  # Union of sets to remove duplicates
    duplicated_values = [value for value in set(tuple1) & set(tuple2)]  # Intersection of sets for duplicates
    return tuple(combined), duplicated_values

def main():
    tuple1 = (1, 2, 3, 4, 5, 6)
    tuple2 = (4, 5, 5, 6, 6, 7)
    combined_tuple, duplicated_values = combine_tuples(tuple1, tuple2)
    print("Combined Tuple:", combined_tuple)
    print("Duplicated Values:", duplicated_values)

if __name__ == "__main__":
    main()
