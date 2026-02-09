class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.__name = name
    def greet(self):
        print(f"Hello, {self.__name}")
    @classmethod
    def get_species(cls):
        return cls.species
    @staticmethod
    def arbitrary():
        return "Arbitrary message"
    
human = Human("Artur")
human.greet()
print(Human.get_species())
print(Human.arbitrary())
