"""
Module for generating address fixtures.
"""
import json
from faker import Faker

fake = Faker()


def generate_address_data(num_addresses=10):
    """
    Generate fake address data.

    Args:
        num_addresses (int): Number of addresses to generate.

    Returns:
        list: A list of dictionaries containing generated address data.
    """
    addresses = []
    for _ in range(num_addresses):
        address = {
            "model": "part_ad.Address",
            "fields": {
                "street_name": fake.street_name(),
                "street_number": fake.building_number(),
                "city": fake.city(),
                "state_province": fake.state(),
                "postal_code": fake.postcode(),
                "latitude": str(fake.latitude()),
                "longitude": str(fake.longitude()),
            }
        }
        addresses.append(address)
    return addresses


if __name__ == "__main__":
    num_addresses = 10
    addresses = generate_address_data(num_addresses)

    with open("address_fixtures.json", "w", encoding="utf-8") as outfile:
        json.dump(addresses, outfile, ensure_ascii=False)
