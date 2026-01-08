
# d = dict()
# print(type(d), d)
# d = dict(a=1, b=2, c=3)
# print(type(d), d)
# d = dict([("a", 1), (111, 2), ("c", 3)])
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     "a": 1,
#     10: 2,
#     (1,2,3): 3
# }
# print(type(d), d)
# print(d["a"])
# print(d[10])
# print(d[(1,2,3)])
# # print(d[20])  # KeyError: 20
# d["a"] = 10
# d[10] = 20
# print(d)
# d[20] = 30
# print(d)



methods = [method for method in dir(dict) if not method.startswith("__")]
print(methods)
d = {"a": 1, "b": 2, "c": 3}
# d2 = d.fromkeys("test", 100)
# print(d2)
# value = d.get("a")
# value2 = d["a"]
# print(value, value2)
# value3 = d.get("z")
# print(value3)
# value3 = d.get("z", 999)
# print(value3)
# value3 = d.get("a", 999)
# print(value3)
# print(d)
# e = d.pop("b")
# print(f"popped value: {e}", d)
# e = d.popitem()
# print(f"popped item: {e}", d)
# d.update({"c": 30, "d": 40})
# print(d)
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key in d:
#     print(f"{key}: {d[key]}")
# a, b = (1, 5)
# print(a, b) 
# for key, value in d.items():
#     print(f"{key}: {value}")
# print(d)
# print("a" in d)
# print(1 in d)

d = {key: key*10 for key in range(1,6)}
print(d)