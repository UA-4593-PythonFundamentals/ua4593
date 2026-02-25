def largest_num(num1, num2):
    """
    Returns the larger of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        The larger number.
    """
    if num1 > num2:
        return num1
    
    return num2

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print(f'The largest number is: {largest_num(num1, num2)}')