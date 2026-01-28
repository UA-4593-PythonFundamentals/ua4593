def calculate_chars_in_string(string):
    result = {}
    for char in string.strip():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(calculate_chars_in_string("hello, world!"))