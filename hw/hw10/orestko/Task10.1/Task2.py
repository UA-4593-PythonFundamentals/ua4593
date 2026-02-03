class Human:
    def __init__(self, name):
        self.name = name

    
    def greet(self):
        return f"Hello, my name is {self.name}!"

    @classmethod
    def species_info(cls):
        return "This species is Homosapiens"

    @staticmethod
    def random_message():
        return "Humans are amazing creatures!"
    

person = Human("Alice")


print(person.greet())  
print(Human.species_info())  
print(Human.random_message())  
