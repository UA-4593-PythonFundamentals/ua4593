def count_char(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
input_str = "hello"
res = count_char(input_str)
print(res)