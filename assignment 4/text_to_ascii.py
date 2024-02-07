
def text_to_ascii(text):
    # Convert each character in the text to its ASCII value and store in a list
    ascii_values = [ord(char) for char in text]
    return ascii_values

def main():
    user_input = input("Enter text to convert to ASCII: ")
    ascii_sequence = text_to_ascii(user_input)
    print("ASCII sequence:", ascii_sequence)

if __name__ == "__main__":
    main()
