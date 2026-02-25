class Human:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")

    @classmethod
    def get_species(cls):
        return "Homosapiens"
    
    @staticmethod
    def arbitrary_message():
        return "test message"
    
person1 = Human("Anton")
person1.say_hello()

person2 = Human("Maya")
person2.say_hello()

print(Human.get_species())

print(Human.arbitrary_message())