"""
Module for generating car part fixtures.
"""
import json
import random
from faker import Faker

fake = Faker()


def generate_car_part_data(num_car_parts=10, num_users=10):
    """
    Generates data for car part fixtures.

    Args:
        num_car_parts (int): The number of car parts to generate data for.
        num_users (int): The number of users in the database.

    Returns:
        A list of dictionaries representing car part fixtures.
    """
    car_parts = []
    for _ in range(num_car_parts):
        car_part = {
            "model": "part_ad.CarPart",
            "fields": {
                "title": fake.sentence(nb_words=5),
                "description": fake.text(),
                "brand": fake.company(),
                "model": fake.random_element(elements=("Sedan", "Hatchback", "SUV", "Convertible", "Coupe")),
                "year_from": fake.random_int(min=2000, max=2015),
                "year_to": fake.random_int(min=2016, max=2023),
                "part_number": fake.random_element(elements=(None, fake.bothify(text='??-####-##'))),
                "price": str(round(random.uniform(10, 1000))),
                "color_model": fake.safe_color_name(),
                "condition": fake.random_element(elements=("new", "used")),
                "quality": fake.random_element(elements=("O", "OE", "P", "PJ", "Z", "ZJ")),
                "seller": fake.random_int(min=1, max=num_users),
                "active_until": fake.date_time_this_year().isoformat(),
                "created_at": fake.date_time_this_year().isoformat(),
                "updated_at": fake.date_time_this_year().isoformat(),
            }
        }
        car_parts.append(car_part)
    return car_parts


if __name__ == "__main__":
    num_car_parts = 10
    car_parts = generate_car_part_data(num_car_parts)

    with open("car_part_fixtures.json", "w", encoding="utf-8") as outfile:
        json.dump(car_parts, outfile, ensure_ascii=False, indent=4)
