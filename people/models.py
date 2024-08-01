from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from datetime import datetime
from accounts import models as ACCOUNTS_MODELS


class Person(ACCOUNTS_MODELS.Profile):
    bio = models.TextField("Bio", blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
            self.slug = slugify(
                f"{self.first_name}-{self.last_name}___{current_datetime}"
            )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"slug": self.slug})
