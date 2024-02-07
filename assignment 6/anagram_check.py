
def is_anagram(str1, str2):
    # Remove spaces and convert to lower case for comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if is_anagram(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams.")

if __name__ == "__main__":
    main()
