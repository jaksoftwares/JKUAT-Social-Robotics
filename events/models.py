from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from core import models as CORE_MODELS


class Event(CORE_MODELS.BaseModel):
    location = models.CharField(_("Location"), max_length=50, blank=True, null=True)
    date_starting = models.DateField(_("Date Starting"), blank=True, null=True)
    date_ending = models.DateField(_("Date Ending"), blank=True, null=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
