class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "This is an arbitrary static message."

# --- Testing Task 2 ---
person = Human("Alice")
person.welcome_message()
print(Human.get_species())
print(Human.random_message())