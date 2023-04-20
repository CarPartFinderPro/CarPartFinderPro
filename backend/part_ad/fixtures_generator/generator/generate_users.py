"""
Module for generating user fixtures.
"""
import json
import random
from faker import Faker

fake = Faker()


def generate_user_data(num_users=10):
    """
    Generate fixture data for users.

    Args:
        num_users (int): Number of users to generate (default: 10).

    Returns:
        List of dictionaries, each representing a user fixture.
    """
    users = []
    for _ in range(num_users):
        user = {
            "model": "part_ad.User",
            "fields": {
                "username": fake.user_name(),
                "password": fake.password(),
                "email": fake.email(),
                "mobile": f'+48 {fake.msisdn()[3:]}',
                "active": random.choice([True, False]),
                "registration_date": fake.date_time_this_year().isoformat(),
            }
        }
        users.append(user)
    return users


if __name__ == "__main__":
    num_users = 10
    users = generate_user_data(num_users)

    with open("user_fixtures.json", "w", encoding='utf-8') as outfile:
        json.dump(users, outfile, ensure_ascii=False, indent=4)
