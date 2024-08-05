from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core import models as CORE_MODELS


class Outreach(CORE_MODELS.BaseModel):
    class Meta:
        verbose_name = _("Outreach")
        verbose_name_plural = _("Outreaches")

    def get_absolute_url(self):
        return reverse("outreach:detail", kwargs={"slug": self.slug})
