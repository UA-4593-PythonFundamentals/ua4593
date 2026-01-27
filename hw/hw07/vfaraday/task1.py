def get_max(a, b):
    """
    Return the largest number of two numbers
    """
    if a > b:
        return a
    else:
        return b

result = get_max(10, 25)
print(f"Largest is: {result}")