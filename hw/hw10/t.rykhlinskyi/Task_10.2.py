def class_name_changer(cls, new_name):
    if not new_name:
        raise ValueError("Назва класу не може бути порожньою")

    # 2. Перевірка першої літери (має бути Upper Case)
    if not new_name[0].isupper():
        raise ValueError("Назва класу повинна починатися з великої літери")

    # 3. Перевірка на буквено-цифрові символи (alphanumeric)
    if not new_name.isalnum():
        raise ValueError("Назва класу повинна містити лише літери та цифри")
        
    cls.__name__ = new_name
    return cls

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
        density = self.mass / volume
        return round(density, 5) 
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

class Human:
    def __init__(self, name):
        self.name = name
class Man(Human):
    def __init__(self, name = "Adam"):
        super().__init__(name)
class Woman(Human):
    def __init__(self, name = "Eve"):
        super().__init__(name)
        
def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

import random

class Ghost(object):
    def __init__(self):
        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random.choice(colors)

class Ball(object):
    # your code goes here
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type