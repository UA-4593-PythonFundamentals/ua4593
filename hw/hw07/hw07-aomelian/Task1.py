def largest_number(num1, num2):
    """ 
    Returns the larger of two numbers

    Compares two numbers and returns whichever is greater
    If both numbers are equal, returns either one

    Args:
        num1 (int or float)
        num2 (int or float)
    Returns:
        int or float

    Examples:
        >>> largest_number(5,3)
        5
        >>> largest_number(2,2)
        2
    """
    if num1 > num2:
        return num1
    else:
        return num2

print(largest_number(2,2))
