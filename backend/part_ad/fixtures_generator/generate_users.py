import json
import random
from faker import Faker

fake = Faker()


def generate_user_data(num_users=10):
    users = []
    for _ in range(num_users):
        user = {
            "model": "part_ad.User",
            "fields": {
                "username": fake.user_name(),
                "password": fake.password(),
                "email": fake.email(),
                "active": random.choice([True, False]),
                "registration_date": fake.date_time_this_year().isoformat(),
            }
        }
        users.append(user)
    return users


if __name__ == "__main__":
    num_users = 10
    users = generate_user_data(num_users)

    with open("user_fixtures.json", "w") as outfile:
        json.dump(users, outfile)
