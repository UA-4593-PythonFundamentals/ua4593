from user import User, UserError
from my_logging import logging

def generate_test_users( count=5 ):
    test_names = ["Alice", "Bob", "Charlie", "Diana", "E1ve" ]
    test_emails = ["alice@example.com", "bobexample.com", "charlie@example.com", "diana@example.com", "eve@example.com"]
    test_ages = ["25", "30", "22", "2a8", "35"]
    import random
    users = []
    for _ in range(count):
        name = random.choice(test_names)
        email = random.choice(test_emails)
        age = random.choice(test_ages)
        try:
            user = User(name, email, age)
            users.append(user)
            logging.info(f"Test user created: {user.get_info()}")
        except UserError as e:
            logging.error(f"Failed to create test user: {e}")
    return users