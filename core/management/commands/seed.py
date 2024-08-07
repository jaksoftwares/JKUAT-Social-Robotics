import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from news.models import News
from people.models import Person
from config.settings import BASE_DIR
from projects.models import Project
from publications.models import Publication
from robots.models import Robot


class Command(BaseCommand):
    help = "Import data from JSON files into Django models"

    def handle(self, *args, **kwargs):
        BASE_FILE_PATH = f"{BASE_DIR}/data"
        DATA = [
            {
                "name": "news",
                "file_path": f"{BASE_FILE_PATH}/news.json",
                "class": News,
            },
            {
                "name": "people",
                "file_path": f"{BASE_FILE_PATH}/people.json",
                "class": Person,
            },
            {
                "name": "projects",
                "file_path": f"{BASE_FILE_PATH}/projects.json",
                "class": Project,
            },
            {
                "name": "publications",
                "file_path": f"{BASE_FILE_PATH}/publications.json",
                "class": Publication,
            },
            {
                "name": "robots",
                "file_path": f"{BASE_FILE_PATH}/robots.json",
                "class": Robot,
            },
        ]

        for entry in DATA:
            try:
                with open(entry["file_path"]) as f:
                    data_list = json.load(f)
            except FileNotFoundError:
                self.stdout.write(
                    self.style.ERROR(f"File not found: {entry['file_path']}")
                )
                continue
            except json.JSONDecodeError as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Error decoding JSON in file {entry['file_path']}: {e}"
                    )
                )
                continue

            for data in data_list:
                if entry["name"] == "publications" and "author" in data:
                    author_id = data.pop("author")
                    try:
                        author_instance = Person.objects.get(id=author_id)
                        data["author"] = author_instance
                    except Person.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Person with id {author_id} does not exist. Skipping publication."
                            )
                        )
                        continue
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Unexpected error fetching Person with id {author_id}: {e}"
                            )
                        )
                        continue

                try:
                    entry["class"].objects.create(**data)
                except ValidationError as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Validation error creating {entry['name']} instance: {e}"
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Unexpected error creating {entry['name']} instance: {e}"
                        )
                    )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully imported {entry['name']} data")
            )
