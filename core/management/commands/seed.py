import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from datetime import datetime
from news.models import News
from people.models import Person
from projects.models import Project
from publications.models import Publication
from robots.models import Robot
from django.conf import settings
from django.db import IntegrityError


class Command(BaseCommand):
    help = "Seed data from JSON files into Django models"

    def handle(self, *args, **kwargs):
        BASE_FILE_PATH = f"{settings.BASE_DIR}/data"
        DATA = [
            {
                "name": "people",
                "file_path": f"{BASE_FILE_PATH}/people.json",
                "class": Person,
            },
            {"name": "news", "file_path": f"{BASE_FILE_PATH}/news.json", "class": News},
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
            self.seed_data(entry)

    def seed_data(self, entry):
        try:
            with open(entry["file_path"]) as f:
                data_list = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {entry['file_path']}"))
            return
        except json.JSONDecodeError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Error decoding JSON in file {entry['file_path']}: {e}"
                )
            )
            return

        for data in data_list:
            if entry["name"] == "publications":
                self.handle_publication(data, entry)
            elif entry["name"] == "projects":
                self.handle_project(data, entry)
            elif entry["name"] == "people":
                self.handle_person(data, entry)
            else:
                self.create_instance(data, entry)

    def handle_person(self, data, entry):
        try:
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S%f")
            data["slug"] = slugify(
                f"{data['first_name']}-{data['last_name']}___{current_datetime}"
            )
            person, created = Person.objects.get_or_create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                defaults=data,
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully created person: {person}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Person already exists: {person}")
                )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating person: {e}"))

    def handle_publication(self, data, entry):
        if "author" in data:
            author_data = data.pop("author")
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S%f")
            author_data["slug"] = slugify(
                f"{author_data['first_name']}-{author_data['last_name']}___{current_datetime}"
            )
            author, created = Person.objects.get_or_create(
                first_name=author_data["first_name"],
                last_name=author_data["last_name"],
                defaults=author_data,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created new author: {author}"))
            data["author"] = author

        self.create_instance(data, entry)

    def handle_project(self, data, entry):
        if "team" in data:
            team_data = data.pop("team")
            project, created = self.create_instance(data, entry)
            if project:
                for member in team_data:
                    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S%f")
                    member["slug"] = slugify(
                        f"{member['first_name']}-{member['last_name']}___{current_datetime}"
                    )
                    person, person_created = Person.objects.get_or_create(
                        first_name=member["first_name"],
                        last_name=member["last_name"],
                        defaults=member,
                    )
                    if person_created:
                        self.stdout.write(
                            self.style.SUCCESS(f"Created new team member: {person}")
                        )
                    person.project = project
                    person.save()
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Added team member: {person} to project: {project}"
                        )
                    )
        else:
            self.create_instance(data, entry)

    def create_instance(self, data, entry):
        try:
            if "slug" not in data:
                current_datetime = datetime.now().strftime("%Y%m%d%H%M%S%f")
                data["slug"] = slugify(f"{data.get('title', '')}___{current_datetime}")

            instance, created = entry["class"].objects.get_or_create(**data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully created {entry['name']} instance: {instance}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"{entry['name']} instance already exists: {instance}"
                    )
                )
            return instance, created
        except IntegrityError as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Integrity error creating {entry['name']} instance: {e}"
                )
            )
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
        return None, False
