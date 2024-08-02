from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from core import models as CORE_MODELS


class Project(CORE_MODELS.BaseModel):
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
