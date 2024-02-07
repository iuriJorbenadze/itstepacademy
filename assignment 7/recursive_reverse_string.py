
def reverse_string(s):
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest of the string and add the first character at the end
    return reverse_string(s[1:]) + s[0]

def main():
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()
