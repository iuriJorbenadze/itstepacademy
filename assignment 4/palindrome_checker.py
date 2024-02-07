
def is_palindrome(text):
    # Remove spaces and convert to lower case for comparison
    text = text.replace(" ", "").lower()
    # Check if the text is equal to its reverse
    return text == text[::-1]

def main():
    user_input = input("Enter text to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("The text entered is a palindrome")
    else:
        print("The text entered is not a palindrome")

if __name__ == "__main__":
    main()
