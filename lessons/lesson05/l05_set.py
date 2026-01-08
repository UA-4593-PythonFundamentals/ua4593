# s = set()
# print(type(s), s)
# s = set("hello")
# print(type(s), s)
# # s = {} # this creates a dict, not a set
# s = {"h", "e", "l", "o", "o", "o", "o", "o", "o", "o"}
# print(type(s), s)
# for item in s:
#     print(item)

methods = [method for method in dir(set) if not method.startswith("__")]
print(methods)
s = set()
s.add(1)
s.add(2)
s.add("text")
s.add((3, 4))
print(s)
e = s.pop()
print(f"popped element: {e}", s)
s.remove(2)
print(s)
s.update((4, 5, 6, 'text'))
print(s)
s.add((4, 5, 6, 'text'))
print(s)
