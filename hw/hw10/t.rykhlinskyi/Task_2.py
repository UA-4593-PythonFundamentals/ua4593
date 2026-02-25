class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, my name is {self.name}!"
    
    @classmethod
    def species_info(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_info():
        return "This is some arbitrary information about humans."

person = Human("Орест")
print(person.welcome())
print(Human.species_info())   
print(Human.arbitrary_info())