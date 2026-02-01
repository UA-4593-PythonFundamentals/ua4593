def calculate_char_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

print   ("Character frequency in 'hello world':", calculate_char_frequency("hello world"))