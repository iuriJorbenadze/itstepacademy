
def search_words(text):
    words_to_search = ['small', 'tall', 'middle']
    for word in words_to_search:
        if word in text:
            return word
    return 'None of these words are found in the text'

if __name__ == "__main__":
    user_text = input("Enter your text: ")
    print(search_words(user_text))
