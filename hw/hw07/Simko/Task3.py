def number_of_characters_in_string(word):
    """Return the number of characters included in given string"""
    return {vocabulary: word.count(vocabulary) for vocabulary in word}
print(number_of_characters_in_string("hello")) 
