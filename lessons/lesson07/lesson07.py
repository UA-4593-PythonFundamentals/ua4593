# def first_function():
#     """
#     Docstring for first_function.
#     """
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print("This is the first function.")
#     print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

# print(first_function)
# first_function()
# first_function()
# first_function()
# print()
# # help(print)
# help(first_function)
# print(first_function.__doc__)
# print(print.__doc__)

# def second_function():
#     """
#     Docstring for second_function.
#     """
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print("This is the second function.")
#     print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

# s = second_function()
# print(f"s: {s}")

# def third_function(value):
#     if value:
#         return "This is the third function."
    
# result = third_function(True)
# print(f"result: {result}")
# result = third_function(False)
# print(f"result: {result}")

# def print_info(name, age):
#     print(f"Name: {name}")
#     print(f"Age: {age}")

# print_info()#TypeError: print_info() missing 2 required positional arguments: 'name' and 'age'
# print_info("Alice") #TypeError: print_info() missing 1 required positional argument: 'age'
# print_info("Alice", 30, "Lviv") #TypeError: print_info() takes 2 positional arguments but 3 were given
# print_info("Alice", 30)
# print_info(35, "Bob")

# def print_info(name, age=18, city="Unknown"):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"City: {city}")
# print_info()#TypeError: print_info() missing 1 required positional argument: 'name'
# print_info("Alice")
# print_info("Bob", 30)
# print_info("Charlie", 25, "New York")
# print_info("Diana")
# print_info("Mark", 99,"Los Angeles", 40) #TypeError: print_info() takes from 1 to 3 positional arguments but 4 were given
# print_info("Alice", 25,"San Francisco")
# print_info("Lviv","Anrii", 55)
# print_info(city="Lviv", name="Anrii", age=55)

# def args_function(*args, **kwargs):
#     print("Function with *args and **kwargs")
#     print("\tPositional arguments (args):", args)
#     print("\tKeyword arguments (kwargs):", kwargs)

# args_function(1, 2, 3)
# args_function(name="Alice", age=30)
# args_function(1, 2, name="Bob", city="New York")
# args_function()

# def nested_function(a, b, *args, name="Unknown", **kwargs):
#     print(f"'a': {a} 'b': {b} *args: {args} 'name': {name} **kwargs: {kwargs}")

# nested_function(1, 2)
# nested_function(1, 2, 3, 4, 5)
# nested_function(1, 2, name="Alice")
# nested_function(1, 2, 3, 4, name="Bob", age=30, city="New York")


# SyntaxError: parameter without a default follows parameter with a default
# def f(a, b=1, c): 
#     print(f"a: {a}, b: {b}, c: {c}")


# def f(a, b, c=3):
#     print(f"a: {a}, b: {b}, c: {c}")

# f(1, 2)
# # f(a=1, 2, 4)#SyntaxError: positional argument follows keyword argument
# f(1, b=2, c=4)
# a = 1
# def f():
#     a = 10
#     b = 20
#     print(f"Inside f() a: {a} b: {b}")
# print(a)
# f()
# print(a)
# # print(b) #NameError: name 'b' is not defined


# print("In global scope:", dir())
# print()
# a = 5
# def outer_function():
#     b = 10
#     print("Inside outer_function:", dir(), end="\n\n")
# c = 15
# outer_function()
# print("In global scope:", dir())

# a = 5
# def f():
#     print("Inside f() before modifying a:", a)

# print("In global scope before calling f():", a)
# f()
# print("In global scope after calling f():", a)

# a = 5
# def f():
#     a = 10
#     print("Inside f() before modifying a:", a)

# print("In global scope before calling f():", a)
# f()
# print("In global scope after calling f():", a)

# a = 5
# def f():
#     print("Inside f() before modifying a:", a)
#     a = 10
#     print("Inside f() after modifying a:", a)

# print("In global scope before calling f():", a)
# f()
# print("In global scope after calling f():", a)

# l = [1, 2, 3]
# def modify_list():
#     l.append(4)
#     print("Inside modify_list():", l)

# modify_list()
# print("In global scope after calling modify_list():", l)


# a = 5
# print("In global scope before calling f():", a)
# def f():
#     global a
#     print("Inside f() before modifying a:", a)
#     a = 10
#     print("Inside f() after modifying a:", a)
# f()
# print("In global scope after calling f():", a)

# def outer_function():
#     outer_var = "I am from outer_function"
#     def inner_function():
#         inner_var = "I am from inner_function"
#         print(outer_var)
#         print(inner_var)
#     inner_function()
#     # print(inner_var) #NameError: name 'inner_var' is not defined

# def outer_function():
#     s = "0"
#     def add_to_s(value):
#         nonlocal s
#         s += value
#         print(f"Inside add_to_s(): s = {s}")
#     def print_s():
#         print(f"Inside print_s(): s = {s}") 
#     return (add_to_s, print_s)


# f, p_s = outer_function()
# f("1")
# f("2")
# f("3")
# p_s()

# def closure_example(name):
#     message = "Hello, " + name + "!"
#     def display_message(msg):
#         nonlocal message
#         message += "\n\t" + msg
#         print(message)
#     return display_message

# greet_alice = closure_example("Alice")
# greet_tom = closure_example("Tom")
# greet_alice("Welcome to the Python course.")
# greet_tom("Glad to have you here.")
# greet_alice("Let's learn about functions.")
# greet_tom("Functions are powerful!")

# def factorial_for(n):
#     """Calculate the factorial of a non-negative integer n using a for loop."""
#     print(f"Calculating factorial_for({n})")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# def factorial(n):
#     """Calculate the factorial of a non-negative integer n."""
#     print(f"Calculating factorial({n})")
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(f"Factorial of 5: {factorial(5)}")
# print(f"Factorial of 0: {factorial(0)}")
# print(f"Factorial of 5: {factorial_for(5)}")
# print(f"Factorial of 0: {factorial_for(0)}")


# def get_factorial():
#     values = {

#     }
#     def inner_factorial(n):
#         if n not in values:
#             print(f"Calculating inner_factorial({n})")
#             if n == 0 or n == 1:
#                 values[n] = 1
#             else:
#                 values[n] = n * inner_factorial(n - 1)
#         else:
#             print(f"Retrieving cached value for inner_factorial({n})")
#         return values[n]
    
#     return inner_factorial, values
# factorial_memoized, values_cache = get_factorial()
# print(f"Factorial of 5 with memoization: {factorial_memoized(5)}")
# print(f"Factorial of 6 with memoization: {factorial_memoized(6)}")
# print(f"Factorial of 5 with memoization again: {factorial_memoized(5)}")

# print(f"Cached values: {values_cache}")

# def add(x, y):
#     return x + y

# subtract = lambda x, y: x - y

l = [5, 2, 9, 1, 5, 6, "3", "10", "2", "test"]
# def custom_sort_key(value):
#     if isinstance(value, int):
#         return value
#     elif isinstance(value, str):
#         return len(value)
# l.sort(key=custom_sort_key)
l.sort(key=lambda value: value if isinstance(value, int) else len(value))
print(f"Sorted list (custom key): {l}")