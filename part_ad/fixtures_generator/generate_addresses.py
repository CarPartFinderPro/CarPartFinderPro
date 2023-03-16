import json
from faker import Faker

fake = Faker()


def generate_address_data(num_addresses=10):
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
                "latitude": fake.latitude(),
                "longitude": fake.longitude(),
            }
        }
        addresses.append(address)
    return addresses


if __name__ == "__main__":
    num_addresses = 10
    addresses = generate_address_data(num_addresses)

    with open("address_fixtures.json", "w") as outfile:
        json.dump(addresses, outfile)
