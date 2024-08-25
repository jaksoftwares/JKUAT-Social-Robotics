from django.urls import path
from .views import (
    OutreachListView,
    OutreachDetailView,
    OutreachCreateView,
    OutreachUpdateView,
    OutreachDeleteView,
)


app_name = "outreach"
urlpatterns = [
    path("", OutreachListView.as_view(), name="list"),
    path("<slug:slug>/", OutreachDetailView.as_view(), name="detail"),
    # path("create/", OutreachCreateView.as_view(), name="create"),
    # path("<slug:slug>/update/", OutreachUpdateView.as_view(), name="update"),
    # path("<slug:slug>/delete/", OutreachDeleteView.as_view(), name="delete"),
]
