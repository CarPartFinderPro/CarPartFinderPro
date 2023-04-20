"""
Fixture generator module
"""

import os
import json

from .generator.generate_users import generate_user_data
from .generator.generate_addresses import generate_address_data
from .generator.generate_deliveries import generate_delivery_data
from .generator.generate_parcels import generate_parcel_data
from .generator.generate_car_parts import generate_car_part_data
from .generator.generate_favorite import generate_favorite_data


class FixtureGenerator:

    def __init__(self):
        self.fixtures_path = os.path.join(os.path.dirname(__file__), "..", "fixtures") + os.path.sep
        if not os.path.exists(self.fixtures_path):
            os.makedirs(self.fixtures_path)

    def init_fixtures(self):
        """
        Generates and saves fixtures for the user, address, delivery, parcel, car part, and favorite models.
        """
        generate_num = 10

        users = generate_user_data(num_users=generate_num)
        addresses = generate_address_data(num_addresses=generate_num)
        deliveries = generate_delivery_data(num_deliveries=generate_num, num_users=generate_num,
                                            num_addresses=generate_num)
        parcels = generate_parcel_data(num_parcels=generate_num, num_users=generate_num, num_deliveries=generate_num)
        car_parts = generate_car_part_data(num_car_parts=generate_num, num_users=generate_num)
        favorite = generate_favorite_data(num_favorite=generate_num, num_part_ad=generate_num)

        with open(self.fixtures_path + "user_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(users, outfile, default=str, ensure_ascii=False)

        with open(self.fixtures_path + "address_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(addresses, outfile, default=str, ensure_ascii=False)

        with open(self.fixtures_path + "delivery_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(deliveries, outfile, default=str, ensure_ascii=False)

        with open(self.fixtures_path + "parcel_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(parcels, outfile, default=str, ensure_ascii=False)

        with open(self.fixtures_path + "car_part_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(car_parts, outfile, default=str, ensure_ascii=False)

        with open(self.fixtures_path + "favorite_fixtures.json", "w", encoding='utf-8') as outfile:
            json.dump(favorite, outfile, default=str, ensure_ascii=False)


if __name__ == "__main__":
    FixtureGenerator().init_fixtures()
