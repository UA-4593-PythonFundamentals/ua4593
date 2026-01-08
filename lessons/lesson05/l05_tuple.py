# t = tuple()
# print(type(t), t)
# t = tuple("hello")
# print(type(t), t)
# t = ()
# print(type(t), t)
# # t=("text")
# t=("text",)
# print(type(t), t)
# t=("text",1)
# print(type(t), t)
# t = (1, 2, 3, (4, 5, "text"))
# print(type(t), t)
# print(t[0])
# print(t[-1])
# print(t[-1][0])
# t[0] = 10  # TypeError: 'tuple' object does not support item assignment


# methods = [method for method in dir(tuple) if not method.startswith("__")]
# print(methods)
n = 10
for i in range(1, 5):
    
    l = list(range(n**i))
    t = tuple(range(n**i))
    print(f"n={n**i}: list size={l.__sizeof__()} bytes, tuple size={t.__sizeof__()} bytes")