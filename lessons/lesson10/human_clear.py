class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []
        self.family = []
        

    def add_friend(self, friend):
        self.friends.append(friend)
        
    def add_family_member(self, family_member):
        self.family.append(family_member)
    def __str__(self):
        return f"Human(Name: {self.name}, Age: {self.age}\n\tFriends: {[friend.name if isinstance(friend, Human) else friend for friend in self.friends]}\n\tFamily: {[member.name if isinstance(member, Human) else member for member in self.family]})"
    def __repr__(self):
        return f"<{self.name}, {self.age}>"
    def __lt__(self, other):
        return self.age < other.age


def create_random_human():
    import random
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    name = random.choice(names)
    age = random.randint(1, 100)
    human = Human(name, age)

    if (r:=random.random()) < 0.5:

        return None
        
    
    return human
if __name__ == "__main__":

    peaple = []
    for _ in range(10):
        if human := create_random_human():
            peaple.append(human)
    print("Generated Humans:", len(peaple), peaple)
    peaple.sort()
    print("Generated Humans:", len(peaple), peaple)
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



