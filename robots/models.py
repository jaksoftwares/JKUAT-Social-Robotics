from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core import models as CORE_MODELS


class Robot(CORE_MODELS.BaseModel):
    class Meta:
        verbose_name = _("Robot")
        verbose_name_plural = _("Robots")

    def get_absolute_url(self):
        return reverse("robots:detail", kwargs={"slug": self.slug})
