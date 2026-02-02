
from util import generate_test_users
from my_logging import logging



if __name__ == "__main__":
    print("\nGenerating test users:")
    users = generate_test_users(15)
    print(f"\nTotal test users created: {len(users)}")
    for user in users:
        print(user.get_info())