
def count_character_in_string(string, character):
    # Count the number of times the character appears in the string
    return string.count(character)

def main():
    string = input("Enter a string: ")
    character = input("Enter a character: ")
    count = count_character_in_string(string, character)
    print(f"The character '{character}' appears {count} times in the string.")

if __name__ == "__main__":
    main()
