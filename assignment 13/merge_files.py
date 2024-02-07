
def merge_and_read_files(file1, file2, output_file):
    # Merge two files
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as outfile:
        outfile.write(f1.read())
        outfile.write("\n")
        outfile.write(f2.read())

    # Read and print the combined file
    with open(output_file, 'r') as file:
        content = file.read()
        print(content)

# Example usage
if __name__ == "__main__":
    file1 = "file1.txt"  # Replace with actual file path
    file2 = "file2.txt"  # Replace with actual file path
    output_file = "merged_file.txt"
    merge_and_read_files(file1, file2, output_file)
