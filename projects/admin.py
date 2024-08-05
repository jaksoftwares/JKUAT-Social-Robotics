from django.contrib import admin
from django.utils import timezone
from django.utils.text import slugify
from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created_at",
        "updated_at",
    ]

    prepopulated_fields = {
        "slug": [
            "title",
        ],
    }

    def save_model(self, request, obj, form, change):
        obj.updated_at = timezone.now()
        if not obj.created_at:
            obj.created_at = timezone.now()
        slug = slugify(f"{obj.title}___{obj.created_at.strftime('%Y%m%d%H%M%S')}")
        obj.slug = slug
        super().save_model(request, obj, form, change)


admin.site.register(models.Project, ProjectAdmin)
