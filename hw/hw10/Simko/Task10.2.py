#I. Ball-super-ball
class Ball(object):
    # your code goes here
    def  __init__(self, ball_type = "regular"):
             self.ball_type = ball_type

#II. Color-ghost
import random
class Ghost(object):
    pass
    def __init__(self):
             colors = ["white", "yellow", "purple", "red"]
             self.color = random.choice(colors)

#III. Basic-subclasses-Adam-and-Eve
def God():
    #code
        Adam = Man("Adam")
        Eva = Woman("Eva")
        return [Adam, Eva]
class Human:
        def __init__(self, Adam, Eva):
                self.Adam = Adam
                self.Eva = Eva
class Man(Human):
        def __init__(self, Adam):
                self.Adam = Adam

class Woman(Human):
        def __init__(self, Eva):
                self.Eva = Eva

#IV. Classy-classes
class Person:
   
   def __init__(self, name,age):
        self.name=name    
        self.age=age
   
   @property
   def info(self):
        return f"{self.name}s age is {self.age}"
   
#V. Building Spheres
import math
class Sphere(object):
    pass
    def __init__(self, radius, mass):
         self.radius = radius
         self.mass = mass
    def get_radius(self):
         return self.radius
    def get_mass(self):
         return self.mass
    def get_volume(self):
         return (4/3)*math.pi*self.radius**3
    def get_surface_area(self):
         return 4*math.pi*self.radius**2
    def get_density(self):
         return self.mass/self.get_volume()

#VI. Dynamic Classes
import re
def class_name_changer(cls, new_name):
    pass
    """This function changes the name of a class"""
    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
        raise ValueError("Invalid class name")

    cls.__name__ = new_name
def main():
     class MyClass:
         pass
     class_name_changer(MyClass, "UsefulClass")
     print(MyClass.__name__)

     class_name_changer(MyClass, "SecondUsefulClass")
     print(MyClass.__name__)

     try:
         class_name_changer(MyClass, "invalid-class-name")
     except ValueError as e:
         print(e)
if __name__ == "__main__":
     main() 






