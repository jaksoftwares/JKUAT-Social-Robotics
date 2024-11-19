from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from core import models as CORE_MODELS


class News(CORE_MODELS.BaseModel):
    date_published = models.DateField(_("Date Published"), blank=True, null=True)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
