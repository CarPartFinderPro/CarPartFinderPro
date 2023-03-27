import os
import glob
from django.core.management import call_command
from django.core.management.base import BaseCommand
from part_ad.fixtures_generator.fixture_generator import FixtureGenerator


class Command(BaseCommand):
    help = "Generate and load all fixtures from the 'fixtures' directory."

    def __init__(self):
        super().__init__()
        self.fixture_generator = FixtureGenerator()

    def handle(self, *args, **options):
        self.fixture_generator.init_fixtures()
        # fixture_files = os.listdir(os.path.join(os.path.dirname(__file__), "../..", "fixtures"))
        # # Sort fixture_files to ensure users are loaded first
        # fixture_files.sort()

        fixture_files = ['address_fixtures.json', 'user_fixtures.json', 'delivery_fixtures.json', 'parcel_fixtures.json',
                         'car_part_fixtures.json']
        # Flush the current data in the database before loading fixtures
        # call_command("flush", "--noinput", verbosity=0)

        if fixture_files:
            call_command("loaddata", *fixture_files, verbosity=2)
        else:
            print("No JSON files found in the fixtures directory.")
