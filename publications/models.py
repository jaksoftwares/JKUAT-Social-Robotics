from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from core import models as CORE_MODELS


class Publication(CORE_MODELS.BaseModel):
    reference = models.CharField(_("Reference"), max_length=200, blank=True, null=True)
    document = models.FileField(
        _("Document"), upload_to=None, max_length=100, blank=True, null=True
    )

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def get_absolute_url(self):
        return reverse("publications:detail", kwargs={"slug": self.slug})
