from django.utils.translation import gettext_lazy as _
from django.db import models


class Question(models.Model):
    text = models.TextField(_("Question"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text



class Response(models.Model):
    text = models.TextField(_("Response"))

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text
