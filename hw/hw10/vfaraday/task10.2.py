#Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#Color Ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#Basic subclasses - Adam and Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

#Classy Classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

#Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        area = 4 * math.pi * (self.radius ** 2)
        return round(area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(self.mass / volume, 5)

#Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("Invalid class name: Must start with uppercase and contain only alphanumeric characters.")

    cls.__name__ = new_name