

class Animal:
    def print_speak(self):
        print(self.speak())
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    # def speak(self):
    #     return "Meow!"
    def speak(self, loud=False):
        return "MEOW!" if loud else "Meow!"
    

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.print_speak()