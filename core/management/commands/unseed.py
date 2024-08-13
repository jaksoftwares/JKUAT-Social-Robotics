from django.core.management.base import BaseCommand
from events.models import Event
from news.models import News
from people.models import Person
from projects.models import Project
from publications.models import Publication
from robots.models import Robot


class Command(BaseCommand):
    help = "Remove all data from the specified models"

    def handle(self, *args, **kwargs):
        MODELS = [
            {"name": "news", "class": News},
            {"name": "people", "class": Person},
            {"name": "projects", "class": Project},
            {"name": "events", "class": Event},
            {"name": "publications", "class": Publication},
            {"name": "robots", "class": Robot},
        ]

        for entry in MODELS:
            self.delete_data(entry)

    def delete_data(self, entry):
        try:
            count, _ = entry["class"].objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully deleted {count} {entry['name']} instances"
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error deleting {entry['name']} instances: {e}")
            )
