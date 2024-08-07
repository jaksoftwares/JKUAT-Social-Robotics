from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from datetime import datetime
from accounts import models as ACCOUNTS_MODELS

POSTGRADUATE = "P"
UNDERGRADRUATE = "U"
ADMIN = "A"
PI = "I"
LECTURER = "L"
PERSON_CATEGORIES = (
    (POSTGRADUATE, "Postgraduate"),
    (UNDERGRADRUATE, "Undergraduate"),
    (ADMIN, "Admin"),
    (PI, "PI"),
    (LECTURER, "Lecturer"),
)


class Person(ACCOUNTS_MODELS.Profile):
    degree = models.CharField("Degree", blank=True, null=True, max_length=200)
    specialty = models.CharField("Specialty", blank=True, null=True, max_length=200)
    pursuing = models.CharField("Pursuing", blank=True, null=True, max_length=200)
    focus_title = models.CharField("Focus Title", blank=True, null=True, max_length=200)
    focus_short = models.CharField("Focus Short", blank=True, null=True, max_length=200)
    focus_long = models.TextField("Focus Long", blank=True, null=True)
    quote = models.TextField("Quote", blank=True, null=True)
    category = models.CharField(
        _("Category"), choices=PERSON_CATEGORIES, max_length=1, blank=True, null=True
    )
    bio = models.TextField("Bio", blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def save(self, *args, **kwargs):
        if not self.slug:
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
            self.slug = slugify(
                f"{self.first_name}-{self.last_name}___{current_datetime}"
            )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("people:detail", kwargs={"slug": self.slug})
