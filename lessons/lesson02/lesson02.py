# a = 10
# print(a, id(a))
# a += 5
# print(a, id(a))

# l = [1, 2, 3]
# print(id(l), l)
# l.append(4)
# print(id(l), l)
# l[2] = 10
# print(id(l), l)
# t = (1, 2, 3)
# print(id(t), t)
# t[1] = 10  # This will raise a TypeError because tuples are immutable

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l1
# print(id(l1), l1)
# print(id(l2), l2)
# print(id(l3), l3)
# print(l1 == l2)  # True, same content
# print(id(l1) == id(l2))  # False, different objects


# a = 256
# print(a, type(a), type(a) == int, int)
# a = [1, 2, 3]
# print(a, type(a), type(a) == list)

# a = 10
# print(isinstance(a, int))

# class A: pass
# class B(A): pass

# a = A()
# b = B()
# print(f"{isinstance(a, A)=}")
# print(f"{isinstance(b, B)=}")
# print(f"{isinstance(b, A)=}")
# print(f"{type(b)==A =}")

# print(f"{isinstance(a, B)}")
# print(f"{isinstance(a, B)=}")
# a = 1+2+3+4+5+6+7+8+9+10
# print(a)
# a = 1+2+3+4
# +5+6+7+8+9+10
# a = 1+2+3+4\
# +5+6+7+8+9+10
# print(a)
# a="Hello, world!"; b=10
# a, b = "Hello, world!", 10
# print(f"{a=}, {b=}")
# b = [1,
#       2,
#       3]

# print(f"{b=}")

# b = (1 +
#       2
#       + 3)

# print(f"{b=}")
# print("start loop")
# for i in range(3):
#     print("\tstart iteration")
#     print(f"\t\ttiteration {i}")
#     for j in range(2):
#           print("\t\t\tstart inner iteration")
#           print(f"\t\t\t\tinner iteration {j}")
#           print("\t\t\tend inner iteration")
#     print("\tend iteration")
# print("end loop")


# a = 10
# b = [20, 30, 40]
# c = "30"
# print(f"{a=}, {b=}, {c=}")
# a, b, c = 100, [200, 300, 400], "300"
# print(f"{a=}, {b=}, {c=}")
# a, b, c = 100, [200, 300, 400], "300", 400 # This will raise a ValueError because there are too many values to unpack
# aa, a, b, c = 100, [200, 300, 400], "300" # This will raise a ValueError because there are too few values to unpack

# MY_CONST = 3.14
# print(MY_CONST)
# MY_CONST = 2.71
# print(MY_CONST)

# a = 10
# print(f"{a=}")
# b = 0b1010 # binary for 10. 0 1
# print(f"{b=}")
# c = 0o12 # octal for 10. 0 1 2 3 4 5 6 7 
# print(f"{c=}")
# d = 0xA # hexadecimal for 10. 0 1 2 3 4 5 6 7 8 9 A B C D E F
# print(f"{d=}")
# d = 0x10
# print(f"{d=}")

# for i in range(16):
#     print(f"{bin(i)[2:].zfill(4)}\t{oct(i)[2:].zfill(2)}\t{i}\t{hex(i)[2:]}")


# a = 1_0_0_0_000
# print(f"{a=}", type(a))

# a = 10.5_5_5
# print(f"{a=}", type(a))
# a = 12345e3 # 12345 * 10^3
# print(f"{a=}", type(a))
# a = 12345e-3 # 12345 * 10^-3
# print(f"{a=}", type(a))
# t = True
# f = False
# print(t, f)
# print(type(t), type(f))
# print(True + True + False + True+ 74)  # 1 + 1 + 0 + 1 + 74 = 77

# a = None # null nil nullptr 
# print(a, type(a))


# l = [1, 2, 3, 4, 5, 5, 5, 5]
# print(f"{l=}", type(l))
# t = (1, 2, 3, 4, 5, 5, 5, 5)
# print(f"{t=}", type(t))
# # t[0] = 10  # This will raise a TypeError because tuples are immutable
# s = {1, 2, 3, 4, 5, 5, 5, 5}
# print(f"{s=}", type(s))
# d = { "a": 1, "b": 2, "c": 3 }
# print(f"{d=}", type(d))
# d["a"] = 10
# print(f"{d=}", type(d))

# c = (-1)**0.5
# print(f"{c=}", type(c))

# a = "152"
# b = "3.14"
# print(type(a), type(b), f"{a+b=}")
# a_int = int(a)
# b_float = float(b)
# print(type(a_int), type(b_float), f"{a_int + b_float=}")

# print(int("FF", 16))
# print(int("FF", 1000)) # ValueError: int() base must be >= 2 and <= 36, or 0
# a = ["1", "2", "3"]
# a_str = str(a)
# print(type(a), type(a_str), f"{a_str=}")
# l = [1, 2, 3]
# t = tuple(l)
# # t = tuple(1) # TypeError: 'int' object is not iterable
# print(type(l), type(t), f"{t=}")

# for i in range(256):
#     print(f"{i}\t{chr(i)}")

# for c in "Hhello, world!":
#     print(f"{c}\t{ord(c)}")


# a = 39
# print(f"{a=}, {bin(a)=}, {oct(a)=}, {hex(a)=}")
# s1 = "Hello"
# s2 = 'Hello'
# text = """This is a multi-line
# string that spans
# multiple lines."""
# text2 = '''Another multi-line
# string using single quotes.'''
# print(s1, s2)
# print(text, type(text))
# print(text2, type(text2))

# text = "Hello, world! \nWelcome to Python programming."
# print(text)
# text = "0123456789\rabc"
# print(text)
# time_in_secondsto_run = 100
# s = ["\\", "|", "/", "-"]
# while time_in_secondsto_run > 0:
#     print("\t",s[time_in_secondsto_run % 4], end="\r")    
#     time_in_secondsto_run -= 1
#     import time
#     time.sleep(0.1)

# text = "Hello, \"text\" world!"
# text = 'Hello, "text" world!'
# text = 'Hello, \'text\' world!'

# template_string = "%s is %d years old. Your sallary is %.3f $"
# print(template_string)
# print(template_string % ("Alice", 30, 1234.56789))
# print(template_string % ("Bob", 25, 9876.54321))
# name = "Charlie"
# age = 28
# salary = 4567.89
# print(template_string % (name, age, salary))

# template_string = "{} is {} years old. Your sallary is {:.3f} $"
# print(template_string)
# print(template_string.format("Alice", 30, 1234.56789))
# print(template_string.format("Bob", 25, 9876.54321))
# template_string = "{name} is {age} years old. Your sallary is {salary:.3f} $"
# print(template_string)
# print(template_string.format(name="Alice", age=30, salary=1234.56789))
# print(template_string.format(age=25, salary=9876.54321, name="Bob"))

# name = "Charlie"
# age = 28
# salary = 4567.89
# print(f"{name} is {age} years old. Your sallary is {salary:.3f} $")
# print(f"{name=}, {age=}, {salary=:.3f}")
# print(f"{(name*3).replace('Ch', '<>')=}")


# text = "Hello, world!"
text = "my string"
index = list(range(len(text)))
reversed_index = list(range(-len(text), 0))
print(text)
print(index)
print(reversed_index)
zipped = zip(text, index, reversed_index)
print("Char\tIndex\tRevIndex")
# for char, idx, rev_idx in zipped:
#     print(f"{char}\t{idx}\t{rev_idx}")
line_0 = ""
line_1 = ""
line_2 = ""
n = 3
for char, idx, rev_idx in zipped:
    line_0 += f"{char}\t".center(n)
    line_1 += f"{idx}\t".center(n)
    line_2 += f"{rev_idx}\t".center(n)
print(line_0)
print(line_1)
print(line_2)

print("----- Accessing characters -----")
print(text[0])      # H - first character
print(text[7])      # w - eighth character
print(text[-1])     # ! - last character
print(text[-6])     # w - sixth character from the end
