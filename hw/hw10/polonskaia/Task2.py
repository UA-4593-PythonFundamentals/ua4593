class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f'Welcome, {self.name}!'
    
    @classmethod
    def species(cls):
        return f'{cls.__name__} is Homo sapiens.'
    
    @staticmethod
    def arbitrary_message():
        return 'This is an arbitrary message in the static method.'


person = Human('Jane')

print(person.welcome_message())
print(Human.species())
print(Human.arbitrary_message())