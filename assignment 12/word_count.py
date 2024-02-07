
def word_count(sentence):
    # Convert the sentence to lowercase to ensure case-insensitive counting
    sentence = sentence.lower()
    # Split the sentence into words
    words = sentence.split()
    # Create a dictionary to store the count of each word
    word_dict = {}
    for word in words:
        # Increment the count for each word
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    counts = word_count(sentence)
    print(counts)
