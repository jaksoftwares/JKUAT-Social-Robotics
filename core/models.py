from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    cover_image = models.ImageField(
        _("Cover Image"),
        upload_to="images/",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    external_link = models.URLField(
        _("External Link"), max_length=200, blank=True, null=True
    )
    slug = models.SlugField(unique=True, max_length=100)
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
            self.slug = slugify(f"{self.title}___{current_datetime}")
        super().save(*args, **kwargs)
