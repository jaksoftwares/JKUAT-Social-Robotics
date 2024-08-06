import json
from django.core.management.base import BaseCommand
from people.models import Person
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = "Import people from a JSON file"

    def handle(self, *args, **kwargs):
        with open(f"{BASE_DIR}/data/people.json") as f:
            data = json.load(f)
        for person_data in data:
            Person.objects.create(
                title=person_data["title"],
                first_name=person_data["first_name"],
                last_name=person_data["last_name"],
                specialty=person_data["specialty"],
                profile_picture=person_data["profile_picture"],
                degree=person_data["degree"],
                pursuing=person_data["pursuing"],
                focus_title=person_data["focus_title"],
                focus_short=person_data["focus_short"],
                focus_long=person_data["focus_long"],
                quote=person_data["quote"],
                bio=person_data["bio"],
                category=person_data["category"],
            )

        self.stdout.write(self.style.SUCCESS("Successfully imported people data"))
