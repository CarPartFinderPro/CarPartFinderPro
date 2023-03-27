import json
import random

from faker import Faker

fake = Faker()


def generate_parcel_data(num_parcels=10, num_users=10, num_deliveries=10):
    parcels = []
    for _ in range(num_parcels):
        parcel = {
            "model": "part_ad.Parcel",
            "fields": {
                "sender": fake.random_int(min=1, max=num_users),
                "recipient": fake.random_int(min=1, max=num_deliveries),
                "weight": round(random.uniform(0.1, 10), 2),
                "tracking_number": fake.unique.bothify(text='??-####-??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "status": fake.random_element(elements=("delivered", "in transit", "processing")),
            }
        }
        parcels.append(parcel)
    return parcels


if __name__ == "__main__":
    num_parcels = 10
    parcels = generate_parcel_data(num_parcels)

    with open("parcel_fixtures.json", "w") as outfile:
        json.dump(parcels, outfile)
