def count_characters(s):
    count_dict = {}

    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

print(count_characters("hello world"))