from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from core import models as CORE_MODELS


class Publication(CORE_MODELS.BaseModel):
    author = models.ForeignKey("people.Person", on_delete=models.CASCADE, related_name='publications')

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def get_absolute_url(self):
        return reverse("publications:detail", kwargs={"slug": self.slug})
