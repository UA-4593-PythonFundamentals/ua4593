
def largest_number_return(first, second):
    """
    This function return the largest of two numbers.
    """
    if first > second:
        return first
    else:
        return second

def print_first_second_and_result_lnr(first, second):
    """
    This function help print result
    """
    print("-----------------------------------------------------------")
    print("First = " + str(first) + "\nSecond = " + str(second) + "\n Biger = " + str(largest_number_return(first,second)))
    print("-----------------------------------------------------------")



#And now we create first and second and check how all functions work

first = 10
second = 11

print_first_second_and_result_lnr(first,second)
first = 20
second = 10
print_first_second_and_result_lnr(first,second)
first = 20
second = 10
print_first_second_and_result_lnr(first,second)


#Checks DocString
print(print_first_second_and_result_lnr.__doc__)

print(largest_number_return.__doc__)