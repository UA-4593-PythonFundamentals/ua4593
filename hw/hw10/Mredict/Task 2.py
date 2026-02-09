class Human:
    species = "Homosapiens"
    def __init__ (self, name):
        self.name = name

    def greet(self):
        print(f"Welcome, {self.name}!!!")

    @classmethod
    def get_species(cls):
        print(f"This species is {cls.species}.")
    
    @staticmethod
    def arbitrary_message():
        print("This is arbitrary message.")
    
# Example usage
if __name__ == "__main__":
    person = Human("Alice")
    person.greet()
    Human.get_species()
    Human.arbitrary_message()