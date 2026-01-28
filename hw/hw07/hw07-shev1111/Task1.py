def lagerst_number(number1, number2):
    """
Return the larger of two numbers.

Args:
    number1 (int | float): First number
    number2 (int | float): Second number

Returns:
    int | float: The larger number
    """

    if number1 > number2:
        return number1
    else:
        return number2


print(lagerst_number(10, 20))  # Output: 20
