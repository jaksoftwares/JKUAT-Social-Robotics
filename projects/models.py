from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Project(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = CKEditor5Field()
    cover_image = models.ImageField(
        _("Cover Image"),
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    external_link = models.URLField(
        _("External Link"), max_length=200, blank=True, null=True
    )
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
