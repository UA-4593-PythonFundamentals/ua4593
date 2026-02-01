def the_largest_number(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "The numbers are equal"

print(the_largest_number(1, 2))
print(the_largest_number(2, 1))
print(the_largest_number(1, 1))