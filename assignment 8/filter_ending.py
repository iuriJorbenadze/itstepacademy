
def filter_by_ending(strings_list, ending):
    try:
        # Lambda function to check if a string ends with the given ending
        filter_func = lambda s: s.endswith(ending)
        filtered_list = list(filter(filter_func, strings_list))
        return filtered_list
    except TypeError:
        return "Error: Invalid input types."

def main():
    try:
        strings_list = ['hello', 'world', 'coding', 'nod']
        ending = 'ing'
        result = filter_by_ending(strings_list, ending)
        print("Strings ending with '{}':".format(ending), result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
