def char_calculate(string):
    """
    Calculate the number of characters in a given string.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1

    return char_count

string = input('Enter the string: ').lower().replace(' ', '')

calculate_result = char_calculate(string)

print(calculate_result)