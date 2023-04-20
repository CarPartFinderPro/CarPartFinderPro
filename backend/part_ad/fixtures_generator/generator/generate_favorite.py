"""
Module for generating favorite fixtures.
"""

import json
from faker import Faker

fake = Faker()


def generate_favorite_data(num_favorite=10, num_part_ad=10):
    """
    Generate favorite fixtures data.

    Args:
        num_favorite (int): Number of favorites to generate.
        num_part_ad (int): Number of part advertisements to choose from.

    Returns:
        list: A list of dictionaries containing fixture data.
    """
    favorites = []
    for _ in range(num_favorite):
        favorite = {
            "model": "part_ad.Favorite",
            "fields": {
                "user": fake.random_int(min=1, max=num_favorite),
                "part_ad": fake.random_int(min=1, max=num_part_ad),
                "create_date": fake.date_time_this_year().isoformat(),
            }
        }
        favorites.append(favorite)
    return favorites


if __name__ == "__main__":
    num_favorite = 10
    favorite = generate_favorite_data(num_favorite)

    with open("favorite_fixtures.json", "w", encoding="utf-8") as outfile:
        json.dump(favorite, outfile)
