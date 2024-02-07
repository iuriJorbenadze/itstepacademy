
def create_file_with_numbers(filename):
    # Define the line numbers and their respective texts
    lines_with_numbers = {
        2: "Two",
        8: "Eight",
        10: "Ten",
        13: "Thirteen",
        17: "Seventeen"
    }

    # Create a text file and write numbers at specified lines
    with open(filename, 'w') as file:
        for i in range(1, 18):
            if i in lines_with_numbers:
                file.write(lines_with_numbers[i] + "\n")
            else:
                file.write("\n")

# Example usage
if __name__ == "__main__":
    filename = "numbers_file.txt"
    create_file_with_numbers(filename)
