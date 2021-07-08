def print_upper_words(words,must_start_with=['e']):
    """Takes list of words and a list of letters, and prints each word out that starts with a letter in the list of letters in upper case"""
    for word in words:
        word = word.upper()
        for letter in must_start_with:
            if(word.startswith(letter.upper())):
                print(word)

