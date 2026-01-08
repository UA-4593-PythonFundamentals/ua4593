# list

# l = list()
# print(type(l), l)
# l = list("hello")
# # l = list(10) #TypeError: 'int' object is not iterable
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, 2, 3, [4, 5, "text"]]
# print(type(l), l)
# print(l[0])
# print(l[-1])
# print(l[-1][0])
# print(l[-1][2])
# print(l[-1][2][0])
# # print(l[10])  # IndexError: list index out of range
# print(l[1:3])
# print(l[::2])
# print(l[1::2])
# l[0] = 10
# l[-1][2] = "new text"
# print(l)
# print(10 in l)
# print(4 in l)
# print([4, 5, 'new text'] in l)
# l1 = [6, 7, 8]
# l2 = [6, 7, 8]
# l3 = [6, 9, 8]
# print(l1 == l2)
# print(l1 == l3)
# print(l1 is l2)
# methods = [method for method in dir(list) if not method.startswith("__")]
# print(methods)
# l = []
# l.append(1)
# l.append(2)
# l.append("text")
# l.append([3, 4])
# print(l)
# # l.extend(10)  # TypeError: 'int' object is not iterable
# l.extend("text")
# print(l)
# l.insert(0, "start")
# print(l)
# l.insert(2, "new")
# print(l)
# l.insert(100, "end")
# l.insert(-100, "begin")
# print(l)
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [l1, l2]
# print(l1, l2, l3)
# l1.clear()
# print(l1, l2, l3)
# l2 = []
# print(l1, l2, l3)
# l = [1, 2, 3, 2, 4, 2]
# l2 = l.copy()
# l3 = l
# print(l, l2, l3)
# print(id(l), id(l2), id(l3))
# l = [1, 22, 3, 22, 4, 22]
# print(l)
# e = l.remove(22)
# print(l, e)
# # l.remove(322) # ValueError: list.remove(x): x not in list
# e = l.pop()
# print(l, e)
# e = l.pop(2)
# print(l, e)
# l.append(22)
# print(l)
# print(l.count(22))
# print(l.index(22))
# l = [3, 1, 4, 2, 3, 7, 5, 3, 8, 7]
# print(l)
# # print(l.index(3))
# # print(l.index(3, 1))
# # p = -1
# # while True:
# #     try:
# #         p = l.index(3, p + 1)
# #         print(p)
# #     except ValueError:
# #         break

# l.reverse()
# print(l)
# l.sort()
# print(l)

# l = [True, [1,230], "abc", 3.14, 42]
# print(all(l))
# l.append(0)
# print(all(l))
# print(any(l))
# print(list(enumerate(l)))
# print(len(l))

# l = [3,5,7,8,1,2]
# print(l)
# ls= sorted(l)
# print(ls)
# print(l)  # original list is unchanged
# print(list(reversed(l)))
# print(l)  # original list is unchanged
# l = []
# for i in range(5):
#     l.append(i * i)
# print(l)
# l = [i * i for i in range(5)]
# print(l)
# l = []
# for i in range(3):
#     for j in range(i, 3):
#         l.append((i, j, i + j))
# print(l)
# l = [(i, j, i + j) for i in range(3) for j in range(i, 3)]



