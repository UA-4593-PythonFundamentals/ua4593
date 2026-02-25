number1 = input()
number2 = input()

def largest_number(n1,n2):
    """This function returns the largest numbers of two numbers"""
    if n1 > n2:
        return n1
    else:
        return n2

print(largest_number.__doc__)
print(largest_number(number1,number2))
