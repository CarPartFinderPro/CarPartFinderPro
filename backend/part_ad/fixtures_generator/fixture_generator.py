import os
import json

from part_ad.fixtures_generator.generator import *


class FixtureGenerator:

    def __init__(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), "..", "fixtures") + os.path.sep
        if not os.path.exists(self.fixtures_path):
            os.makedirs(self.fixtures_path)

    def init_fixtures(self):
        generate_num = 10

        users = generate_users.generate_user_data(generate_num)
        addresses = generate_addresses.generate_address_data(generate_num)
        deliveries = generate_deliveries.generate_delivery_data(generate_num, generate_num, generate_num)
        parcels = generate_parcels.generate_parcel_data(generate_num, generate_num, generate_num)
        car_parts = generate_car_parts.generate_car_part_data(generate_num, generate_num)
        favorite = generate_favorite.generate_favorite_data(generate_num,generate_num)

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

        with open(self.fixtures_path + "favorite_fixtures.json", "w") as outfile:
            json.dump(favorite, outfile, default=str)


if __name__ == "__main__":
    FixtureGenerator().init_fixtures()
