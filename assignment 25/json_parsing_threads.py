
import json
import threading

# Function to parse and print JSON data from a given file
def parse_and_print_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        print(f"File: {file_path} contains: {data}\n")

def main():
    # Example JSON data
    json_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Paris"},
        {"name": "Charlie", "age": 35, "city": "London"}
    ]

    # Assuming JSON files are saved and paths are known
    json_file_paths = ['json_file_1.json', 'json_file_2.json', 'json_file_3.json']

    # Creating and starting a thread for each JSON file
    threads = [threading.Thread(target=parse_and_print_json, args=(file_path,)) for file_path in json_file_paths]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
