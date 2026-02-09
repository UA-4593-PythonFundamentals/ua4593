def letter_count(text):
    '''
    Counts the number of letters in the given string.
    '''
    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

text = input("Enter a string: ")
print("Letter count:", letter_count(text))