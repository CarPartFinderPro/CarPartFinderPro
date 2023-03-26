import os

from .generate_users import generate_user_data
from .generate_addresses import generate_address_data
from .generate_deliveries import generate_delivery_data
from .generate_parcels import generate_parcel_data
from .generate_car_parts import generate_car_part_data
import json


class FixtureGenerator:

    def __init__(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), "..", "fixtures") + os.path.sep
        if not os.path.exists(self.fixtures_path):
            os.makedirs(self.fixtures_path)

    def init_fixtures(self):
        num_users = 10
        num_addresses = 10
        num_deliveries = 10
        num_parcels = 10
        num_car_parts = 10

        users = generate_user_data(num_users)
        addresses = generate_address_data(num_addresses)
        deliveries = generate_delivery_data(num_deliveries, num_users, num_addresses)
        parcels = generate_parcel_data(num_parcels, num_users, num_deliveries)
        car_parts = generate_car_part_data(num_car_parts, num_users)

        with open(self.fixtures_path + "user_fixtures.json", "w") as outfile:
            json.dump(users, outfile, default=str)

        with open(self.fixtures_path + "address_fixtures.json", "w") as outfile:
            json.dump(addresses, outfile, default=str)

        with open(self.fixtures_path + "delivery_fixtures.json", "w") as outfile:
            json.dump(deliveries, outfile, default=str)

        with open(self.fixtures_path + "parcel_fixtures.json", "w") as outfile:
            json.dump(parcels, outfile, default=str)

        with open(self.fixtures_path + "car_part_fixtures.json", "w") as outfile:
            json.dump(car_parts, outfile, default=str)

    if __name__ == "__init_fixtures__":
        init_fixtures()
