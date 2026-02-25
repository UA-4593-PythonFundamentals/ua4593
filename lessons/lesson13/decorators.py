

# def super_star(func):

#     def wrapper(*args, **kwargs):
#         print(f"This is super star decorator {func.__name__}")
#         return func(*args, **kwargs)
    

#     return wrapper


# @super_star
# def add(a, b):
#     print(f"Adding {a} and {b}")
#     return a + b

# @super_star
# def subtract(a, b):
#     print(f"Subtracting {b} from {a}")
#     return a - b

# # add = super_star(add)


# add(1, 2)
# add(1, 2)
# subtract(5, 3)
# add(1, 2)
# subtract(5, 3)
# add(1, 2)

# def car_decorator(symbol, times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(symbol * times)
#             value =  func(*args, **kwargs)
#             print(symbol * times)
#             return value
#         return wrapper
#     return decorator

# @car_decorator("*", 10)
# def add(a, b):
#     print(f"Adding {a} and {b}")
#     return a + b

# @car_decorator("#", 15)
# def subtract(a, b):
#     print(f"Subtracting {b} from {a}")
#     return a - b

# a = add(1, 2)
# print(f"Result of add: {a}")
# s = subtract(5, 3)  
# print(f"Result of subtract: {s}")
# s = subtract(5, 3)
# print(f"Result of subtract: {s}")
# a = add(1, 2)
# print(f"Result of add: {a}")
# s = subtract(5, 3)
# print(f"Result of subtract: {s}")






# def add(x:int, y:int):
#     return x + y
# print(add(1, 2))


# def add(x:str, y:str):
#     return f"Adding {x} and {y} to get {x + y}"
# print(add(1, 2))
# print(add("Hello, ", "world!"))

# def add(x, y):
#     if isinstance(x, int) and isinstance(y, int):
#         return x + y
#     elif isinstance(x, str) and isinstance(y, str):
#         return f"Adding {x} and {y} to get {x + y}"
#     else:
#         raise TypeError("Unsupported types for add function")

funks = {}
def parametrize(*types):
    def decorator(func):
        def wrapper(*args):
            t = tuple(type(arg) for arg in args)
            t = map(type, args)
            f = funks.get(tuple(t))
            return f(*args) 
        funks[types] = func
        return wrapper
    return decorator





@parametrize(int, int)
def add(x, y):
    return x + y
print(add(1, 2))

@parametrize(int, float)
def add(x, y):
    return x * y

@parametrize(str, str)
def add(x, y):
    return f"Adding {x} and {y} to get {x + y}"


print(add(1, 2))
print(add("Hello, ", "world!"))
print(add(1, 2.5))
print(add("Hello, ", "world!"))

print(funks)