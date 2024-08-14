from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    TITLE_CHOICES = (
        ("MR", "Mr."),
        ("MRS", "Mrs."),
        ("MS", "Ms."),
        ("DR", "Dr."),
        ("PROF", "Prof."),
    )
    title = models.CharField(_("Title"), max_length=5, blank=True, null=True)
    first_name = models.CharField(_("First Name"), max_length=50)
    surname = models.CharField(_("Surname"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50)
    profile_picture = models.ImageField(
        _("Profile Picture"),
        upload_to="profiles/",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        unique_together = (
            "title",
            "first_name",
            "last_name",
        )

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.title} {self.first_name} {self.last_name}"
