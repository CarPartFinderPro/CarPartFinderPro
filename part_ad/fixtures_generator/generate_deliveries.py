import json
from faker import Faker

fake = Faker()


def generate_delivery_data(num_deliveries=10, num_users=10, num_addresses=10):
    deliveries = []
    for _ in range(num_deliveries):
        delivery = {
            "model": "part_ad.Delivery",
            "fields": {
                "user": fake.random_int(min=1, max=num_users),
                "address": fake.random_int(min=1, max=num_addresses),
                "address_type": fake.random_element(elements=("home", "work")),
                "primary": fake.boolean(chance_of_getting_true=50),
            }
        }
        deliveries.append(delivery)
    return deliveries


if __name__ == "__main__":
    num_deliveries = 10
    deliveries = generate_delivery_data(num_deliveries)

    with open("delivery_fixtures.json", "w") as outfile:
        json.dump(deliveries, outfile)
