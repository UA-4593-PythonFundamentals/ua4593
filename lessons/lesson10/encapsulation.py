

# class EncapExample:
#     def __init__(self, public_var=None, protected_var=None, private_var=None):
#         self.public_var = public_var if public_var is not None else "I am public"
#         self._protected_var = protected_var if protected_var is not None else "I am protected"
#         self.__private_var = private_var if private_var is not None else "I am private"
        
#     def __str__(self):
#         return (f"Public: {self.public_var}\n"
#                 f"Protected: {self._protected_var}\n"
#                 f"Private: {self.__private_var}")
    
# e = EncapExample()
# print(e)
# print(e.public_var)          # Accessible
# print(e._protected_var)      # Accessible but discouraged
# # print(e.__private_var)     # Not accessible, will raise AttributeError
# # Accessing private variable using name mangling
# print(e._EncapExample__private_var)  # Accessible using name mangling


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
    def __str__(self):
        return f"Point({self.__x}, {self.__y}, {self.__z})"
    
    def get_x(self):
        print(">>>\tGetter for x called")
        return self.__x
    def set_x(self, x):
        print(f">>>\tSetter for x called with value {x}")
        if type(x) not in (int, float):
            print("x must be an integer or float")
            return
        self.__x = x

    def get_y(self):
        print(">>>\tGetter for y called")
        return self.__y
    def set_y(self, y):
        print(f">>>\tSetter for y called with value {y}")
        self.__y = y

    y = property(get_y, set_y)
    
    @property
    def z(self):
        print(">>>\tGetter for z called")
        return self.__z
    @z.setter
    def z(self, z):
        print(f">>>\tSetter for z called with value {z}")
        if type(z) not in (int, float):
            print("z must be an integer or float")
            return
        self.__z = z

    

    
p = Point(3, 4, 5)
print(p)
# print(p.__x)  # This will raise an AttributeError
print(p.get_x())  # Accessing private variable via getter
p.set_x(10)       # Modifying private variable via setter
print(p)
print(p.y)        # Accessing y via property
p.y = 20         # Modifying y via property setter
print(p)

print(p.z)        # Accessing z via @property
p.z = 30         # Modifying z via @z.setter    
print(p)

p.set_x("hello")  # Trying to set invalid value for x
p.z = [1, 2, 3]   # Trying to set invalid value for z
print(p)