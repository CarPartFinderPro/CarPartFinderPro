"""
Module for generating delivery fixtures.
"""

import itertools
from faker import Faker

fake = Faker()

def generate_delivery_data(num_deliveries=10, num_users=10, num_addresses=10):
    """
    Generate delivery fixtures data.

    Args:
        num_deliveries (int): The number of deliveries to generate.
        num_users (int): The number of users.
        num_addresses (int): The number of addresses.

    Returns:
        list: List of dictionaries representing delivery fixtures.
    """
    deliveries = []

    user_address_combinations = list(itertools.product(range(1, num_users + 1), ("home", "work")))

    for _ in range(num_deliveries):
        if not user_address_combinations:
            break

        user, address_type = user_address_combinations.pop(0)

        delivery = {
            "model": "part_ad.Delivery",
            "fields": {
                "user": user,
                "address": fake.random_int(min=1, max=num_addresses),
                "address_type": address_type,
                "primary": fake.boolean(chance_of_getting_true=50),
            }
        }
        deliveries.append(delivery)
    return deliveries
