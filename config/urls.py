from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("core.urls", namespace="core")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("publications/", include("publications.urls", namespace="publications")),
    path("projects/", include("projects.urls", namespace="projects")),
    path("faqs/", include("faqs.urls", namespace="faqs")),
    path("news/", include("news.urls", namespace="news")),
    path("outreach/", include("outreach.urls", namespace="outreach")),
    path("team/", include("team.urls", namespace="team")),
    path("robots/", include("robots.urls", namespace="robots")),
    path(
        "responsible_computing/",
        include("responsible_computing.urls", namespace="responsible_computing"),
    ),
]
