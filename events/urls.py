from django.urls import path
from .views import (
    EventListView,
    EventDetailView,
    EventCreateView,
    EventUpdateView,
    EventDeleteView,
)


app_name = "events"
urlpatterns = [
    path("", EventListView.as_view(), name="list"),
    path("<slug:slug>/", EventDetailView.as_view(), name="detail"),
    # path("create/", EventCreateView.as_view(), name="create"),
    # path("<slug:slug>/update/", EventUpdateView.as_view(), name="update"),
    # path("<slug:slug>/delete/", EventDeleteView.as_view(), name="delete"),
]
