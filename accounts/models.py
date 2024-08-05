from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Profile(models.Model):
    class Title(models.TextChoices):
        MR = "MR", _("Mr.")
        MRS = "MRS", _("Mrs.")
        MS = "MS", _("Ms.")
        DR = "DR", _("Dr.")
        PROF = "PROF", _("Prof.")

    title = models.CharField(
        _("Title"),
        max_length=5,
        choices=Title.choices,
        blank=True,
        null=True
    )
    first_name = models.CharField(_("First Name"), max_length=50)
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

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.title} {self.first_name} {self.last_name}"
