

# print(list, type(list))

# l= [1,2,3,4,5]
# print(l, type(l))
# l.append(6)
# print(l)

# class Car:
#     """
#     Docstring for Car
#     """
#     pass

# print(Car, type(Car))
# print(Car.__doc__)

# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
# print(car_1, type(car_1))
# print(id(car_1), int(str(car_1).split('at')[1].strip()[2:-1], 16), id(car_1) == int(str(car_1).split('at')[1].strip()[2:-1], 16))
# print(car_2, type(car_2))
# print(car_3, type(car_3))

# class Car:
#     attr1 = "value1"
#     def print_info(self, name):
#         print("This is a car class object:", name)
#         print("\tattr1:", self.attr1)
#     def static2(self):
#         print(f"dir({self}):", dir(self))
#         print(f"{self}.__dict__:", self.__dict__)

# car_1 = Car()
# car_1.print_info("car_1")
# car_2 = Car()
# car_2.print_info("car_2")
# car_2.print_info("another car_2")

# print(Car.attr1)
# print(Car.print_info)
# print(car_1.attr1)

# def static(obj):
#     print(f"dir({obj}):", dir(obj))
#     print(f"{obj}.__dict__:", obj.__dict__)

# print("-----")
# static(Car)
# print("-----")
# static(car_1)

# Car.print_static = static
# car_1.print_static()
# car_1.static2()

# s = Car.static2
# s(car_1)

# class Car:
#     wheels = 4  # class attribute
#     cars_list = []
#     def __init__(self, make, model, color="Red"):
#         self.make = make  # instance attribute
#         self.model = model  # instance attribute
#         self.color = color  # instance attribute
#         Car.cars_list.append(self)
#     def display_info(self):
#         print(f"Car Info: {self.color} {self.make} {self.model} with {Car.wheels} wheels.")
# car_1 = Car("Toyota", "Corolla", "Blue")
# car_2 = Car("Honda", "Civic")
# car_1.display_info()
# car_2.display_info()
# print(car_1.__dict__)
# print(car_2.__dict__)
# car_1.wheels = 6  # modifying instance attribute
# Car.wheels = 8  # modifying class attribute
# car_1.display_info()
# car_2.display_info()
# print(car_1.__dict__)
# print(car_2.__dict__)
# print("All cars created:")
# print("Total cars:", len(Car.cars_list))
# print("Total cars:", Car.cars_list)
# for car in Car.cars_list:
#     car.display_info()