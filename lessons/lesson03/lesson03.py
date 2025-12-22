# a = 5
# b = 10
# print(a == b)  # This will print False since 5 is not equal to 10
# print(a != b)  # This will print True since 5 is not equal to 10
# print(a < b)   # This will print True since 5 is less than 10
# print(a <= b)  # This will print True since 5 is less than or equal to 10
# print(a > b)   # This will print False since 5 is not greater than
# print(a >= b)  # This will print False since 5 is not greater than or equal to 10

# a = [1, 2, 3]
# b = [1, 2, 3]
# c = [1,3,2]
# print(a == b)  # This will print True since both lists have the same elements
# print(a == c)  # This will print False since the order of elements is different

# a = True
# b = False
# print(a, not a)  # This will print True False
# print(b, not b)  # This will print False True
# a = [False, False, True, True]
# b = [False, True, False, True]
# for i in range(len(a)):
#     print(f"{a[i]}\t{b[i]}\t{a[i] and b[i]=}\t{a[i] or b[i]=}")

# print(10 and "Hello" and 3.14)  
# print(10 and "Hello" and 3.14 and 0)  
# print(10 and [] and 3.14 and 0)  
# print(0 or "" or None or "Python")  
# print(0 or "" or None or "Python" or 42)
# print(0 or "" or None or [] )

# is_false = [False, 0, 0.0, None, "", [], {}, ()]
# print("is_false values:")
# for value in is_false:
#     if value:
#         print(f"\t{value!r} is True")
#     else:
#         print(f"\t{value!r} is False")

# is_true = [True, 1, -1, 3.14, "Hello", [1, 2], {1: 'a'}, (1, 2), {1}]
# print("is_true values:")
# for value in is_true:
#     if value:
#         print(f"\t{value!r} is True")
#     else:
#         print(f"\t{value!r} is False")

# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# c = a
# print(f"a == b: {a == b}")   # True, because the contents are the same
# print(f"a is b: {a is b}")   # False, because they are different
# print(f"a is c: {a is c}")   # True, because c references the same object as a
# print(f"{id(a) == id(b)=}")  # False, different objects
# print(f"a is not c: {a is not c}")  # False, same object

# 1 in 10 # This will raise a TypeError since 'in' cannot be used between an integer and another integer

# a = [1,2, [3,4], "hello"]
# print(f"{3 in a=}")            # This will print False since 3 is not a direct element of the list a
# print(f"{[3,4] in a=}")        # This will print True since [3,4] is an element of the list a
# print(f"{'hello' in a=}")      # This will print True since "hello" is an element of the list a
# print(f"{'hel' in a=}")        # This will print False since "hel" is not an element of the list a
# print(f"{'hel' in a[3]=}")     # This will print True since "hel" is a substring of the string "hello"
# print(f"{4 in a=}")          # This will print False since 4 is not a direct element of the list a
# print(f"{4 not in a=}")     # This will print True since 4 is not a direct element of the list a

# d = {'key1': 1, 'key2': 2}
# print(f"{'key1' in d=}")        # This will print True since 'key1' is a key in the dictionary d
# print(f"{1 in d=}")        # This will print False since 1 is a value, not a key, in the dictionary d

# a = 13

# # if a % 2 == 0:
# if not a % 2:
#    print(f"---{a} is even---")
#    print(f"{a} is even")
#    print(f"{a} % 2 = {a % 2}")
# print("This line is always printed")

# age = 15
# # if age >=18 and age < 65:
# if 18 <= age < 65:
#     print("You are an adult.")

# print("This line is always printed")

# a =1
# b = 2
# c = 1
# d = 4
# if a <b < c < d:
#     print("a is less than b, b is less than c, and c is less than d")   
# print("This line is always printed")

# temperature = float(input("Enter the temperature: "))
# if temperature > 30:
#     print("It's a hot day.")
# else:
#     print("It's not a hot day.")
# print("This line is always printed")

# age = int(input("Enter your age: "))
# if age < 0:
#     print("Invalid age.")
# else:
#     if age < 18:
#         print("You are a minor.")
#     else:
#         if age < 65:
#             print("You are an adult.")
#         else:
#             print("You are a senior.")
# print("This line is always printed")
# if age < 0:
#     print("Invalid age.")
# elif age < 18:
#     print("You are a minor.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior.")

# temperature = float(input("Enter the temperature: "))
# message = None
# if temperature > 30:
#     message = "It's a hot day."
# else:
#     message = "It's not a hot day."
# print(message)
# msg = "It's a hot day." if temperature > 30 else "It's not a hot day."
# # msg = temperature > 30 ? "It's a hot day." : "It's not a hot day."
# print(msg)

# status_code = int(input("Enter the status code: "))
# match status_code:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Internal Server Error")
#     case _:
#         print("Unknown Status Code")
# print("This line is always printed")


# status_code = int(input("Enter the status code: "))
# match status_code:
#     case 200 | 201 as sc:
#         print("OK", sc)
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Internal Server Error")
#     case _:
#         print("Unknown Status Code")


# for values in [("load", "http://example.com"),
#                ("save", "http://example.com", "file1.txt"),
#                 ("save", "http://example.com", "file1.txt", "file2.txt", "file3.txt"),
#                 ("delete", "http://example.com"),
#                 ("delete", "http://example.com", "file1.txt"),
#                 ("save", "http://example.com"),
#                 15,
#                 "test",
#                 [1,2],
#                 "AB"]:
#     print(f"Processing command: {values}")
#     match values:
#         case "load", link:
#             print(f"\tloading {link}")
#         case "save", link, filename:
#             print(f"\tsaving {filename} to {link}")
#         case "save", link, *filenames:
#             print(f"\tsaving multiple files to {link}:")
#             for filename in filenames:
#                 print(f"\t\t{filename}")
#         case comand, link:
#             print(f"\tUnknown command '{comand}' for link: {link}")
#         case _:
#             print(f"\tUnknown command: {values}")

# for item in [['morning', 'have breakfast'],
#                  ['afternoon', 'have lunch'],
#                  ['evening', 'have dinner'],
#                  ['night', 'go to sleep'],
#                  ['midnight', 'party'],
#                  ('invalid', "do something"),
#                  ('morning', 'have breakfast')]:
#     match item:
#         case ['evening', action]:
#             print(f'You almost finished the day! Now{action}!')
#         case [time, action]:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')

# for item in [['morning', 'have breakfast'],
#                  ['afternoon', 'have lunch'],
#                  ['evening', 'work'],
#                  ['evening', 'have dinner'],
#                  ['night', 'go to sleep'],
#                  ['midnight', 'party'],
#                  ('invalid', "do something"),
#                  ('morning', 'have breakfast')]:
#     match item:
#         case ['evening', action] if action not in ['work', 'study']:
#             print(f'You almost finished the day! Now {action}!')
#         case ['evening', _]:
#             print('Come on, you deserve some rest!')
#         case [time, action]:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')


a = int(input("Enter an integer: "))
if a > 0:
    b = "positive"
print(f"The number {a} is {b}.")