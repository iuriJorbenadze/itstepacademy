
def create_and_read_file(filename):
    # Create a text file and write 1000 lines to it
    with open(filename, 'w') as file:
        for i in range(1, 1001):
            file.write(f"Line {i}: This is a sample text.\n")

    # Read the file and count the number of lines
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1

    return line_count

# Example usage
if __name__ == "__main__":
    filename = "sample_text_file.txt"
    line_count = create_and_read_file(filename)
    print("Number of lines in the file:", line_count)
