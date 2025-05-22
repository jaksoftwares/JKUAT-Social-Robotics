from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("core.urls", namespace="core")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("publications/", include("publications.urls", namespace="publications")),
    path("projects/", include("projects.urls", namespace="projects")),
    # path("faqs/", include("faqs.urls", namespace="faqs")),
    path("news/", include("news.urls", namespace="news")),
    path("outreach/", include("outreach.urls", namespace="outreach")),
    path("team/", include("people.urls", namespace="team")),
    path("events/", include("events.urls", namespace="events")),
    path("robots/", include("robots.urls", namespace="robots")),
    path(
        "responsible_computing/",
        include("responsible_computing.urls", namespace="responsible_computing"),
    ),
    path("robots.txt", serve, {'path': 'seo/robots.txt', 'document_root': settings.STATIC_ROOT}),
    path("sitemap.xml", serve, {'path': 'seo/sitemap.xml', 'document_root': settings.STATIC_ROOT}),
    path("BingSiteAuth.xml", serve, {'path': 'seo/BingSiteAuth.xml', 'document_root': settings.STATIC_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
