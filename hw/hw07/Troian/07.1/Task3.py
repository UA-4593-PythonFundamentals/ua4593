def calculates_number_fo_characters_in_string(value):
    """
    This funcsion calculates number fo characters in string
    
    :param value: must be a string
    """
    result = {}

    for i in value:
        result[i] = 0
        for ii in value:
            if i == ii:
                result[i] += 1

    return result


#Checks function
print("input your string:")
inp = input()

print(calculates_number_fo_characters_in_string(inp))
