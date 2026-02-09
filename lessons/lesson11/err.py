# print(" This is lesson 11 error handling example.
# print(" Intentional syntax error for demonstration purposes.")

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("The result of division is:", a / b)# The above line is missing a closing parenthesis.

# print(" End of lesson 11.")

# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except:
#         return None
#     return result
   
# print(divide_numbers(10, 0))  # This will return None due to division by zero.
# print(" This is lesson 11 error handling example.")


# try:
#     a = int(input("Enter your number: ")) # throws ValueError
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError):
#     print("Error Occurred and Handled")

# print(" End of lesson 11.")

# try:
#     a = int(input("Enter your number: ")) # throws ValueError
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# except NameError:
#     print("Variable b is not defined.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# else:
#     print(f"No errors occurred. Value of b is {b}.")
# finally:
#     print("Execution completed.")

# print(" End of lesson 11.")

# def foo():
#     try:
#         return 1
#     finally:
#         # return 2
#         print("In finally block")
    
# print(foo())  



def read_integer():
    value = input("Enter a positive integer: ")
    if not value.isdigit():
        raise ValueError(f"The input is not a valid positive integer. You entered: {value}")
    return int(value)

try:
    number = read_integer()
    print(f"You entered: {number}")

except ValueError as e:
    print(f"Error: {e}")
