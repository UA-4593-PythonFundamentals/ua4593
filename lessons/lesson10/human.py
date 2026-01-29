class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        self.family = []
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     self.friends = [12, 3]
    #     self.family = [1, 2]
        

    def add_friend(self, friend):
        self.friends.append(friend)
        
    def add_family_member(self, family_member):
        self.family.append(family_member)
    def __str__(self):
        return f"Human(Name: {self.name}, Age: {self.age}\n\tFriends: {[friend.name if isinstance(friend, Human) else friend for friend in self.friends]}\n\tFamily: {[member.name if isinstance(member, Human) else member for member in self.family]})"
    def __repr__(self):
        return f"<{self.name}, {self.age}>"
    def __del__(self):
        print(f"\tHuman {self.name} is being deleted.")

def create_random_human():
    import random
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    name = random.choice(names)
    age = random.randint(1, 100)
    human = Human(name, age)
    print(f"Created human: {human.__repr__()}")
    if (r:=random.random()) < 0.5:
        print(f"\trandom value {r} < 0.5, returning None instead of human")
        return None
    
    return human
if __name__ == "__main__":
    # alice = Human("Alice", 30)
    # bob = Human("Bob", 25)
    # alice.add_friend(bob)
    # alice.add_family_member(Human("Charlie", 60))
    # print(f"{alice.name}'s friends: {[friend.name for friend in alice.friends]}")
    # print(f"{alice.name}'s family: {[member.name for member in alice.family]}")
    peaple = []
    for _ in range(10):
        if human := create_random_human():
            peaple.append(human)
    print("Generated Humans:", len(peaple), peaple)
    for person in peaple:
        print(person)
    for person in peaple:
        for other in peaple:
            if person != other:
                if other.age < person.age:
                    person.add_family_member(other)
                else:
                    person.add_friend(other)
    print("After adding friends and family:")
    for person in peaple:
        print(person)
    from pprint import pprint
    pprint(Human.__dict__)

