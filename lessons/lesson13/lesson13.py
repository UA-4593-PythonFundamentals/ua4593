# doubled_odds = [x * 2 for x in range(1, 11) if x % 2 != 0]

# print(doubled_odds, type(doubled_odds))

# z1 = zip([1, 2, 3], ['a', 'b', 'c'])
# print(z1, type(z1), list(z1))
# z2 = zip([1, 2, 3], ['a', 'b', 'c'], "xyz")
# print(z2, type(z2), list(z2))
# z3 = zip([1, 2, 3], ['a', 'b', 'c'], "wxyz")
# print(z3, type(z3), list(z3))

# def add(x, y):
#     return x + y
# from pprint import pprint
# lambda_add = lambda x, y: x + y
# pprint(locals())

# l = [1, 2, 3, 4, 5]
# squared = map(lambda x: x ** 2, l)
# for x in squared:
#     print(x)
# print(squared, type(squared))
# print(list(squared))

# def print_info(x):
#     print(f"Value: {x}, Type: {type(x)}")
# data = [1, 'hello', 3.14, [1, 2, 3], {'key': 'value'}]
# # m = map(print_info, data)

# # print(m, type(m), list(m))

# def is_iterable(x):
#     try:
#         iter(x)
#         return True
#     except TypeError:
#         print(f"{x} is not iterable")
#         return False
# f = filter(is_iterable, data)  # False
# print(f, type(f), list(f))

# from functools import reduce
# def add(x, y):
#     value = x + y
#     print(f"Adding {x} and {y} to get {value}")
#     return value
# value = reduce(add, [47, 11, 42, 13])
# print(f"Final result: {value}")
# value = reduce(add, [47, 11, 42, 13], 1000)
# print(f"Final result: {value}")

# l = [1, 2, 3, 4, 5]
# it = iter(l) # l.__iter__()
# print(it, type(it))
# print(next(it)) # it.__next__()
# print(it, type(it))
# print(next(it)) # it.__next__()
# print(next(it)) # it.__next__()
# print(next(it)) # it.__next__()
# print(next(it)) # it.__next__()
# print(next(it)) # it.__next__()
# print(next(it)) # it.__next__()
# for x in l:
#     print(x)

# it = iter(l)
# for v in it:
#     print(v)

# class MyRange:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             end = start
#             start = 0
#         self.start = start
#         self.end = end
#         self.step = step
#     def __repr__(self):
#         return f"MyRange({self.start}, {self.end}, {self.step})"
#     def __iter__(self):
#         print("Creating an iterator")
#         self.current = self.start
#         return self
#     def __next__(self):
#         print("Getting the next value")
#         if self.current >= self.end:
#             print("No more values to iterate")
#             raise StopIteration
#         value = self.current
#         self.current += self.step
#         return value

# r = MyRange(5)
# print(r)
# for x in r:
#     print(x)
# r = MyRange(1, 10)
# print(r)
# for x in r:
#     print(x)
# r = MyRange(1, 10, 2)
# print(r)
# for x in r:
#     print(x)

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# g = my_generator()
# print(g, type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# def my_generator(n):
#     print("Starting generator")
#     for i in range(n):
#         print(f"Yielding value: {i}")
#         yield i
#     print("Generator finished")

# # # g = my_generator(5)
# # # print(list(g))
# # for value in my_generator(5):
# #     print(f"Received value: {value}")
# #     _ = input("Press Enter to continue...")

# N = 3
# for i in range(5):
#     print(f"N {N}")
#     g = my_generator(N)
#     l = list(range(N))
#     print(f"\tList: {l.__sizeof__()}")
#     print(f"\tGenerator: {g.__sizeof__()}")
#     N *= 10


class UserModel:

    pk=None
    def __init__(self, name=None):

        self.name = name
    
    def __iter__(self):
        self.pk = 1
        self.step = 5
        return self
        
    def __next__(self):
        if self.pk > 100:
            raise StopIteration
        value = self.pk
        self.pk += self.step
        users_pk = [i for i in range(value, self.pk)]
        return users_pk

    def get_all_users(self):
        # Simulate fetching users from a database

        for rows in self.__iter__():
            print(f"Fetched rows with PKs: {rows}")
            for i in rows:
                sql_query = f"\tSELECT * FROM users WHERE pk={i}"
                print(f"\tExecuting SQL query: {sql_query}")
                yield UserModel(f"User{i}")
    
for user in UserModel().get_all_users():
    print(f"\tUser name: {user.name}")