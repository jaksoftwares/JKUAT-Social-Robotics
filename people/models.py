from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from accounts import models as ACCOUNTS_MODELS


class Person(ACCOUNTS_MODELS.Profile):
    title = models.CharField(_("Title"), max_length=10, blank=True, null=True)
    specialty = models.CharField(_("Specialty"), max_length=50, blank=True, null=True)
    bio = models.TextField(_("Bio"), blank=True, null=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")

    def __str__(self):
        return f"{self.title}. {self.first_name} {self.last_name}"

    def __repr__(self):
        return f"{self.title}. {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})
