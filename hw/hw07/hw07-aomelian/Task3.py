def count_chars(text):
    """
    Count the frequency of each character in a string.

    Args:
        text (str)
    
    Returns:
        dict: A dictionary with characters as keys and counts as values
    
    Example:
        >>> count_characters("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_chars("hello"))