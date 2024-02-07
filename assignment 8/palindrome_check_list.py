
def main():
    strings_list = ["radar", "hello", "level", "world", "madam"]
    # Lambda function to check if a string is a palindrome
    is_palindrome = lambda s: s == s[::-1]
    palindromes = list(filter(is_palindrome, strings_list))
    print("Palindromes in the list:", palindromes)

if __name__ == "__main__":
    main()
