def calculate_char(input_string):
    """Calculate the frequency of each character in the input string."""
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
print(calculate_char("hello"))