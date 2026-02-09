from uuid import uuid4

class User:
    def __init__(self, username, email, age, phone):
        self.pk = str(uuid4())
        self.username = username
        self.email = email
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"User(pk={self.pk}, username={self.username}, email={self.email}, age={self.age}, phone={self.phone})"
    
    def __repr__(self):
        return f"({self.pk} {self.email})"
    def to_dict(self):
        return {
            "pk": self.pk,
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "phone": self.phone
        }
    
def generate_random_user():
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    domains = ["example.com", "test.com", "sample.org"]
    import random
    random_username = random.choice(names) + str(random.randint(1, 100))
    random_email = random_username.lower() + "@" + random.choice(domains)
    random_age = random.randint(18, 70)
    random_phone = f"+1-555-{random.randint(1000,9999)}"
    return User(random_username, random_email, random_age, random_phone)

    